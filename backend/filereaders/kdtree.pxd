

import cython


cdef class Hyperrectangle:
    cdef int dim
    cdef object min
    cdef object max

    @cython.locals(
        i = cython.int
    )
    cpdef extend(self, list pos)

    @cython.locals(
        i = cython.int
    )
    cpdef distance_squared(self, list pos)



cdef class Node:
    cdef public list pos
    cdef public object data
    cdef public Node left
    cdef public Node right
    cdef public int dim
    cdef public int dir
    cdef int count
    cdef public int level
    cdef Hyperrectangle rect

    @cython.locals(
        i = cython.int
    )
    cpdef distance_squared(self, list pos)



cdef class Tree:
    cdef Node root
    cdef int nnearest
    cdef int count
    cdef int level

    cpdef _insert(self, Node node, list pos, data)

    @cython.locals(
        d = cython.float
    )
    cpdef _nearest(self, Node node, list pos, bint checkempty, int level=*)