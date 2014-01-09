#THIS IS A SIMPLE PREDATOR PREY ALGORITHM TO 
# DETERMINE CHANGES IN THE RELATIVE POPULATIONS
# BASED ON THE PROPORTIONALITY OF THE POPULATIONS 
# BY: CAROLINE GORHAM, 1 MARCH 2013

# GENERATES AND RETURNS A RANDOM NUMBER BETWEEN THE BOUNDS 
# upper_bound/ratio AND lower_bound, INCLUSIVE
randint() {
    
    upper_bound=$1
    lower_bound=$2
    ratio=$3
    
    numValues=$((upper_bound/ratio - lower_bound  + 1))

    number=$RANDOM

    let "number%=$((numValues))"
    newnumber=$((number+lower_bound))

    return $newnumber  
}


# DETERMINES THE CHANGE IN POPULATION BASED ON 
# A RANDOMLY GENERATED NUMBER BETWEEN THE BOUNDS 
# initial_population/ratio AND lower_bound, INCLUSIVE
deltaPop(){ 

    initial_population=$1
    ratio=4
    lower_bound=0

    randint $initial_population $lower_bound $ratio
    change_population=$?

    return $change_population  
}

# INTIAL POPULATIONS
predatorPopulation=500

preyPopulation=500

# RUN 'i' ITERATIONS OF CHANGING THE PREDATOR/PREY POPULATIONS
# BASED ON THEIR PROPORTIONALITY. STARTING WITH INITIAL POPULATIONS
for i in {1..10}
do
	deltaPop $predatorPopulation
        deltapredator=$?

	deltaPop $preyPopulation
	deltaprey=$?

	if [[ "$preyPopulation" -gt "$predatorPopulation" ]]; then
                
		let "preyPopulation=$((preyPopulation-deltapredator))"
		let "predatorPopulation=$((predatorPopulation+deltaprey))"

	elif [[ "$preyPopulation" -gt "$((predatorPopulation/2))" ]]; then

                let "preyPopulation=$((preyPopulation-deltapredator))"
                let "predatorPopulation=$((predatorPopulation-deltaprey))"

	else 

                let "preyPopulation=$((preyPopulation+deltapredator))"
                let "predatorPopulation=$((predatorPopulation-deltaprey))"
        fi

	echo -e "\nOn iteration " $i 
	echo "The prey population is " $preyPopulation
	echo "The predator population is " $predatorPopulation

done
