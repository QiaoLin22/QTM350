#!/bin/bash
ls -l  > string
cut "-d " -f1 string > string2
sort string2 > string3
uniq string2 > string4
wc string4 > res
wc -w res 
cat string4
