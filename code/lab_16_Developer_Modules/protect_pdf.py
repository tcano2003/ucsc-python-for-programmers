#!/usr/bin/env python
"""(Optional) protect_pdf.py [-h for complete help] input_pdf_file
-p password [-o output_pdf_file] [-v for verbose]

Puts password protection on the renamed input_pdf_file.

If output_pdf_file is not given, it manufactures it as:
pdf_file - ".pdf" + '_protected' + ".pdf"

Demonstrates the optparse module for parsing the command line
options and putting them into suitably-named identifiers in a 
namespace. 
"""
import optparse  
import subprocess

def ProtectPDF(options):
    """options is a namespace with these attributes:
    
    input_pdf_file = file to be password protected
    user_pw = password
    output_pdf_file = password protected version
    verbose = True or False
    Note, the unprotected input_pdf_file still exists.
    """
    if not options.output_pdf_file:
        front, back = options.input_pdf_file.rsplit('.', 1)
        options.output_pdf_file = front + "_secured." + back
        
    command_sequence = ["pdftk", options.input_pdf_file,
                        "output", options.output_pdf_file,
                        "owner_pw", "FriedFlavors",
                        "user_pw", options.password, "allow",
                        "Printing", "DegradedPrinting",
                        "ScreenReaders"]
    if options.verbose:
        print "Calling:", " ".join(command_sequence)
        
    command_process = subprocess.Popen(command_sequence,
                                       stderr=subprocess.PIPE)
    some_output = False
    for line in command_process.stderr:
        some_output = True
        print line,
        
    if options.verbose and not some_output: # success!
        print "Done.",
        print "%s is password-protected with the password=%s" % (
            options.output_pdf_file, options.password)

def CollectCommand(parser):
    """Here we have the parser harvest the command line and
    we check that we have an appropriate arguments.
    """
    (options, args) = parser.parse_args()
    if len(args) != 1:  
        parser.error("A pdf file name is needed.")
    options.input_pdf_file = args[0]
    if not options.password:
        parser.error("A password is needed.")
    return options

def main():
    parser = SetUpParsing()
    options = CollectCommand(parser)
    ProtectPDF(options)

def SetUpParsing():
    """Calls add_option repeatedly, once for every unix-style
    option we need. """

    parser = optparse.OptionParser("%prog [-h for complete help] input_pdf_file -p password [-o output_pdf_file] [-v for verbose]")

    parser.add_option("-o", "--output_pdf_file", dest="output_pdf_file", default=None, help='OPTIONAL: Write the password-protected pdf file to output_pdf_file, if given.  Default is input_pdf_file with "secured" inserted before the ".pdf".')
    parser.add_option("-p", "--password", dest="password", help="password for protecting the input_pdf_file")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="OPTIONAL: Details of the processing are written to stdout.")
    return parser

if __name__ == "__main__":
    main()
