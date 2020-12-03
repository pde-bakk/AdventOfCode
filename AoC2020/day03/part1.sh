#!/bin/bash
input="sample"
declare -i trees=0
declare -i i=0
while IFS= read -r line
do
	declare -i len=$(echo "$line" | wc -m)
	len=$(( len - 1 ))
	i=$(( i % len ))
	c=${line:$i:1}
	if [[ "$c" == "#" ]]; then
		let "trees++"
	fi
	let "i+=3"
done < $input

echo "found $trees trees"
