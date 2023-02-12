#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A hello world program.  Cool, right?"""


DATE = "2 Sept 2022"
VERSION = "i"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"

# Bold colour list
colour_list =['\033[1;30m',
'\033[1;31m',
'\033[1;32m',
'\033[1;33m',
'\033[1;34m',
'\033[1;35m',
'\033[1;36m',
'\033[1;37m',
'\033[1;90m',
'\033[1;91m',
'\033[1;92m',
'\033[1;93m',
'\033[1;94m',
'\033[1;95m',
'\033[1;96m']

BIWhite='\033[1;97m'      # White

# Main banner
banner1_str = """
\t
\t ██╗  ██╗███████╗██╗     ██╗      ██████╗
\t ██║  ██║██╔════╝██║     ██║     ██╔═══██╗
\t ███████║█████╗  ██║     ██║     ██║   ██║
\t ██╔══██║██╔══╝  ██║     ██║     ██║   ██║
\t ██║  ██║███████╗███████╗███████╗╚██████╔╝
\t ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝

\t ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ ██╗
\t ██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗██║
\t ██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║██║
\t ██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║╚═╝
\t ╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝██╗
\t  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝
\t ----------------------------------------------
"""

#
<<<<<<< HEAD
# TODO: Please remove the 'TO-DOs' when you have resolved this part of your lab.
=======
# TODO: Please remove the 'TODOs' when you have resolved this part of your lab.
>>>>>>> 102c7bb010c3300f093a977a475e264c446aab89
#Alternative banner
#banner1_str = """
#\t ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
#\t ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
#\t ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
#\t ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
#\t ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
#\t ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
#\t
#\t ███████╗ ██████╗ ██████╗ ███████╗██╗   ██╗███████╗██████╗ ██╗
#\t ██╔════╝██╔═══██╗██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗██║
#\t █████╗  ██║   ██║██████╔╝█████╗  ██║   ██║█████╗  ██████╔╝██║
#\t ██╔══╝  ██║   ██║██╔══██╗██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚═╝
#\t ██║     ╚██████╔╝██║  ██║███████╗ ╚████╔╝ ███████╗██║  ██║██╗
#\t ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝
#\t -------------------------------------------------------------
#"""

# banner ref: https://manytools.org/hacker-tools/ascii-banner/

def get_platformType() -> str:
	"""Function to dermine the OS type."""
	platforms = {
	'darwin' : 'OSX',
	'win32'  : 'Windows',
	'linux1' : 'Linux',
	'linux2' : 'Linux'}
	if sys.platform not in platforms:
		return sys.platform
	return platforms[sys.platform]
#end of get_platformType()


def main() -> str:
	"""Drives the program"""
	for i in range(3):
		randomColour_str = random.choice(colour_list) # choose a random colour to display the title screen.

	# print the hello world already!!
		print(randomColour_str + banner1_str + BIWhite)

	# report the perceived OS type
	platform_str = get_platformType()

	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		#print("\t" + " \U0001f5ff \U0001F608 \U0001F601" * 8)
		print("\t This code is running in a Linux or OSX environment.")
		#print("\n\t+ \U0001f600 ")
	else:
		print("\t This code is running in a Windows environment.")
	#end of main()


############################################################################

# import statements
import os, random, sys

# Run the code by calling main()
# TODO: you will have to remove the comment below as well.
# main()
