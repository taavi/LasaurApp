

import cython


@cython.locals(
    join_count = cython.int,
    reverse_count = cython.int,
    i = cython.int,
    d2_start = cython.float,
    d2_end = cython.float
)
cpdef list connect_segments(list paths, float epsilon2)



cpdef inline d2(list u, list v)

@cython.locals(
    maxi = cython.int,
    maxd2 = cython.float,
    cu = cython.float,
    i = cython.int,
    cw = cython.float,
    dw2 = cython.float,
    b = cython.float
)
cpdef simplifyDP(float tol2, list v, int j, int k, list mk)


@cython.locals(
    n = cython.int,
    pv = cython.int,
    i = cython.int
)
cpdef list simplify(list path, float tolerance2)



