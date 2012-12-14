#!/bin/awk -f
# Account password retrieval
#
# Author: Svend Sorensen

# Field information:
# $1: username
# $2: account title
# $3: account password
# $4: comment
#
# Fields are separated by commas. Blank lines and comments (lines
# beginning with #) are ignored. All fields after the first three are
# ignored.
#
# Matching records are printed, with the account information sent to
# stderr, and the password sent to stdout.
#
# For example:
#
# # This is a comment
# user,example.com,password,comment

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

{
	username = $1
	title = $2
	# Only store password if account matches
	comment = $4

	if (title ~ regexp) {
		# One more match found
		n++

		# Print maching account information to stderr
		printf "title: %s, username: %s (%s)\n", title, username, comment > "/dev/stderr"

		password = $3
	}
}

# Print statistics to stderr
END {
	if (n == 1) {
		print password
	} else {
                print "Error: " n " matches" > "/dev/stderr"
		exit 1
	}
}
