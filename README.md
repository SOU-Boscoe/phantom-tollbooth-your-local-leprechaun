# Design Document Lab 6
Luke Wulf <br>
11/9/23

### Introduction
This program, tollbooth_starter.py, is meant to be a word counting program. When given a large amount of text, it should be able to split, format and count all the words in the text. For this program, the book "Phantom Tollbooth" was used. 

### Functional Requirements
When this program is given the text, it should remove any special characters, and split the text into a list. It will then take this list of all the words, sorting out any unwanted words, and creating a dictionary with key words and values of how many times that word shows up. Finally, it will organize that dicitonary from highest to lowest count and print out the 50 most seen words. The user should see a list of the 50 most counted words with one word on each line

### Decomposition Strategy
For the first version of this program, I will make a version of this program without any functions to understand each step better, and so I can later sort them into different areas. I might also make a quick just count for a single word, just so I can get down how to count for the entire text.

### Design Requirements
#### Data
I will be given the entire text of the book, "Phantom Tollbooth" as a massive string. My program will keep track of and create different versions of this str, creating a list of all the words in it, and then changing that list into a dictionary where keys = words and values = number of instances. 

#### Loops
A few loops will be in play, mostly for loops. I need a loop to check and go through all the words, check each character for special characters and delete it, and finally to to go through dictionary and print them off. I'll also need a while loop to sort through my dictionary, as it needs to repeats many times, but not for each in the dicitonary. This last loop will be the hardest to work with

#### Conditions
I will be checking characters against a list of special characters so I can sort them out of the massive string. I will also check words against another list of what words shouldn't be counted.

### Testing Strategy
I think the biggest issue will be formatting words correctly. To help learn how I want to do this, I'll make a few versions that test how best to get rid of characters and split the string into a list. To start, I'll just make a version that prints out all the words after some changes, such as replacing some special character in a few lines and spliting them all.<br>
If this version comes out successful, then I can change some of the replacing into a for char loop that will make a new string. then print it all out to make sure they are all still showing up properly.<br>
Finally, I'll make a more final version of the code, adding in the rest of the code, mostly looking to find how to properly sort a dictionary, as python doesn't have a method to do that. I will mainly be working on that for my mostly final version of the code. 
