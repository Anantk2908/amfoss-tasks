Level 0 -> Level 1:For this level password was saved in a file named readme which was accessed using the cat command

Level 1 -> Level 2:For this level the password was saved in a file named "-" so I used "./-" with the cat command

Level 2 -> Level 3:For this level the password was stored in a file named "spaces in the filename" so  I used cat command with with the file name in between double quotation marks treats it like a single string

Level 3 -> Level 4:For this level the password was stored in file which was hidden so using ls-a it was found that the file name was ".hidden" using cat command I found the password

Level 4 -> Level 5:For this level the password was in the files of "inhere" directory there were nine files in total opening one by one the password was found in the eight file

Level 5 -> Level 6:For this level there were 80 files in the directory so using the find command and using the the "-size" and "-r" options we find the password in the folder named"maybehere07" in the file named "file2"

Level 6 -> Level 7:This level was similar to the last level just it required more parameters in the find command.

Level 7 -> Level 8:In this level the password the password was net to the word millionth so I had to just grep the word millionth

Level 8 -> Level 9:In this level the password was stored in a file called data.txt and it is given the password is the line that appears once so we had to use sort -u(It removes duplicate instances in the file) and uniq -c(It counts how many times a line is repeating) and the line repeating once was the password.

Level 9 -> Level 10:In this level the password was stored in a data.txt which had few human readable strings so we had to use string command(It shows the human readable strings in the file) and the grep
