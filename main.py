# Author: Varun Upadhyay
# Batch Renaming of Files
# Give the path to the folder which contains the files in os.listdir and os.chdir function

import os

# Getting the initial count of files in the folder
initial_count = 0
for i in os.listdir("/home/varun/Desktop/Github Projects/CodeKata/Python"): 
	initial_count += 1

# Valid set of characters in a file
alpha_arr = list('abcdefghijklmnopqrstuvwxyz0123456789.')

for i in os.listdir("/home/varun/Desktop/Github Projects/CodeKata/Python"):
	ans = ''
	for j in i:
		if j.lower() in alpha_arr:
			ans += j
		else:
			if j == ' ':
				ans += '_'
	os.chdir("/home/varun/Desktop/Github Projects/CodeKata/Python")
	os.rename(i, ans)

# Getting the final count of files in the folder after renaming
final_count = 0
for i in os.listdir("/home/varun/Desktop/Github Projects/CodeKata/Python"):
	final_count += 1

# Final Verification
print('Number of files present initially: ' + str(initial_count))
print('Number of file renamed: ' + str(final_count))
print('Difference: ' + str(initial_count - final_count))


