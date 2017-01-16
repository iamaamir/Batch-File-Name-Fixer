#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Varun Upadhyay
from os import listdir, chdir, rename

# Valid chars in a file name
valid_chars = 'abcdefghijklmnopqrstuvwxyz0123456789._'
dir_path = input("Enter the file path")
dir_list = listdir(dir_path)
total_files = len(dir_list)

for i in dir_list:
    ans = ''
    for j in i:
        if j.lower() in valid_chars:
            ans += j
        else:
            if j == ' ':
                ans += '_'
    chdir(dir_path)
    rename(i, ans)

# Getting the final count of files in the folder after renaming
# this is bad idea must count only renamed files 
final_count = len(dir_list)

# Final Verification
print('Number of files present initially: ', total_files)
print('Number of file renamed: ', final_count)
print('Difference: ', (total_files - final_count))
