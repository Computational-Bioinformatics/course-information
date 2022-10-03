#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Originally written by: Oliver Bonham-Carter
# Ref: BioPython,
# Link: https://biopython.org/docs/1.75/api/Bio.pairwise2.html?highlight=pairwise2#module-Bio.pairwise2

# email: obonhamcarter@allegheny.edu
# Date: 24 March 2021
# Comment: A sequence alignment tool using Biopython.



DATE = "3 Oct 2022"
VERSION = "i"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"



# Bold High Intensity
BIBlack='\033[1;90m'      # Black
BIRed='\033[1;91m'        # Red
BIGreen='\033[1;92m'      # Green
BIYellow='\033[1;93m'     # Yellow
BIBlue='\033[1;94m'       # Blue
BIPurple='\033[1;95m'     # Purple
BICyan='\033[1;96m'       # Cyan
BIWhite='\033[1;97m'      # White

# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White

# Bold
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White
BIWhite='\033[1;97m'      # White


def getSeq():
	""" function to ask user for a sequence and return it to a caller function"""
	prompt_str =  BIGreen + "Enter a seq : " + BIWhite
	inputSeq_str = input(prompt_str)
	return Seq(inputSeq_str)
#end of getSeq()


def getGlobalAlign(seq1, seq2):
	""" Complete global alignment using Needleman-Wunsch algorithm"""

	print(BIYellow + "GLOBAL ALIGNMENTS (Needleman-Wunsch algorithm)" +White)
	myAlignments = pairwise2.align.globalxx(seq1, seq2)
	# print(myAlignments) # print out sequence gap information

	for thisAlignment in myAlignments:
		print(thisAlignment)

	from Bio.pairwise2 import format_alignment
	#alignments = pairwise2.align.globalxx(seq1, seq2)
	print(BICyan)
	for thisAlignment in myAlignments:
		print(format_alignment(*thisAlignment))
	print(BWhite)
#end of getGlobalAlign()

def getLocalAlign(seq1, seq2):
	""" Complete local alignments using Smith-Waterman algorithm"""

	print(BIYellow +"LOCAL ALIGNMENTS (Smith-Waterman algorithm)"+White)
	myAlignments = pairwise2.align.localxx(seq1, seq2)
	# print(myAlignments) # print out sequence gap information

	for thisAlignment in myAlignments:
		print(thisAlignment)

	from Bio.pairwise2 import format_alignment
	#alignments = pairwise2.align.globalxx(seq1, seq2)
	print(BICyan)
	for thisAlignment in myAlignments:
		print(format_alignment(*thisAlignment))
	print(BWhite)

# end of getLocalAlign()



def main():
	"""Driver function for the program"""
	print()

	# ask the user to enter a sequences
	seq1 = getSeq()
	seq2 = getSeq()
	# Or use hard-coded short sequences
	# seq1 = Seq("GATC")
	# seq2 = Seq("CATC")
	print("\n")
	getGlobalAlign(seq1, seq2) # complete global alignment: Needleman-Wunsch
	getLocalAlign(seq1, seq2) # complete local alignment: Smith-Waterman
# end of main()


# import statements
# check that the library is available to the code...
try:
	import Bio
except ModuleNotFoundError:
	print("\t [-]" + BIRed + "\t Error loading BioPython." + White + "\n\t [-]"+BIRed+ "\t Are you using your Docker container?" + White)
	exit()

from Bio import pairwise2
from Bio.Seq import Seq


# Run the code by calling main()
main()
