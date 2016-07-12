#!/usr/bin/python3
# coding=utf8
#
# Copyright (c) 2016 - Luís Moreira de Sousa
#
# Creates a rectangular ESRI ASCII grids by sampling a a given surface.
#
# Author: Luís Moreira de Sousa (luis.de.sousa[@]protonmail.ch)
# Date: 03-06-2016 
#
# [0] https://github.com/ldesousa/HexAsciiBNF

import math
from hex_utils.asc import ASC
from surfaceSimple import fun

# ----- Main ----- #
def main():

	x_start = 0
	y_start = 0
	x_end = 2001
	y_end = 2001
	size = 20
	
	grid = ASC()
	grid.init(	
		math.trunc((x_end - x_start) / size), 
		math.trunc((y_end - y_start) / size), 
		x_start,
		y_start,
		size, "")
	
	print("(0,0): " + str(fun(0,0)))	
	print("(0,2000): " + str(fun(0,2000)))
	print("(2000,0): " + str(fun(2000,0)))
	print("(2000,2000): " + str(fun(2000,2000)))
	
	x_start += size / 2
	y_start += size / 2
	
	for i in range(grid.ncols):
		for j in range(grid.nrows):
			grid.set(i, grid.nrows - j - 1, 
				fun(x_start + i * size, y_start + j * size))
		
	grid.save("temp.asc")
	
	print("Created new grid successfully")
	
main()