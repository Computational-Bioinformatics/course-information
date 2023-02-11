#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# install biopython
# python3 -m pip install biopython

DATE = "10 Sept 2022"
VERSION = "i"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"



def main():
	""" The driver function of the program. This function
	demonstrates gthe central dogma of bio in biopython. """

	print("\t Welcome to the Central Dogma of Biology Demo")
	print("\t BioPython version", Bio.__version__)

	# define the DNA sequences
	myDNASeqA = Seq("AGTACAGTA")
	myDNASeqB = Seq("AGTAGAGAA")

	print("\t The sequences:")
	print("\t myDNASeqA :", myDNASeqA)
	print("\t myDNASeqB :", myDNASeqB)


	# compliment of sequences

	compOfMyDNASeqA = myDNASeqA.complement()
	print("\n\t The comp of seq A is:", compOfMyDNASeqA)
	compOfMyDNASeqB = myDNASeqB.complement()
	print("\t The comp of seq B is:", compOfMyDNASeqB)


	# reverse compliment of sequences

	revCompOfMyDNASeqA = myDNASeqA.reverse_complement()
	print("\n\t The REV comp of seq A is:", revCompOfMyDNASeqA)
	revCompOfMyDNASeqB = myDNASeqB.reverse_complement()
	print("\t The REV comp of seq B is:", revCompOfMyDNASeqB)

	# transcribe: DNA to RNA

	RNAOfMyDNASeqA = myDNASeqA.transcribe()
	print("\n\t The RNA of seq A is:", RNAOfMyDNASeqA)
	RNAOfMyDNASeqB = myDNASeqB.transcribe()
	print("\t The RNA of seq B is:", RNAOfMyDNASeqB)


	# translate: RNA to Protein


	protOfMyDNASeqA = myDNASeqA.translate()
	print("\n\t The protein of seq A is:", protOfMyDNASeqA)
	protMyDNASeqB = myDNASeqB.translate()
	print("\t The protein of seq B is:", protMyDNASeqB)


	# comparison

	print("\n\t Compare the sequences char by char")
	print("\n\t seqA seqB")
	mismatchCount_int = 0 # keep a tally of the number of mismatches
	for i in range(len(myDNASeqA)):
		match_str = "  "
		if (myDNASeqA[i] != myDNASeqB[i]):
			mismatchCount_int += 1
			match_str = "!=" # replace this connection string to show that there is no match

		tmp_str = f"\t {myDNASeqA[i]} {match_str} {myDNASeqB[i]}"
		print(tmp_str)
	print(f"\n\t Total mismatches: {mismatchCount_int}")

	#end main()





# import biopython library
import Bio
from Bio.Seq import Seq

main() # run the program
