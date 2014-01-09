
# if the $dirToCopy is not in its home location, youcs into an empty folder to enjoy
# Author: Caroline Gorham, 20 Feb 2013

#script variables
dir=~/some_pics
dirToCopy=funny_pics
dirLocToCopy=/share/apps/tutorials/unix/funny_pics/
funnyPicQuota=20

# function to determine the number of files and 
# indicate if you have too many or too few funny pictures
# indicate if a file  contains the word racoon/raccoon
numberOfFiles ()
{
echo "The number of files is" "$(find $dir  -type f | wc -l)"


        if [[ "$fileCount" -lt $funnyPicQuota ]]; then
                echo "You need more funny pictures!"
        else
                echo "You have too many funny picture!"
        fi

	if [[ -f $(find . -name *racoon* ) ]]; then
    		echo "The file spells it racoon"

	elif [[ -f $(find . -name *raccoon* ) ]]; then
    		echo "The file spells it raccoon"
	else
   		echo "I couldn't find a raccoon file."
	fi
}

#main

# create $dir directory if it does not exist 
if [ ! -d $dir ]; then
 mkdir $dir   
fi

cd $dir

# copy the $dirToCopy to the folder if the folder contains no files
# and if $dirToCop exists in its home location
if [[ $(find $dir  -type f | wc -l)  ==  "0" ]]; then

    if [[ -d $dirLocToCopy ]]; then
        
	cp -r  $dirLocToCopy $dir
         

	numberOfFiles

 
# you are out of luck if the $dirToCopy is not in its home location

    else
	echo "You're are out of luck!"
    fi


# if you already have files in the $dir foler, consider making a new 
# empty folder to put funny pics in --- just change the $dir variable
# if you really want to add more files to this location, enter <y..> 
# and the file location from /

else

   numberOfFiles

    echo "You should consider making an empty directory to \
put funny pictures in. Just change the dir variable \
to your new funny picture directory and run the script." 

    echo "Do you want to add more to this folder?"

    read   moreInput

    moreInput="$(echo $moreInput | head -c 1)"
    
    if [[ $moreInput == "y" || $moreInput == "Y" ]]; then
	    
	    echo "what is the folder location?" 
	    
	    read fileLocation
	    
	    if [[ -d $fileLocation ]]; then

       		 if cp -r  $fileLocation  $dir
                  	then echo "directory copied."
	         fi

            else
		echo "You're out of luck. This location DNE"
	    fi	
    fi
fi

