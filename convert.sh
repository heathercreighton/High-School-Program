#!/bin/sh

# Colourise the output
RED='\033[0;31m'        # Red
GRE='\033[0;32m'        # Green
YEL='\033[1;33m'        # Yellow
NCL='\033[0m'           # No Color

file_specification() {
    FILE_NAME="$(basename "${entry}")"
    DIR="$(dirname "${entry}")"
    NAME="${FILE_NAME%.*}"
    SIZE="$(du -sh "${entry}" | cut -f1)"
    ADDLINES="--- \nlayout: default\n--- \n"

    showdown makehtml -i "$DIR/$NAME.md" -o "docs/$NAME.html"

    echo $ADDLINES | $(cat - "docs/$NAME.html" > tmp && mv tmp "docs/$NAME.html")

    printf "%*s${GRE}%s${NCL}\n"                    $((indent+4)) '' "${entry}"
    printf "%*s\tFile name:\t${YEL}%s${NCL}\n"      $((indent+4)) '' "$FILE_NAME"
    printf "%*s\tDirectory:\t${YEL}%s${NCL}\n"      $((indent+4)) '' "$DIR"
}

walk() {
    printf "In walk()"
    # If the entry is a file do some operations
    for entry in "$1"/*.md; do [[ -f "$entry" ]] && file_specification; done
    # If the entry is a directory call walk() == create recursion
    for entry in "$1"/*; do [[ -d "$entry" ]] && walk "$entry" $((indent+4)); done
}

# If the path is empty use the current, otherwise convert relative to absolute; Exec walk()
[[ -z "${1}" ]] && ABS_PATH="${PWD}" || cd "${1}" && ABS_PATH="${PWD}"
rm -rf "docs/"
mkdir -p "${ABS_PATH}/docs"
walk "${ABS_PATH}"      
echo 