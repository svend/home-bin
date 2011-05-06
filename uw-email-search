#!/bin/sh

ldap_uri="ldap://directory.washington.edu"
ldap_base="o=University of Washington,c=US"

print_results()
{
	mail=
	name=

	while read s; do
		case "$s" in
		dn:*)
			# New entry

			# Clear all variables
			name=
			mail=
			;;
		mail:*)
			mail=${s#mail:[ 	]*}
			;;
		cn:*)
			name=${s#cn:[ 	]*}
			;;
		esac

		# Print result if we have both a name and an email address
		# FIXME: Won't work if name comes after multiple email addresses
		if [ -n "$mail" -a -n "$name" ]; then
			echo "$name <$mail>"
			mail=
		fi
	done

	# Catch last entry
	if [ -n "$mail" -a -n "$name" ]; then
		echo "$name <$mail>"
	fi
}

main()
{
	for s in "$@"; do
		filter="(|(cn=*$s*)(mail=$s*))"

		ldapsearch -H $ldap_uri -b "$ldap_base" -x "$filter" mail cn | print_results | sort | uniq
	done
}

main "$@"
