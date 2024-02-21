#!/usr/bin/env python3

import sys 


def main(src,dest):
	pass

	
# invoca main 
if len(sys.argv) == 3:
		main(sys.argv[1], sys.argv[2])
else:
		print("Uso:", sys.argv[0], "src_dir dest_dir")
		exit(1)