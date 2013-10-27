"""
http://www.reddit.com/r/dailyprogrammer/comments/1kphtf/081313_challenge_136_easy_student_management/

Input Description

        On standard console input, you will be given two space-delimited integers N and M: N is the number of students (which ranges from 1 to 60, inclusive), and M is the number of assignments (which ranges from 4 to 100, inclusive). This will be followed by N lines of text, each starting with an upper-case unique string being is your students name. This is then followed by M integers, which are the grades ranging from 0 to 20, inclusively.

Output Description

        On the first line of output, print the class' average grade. Then, for each student, print their name and average grade (up to two decimal points precision).

Sample Inputs & Outputs

Sample Input 1
        3 5
        JON 19 14 15 15 16
        JEREMY 15 11 10 15 16
        JESSE 19 17 20 19 18

Sample Output 1
        15.93
        JON 15.80
        JEREMY 13.40
        JESSE 18.60

Sample Input 2
        10 10
        ABIGAIL 11 3 5 20 4 2 8 17 4 5
        ALEXANDER 2 12 20 0 6 10 3 4 9 7
        AVA 11 15 2 19 14 5 16 18 15 19
        ETHAN 6 12 0 0 5 11 0 11 12 15
        ISABELLA 16 0 10 7 20 20 7 2 0 1
        JACOB 2 14 17 7 1 11 16 14 14 7
        JAYDEN 10 10 3 16 15 16 8 17 15 3
        MADISON 10 11 19 4 12 15 7 4 18 13
        SOPHIA 5 17 14 7 1 17 18 8 1 2
        WILLIAM 12 12 19 9 4 3 0 4 13 14

Sample Output 2
        9.50
        ABIGAIL 7.90
        ALEXANDER 7.30
        AVA 13.40
        ETHAN 7.20
        ISABELLA 8.30
        JACOB 10.30
        JAYDEN 11.30
        MADISON 11.30
        SOPHIA 9.00
        WILLIAM 9.00
"""

from sys import argv

with open(argv[1]) as data:
        # first line of input contains total # of students and the total # of assignments for each student
        num_students, num_assignments = map(int, data.readline().split())

        students = []
        sum_of_averages = 0

        # calculate the average of each student and put them in a list
        for line in data.readlines():
                line = line.split()

                # average the student's list of test values (strings)
                average = float(sum(map(int, line[1:]))) / num_assignments
                sum_of_averages += average

                # add to student name, average to list
                students.append([line[0], average])

        # print average of student averages with 2 decimal points
        print "{0:.2f}".format(sum_of_averages / num_students)
        
        # print all student names and their individual averages with 2 decimal points
        print "\n".join("{0} {1:.2f}".format(name, average) for name, average in students)