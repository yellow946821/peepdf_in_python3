#!/usr/bin/env python

#
# peepdf is a tool to analyse and modify PDF files
#    http://peepdf.eternal-todo.com
#    By Jose Miguel Esparza <jesparza AT eternal-todo.com>
#
#    Copyright (C) 2011-2017 Jose Miguel Esparza
#
#    This file is part of peepdf.
#
#        peepdf is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        (at your option) any later version.
#
#        peepdf is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with peepdf.    If not, see <http://www.gnu.org/licenses/>.
#

'''
    Initial script to launch the tool
'''

import sys
import os
import re

from PDFCore import PDFParser


VT_KEY = 'fc90df3f5ac749a94a94cb8bf87e05a681a2eb001aef34b6a0084b8c22c97a64'

root = '/home/lai/Desktop/peepdf3'
folderName = '/home/lai/Desktop/peepdf3/contagio_Benign_OriginalName'
allFileList = os.listdir(folderName)

JSFolder = 'BenignJS'
if not (os.path.exists(JSFolder)):
	os.mkdir(JSFolder)
	print("create folder")
JSFolderPath = os.path.join(root,JSFolder)


##ret, pdf = pdfParser.parse(fileName, options.isForceMode, options.isLooseMode, options.isManualAnalysis)



testfile = ['3D_ch2mhill_pump_station_3.pdf'] ## , '02solp.pdf'
newLine = os.linesep
JS = 0
NoJS = 0
for fileName in testfile:
	print(fileName)
	
	output = ''
	##extractedUrisPerObject = []
	extractedJsPerObject = []
	pdfParser = PDFParser()
	ret, pdf = pdfParser.parse(os.path.join(folderName,fileName), True, False, False)
	
	print(pdf.getStats()['Versions'][0])
	
	##extractedUrisPerObject = pdf.getURIs(None, perObject=True)
	extractedJsPerObject = pdf.getJavascriptCode(None, perObject=True)
	'''
	for version in range(len(extractedUrisPerObject)):
	    for extractedUri in extractedUrisPerObject[version]:
		output += '%s (%d)%s' % (extractedUri[1], extractedUri[0], newLine)
		
	if output:
	    output += newLine
	'''   
	for version in range(len(extractedJsPerObject)):
	    for extractedJs in extractedJsPerObject[version]:
	    	output += '// peepdf comment: Javascript code located in object %d (version %d)%s%s%s' % (extractedJs[0],version,newLine*2,extractedJs[1],newLine*2)
		       
	'''
	if output is not '':
		newfilename = os.path.splitext(fileName)[0] + '.txt'
		f = open(os.path.join(JSFolderPath,newfilename), 'w')
		f.write(output)
		f.close()
		print '%-50s %s' % (fileName , "Done")
		JS += 1
	else: 
		print '%-50s %s' % (fileName , "No JS")
		NoJS += 1
	'''
	print(output)

##print 'JS: %d , NoJS: %d' % (JS , NoJS)







'''
fileName = '/home/lai/Desktop/peepdf/contagio_Benign_OriginalName/3D_ch2mhill_pump_station_3.pdf'

pdfParser = PDFParser()
ret, pdf = pdfParser.parse(fileName, True, True, True)
print os.path.basename(fileName)
print len(pdf.getStats()['Versions'])
print pdf.getStats()['Versions'][0]
print pdf.getStats()['Versions'][1]
##print pdf.body[0].getJSCode()
'''




'''
newLine = os.linesep
output = ''
extractedUrisPerObject = []
extractedJsPerObject = []



extractedUrisPerObject = pdf.getJavascriptCode(None, perObject=True)
for version in range(len(extractedUrisPerObject)):
    for extractedUri in extractedUrisPerObject[version]:
        output += '%s (%d)%s' % (extractedUri[1], extractedUri[0], newLine)
        
if output:
    output += newLine
for version in range(len(extractedJsPerObject)):
    for extractedJs in extractedJsPerObject[version]:
        output += '// peepdf comment: Javascript code located in object %d (version %d)%s%s%s' % (extractedJs[0],
                                                                                                  version,
                                                                                                  newLine*2,
                                                                                                  extractedJs[1],
                                                                                                  newLine*2)

print output





path = 'output.txt'
f = open(path, 'w')
f.write(output)
f.close()
'''
