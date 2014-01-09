'''
- this module includes functions to convert between
SI, imperial, and other scientific units for
height, weight, and temperature

By: Caroline Gorham, 25 Feb 2013
'''



"""FYI : / and * functions only work with np.arrays """

def F_to_C (var):
    var=5./9*(var-32)
    return var

def C_to_F (var):
    var=9./5*(var+32)
    return var

def C_to_K (var):
    var=var+273.15
    return var

def K_to_C (var):
    var=var-273.15
    return var

def F_to_K (var):
    var=5./9*(var-32)+273.15
    return var

def K_to_F (var):
    var=(var-273.15)*9./5 + 32
    return var

def inch_to_cm (var):
    var=var*2.54
    return var

def cm_to_inch (var):
    var=var*.39
    return var

def cm_to_m (var):
    var=var/100
    return var

def m_to_cm (var):
    var=var*100
    return var

def ft_to_inch (var):
    var=var*12
    return var

def inch_to_ft (var):
    var=var/12
    return var

def lb_to_kg (var):
    var=var/2.2
    return var

def kg_to_lb (var):
    var=var*2.2
    return var

