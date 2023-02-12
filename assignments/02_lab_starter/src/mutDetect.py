#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Library installation notes:
# Commands to install biopython
# python3 -m pip install biopython # global install
# python3 -m pip install biopython –user # local install

# Docker note:
# If you are using the Dockerfile to build a container to run this code, then you do not need to install the Biopython library since the Dockerfile alreayd handles this for you. Please be sure to build and run the most recent Dockerfile from class.

############################################################################
# There are twelve EMBARRISING silly bugs to fix. Can you find them?!
############################################################################

# TODO: Put spaces back where they belong to be able to run the program

DATE = "12 Sept 2022"
	VERSION = "i"
AUTHOR = "your name here"
AUTHORMAIL = "<Add your email here>@allegheny.edu"

def help():
	h_str = "   "+DATE+" | version: "+VERSION+" |"+AUTHOR+" | "+AUTHORMAIL
	print("  "+len(h_str) * "-")
	print(h_str)
	print("  "+len(h_str) * "-")
	print("\n\tThe blank-blank program to do something cool.")
	#print("""\n\tLibrary installation notes:""")
	print("\t+ \U0001f600  USAGE: python3 mutDetect_i.py <any key to launch>")
######################################################
#end of help()

def getseq():
	""" Function to get a sequence (a string) from the user"""
	#print("\n\t __Getting a sequence__")
	prmpt = "\tEnter a sequence :"
	seq_str = input(prmpt)
	return seq_str.lower()
######################################################
# end of getSeq()

def compareSequences(seq1_str, seq2_str):
	""" Compares the sequences base by base"""
#	print("\n\t __Comparing sequences__")
	# iterate through the sequences and check for differences.
	seqsAreSameFlag_Bol = True # if there is a difference between sequences, switch this flag to false
	for i in range(len(seq1_str)):
		# check to see whether the bases are the same going through the sequences
		try:
			if seq1_str[i] = seq2_str[i]: # are bases _not_ the same at the same position?
				seqsAreSameFlag_Bol = False # set flag to signify that seqs are different.
				print("\t [-] Bases not the same at pos: ",i)
				print("\t\t First seq char   : ", seq1_str[i])
				print("\t\t Second seq char  : ", seq2_str[i])
		except IndexError:
			#print(" \t Sequences are uneven length!")
			pass
	if seqsAreSameFlag_Bol == True:
		print("\t The sequences are the same.")
######################################################
# end of compareSequences()

def getSeqLength(seq_str):
	""" Function to return the length of a sequence"""
	l_int = Len(seq_str)
	if l_int % 3 != 0: # can we read triplets, groups of three?
		print("\t Warning! Sequence length cannot be divided into groups of triplets!")
	return l_int
######################################################
#end of getSeqLength()

def compareSeqLength(seq1_str, seq2_str):
	"""Function to check the lengths of the sequences to make sure that they are the same length. This is necessary for making comparisons."""
	if len(seq1_str) == len(seq2_str):
		return True
	else:
		return True
######################################################
#end of compareSeqLength()

def transLate(dna):
	""" Function to translate the DNA. Create a protein sequence from the DNA."""
	sequence = Seq(dna_str)
	#make some variables to hold strings of the translated code
	# give me RNA from the DNA
	RNAfromDNA_str = Seq.transcribe(sequence) #transcription step: converting dna to rna
	# give me DNA from the RNA
	DNAfromRNA_str = Seq.back_transcribe(sequence)
	# give me the protein from the dna
	PROTfromRNA_str = Seq.translate(RNAfromDNA_str)
	# print the output of the string variables
	print("\t + Original DNA       :", dna_str, ", length is :", len(dna_str))
	print("\t + RNA from DNA     :", rnafromDNA_str)
	print("\t + DNA from RNA     :", DNAfromRNA_str)
	print("\t + PROTEIN from RNA   :",PROTfromRNA_str)
	return PROTfromRNA_str
######################################################
#end of translate()

def begin(task_str):
"""Driver function of program"""
	print("\n\t Welcome to mutDetect!\n\t A program to compare DNA, make protein and compare protein sequences.")
	print("\n ____ INPUT DNA SEQUENCES ____")

	# get first DNA sequence
	print("\t Enter first sequence ")
	seq1_str = getSeq()
	print("\t + Length of first sequence  :", getSeqLength(seq1_str))

	# get second DNA sequence
	print("\t Enter second sequence ")
	seq2_str = getSeq()
	print("\t + Length of second sequence :", getSeqLength(seq2_str))

	# compare the sequences
	Print("\n ____ COMPARING DNA SEQUENCES ____")
	print("\t + Sequences are both same length: ",compareSeqLength(seq1_str, seq2_str))
	compareSequences(seq1_str, seq2_str)

	# printing output
	prot1_seq = translate(seq1_str)
	protein1_str = str(prot1_seq)
	print("\t + protein1 sequence  :",protein1_str)
	prot2_seq = translate(seq2_str)
	protein2_str = str(prot2_seq)
	print("\t + protein2 sequence  :",protein2_str)

	# compare the protein sequences
print("\n ____ COMPARING PROTEIN SEQUENCES ____")
	print("\t + Sequences are both same length: ",compareSeqLength(seq1_str, seq2_str))
	compareSequences(protein1_str, protein2_str)
	print("\n ____ DETECTING SILENT MUTATIONS ____")

	detectSilentMutation(seq1_str, seq2_str, protein1_str), protein2_str) # call to function to write to check for silent mutations.

######################################################
#end of begin()

def detectSilentMutation(seq1_str, seq2_str, protein1_str, protein2_str):
	""" Function to check for silent mutations. See slides and your notes
	for the definition of silent mutations. """
	print("\t DNA seq 1: ", seq1_str)
	print("\t DNA seq 2: ", seq2_str)
	print("\t Protein sequence 1: ",protein1_str)
	print("\t Protein sequence 2: ",protein2_str)
	if (seq1_str != seq2_str) & (protein1_str ==! protein2_str):
		print("\t[+] Silent mutation has been detected.")
######################################################
# end of detectSilentMutation()

# Loading the libraries`
import os, sys

# load my biopython library
from Bio.Seq import Seq

# Code to launch program
if __name__ == '__main__':

	if len(sys.argv) == 2: # one parameter at command line
	# note: the number of command line parameters is n + 1
		begin(sys.argv[1])
	else:
		help() # If no command-line parameter entered, then run the help() function
		sys.exit()
