"""
http://www.reddit.com/r/dailyprogrammer/comments/1heozl/070113_challenge_131_easy_who_tests_the_tests/

Input Description

        You will be given an integer N on the first line of input: it represents the following N lines of input. For each 
        line, you will be given an integer T and then two strings A and B. If the integer T is zero (0), then you must 
        reverse the string A. If the integer T is one (1), then you must upper-case (capitalize) the entire string A. At
         the end of either of these operations, you must test if the expected result (string B) and the result of the 
         function (string A) match.

Output Description

        If string A, after the above described functions are executed, and B match, then print "Good test data". 
        Else, print "Mismatch! Bad test data". "Matching" is defined as two strings being letter-for-letter, equivalent 
        case, and of the same length.

Sample Input
        6
        0 Car raC
        0 Alpha AhplA
        0 Discuss noissucsiD
        1 Batman BATMAN
        1 Graph GRAPH
        1 One one

Sample Output
        Good test data
        Mismatch! Bad test data
        Mismatch! Bad test data
        Good test data
        Good test data
        Mismatch! Bad test data
"""

from sys import argv

with open(argv[1]) as data:
        # skip num lines since we won't use it
        lines = [line.strip() for line in data.readlines()]

        for line in lines[1:]:
                flag, a, b = line.split()
                flag = int(flag)

                if flag:
                        # if flag is 1 then an uppercased a must == b
                        if a.upper() == b:
                                print("Good test data")
                        else:
                                print("Mismatch! Bad test data")
                else:
                        # if flag is 0 then reversed a must == b
                        if a[::-1] == b:
                                print("Good test data")
                        else:
                                print("Mismatch! Bad test data")