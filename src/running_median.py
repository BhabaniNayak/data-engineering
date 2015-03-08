#!/usr/bin/python
# Copyright 2015 Bhabani Nayak. All Rights Reserved.

"""
    Program Description:

        This program calculates the running median, the median number of words per line,
        for each line of the text files in the wc_input directory. If there are multiple
        files in that directory, the files should be combined into a single stream and
        processed by the running median program in alphabetical order, so a file named
        Hello.txt should be processed before a file named world.txt. The resulting
        running median for each line should then be outputted to a text file named
        med_result.txt in the wc_output directory.

    Unit Test Case:

        Input:
            So call a big meeting,
            Get everyone out out,
            Make every Who holler,
            Make every Who shout shout.

        Output:
            5.0
            4.5
            4.0
            4.5

        Explanation:
            The first line of the input has 5 words so the running median for the first
            line is simply 5. Since the second line has 4 words, the running median for
            the first two lines is the median of (4, 5) = 4.5 (since the median of an
            even set of numbers is defined as the mean of the middle two elements after
            sorting). After three lines, the running median would be the median of
            (4, 4, 5) = 4, and after all four lines the running median is the median
            of (4, 4, 5, 5) = 4.5.

"""

__author__ = 'Bhabani Nayak'

# import relevant python modules
import sys
import operator
import os

# Input and Output file paths and name
input_file_path = "./wc_input"
output_file_path = "./wc_output/"
output_file_name = "med_result.txt"

'''
    Name :          get_median
    Description :   Helper function to calculate the median of a list of numbers
    Input :         list of word counts per line in the stream words
    Output:         None
    Return :        running median of the stream
    Error :         None
'''


def get_median(word_stream):
    # Python 3 does actual division and list index can not be float. Hence //
    median_index = len(word_stream) // 2
    word_stream.sort()
    len_stream = len(word_stream)

    if len_stream < 1:
        return None

    # Used x.0 to divide to make the median format consistent for even and odd number of elements
    elif len_stream == 1:
        return word_stream[len_stream-1] / 1.0

    elif len_stream % 2 == 0:
        return (word_stream[median_index-1] + word_stream[median_index]) / 2.0

    elif len_stream % 2 == 1:
        return word_stream[median_index] / 1.0

    else:
        return None

'''
    Name :          get_sorted_file_paths
    Description :   Traverse the root directory and its sub directories and returns the list of sorted files path
    Input :         Root directory of files
    Output:         None
    Return :        File paths, else blank list
    Error :         IOError
'''


def get_sorted_file_paths(root):
    # List to store file paths in a directory
    file_paths = []

    # Traverse the root and its sub directories
    try:
        for root, directories, files in os.walk(root):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file_paths.append(file_path)
    except IOError:
        print("Unable to open directory", root)
        sys.exit()

    # Sort the file names as per the requirement
    file_paths.sort()

    return file_paths


'''
    Name :          calculate_median_in_file
    Description :   Read all words per line in a file and calculate the running median
    Input :         File path
    Output:         word_stream_count, median_stream
    Return :        None
    Error :         IOError
'''


def calculate_median_in_file(file, word_stream_count, median_stream):
    try:
        file = open(file, "r+")
    except IOError:
        print("Unable to open file", output_file_name)
        sys.exit()

    lines = file.readlines()

    # Count the number of words in each line for a file
    for line in lines:
        count = 0
        for word in line.split():
            count += 1

        # Append the word count and running median to the streams
        if count > 0:   # Handle blank lines
            word_stream_count.append(count)
            median_stream.append(get_median(word_stream_count))

    file.close()


'''
    Name :          calculate_running_median
    Description :   Read all files in files path and calculate the running median
    Input :         File paths
    Output:         word_stream_count, median_stream
    Return :        None
    Error :         None
'''


def calculate_running_median(file_paths, word_stream_count, median_stream):
    # Calculate median for each file in the file path
    for file in file_paths:
        calculate_median_in_file(file, word_stream_count, median_stream)


'''
    Name :          write_result_to_file
    Description :   Write the result into the output file
    Input :         Result stream (result_stream) and output file(out_file)
    Output:         out_file
    Return :        None
    Error :         IOError
'''


def write_result_to_file(result_stream, out_file):
    try:
        file_to_write = open(out_file, "w")
    except IOError:
        print("Unable to open file", output_file_name)
        sys.exit()

    for med in result_stream:
        line = '{} {}'.format(med, "\n")
        file_to_write.write(line)

    file_to_write.close()


# Main function of the file
def main():
    print("Running median program executed. Please check ./wc_output/med_result.txt for output.")

    # Variables to store the root directory of text files
    root_path = input_file_path

    # List to store the number of words in the stream
    word_stream_count = []

    # List to store the median of each line in each file of input stream
    median_stream = []

    # Read all files from the root_path and get the sorted the file names
    sorted_file_paths = get_sorted_file_paths(root_path)

    # Calculate running median of the stream
    calculate_running_median(sorted_file_paths, word_stream_count, median_stream)

    # Write the result to output file
    write_result_to_file(median_stream, output_file_path + output_file_name)

if __name__ == '__main__':
    main()