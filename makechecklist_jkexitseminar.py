#/usr/bin/python
import os
import sys
import re

# makechecklist.py: a quick parser for a specifically-formatted LaTeX file
# that produces a nice checklist in {longtable} for the entire list.
# The list is, or should be, larger than the number of cells on any one 
# bingo card, so a canonical list of the cells is useful when evaluating any
# one card.
#
# Jesse Hamner, 2016

# Functions:

def makeEntry(varname):
    """Take a nicely formatted variable (string) and write it into a LaTeX \
    [long]table cell"""
    tabline = str( "$\\square$ & %s \\\\[\\sep]\n" % varname )
    return(tabline)

def slurpInFile(fn, theList):
    """Open an input file, parse it, ignore some fields, and nicely format the\
    remainder of the file into a long text string of LaTeX tabular fields."""
    f=open(fn, 'r')
    li=f.read()
    grr = li.split('\n')
    for i in grr:
        if( re.search('^%|^\s*$', i) ):
            continue
        elif (re.match('\s*}\s*$', i) ):
            return(theList)
        else:
            mline=i.split(';')
#            print (mline)
            for j in mline:
                if ( re.match ('^\s*$', j) ):
                    continue
                j = re.sub('\\\\myItems{', "", j)
                theList=theList+makeEntry(j)

    return 0

# Main loop:

filename="bingolist_jkexitseminar.tex"
nicetable="% Hopefully a nice table\n\n"
nicetable = slurpInFile(filename, nicetable)

# write out the table to a file:

ofile="checklist_jkexitseminar.tex"
output=open(ofile, 'w')
output.write(nicetable)
output.close()

# let user know: 

print("wrote output to %s" % ofile)

# EOF
