import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-v","--verbosity",help="increase output verbosity",
                    action="store_true")
args=parser.parse_args()

if args.verbosity:
   print "verbosity turned on"
#$ python prog.py --verbosity 1
#verbosity turned on
#$ python prog.py
#$ python prog.py --help
#usage: prog.py [-h][--verbosity VERBOSITY]

#optional arguments:
#  -h, --help            show this help message and exit
#  --verbosity VERBOSITY
#                        increase output verbosity
#$ python prog.py --verbosity
#usage: prog.py [-h][--verbosity VERBOSITY]
#prog.py: error: argument --verbosity: expected one argument
