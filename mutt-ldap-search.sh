#!/bin/sh

ldap_uri="ldap://directory.washington.edu"
ldap_base="o=University of Washington,c=US"

print_results()
{
	mail=
	name=
	title=

	while read s; do
		case "$s" in
		dn:*)
			# New entry
			if [ -n "$mail" -a -n "$name" ]; then
				echo "$mail	$name	$title"
			fi

			# Clear all variables
			mail=
			name=
			title=
			;;
		mail:*)
			mail=${s#mail:[ 	]*}
			;;
		cn:*)
			name=${s#cn:[ 	]*}
			;;
		title:*)
			title=${s#title:[ 	]*}
			;;
		esac
	done

	# Catch last entry
	if [ -n "$mail" -a -n "$name" ]; then
		echo "$mail	$name	$title"
	fi
}

main()
{
	echo "Mutt requires this line."

	for s in "$@"; do
		filter="(|(cn=*$s*)(mail=$s*))"

		ldapsearch -H $ldap_uri -b "$ldap_base" -x "$filter" mail cn title | print_results | sort | uniq
	done
}

main "$@"
