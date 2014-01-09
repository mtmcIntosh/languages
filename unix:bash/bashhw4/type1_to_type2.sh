#!/bin/bash
# This script converts files in a 
# user specified directory from one 
# file type to another (as allowed for 
# by `convert`
# By: Caroline Gorham, 18 March 2013

# user specified directory and file types
dir=~/some_pics/funny_pics
convert_from_type=jpg
convert_to_type=png


convert_1type_to_Othertype () {
# conversion function takes a count of the files 
# of the original file type and converts them to 
# the desired type using the `convert` command.
# This function also ensures that the file is named
# *.$convert_to_type  

# define array of the files corresponding to the 
# original file type
array=($dir/*.$convert_from_type )

# print number of files of the file type
echo "The number of .""$convert_from_type" " files is" "${#array[@]}"

# print the last file recorded in the array to ensure all accounted
if [[ ${#array[@]} -gt 0 ]]; then
	echo "The last one is " "${array[ ${#array[@]}-1 ]}"
fi 

# convert all files in the array to the new file type
# if converted properly, delete the original file type
# if the file is empty, or convert does malfunctions return error
for file_to_convert in ${array[@]}
do
	if [[ -s $file_to_convert ]]; then
		if  convert $file_to_convert $file_to_convert.$convert_to_type
			then rm $file_to_convert
			else "The conversion was not possible"
		fi
	else
		echo "$file_to_convert is empty, therefore it cannot be converted to .png."
	fi
done

# rename all converted files to represent the conversion file type properly
`find $dir -type f -name "*.$convert_from_type.$convert_to_type" -exec rename .jpg.png .png {} \;`

}


convert_1type_to_Othertype
