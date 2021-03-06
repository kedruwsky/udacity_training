#!/usr/bin/python

import sys
import operator

#-----------------------------------------------------------#
# The reducer reads through all the records in the input.   #
# These are the individual topN lists generated by mappers. #
#                                                           #
# The reducer builds the global topN list by combining the  #
# individual lists.                                         #
#-----------------------------------------------------------#

n = 10
tagOccurence = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    thisTag, Occ = data_mapped

    print thisTag,
    if thisTag not in tagOccurence:
       print "is not in dict",  
       print "initializing to ",
       print int(Occ)
       tagOccurence[thisTag] = int(Occ) 
    else:
       print "is in dict",
       print "is currently set to ",
       print int(tagOccurence[thisTag]),
       print "adding",
       print int(Occ),
       tagOccurence[thisTag] = int(tagOccurence[thisTag])+int(Occ)
       print "final value is",
       print int(tagOccurence[thisTag])

tagOccurence1 = [(v, k) for k, v in tagOccurence.items()]
tagOccurence1 = sorted(tagOccurence1, reverse=True, key=lambda x: int(x[0]))[:n]

for i in tagOccurence1:
    print "{0}\t{1}".format(i[1], i[0])
