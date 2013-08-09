# ##### BEGIN GPL LICENSE BLOCK #####
#
#  SCA Tree Generator, a Blender addon
#  (c) 2013 Michel J. Anders (varkenvarken)
#
#  This module is: kdtree.py
#  a pure python implementation of a kdtree
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####



# cdef class Pos:
#     cdef float x
#     cdef float y
#     def __cinit__(self, float x, float y):
#         self.x = x
#         self.y = y


cdef class Hyperrectangle:
    '''an axis aligned bounding box of arbitrary dimension'''

    cdef float xmin
    cdef float ymin
    cdef float xmax
    cdef float ymax

    def __cinit__(self, float xmin, float ymin, float xmax, float ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    cdef void extend(self, float x, float y):
        '''adapt the hyperectangle if necessary so it will contain pos.'''
        if x < self.xmin: self.xmin = x
        elif x > self.xmax: self.xmax = x
        if y < self.ymin: self.ymin = y
        elif y > self.ymax: self.ymax = y
        
    cdef float distance_squared(self, x, y):
        '''return the distance squared to the nearest edge, or zero if pos lies within the hyperrectangle'''
        cdef float result = 0.0
        if x < self.xmin:
            result += (x-self.xmin)**2
        elif x > self.xmax:
            result += (x-self.xmax)**2
        if y < self.ymin:
            result += (y-self.ymin)**2
        elif y > self.ymax:
            result += (y-self.ymax)**2
        return result



cdef class Node:
    """implements a node in a kd-tree"""
    cdef float x
    cdef float y
    cdef int data
    cdef Node left
    cdef Node right
    cdef int dir
    cdef int count
    cdef int level
    cdef Hyperrectangle rect
    cdef distsq
    
    def __cinit__(self, float x, float y, int data):
        self.x = x
        self.y = y
        self.data = data
        self.left = None
        self.right = None
        self.dir = 0
        self.count = 0
        self.level = 0
        self.rect=Hyperrectangle.__new__(Hyperrectangle, x, y, x, y)
        self.distsq = 9e9

    cdef void addleft(self, Node node):
        self.left = node
        self.rect.extend(node.x, node.y)
        node.level=self.level+1
        node.dir=(self.dir+1)%2

    cdef void addright(self, Node node):
        self.right = node
        self.rect.extend(node.x, node.y)
        node.level=self.level+1
        node.dir=(self.dir+1)%2
        
    cdef float distance_squared(self, x, y):
        return (self.x - x)**2 + (self.y - y)**2



cdef class Tree:
    """implements a kd-tree"""

    cdef Node root
    cdef int nnearest
    cdef int count
    cdef int level
    
    def __cinit__(self):
        self.root = None
        self.nnearest=0 # number of nearest neighbor queries
        self.count=0  # number of nodes visited
        self.level=0 # deepest node level 
    
    cdef void resetcounters(self):
        self.nnearest=0 # number of nearest neighbor queries
        self.count=0  # number of nodes visited
        
    cdef Node _insert(self, Node node, float x, float y, int data):
        cdef float comp
        if node.dir == 0:
            comp = x < node.x
        else:
            comp = y < node.y

        if comp:
            if node.left is None:
                node.addleft(Node.__new__(Node, x, y, data))
                return node.left
            else:
                node.rect.extend(x,y)
                return self._insert(node.left, x, y, data)
        else:
            if node.right is None:
                node.addright(Node.__new__(Node, x, y, data))
                return node.right
            else:
                node.rect.extend(x, y)
                return self._insert(node.right, x, y, data)


    # def insert(self, pos, data):
    #     if self.root is None:
    #         self.root = Node.__new__(Node, pos, data)
    #         self.level = self.root.level
    #         return self.root
    #     else:
    #         node=self._insert(self.root, pos, data)
    #         if node.level > self.level : self.level = node.level
    #         return node

    def insert(self, data_points):
        """Insert points with data.

        data_points: ((pos,data), (pos,data), ...)
        """
        cdef float x
        cdef float y
        cdef int data
        for item in data_points:
            x = item[0][0]
            y = item[0][1]
            data = item[1]
            if self.root is None:
                self.root = Node.__new__(Node, x, y, data)
                self.level = self.root.level
            else:
                node=self._insert(self.root, x, y, data)
                if node.level > self.level : self.level = node.level


    cdef Node _nearest(self, Node node, float x, float y, int checkempty, int level=0):
        cdef Node result
        # cdef float distsq
        cdef Node neartree
        cdef Node nearnode
        cdef Node fartree
        cdef Node farnode

        self.count+=1
        
        cdef float d
        if node.dir == 0:
            d = x - node.x
        else:
            d = y - node.y
        
        if checkempty and (node.data == -1):
            result = None
        else:
            # distsq = node.distance_squared(x, y)
            node.distsq = node.distance_squared(x, y)
            result = node

        if d <= 0:
            neartree = node.left
            fartree = node.right
        else:
            neartree = node.right
            fartree = node.left

        if neartree is not None:
            # nearnode, neardistsq = self._nearest(neartree,x,y,checkempty,level+1)
            # if (result is None) or (neardistsq is not None and neardistsq < distsq):
            #     result, distsq = nearnode, neardistsq
            nearnode = self._nearest(neartree,x,y,checkempty,level+1)
            if (result is None) or (nearnode is not None and nearnode.distsq < node.distsq):
                result = nearnode
        
        if fartree is not None:
            # if (result is None) or (fartree.rect.distance_squared(x,y) < distsq):
            #     farnode, fardistsq = self._nearest(fartree,x,y,checkempty,level+1)
            #     if (result is None) or (fardistsq is not None and fardistsq < distsq):
            #         result, distsq = farnode, fardistsq
            if (result is None) or (fartree.rect.distance_squared(x,y) < node.distsq):
                farnode = self._nearest(fartree,x,y,checkempty,level+1)
                if (result is None) or (farnode is not None and farnode.distsq < node.distsq):
                    result = farnode     

        # return result, distsq

        return result


    def nearest(self, float x, float y):
        # cdef Node node
        # return 0
        self.nnearest+=1
        if self.root is None:
            return None, None
        self.root.count=0
        # node, distsq = self._nearest(self.root, pos[0], pos[1], checkempty)
        node = self._nearest(self.root, x, y, 1)
        data = node.data
        node.data = -1  # delete from kdtree, requires checkempty=True
        self.count+=self.root.count
        # return node, distsq
        return data
        
