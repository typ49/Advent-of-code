#!/bin/bash

# Parcourir les répertoires day-XX
for dir in day-*/ ; do
    # Construire le nom du fichier basé sur le nom du répertoire
    file_name="day${dir#day-}.txt"

    # Vérifier si le fichier existe
    if [[ -f "${dir}${file_name}" ]]; then
        # Renommer le fichier en input.txt
        mv "${dir}${file_name}" "${dir}input.txt"
    fi
done

