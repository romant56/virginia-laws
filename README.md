# virginia-laws

This is a simple, proof of concept program that collects a list of csv files hosted by the Virginia Law Online Library, parses them, and prints a total and subtotals.

### How many laws are there in Virginia?

This is a difficult quetion to answer.  When we think of laws, we are usually thinking of something like a penal code section for a crime, like theft.  However, a criminal code section is just one very small part of what constitutes "laws" in general.  In addiction to state criminal code statues (criminal laws explicitly enacted by a legislative body), there are: constitutions, civil statutes, executive orders, and regulations.  Furthermore, these exist not only on the state level in America, but also on a much larger federal level.  There are also local city and county ordinances.

However, when most people refer to laws (at the state level for this project), they are usually referring to those statutes that are published in a large code and have code section numbers.  This program counts statutes in the Code of Virginia.


An example statute looks like this:

*§ 18.2-96. Petit larceny defined; how punished.*
*Any person who:*

*1. Commits larceny from the person of another of money or other thing of value of less than $5, or*

*2. Commits simple larceny not from the person of another of goods and chattels of the value of less than $1,000, except as provided in clause (iii) of § 18.2-95, shall be deemed guilty of petit larceny, which shall be punishable as a Class 1 misdemeanor.*


### Program overview

The program first retrieves a JSON list of all the titles in the Code of Virginia (similar to a chapter by subject in a book), converts that to a dictionary of title numbers and addresses of where each title's csv is stored, and then parses each line in the csv and counts it.

### What are we checking each line for?

Each line in the csv is a separate statute, so simply counting the lines and adding them should give us the total, right?  Unfortunately many of these lines still exist in Virginia law even though there is not actually any law there.  This could be because the law associated with that code section has been repealed or because that number is reserved for some potential future law.  And, frequently, when a law is amended it shows up twice.  One will say "Effective until (some date)" and another will say "Effective (some date)".

This program does a check for the way these different scenarios will appear in the csv file and does not count them if they fall into one of those three categories.  For the duplicates with dates, it simply doesn't count the "Effective until..." line.  Since we are concerned solely with the number of laws, the date doesn't matter and we just count the subsequent "Effective..." line.

### Examples of what is not counted/counted only once

*§ 18.2-20. Reserved.*
*Reserved.*

*§ 46.2-314. Repealed.*
*Repealed by Acts 2017, c. 156, cl. 2, effective February 23, 2017.*

*§ 2.2-204. (Effective until October 1, 2021) Position established; agencies for which responsible; additional duties.*

*§ 2.2-204. (Effective October 1, 2021) Position established; agencies for which responsible; additional duties.*

