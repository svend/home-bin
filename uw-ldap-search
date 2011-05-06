#!/bin/sh

ldap_uri="ldap://directory.washington.edu"
ldap_base="o=University of Washington,c=US"

main()
{
	for s in "$@"; do
		filter="(|(cn=*$s*)(mail=$s*))"

		ldapsearch -H $ldap_uri -b "$ldap_base" -x "$filter"
	done
}

main "$@"
