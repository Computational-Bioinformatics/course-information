#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Originally written by: Oliver Bonham-Carter
# Ref: BioPython,
# Link: https://biopython.org/docs/1.75/api/Bio.pairwise2.html?highlight=pairwise2#module-Bio.pairwise2

# email: obonhamcarter@allegheny.edu
# Date: 24 March 2021
# Comment: A sequence alignment tool using Biopython.
# update: Now comes with a fasta file loader!

# How to run this script:
# Need to be in a Python Virtual Environment
# setup environment command:
#   python3 -m venv myvenv
# activate command (linux, MacOS):
#   source myvenv/bin/activate
# activate command (Windows):
#   c:myvenv/scripts/activate (or similar!)

# Install the Biopython library inside the virtual environment
# once you are running the virtual environment,
# you can run the following commands.
# Install Biopython command:
#   pip install biopython

# Install the Black reformatting library
# inside the virtual environment
#   pip install black

# Check your code's formatting with Black
#   python3 -m black <<scriptName.py>>

# Run a Python script program in virtual environment
# command:
#   python3 <<scriptName.py>>

DATE = "4 Oct 2022"
VERSION = "0.0.3"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"

# Bold High Intensity
BIBlack = "\033[1;90m"  # Black
BIRed = "\033[1;91m"  # Red
BIGreen = "\033[1;92m"  # Green
BIYellow = "\033[1;93m"  # Yellow
BIBlue = "\033[1;94m"  # Blue
BIPurple = "\033[1;95m"  # Purple
BICyan = "\033[1;96m"  # Cyan
BIWhite = "\033[1;97m"  # White

# Regular Colors
Black = "\033[0;30m"  # Black
Red = "\033[0;31m"  # Red
Green = "\033[0;32m"  # Green
Yellow = "\033[0;33m"  # Yellow
Blue = "\033[0;34m"  # Blue
Purple = "\033[0;35m"  # Purple
Cyan = "\033[0;36m"  # Cyan
White = "\033[0;37m"  # White

# Bold
BBlack = "\033[1;30m"  # Black
BRed = "\033[1;31m"  # Red
BGreen = "\033[1;32m"  # Green
BYellow = "\033[1;33m"  # Yellow
BBlue = "\033[1;34m"  # Blue
BPurple = "\033[1;35m"  # Purple
BCyan = "\033[1;36m"  # Cyan
BWhite = "\033[1;37m"  # White
BIWhite = "\033[1;97m"  # White


def getSeq():
    """function to ask user for a sequence and return it to a caller function"""
    prompt_str = BIGreen + "\t Enter a seq : " + BIWhite
    inputSeq_str = input(prompt_str)
    return Seq(inputSeq_str)


# end of getSeq()


def getGlobalAlign(seq1: str, seq2: str) -> None:
    """Complete global alignment using Needleman-Wunsch algorithm"""
    from Bio.pairwise2 import format_alignment

    print(
        BIYellow + "\t ~~~~ GLOBAL ALIGNMENTS (Needleman-Wunsch algorithm) ~~~~" + White
    )
    myAlignments = pairwise2.align.globalxx(seq1, seq2)
    # print(myAlignments) # print out sequence gap information

    # print out coded output
    # 	for thisAlignment in myAlignments:
    # 		print(thisAlignment)

    print(BICyan)
    for thisAlignment in myAlignments:
        print(format_alignment(*thisAlignment))
    print(BWhite)


# end of getGlobalAlign()


def getLocalAlign(seq1: str, seq2: str) -> None:
    """Complete local alignments using Smith-Waterman algorithm"""
    from Bio.pairwise2 import format_alignment

    print(BIYellow + "\t ~~~~ LOCAL ALIGNMENTS (Smith-Waterman algorithm) ~~~~" + White)
    myAlignments = pairwise2.align.localxx(seq1, seq2)
    # print(myAlignments) # print out sequence gap information

    # print out coded output
    # 	for thisAlignment in myAlignments:
    # 		print(thisAlignment)

    print(BICyan)
    for thisAlignment in myAlignments:
        print(format_alignment(*thisAlignment))
    print(BWhite)


# end of getLocalAlign()


def openFastaFile(fastaFile_str: str) -> dict:
    """open a fasta file, return the sequence record including name, sequence and other information. Please see biopython documentation for details."""
    try:
        from Bio import SeqIO  # biopython library
    except ModuleNotFoundError:
        print(
            printWithColour(
                BIRed,
                f"\t [+] The BioPython library is not installed.\n\t Please install, or use option -E \n\t to see other options to use {THISPROG}.",
            )
        )
        exit()

    # Determine whether the file exists
    if not exists(fastaFile_str):  # no file found?
        print(BIRed + f"\t [-] No file by that name: {fastaFile_str}" + White)
        exit()  # end program if no file has been found.

    print(f"\t [+] Opening FASTA file :{fastaFile_str}")

    # sequence_list = []
    # there may be multiple sequences in the fasta file. If so, process each one in the order that they were in the FASTA file.
    seq_dict = {} # make a dictionary
    seq_list = []
    for seq_record in SeqIO.parse(fastaFile_str, "fasta"):
        # print("") # drop a line
        print(f"\t [+] Sequence Name: {seq_record.id}")
        print(f"\t [+] Length of Sequence: {len(seq_record)}")
        #sequence_list.append(seq_record)
        seq_dict[seq_record.id] = seq_record.seq
        seq_list.append(seq_record.seq)
    print(f"\t seq_dict :: {seq_dict}")
    print(f"\t seq_list :: {seq_list}")
    
    # return seq_record
    return seq_dict,seq_list


# end of openFastaFile


def main() -> None:
    """Driver function for the program"""
    print(BIYellow + "\t ~~ Welcome to the alignment program! ~~" + White)
    prompt = (
        BIYellow
        + "\t Enter one of the following:\n\t <<F>> to enter a FASTA file containing only two sequences \n\t <<S>> to type-in sequences\n\t\t \U0001f600 S/F? : "
        + White
    )
    whatToDo_str = input(prompt)
    fname_str = ""  # define the fasta file for use in the code block
    seq1 = ""  # define these sequence variables for later
    seq2 = ""
    sequences_dict = {}
    if whatToDo_str.lower() == "s":  # type in some sequences
        print(BIYellow + "\t [+] Type your sequences below... " + White)
        # ask the user to enter a sequences
        seq1 = getSeq()
        seq2 = getSeq()
        getGlobalAlign(seq1, seq2)  # complete global alignment: Needleman-Wunsch
        print("----------------------")

        getLocalAlign(seq1, seq2)  # complete local alignment: Smith-Waterman
        print("----------------------")

        exit()
        # Or use hard-coded short sequences
        # seq1 = Seq("GATC")
        # seq2 = Seq("CATC")

    elif whatToDo_str.lower() == "f":  # load a fasta file of two sequences
        print(
            BIYellow
            + "\t [+] Type the name of the FASTA file containing two sequences below... "
            + White
        )
        prompt = BIYellow + "\t Filename : " + White
        fname_str = input(prompt)
        print(BICyan + f"\t [+] Entered File: {fname_str}" + White)
        sequences_dict,sequences_list  = openFastaFile(fname_str)
        # print(f"sequence_list = {sequences_list}")
        # input()

        # print(f"0 :: {sequences[0].seq}")
        # print(f"1 :: {sequences[1].seq}")

        # seq1 = sequences[0].seq
        # seq2 = sequences[1].seq
    

    else:
        print(BIRed + "\t [-] Response unclear: exiting" + White)
        exit()

    seq_0 = ""
    # for index in sequences_dict:
    #     print(f"\t Name : {index} :: Seq : {sequences_dict[index]}")

    seq0 = sequences_list[0] # first seq in the file; compare all sequences to this one
    print(f" first seq: {seq0}")
    print("\t ~~~~~~~ Alignments ~~~~~~~~\n")


    for i in sequences_dict:
        print(f"\t Top sequence by {i}")
        getGlobalAlign(seq0, sequences_dict[i])  # complete global alignment: Needleman-Wunsch
        print("----------------------")
        print(f"\t End of analysis of top sequence by {i}")
        input()

    print("======================")
    for i in sequences_dict:
        print(f"\t Top sequence by {i}")
        getLocalAlign(seq0, sequences_dict[i])  # complete local alignment: Smith-Waterman
        print("----------------------")
        print(f"\t End of analysis of top sequence by {i}")
        input()



# end of main()

# import statements
# check that the library is available to the code...
try:
    import Bio
except ModuleNotFoundError:
    print(
        "\t [-]"
        + BIRed
        + "\t Error loading BioPython."
        + White
        + "\n\t [-]"
        + BIRed
        + "\t Are you using your container or virtual environment?"
        + White
    )
    exit()


# load the libraries

from Bio import pairwise2
from Bio.Seq import Seq

from os.path import exists

# Run the program by calling the driver function, main()
main()
