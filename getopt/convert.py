import sys
import getopt

def usage():
    print "python convert.py -i input_file -o output_file"
    print "python convert.py -h"    

def convert():
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:") #this mean that h is switch may has not args
                                                     #i & o must has args
    except getopt.GetoptError as err:
        print 'ERROR:', err
        sys.exit(1)

    input_file=""
    output_file=""
    for op, value in opts:
        if op == "-i":
            input_file = value
        elif op == "-o":
            output_file = value
        elif op == "-h":
            usage()
            sys.exit()
    print input_file
    print output_file

def main():
    convert()

if __name__=="__main__":
    main()
