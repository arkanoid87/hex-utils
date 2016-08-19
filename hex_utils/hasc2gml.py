#!/usr/bin/python3
# coding=utf8
#
# Copyright (c) 2016 - Luís Moreira de Sousa
#
# Transforms ASCII encoded cartographic hexagonal grids [0] into GML.
# A geometric hexagon is generated for each grid cell and encoded as a feature
# in the output GML file. The cell value is saved in the 'value' attribute of 
# the new feature. 
#
# Author: Luís Moreira de Sousa (luis.de.sousa[@]protonmail.ch)
# Date: 31-03-2016 
#
# [0] https://github.com/ldesousa/HexAsciiBNF

import sys
from hex_utils.hasc import HASC

def wrongUsage():
    
    print("This programme requires two arguments:\n" +
          " - path to an input HASC file \n" +
          " - path to the output GML file \n" + 
          "Usage example: \n"
          "   hasc2gml /path/to/input.hasc /path/to/output.gml")
    sys.exit()


def processArguments(args):
    
    global inputFile
    global outputFile
    
    if len(args) < 3:
        wrongUsage() 
    else:
        inputFile = str(args[1])
        outputFile = str(args[2])
    

# ----- Main ----- #
def main():
        
    processArguments(sys.argv)
    
    hexGrid = HASC()
    
    try:
        hexGrid.loadFromFile(inputFile)
    except (ValueError, IOError) as ex:
        print("Error loading the grid %s: %s" % (inputFile, ex))
        sys.exit()
    print ("Loaded input HASC, converting...")
    
    try:
        hexGrid.saveAsGML(outputFile)
    except (ImportError, IOError) as ex:
        print("Error saving the grid %s: %s" % (inputFile, ex))
        sys.exit()
    print ("Conversion successfully completed.")

main()
    