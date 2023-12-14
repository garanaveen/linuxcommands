#Similar file : cdfindfirstoccurance.sh

EXCLUDE_DIR1=dist
EXCLUDE_DIR2=Dir2-ReplaceThisAsPerYourNeeds
#Add more exclude paths as per your need.


#-----------------------------------------------------------------------------------
#This is when user provides a path that might not be relative to current directory.
#Ex. "vimff b/parent/child/FileName.txt" will execute "vim child/FileName.txt". i.e. it will trim top directories until a valid relative path is found.

input_path="$1"

# Function to check if a path is valid
is_valid_path() {
    if [ -f "$1" ]; then
        return 0  # Path is valid
    else
        return 1  # Path is not valid
    fi
}

# Function to trim a directory from the given path
trim_directory() {
    path="$1"
    trimmed_path="${path#*/}"
    echo "$trimmed_path"
}

# Function to find a valid relative path
find_valid_path() {
    original_path="$1"
    if [[ "$original_path" == *"/"* ]]; then

       current_path="$original_path"

       while [ -n "$current_path" ] && ! is_valid_path "$current_path"; do
           current_path=$(trim_directory "$current_path")
       done

       if [ -z "$current_path" ]; then
           echo "No valid path found for $original_path"
           exit 1
       fi

       echo "$current_path"
   fi
}

VALID_RELATIVE_PATH=$(find_valid_path "$input_path")

if [[ ! -z ${VALID_RELATIVE_PATH} ]]; then
   echo "FILEPATH : ${VALID_RELATIVE_PATH}"
   vim ${VALID_RELATIVE_PATH}
   exit
fi

#-----------------------------------------------------------------------------------
#This is when user provides Partial filename as first parameter to 'vimff'
#Ex. "vimff FileNa" will execute "vim parent/child/FileName.txt"

FILEPATH=`find . \
-type d -name $EXCLUDE_DIR1 -prune \
-o -type d -name $EXCLUDE_DIR2 -prune \
-o -name .hg -prune \
-o -name .git -prune \
-o -name "*$1*" \
-print -quit`


if [[ ! -z ${FILEPATH} ]]; then
   echo "FILEPATH : ${FILEPATH}"
   vim ${FILEPATH}
   exit
fi

#-----------------------------------------------------------------------------------

