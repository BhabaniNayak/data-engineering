#!/usr/bin/python
# Copyright 2015 Bhabani Nayak. All Rights Reserved.

"""
    Program Description:

        The Word Count program counts all the words from the text
        files contained in a directory named wc_input
        and outputs the counts to a file named wc_result.txt,
        which is placed in a directory named wc_output.

    Unit Test Case:

        Input:
            So call a big meeting,
            Get everyone out out,
            Make every Who holler,
            Make every Who shout shout.

        Output:
            a	        1
            big	        1
            call	    1
            every	    2
            everyone	1
            get	        1
            holler	    1
            make	    2
            meeting	    1
            out	        2
            shout	    2
            so	        1
            who	        2

"""

__author__ = 'Bhabani Nayak'

# import relevant python modules
import sys
import operator
import os

# Input and Output file path and name
input_file_path = "./wc_input"
output_file_path = "./wc_output/"
output_file_name = "wc_result.txt"


'''
    Name :          get_file_paths
    Description :   Traverse the root directory and its sub directories and returns the list of files path
    Input :         Root directory of files
    Output:         None
    Return :        File paths, else blank list
    Error :         IOError
'''


def get_file_paths(root):
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

    return file_paths


'''
    Name :          count_words_in_file
    Description :   Write the result into the output file
    Input :         Result stream (result_stream) and output file(out_file)
    Output:         out_file
    Return :        None
    Error :         IOError
'''


def count_words_in_file(file, word_list):

    file = open(file, "r+")

    for word in file.read().split():
        word = (''.join(e for e in word if e.isalnum())).lower()
        if word not in word_list:
            word_list[word] = 1
        else:
            word_list[word] += 1

    file.close()


'''
    Name :          count_words_in_files
    Description :   Count words in each file in the files_path
    Input :         file_paths,
    Output:         word_list
    Return :        None
    Error :         None
'''


def count_words_in_files(file_paths, word_list):
    for file in file_paths:
        count_words_in_file(file, word_list)


'''
    Name :          write_result_to_file
    Description :   Write the sorted result into the output file
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

    # Sort the words in ascending order
    sorted_word = sorted(result_stream.keys())

    for word in sorted_word:
        line = '{} {} {} {}'.format(word, "\t", result_stream[word], "\n")
        file_to_write.write(line)

    file_to_write.close()


def main():
    print("Word count program executed. Please check ./wc_output/wc_result.txt for output.")

    # Variables to store the root directory for text files
    root_path = input_file_path

    # Dictionary to store the word and its count from text files
    word_list = {}

    # Read all files in the root_path
    file_paths = get_file_paths(root_path)

    # Count words in each file in the directory
    count_words_in_files(file_paths, word_list)

    # Write the result to output file
    write_result_to_file(word_list, output_file_path + output_file_name)


if __name__ == '__main__':
    main()