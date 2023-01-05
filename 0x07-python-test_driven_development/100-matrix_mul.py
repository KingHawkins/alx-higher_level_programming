#!/usr/bin/python3

"""Matrix_mul function which mimmicks the numpy.matmul func"""

def matrix_mul(m_a, m_b):
    """Implementing fucntion.
    Args:
        m_a(list): first matrix par
        m_b(list): second matrix par
    Raises:
        TypeError("m_a and m_b can't be empty")
        TypeError("m_a and m_b must be list of lists")
    """
    if not isinstance(m_a, list) and not all(isinstance(m_b, list)):
        raise TypeError("m_a and m_b must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif (not all(isinstance(item, list) for item in m_b)
            and not all(isinstance(item, list) for item in m_a)):
        raise TypeError("m_a and m_b must be a list of lists")
    elif (not all(isinstance(item, list) for item in m_b)):
        raise TypeError("m_b must be a list of lists")
    elif not all(isinstance(item, list) for item in m_a):
        raise TypeError("m_a must be a list of lists")
    elif (all(len(item) == 0 for item in m_a)
            and all(len(item)==0 for item in m_b)):
        raise ValueError("m_a and m_b can't be empty")
    elif all(len(item) == 0 for item in m_a):
        raise ValueError("m_a can't be empty")
    elif all(len(item) == 0 for item in m_b):
        raise ValueError("m_b can't be empty")
    elif (not all(isinstance(val, (int, float))
        for item in m_a for val in item)
            and not all(isinstance(val, (int, float))
                for item in m_b for val in item)):
        raise TypeError("m_a and m_b should contain only integers or floats")
    elif (not all(isinstance(val, (int, float))
            for item in m_a for val in item)):
        raise TypeError("m_a should contain only integers or floats")
    elif (not all(isinstance(val, (int, float))
            for item in m_b for val in item)):
        raise TypeError("m_b should contain only integers or floats")
    elif (not all(len(m_a[0]) == len(val) for val in m_a)
            and  not all(len(m_b[0]) == len(val) for val in m_b)):
        raise TypeError("each row of m_a and m_b must be of the same size")
    elif (not all(len(m_a[0]) == len(val) for val in m_a)):
        raise TypeError("each row of m_a must be of the same size")
    elif not all(len(m_b[0]) == len(val) for val in m_b):
        raise TypeError("each row of m_b must be of the same size")
    elif (not all(len(m_a[0]) == len(m_b[0]) for i in range(len([m_a,m_b])))):
        raise ValueError("m_a and m_b can't be multiplied")
    if len(m_a) == 2 and len(m_b) == 2:
        new = list(m_b[0])
        partner_new = list(m_b[1])
        cum = list(zip(new, partner_new))
        one = [cum[0][0]*m_a[0][0] + cum[0][1]*m_a[0][1],
                cum[1][0]*m_a[0][0] + cum[1][1]*m_a[0][1]]
        sec = [m_a[1][0]*cum[0][0] + m_a[1][1]*cum[0][1],
                m_a[1][0]*cum[1][0] + m_a[1][1]*cum[1][1]]
        return ([one, sec])
    elif len(m_a) == 1 and len(m_b) == 2:
        one = [m_a[0][0]*m_b[0][0] + m_a[0][1]*m_b[1][0],
                m_a[0][0]*m_b[0][1] + m_a[0][1]*m_b[1][1]]
        return ([one])
    elif len(m_a[0]) == 2 and len(m_b[0]) == 2:
        new = [m_a[0][0]*m_b[0][0] + m_a[0][1]*m_b[0][0],
                m_a[0][0]*m_b[0][1] + m_a[0][1]*m_b[0][1]]
        return ([new])
    elif len(m_a) == 3 and len(m_b) == 3:
        new = [m_a[0][0]*m_b[0][0] + m_a[0][1]*m_b[1][0]+m_a[0][2]*m_b[2][0],
                m_a[0][0]*m_b[0][1] + m_a[0][1]*m_b[1][1]+m_a[0][2]*m_b[2][1],
                m_a[0][0]*m_b[0][2] + m_a[0][1]*m_b[1][2]+m_a[0][2]*m_b[2][2]]
        mid =  [m_a[1][0]*m_b[0][0] + m_a[1][1]*m_b[1][0]+m_a[1][2]*m_b[2][0],
                m_a[1][0]*m_b[0][1] + m_a[1][1]*m_b[1][1]+m_a[1][2]*m_b[2][1],
                m_a[1][0]*m_b[0][2] + m_a[1][1]*m_b[1][2]+m_a[1][2]*m_b[2][2]]
        end =  [m_a[2][0]*m_b[0][0] + m_a[2][1]*m_b[1][0]+m_a[2][2]*m_b[2][0],
                m_a[2][0]*m_b[0][1] + m_a[2][1]*m_b[1][1]+m_a[2][2]*m_b[2][1],
                m_a[2][0]*m_b[0][2] + m_a[2][1]*m_b[1][2]+m_a[2][2]*m_b[2][2]]
        return ([new, mid, end])
    else:
        raise ValueError("m_a and m_b can't be multiplied")
