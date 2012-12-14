#!/bin/awk -f
# Account password retrieval
#
# Author: Svend Sorensen

# Field information:
# $1: account description
# $2: account password
# $3: additional account information (optional)
#
# Fields are separated by commas. Blank lines and comments (lines
# beginning with #) are ignored. All fields after the first three are
# ignored.
#
# Matching records are printed, with the account description and information
# sent to stderr, and the password sent to stdout.
#
# For example:
#
# # This is a comment
# user@example.com,password,Comment

# Variables:
# regexp - Regular expression to search for
# filename - Name of current file

BEGIN {
	# Fields are separated by tabs
	FS = ","

	# Password
	password = ""

	# Number of matches
	n = 0;
}

# Skip blank lines
/^$/ {
	next
}

# Skip comments (lines beginning with #)
/^#/ {
	next
}

# Test description against regular expression
$1 ~ regexp {
	# One more match found
	n++

	# Print maching account information to stderr
	printf "# %s: %s (%s)\n", filename, $1, $3 > "/dev/stderr"

	password = $2
}

# Print statistics to stderr
END {
	if (n == 1) {
		print password
	} else {
                print "Error: " n " matches)" > "/dev/stderr"
		exit 1
	}
}
