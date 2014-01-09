#!/bin/bash

pdb=$1
if [ $# -ne 1 ]
then
    echo "Usage: process_pdbs.sh PDB_FILE"
    exit 1
fi

lines=`wc -l $pdb | awk '{ print $1 }'`
echo "Input PDB File: $pdb Total lines: $lines" > $pdb.data
grep -w ATOM $pdb | awk '{ print $3, $5, $6, $7 }' >> $pdb.data
