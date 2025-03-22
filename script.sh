#!/bin/bash

nombres_pairs() {
    debut=$1
    fin=$2
    pairs=()

    for ((i=debut; i<fin; i++)); do
        if ((i % 2 == 0)); then
            pairs+=("$i")
        fi
    done

    echo "${pairs[@]}"  # Affiche la liste des nombres pairs
}

# Appel de la fonction
nombres_pairs 1 11

