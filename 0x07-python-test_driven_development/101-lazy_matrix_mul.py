#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if (not all(isinstance(item, list) for item in m_b)
            and not all(isinstance(item, list) for item in m_a)):
        raise TypeError("m_a and m_b must be a list of lists")
    elif (not all(isinstance(item, list) for item in m_b)):
        raise TypeError("m_b must be a list of lists")
    elif not all(isinstance(item, list) for item in m_a):
        raise TypeError("m_a must be a list of lists")
    elif all(len(item) == 0 for item in m_a) and all(len(item)==0 for item in m_b):
        raise ValueError("m_a and m_b can't be empty")
    elif all(len(item) == 0 for item in m_a):
        raise ValueError("m_a can't be empty")
    elif all(len(item) == 0 for item in m_b):
        raise ValueError("m_b can't be empty")
    elif not isinstance(m_a, list) and not all(isinstance(m_b, list)):
        raise TypeError("m_a and m_b must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif (not all(isinstance(val, (int, float)) for item in m_a for val in item)
            and not all(isinstance(val, (int, float)) for item in m_b for val in item)):
        raise ValueError("m_a and m_b should contain only integers or floats")
    elif not all(isinstance(val, (int, float)) for item in m_a for val in item):
        raise ValueError("m_a should contain only integers or floats")
    elif not all(isinstance(val, (int, float)) for item in m_b for val in item):
        raise ValueError("m_b should contain only integers or floats")
    elif (not all(len(m_a[0]) == len(val) for val in m_a)
            and  not all(len(m_b[0]) == len(val) for val in m_b)):
        raise TypeError("each row of m_a and m_b must be of the same size")
    elif (not all(len(m_a[0]) == len(val) for val in m_a)):
        raise TypeError("each row of m_a must be of the same size")
    elif not all(len(m_b[0]) == len(val) for val in m_b):
        raise TypeError("each row of m_b must be of the same size")
    elif (not all(len(m_a[0]) == len(m_b[0]) for i in range(len([m_a,m_b])))):
        raise TypeError("m_a and m_b can't be multiplied")

