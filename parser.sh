#!/bin/bash

# Vérifiez si le fichier et le type de données ont été fournis
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <input_file_path> <output_file_path> <data_type>"
    exit 1
fi

input_file=$1
output_file=$2
data_type=$3

echo "{" > "$output_file"
first_block=true

while IFS= read -r line || [[ -n "$line" ]]; do
    if [[ -z "$line" ]]; then
        if [ "$first_block" = false ]; then
            echo -n "}, " >> "$output_file"
        fi
        first_block=true
    else
        if [ "$first_block" = true ]; then
            echo -n "{" >> "$output_file"
            first_block=false
        else
            echo -n ", " >> "$output_file"
        fi
        # Si le type de données est une chaîne, ajoutez des guillemets autour de la ligne
        if [ "$data_type" = "string" ]; then
            echo -n "\"$line\"" >> "$output_file"
        else
            echo -n "$line" >> "$output_file"
        fi
    fi
done < "$input_file"

if [ "$first_block" = false ]; then
    echo "}" >> "$output_file"
fi

echo "}" >> "$output_file"

echo "Fichier transformé avec succès en $output_file"

exit 0