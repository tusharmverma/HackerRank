# Consider the following:
#
#     A string,
#
# , of length where
# .
# An integer,
# , where is a factor of
#

# We can split into subsegments where each subsegment, ,
# consists of a contiguous block of characters in . Then, use each to create string
#
# such that:
#
#     The characters in
#
# are a subsequence of the characters in
#
# Any repeat occurrence of a character is removed from the string such that each character in
# occurs exactly once. In other words, if the character at some index in occurs at a previous
# index in , then do not include the character in string
#
#
#
# Given
# and , print lines where each line denotes string
#
# .
#
# Input Format
#
# The first line contains a single string denoting
# .
# The second line contains an integer,
#
# , denoting the length of each subsegment.
#
# Constraints
#
# , where is the length of It is guaranteed that is a multiple of
#
#
# Output Format
#
# Print
# lines where each line contains string.
from pipenv.vendor.urllib3.connectionpool import xrange


def merge_the_tools(string, k):
    n = len(string)

    for x in xrange(0, n, k):
        slicedStr = string[x: x + k]
        uni = []
        s = ""
        for y in slicedStr:
            if y not in uni:
                uni.append(y)
        print(s.join(uni))


string = "AABCAAADA"
k = 3
merge_the_tools(string, k)
