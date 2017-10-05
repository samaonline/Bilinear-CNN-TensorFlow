mkdir obj
for FILE in *; do mv "$FILE" "$(echo $FILE | sed -e 's/ /_/g')"; done

find . -depth -name '* *' \
| while IFS= read -r f ; do mv -i "$f" "$(dirname "$f")/$(basename "$f"|tr ' ' _)" ; done