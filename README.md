This repository has the solution of the following two problems in data
engineering. The source code is in Python. You need Python version 2.7
and above to run the program. Run the run.sh to view the output in wc_output
directory.

One of the first problems you’ll encounter in data engineering is Word
Count, which takes in a text file or set of text files from a directory
and outputs the number of occurrences for each word. For example, Word
Count on a file containing the following passage:

    So call a big meeting, 
    Get everyone out out, 
    Make every Who holler,
    Make every Who shout shout.

would return:

a           1 big         1 call        1 every       2 everyone    1
get         1 holler      1 make        2 meeting     1 out         2
shout       2 so          1 who         2

The first part of the solution(word_count_insight.py) is to implement
Word Count that counts all the words from the text files contained in
a directory named wc_input and outputs the counts (in alphabetical
order) to a file named wc_result.txt, which is placed in a directory
named wc_output.

Another common problem is the Running Median - which keeps track of the
median for a stream of numbers, updating the median for each new number.
The second part of the coding challenge is to implement a running median
for the number of words per line of text. Consider each line in a text
file as a new stream of words, and find the median number of words per
line, up to that point (i.e. the median for that line and all the
previous lines). For example, the first line of the passage

    So call a big meeting, 
    Get everyone out out, 
    Make every Who holler,
    Make every Who shout shout.

has 5 words so the running median for the first line is simply 5. Since
the second line has 4 words, the running median for the first two lines
is the median of {4, 5} = 4.5 (since the median of an even set of
numbers is defined as the mean of the middle two elements after
sorting). After three lines, the running median would be the median of
{4, 4, 5} = 4, and after all four lines the running median is the median
of {4, 4, 5, 5} = 4.5. Thus, the correct output for the running median
program for the above passage is:

5.0 4.5 4.0 4.5

The second part of the program(running_median.py) is to implement running median that
calculates the median number of words per line, for each line of the
text files in the wc_input directory. If there are multiple files in
that directory, the files should be combined into a single stream and
processed by your running median program in alphabetical order, so a
file named hello.txt should be processed before a file named world.txt.
The resulting running median for each line should then be outputted to a
text file named med_result.txt in the wc_output directory.
