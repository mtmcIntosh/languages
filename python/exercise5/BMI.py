"""Reads user's height weight and preferred method of units.
Converts all values into SI metric units. Calculates BMI,
and offers BMI value and classification to user. Continues until
user indicates to stop.
IMPvars:
user['units', <m or ft>, <cm or in>, <kg or lbs> ]
metricUser = [<'metric'>, <m>, <m (from in or cm)>, <kg> ]
BMIvalue, calculated percentage 
weightClassification, appropriate message indicating BMI class
By: Caroline Gorham, 13 Feb 2013 """

import numpy as np

continuation = [1,1]


"""function to ask user for continuation decision"""    
def continuer (continuation):
    
    yon = raw_input("\nDo you want to run another number? \n")
    yon = yon.lower()

    if yon[0] is not 'y':
        continuation = 0
        userentry = 0
        
        return [continuation, userentry]
    
    return continuation


"""function to input initial user-defined values, these values cannot be changed
return user values (unit type, height, weight) as tuple --- return None if invalid
unit type are entered"""
def userInput(continuation):

    units=''
    height=''
    weight=''

    
    units= raw_input ('\nWill you be entering in <metric> or <imperial> units?\n')
    units=units.lower()

    """ensure appropriate units have been entered before continuing
    to ask about height and weight """
    try:
        int(units)
        print "Please enter a valid measure of units."

        return None

    except ValueError:

        if units[0][0] is not 'i' and  units[0][0] is not 'm':
            print "Please enter a valid measure of units."

            return None
             
        else:
        
    
            height = (raw_input ("\nPlease enter your height.\n(if entering imperial units:"\
            " enter in either <'> and/or <''>,\n<feet> and/or <inches> or  <ft> and/or <in>\n"\
            "if entering in metric: enter in either <metres> and/or <centimetres> \nor <m> and/or "\
            "<cm>, or  <centimetres>). \n"))

            weight = (raw_input ("\nPlease enter your weight. \n(if entering in imperial units: "\
            " write <lbs> \n if entering in metric: " \
            "please indicate with <kg>.)\n"))

            t=units, height, weight 

            return t





"""function to determine if an appropriate value was entered for each parameter of unit type
return validity parameter"""
def stringValidity(variable):

    valid=1

    if variable.replace(" ","").isdigit() !=1 and (variable.find(".") ==-1 or
        variable.find('a')!=-1 or variable.find('b')!=-1 or variable.find('c')!=-1\
        or variable.find('d')!=-1 or variable.find('e')!=-1 or variable.find('f')!=-1\
        or variable.find('g')!=-1 or variable.find('h')!=-1 or variable.find('i')!=-1 \
        or variable.find('j')!=-1 or variable.find('k')!=-1 or variable.find('l')!=-1 \
        or variable.find('m')!=-1 or variable.find('n')!=-1 or variable.find('o')!=-1 \
        or variable.find('p')!=-1 or variable.find('q')!=-1 or variable.find('r')!=-1 \
        or variable.find('s')!=-1 or variable.find('t')!=-1 or variable.find('u')!=-1 \
        or variable.find('v')!=-1 or variable.find('w')!=-1 or variable.find('x')!=-1 \
        or variable.find('y')!=-1 or variable.find('z')!=-1) :
        
        print ("It seems you have entered invalid units. Please start again")

        valid = -1

    return valid
    


"""function to determine which parameters the user has input littleOrBig = [<m,ft>, <cm,in>]
1 if parameter is present, 0 if parameter is not present"""
def cm_in_Or_ft_m (height):

    littleOrBig = [0,0]

    
    if (height.replace(" ","").replace(".","").isdigit() !=1):
        if height.find("in")!=-1 or height.find("inch")!=-1 or height.find("inches")!=-1or  height.find("''")!=-1\
           or height.find("cm")!=-1 or height.find("centimetres")!=-1 or height.find("centimeters")!=-1:

            littleOrBig[1] = 1
            height=height.replace("cm","")
            height=height.replace("''","")
        
        
        if height.find("ft")!=-1 or height.find("feet")!=-1 or height.find("foot")!=-1 or\
             height.find("'")!=-1  or height.find("m")!=-1  \
             or height.find("metres")!=-1 or height.find("meters")!=-1:
        
            littleOrBig[0] = 1

    else:
        
        print ("Please use units. Start over.")
        
        return None
        
            
    return littleOrBig




"""function to  determine if the height parameter is a valid entry, and if only one
value was entered instead of <ft and in> or <m and cm>, which parameters
the user meant the entry for ---- return None if invalid entry"""
def heightValidity(height, lower_ft_m_cutoff, cm_in_cutoff, upper_ft_m_cutoff, littleOrBig, userunits):

    if userunits[0][0] is 'i':
        ft_m = 'feet'
        in_cm = 'inches'
    else:
        ft_m = 'metres'
        in_cm = 'centimetres'


    if len(height) is 1 and 0 == (height[0]):
        
        print ("You must enter a valid height for this calculation to be valid.")

        return None


    elif littleOrBig[0] == 1:
        """If the user entered ft/m, make sure their value is below the maximum, or that they inteded to enter
        a value above the maximum"""
        
        if ( height[0] > upper_ft_m_cutoff) :

            overUpperLimit = raw_input("Are you really over %d" %upper_ft_m_cutoff + " %s?" %ft_m)

            overUpperLimit = overUpperLimit.lower()

            if overUpperLimit[0] is not 'y':
                print ("Then let's start over.")

                return None
            
            height.append(0)
            
        else:
            
            height.append(0)

      
    elif (littleOrBig[1] == 1 and (littleOrBig[0] == 0)):
        """If the user entered cm/in, without ft/m, make sure their value is above the minimum, or that they inteded to enter
        a value below the minimum"""  

        if ( height[0] < cm_in_cutoff) :

            underLowerLimit = raw_input("Are you really under %d" %cm_in_cutoff + " %s?" %in_cm)

            underLowerLimit = underLowerLimit.lower()

            if underLowerLimit[0] is not 'y':
                print ("Then let's start over.")

                return None
            
            height=[int(0), height[0]]
        else:
            
            height=[int(0), height[0]]

    return height




"""function to  determine if the weight parameter is a valid entry ---- return None if invalid entry"""
def weightValidity(weight, lowercutoff, uppercutoff, userunits):

    if userunits[0][0] is 'i':
        kg_lbs = 'lbs'
    else:
        kg_lbs = 'kg'
        

    if (weight == 0 ):
        print ("You must enter a valid weight for this calculation to be valid.")
        
        return None


    elif (0 < weight < lowercutoff ):
        """make sure the entered weight is above the minimum allowed, or that the user intended
        to enter a value below the minimum"""

        newborn = raw_input("Are you sure you are doing this calculation for a newborn?")

        newborn = newborn.lower()

        if newborn[0] is not 'y':
            print ("Then let's start over.")
            return None
        

  
    elif (weight >= uppercutoff ):
        """make sure the entered weight is below the maximum allowed, or that the user intended
        to enter a value above the maximum"""
            
        fatty = raw_input("Are you sure you are over %d" %uppercutoff + " %s?" %kg_lbs)

        if fatty[0] is not 'y':
            print ("Then let's start over.")
            return None

    return weight




"""function to parse, and save, valid entries of height and weight in imperial units
to a userImerial array ---- return None if invalid entry"""
def imperial(user):

    userImperial = [user[0]]

    height = user[1]

    weight = user[2]


    """develop binary array of provided height parameters [ft/m, cm/in] """
    littleOrBig = cm_in_Or_ft_m (height)
    if littleOrBig is None:
        return None
    

    """remove alphbetic characters from string"""
    height = height.replace("'", ' ').rstrip("''").replace("feet", " ").\
              replace("inches", " ").replace("foot", " ").replace("inch"," ").\
              replace("ft"," ").replace("in"," ")


    """ensure validity of entered units"""
    valid=stringValidity(height)

    if valid == -1:
        return None
    
        
    """prepare height array for manipulation"""
    
    height= height.split()
        
    height = map(float,height)


    """ensure validity of height values"""
    height = heightValidity(height, 1, 12, 10, littleOrBig, userImperial)
    
    if height is None:
        return None


    """append valid height to userImperial array""" 
    userImperial.append((height[0]))
    userImperial.append((height[1]))


    """remove alphbetic characters from string"""
    weight = weight.rstrip("lbs").rstrip("lb")


    """ensure validity of entered units"""
    valid = stringValidity(weight)

    if valid == -1:
        return None

        
    """prepare weight array for manipulation"""
    weight = float(weight)


    """ensure validity of weight values"""
    weight = weightValidity(weight,10,1300, userImperial)
    
    if weight is None:
        return None


    """append valid weight to userImperial array"""     
    userImperial.append(weight)

    return userImperial





"""function to parse, and save, valid entries of height and weight in metric units
to a userMetric array ---- return None if invalid entry"""
def metric(user):

    userMetric = [user[0]]

    height = user[1]

    weight = user[2]


    """develop binary array of provided height parameters [ft/m, cm/in] """
    littleOrBig = cm_in_Or_ft_m (height)


    """remove alphbetic characters from string"""    
    height = height.replace("met", ' ').replace("centi", ' ').\
            replace("res", ' ').replace("ers", ' ').\
            replace("m", ' ').replace("c", ' ')


    """ensure validity of entered units"""
    valid = stringValidity(height)

    if valid == -1:
        return None


    """prepare height array for manipulation"""
    height= height.split()
            
    height = map(float,height)


    """ensure validity of height values"""
    height = heightValidity(height, .308, 30.5,  3, littleOrBig, userMetric)
    if height is None:
        return None


    """append valid height to userMetric array""" 
    userMetric.append((height[0]))
    userMetric.append((height[1]))


    """remove alphbetic characters from string"""
    weight = weight.rstrip("kg").rstrip("s")


    """ensure validity of entered units"""
    valid = stringValidity(weight)

    if valid == -1:
        return None


    """prepare weight array for manipulation"""
    weight = float(weight)


    """ensure validity of weight values"""
    weight = weightValidity(weight, 4.6, 589, userMetric)
    if weight is None:
        return None
                     

    """append valid weight to userMetric array""" 
    userMetric.append(weight)
    
    return userMetric




"""function to convert entries of either units to <m> and <kg>
return as metricUser, ready to calculate BMI
parsedUser=[imperial, ft, in, lbs] or parsedUser=[metric, m, cm, kg]
metricUser = [metric, m, kg]"""
def conversion(parsedUser,i):
    metricUser=np.zeros(shape=(i,2))
    m=0
    for line in parsedUser:
        metricUser[m,:]=[( line[1] * .0254 ),\
                (line[0] * 0.453592)]
        m=m+1

    return metricUser


"""calculate BMI /// kg/m^2"""
def BMI(user,i):
    BMIvalue=np.zeros(shape=(i))

    m=0
    for line in user:
        BMIvalue[m] = user[m,1]/ ( user[m,0])**2
        m=m+1

    return BMIvalue



"""determine and return weightClass as definied by BMI value"""    
def weightClass(BMIvalue):

    bin1=0
    bin2=0
    bin3=0
    bin4=0
    bin5=0
    bin6=0
    bin7=0

    for bins in BMIvalue:
        
         if ( BMIvalue[bins] < 16.0 ):

            bin1=bin1+1

        

         elif (16 <= BMIvalue[bins] < 18.5):

            bin2=bin2+1


         elif (18.5 <= BMIvalue[bins] < 25):

            bin3=bin3+1



         elif (25 <= BMIvalue[bins] < 30):

            bin4=bin4+1



         elif (30 <= BMIvalue[bins] < 35):

            bin5=bin5+1

 

         elif (35 <= BMIvalue[bins] < 40):

            bin6=bin6+1



         elif (BMIvalue[bins] >= 40):

            bin7=bin7+1

    return (bin1, bin2, bin3, bin4, bin5, bin6, bin7)




    

"""print important information to screen"""    
def printInfo (user, metricUser, BMIvalue, weightClassification):

    print('\n%s' %(user,) + "\n")
    print('In %s' %metricUser[0] +  ' units you are: %s' %(metricUser[1]) + "m, %s" %metricUser[2]+ "kg.\n")
    print ("your BMI is: %f" %BMIvalue+ " %.\n")
    print("You are %s" %weightClassification)






    
