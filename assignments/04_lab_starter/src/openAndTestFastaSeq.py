#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Original author: Oliver Bonham-Carter
# Date: 3 Oct 2022

# getting setup to run this script
# Need to be in a Python Virtual Environment
# command: python3 -m venv myvenv
# command (linux, MacOS): source myvenv/bin/activate
# command (Windows): c:myvenv/scripts/activate (or similar!)

# Install the Biopython library
# Command: pip install biopython
# Run a Python script program
# command: python3 scriptName.py


from os.path import exists

def openFastaFile(fastaFile_str):
	""" open a fasta file, return the sequence record including name, sequence and other information. Please see biopython documentation for details."""
	try:
		from Bio import SeqIO #biopython library
	except ModuleNotFoundError:
		print(printWithColour(BIRed,f"\t [+] The BioPython library is not installed.\n\t Please install, or use option -E \n\t to see other options to use {THISPROG}."))
		exit()

	# Determine whether the file exists
	if not exists(fastaFile_str): # no file found?
		print(f"\t [-] No file by that name: {fastaFile_str}")
		exit() # end program if no file has been found.


	print(f"\t [+] Opening FASTA file :{fastaFile_str}")

	# there may be multiple sequences in the fasta file. If so, process each one in the order that they were in the FASTA file.
	for seq_record in SeqIO.parse(fastaFile_str, "fasta"):
		print("") # drop a line
		print(f"\t [+] Sequence Name: {seq_record.id}")
		print(f"\t [+] First 50 bases of sequence data: {seq_record.seq[:50]}")
		print(f"\t [+] Length of Sequence: {len(seq_record)}")
		print("\t [+] Running some tests on sequence from BioPython ...")

		completeSequenceTests(seq_record) # for each iteration in this loop, send the current record to this function to further process the record.
	return seq_record
# end of openFastaFile

def main():
	""" print the sequence that we opened and then complete operations on it. """
	prmpt = "\t Enter the name of the FASTA file to open :"
	seqFileName_str = input(prmpt)
	# seqFileName_str = "3_seq.fasta" # used for debugging purposes
	seq_record = openFastaFile(seqFileName_str)
# end of main()

def completeSequenceTests(seq_record):
	""" function to run some tests over the inputted sequence. The inputted seq_record is sequence loaded from the openDnaSeq """
	print(f"\t\t - Further processing: {seq_record.id}")

	# Add four interesting tests or other code that you researched from biopython documentation. Two code blocks are requested and you can pick the other two yourself. Please be sure to print out your results with clear formatting to be readable.

	# TODO 1: Give the GC content of the DNA using GC(record.seq). Then determine the AT content percentage from this calculation.
	# print("GC content:")
	# print("AT content:")
	#
	#
	#
	# TODO 2: Give the protein sequence for the DNA.
	# See https://biopython.org/docs/1.75/api/Bio.Seq.html for ideas about how to do this.
	# print("Protein Content")
	#
	#
	#
	#
	# TODO 3
	# print("This test is : TODO")
	#
	#
	#
	#
	# TODO 4
	# print("This test is : TODO")
	#
	#
	#
	#
# end of completeSequenceTests()


main() # initiate the code by running the main function
