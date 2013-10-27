"""
http://www.reddit.com/r/dailyprogrammer/comments/1m1jam/081313_challenge_137_easy_string_transposition/

Input Description
        You will first be given an integer N which is the number of strings that follows. N will range inclusively from 1 to 16. 
        Each line of text will have at most 256 characters, including the new-line (so at most 255 printable-characters, with
         the last being the new-line or carriage-return).

Output Description
        Simply print the given lines top-to-bottom. The first given line should be the left-most vertical line.

Sample Inputs & Outputs

Sample Input 1
        1
        Hello, World!

Sample Output 1
        H
        e
        l
        l
        o
        ,

        W
        o
        r
        l
        d
        !

Sample Input 2
        5
        Kernel
        Microcontroller
        Register
        Memory
        Operator

Sample Output 2
        KMRMO
        eieep
        rcgme
        nrior
        eosra
        lctyt
         oe o
         nr r
         t
         r
         o
         l
         l
         e
         r
"""

from sys import argv

with open(argv[1]) as data:
        num_strings = int(data.readline().strip())

        strings = []
        longest_string = 0

        for line in data.readlines():
                string = line.strip()

                strings.append(string)

                if len(string) > longest_string:
                        longest_string = len(string)

        for x_char in range(0, longest_string):
                temp = []

                for string in strings:
                        if len(string) > x_char:
                                temp.append(string[x_char])
                        else:
                                temp.append(" ")

                print "".join(temp)
