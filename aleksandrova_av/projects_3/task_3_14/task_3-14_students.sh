#!/bin/bash

echo -e "\nИмена студентов"
awk '{ print $1 }' students.txt

echo -e "\nОценки"
awk '{ print $2 }' students.txt

echo -e "\nНомер строки и имя студента"
awk '{ print NR, $1 }' students.txt
