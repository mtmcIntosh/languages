user=[]
    
    user.append( raw_input ('\nWill you be entering in metric or imperial units?\n'))

    user[-1]=user[-1].lower()
    
    height = (raw_input ("\nPlease enter your height, (if entering imperial units: '\
    ' separate by <'> and <''>, or <feet>, <ft> and <inches>, <in>; if metric: ;\
    'you may choose to separate metres from centimetres with <m>, <metres> and <cm>, '\
    '<centimetres> ). \n"))

    weight = (raw_input ("\nPlease enter your weight, (if entering imperial units: "\
    " write <lbs> (for good practice, always use units); if metric: " \
    "please indicate with <kg>. )\n"))


    if user[0][0] is 'i' :
        height = height.replace("'", ' ').rstrip("''").replace("feet", " ").\
              replace("inches", " ").replace("foot", " ").replace("inch"," ").\
              replace("ft"," ").replace("in"," ")


        if height.find('m')==1 or height.find('c')==1:

            print ("It seems you have entered metric units. Please start again")

            userInput()

        height= height.split()
        
        height = map(float,height)
        
        
        if len(height) is 1 and 0 < (height[0]) <= 10 :
            height.append(0)
        elif len(height) is 1 and (height[0]) > 10:
            height=[int(0), height[0]]
        elif len(height) is 1 and 0 >= (height[0]):
            print ("You must enter a valid height for this calculation to be valid.")
        elif len(height) is 2 and 1 > (height[0]):
            newborn = raw_input("Are you sure you are doing this calculation for a newborn? (< 1 ft)")

            newborn = newborn.lower()

            if newborn[0] is not 'y':
                print ("Then let's start over.")
                userInput ()
            
            
        user.append((height[0]))
        user.append((height[1]))

        weight = weight.rstrip("lb").rstrip("s")


        if weight.find('kg')==1:

            print ("It seems you have entered metric units. Please start again")

            userInput()

        weight = map(float,weight)

        if (weight[0]) <= 0:
            print ("You must enter a valid weight for this calculation to be valid.")
        elif (weight[0]) >= 1400:
            fatty = raw_input("Are you sure you are over 1400 lbs?")

            if fatty[0] is not 'y':
                print ("Then let's start over.")
                userInput ()

        
        user.append(weight)
        
