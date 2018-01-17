import os
#A list of includes for file io
def createEmptyFiles(paths):
	for path in paths:
		f=open(path,"w")
		f.close()
def testPath(path):
	if not os.path.exists(path):
		os.mkdir(path)
def appendFile(path,content):
	f=open(path,"a")
	f.write(content)
	f.close()
def readFile(path):
	f=open(path,"r")
	content=f.read()
	f.close()
	return content
def processSeqFile(path):
	read=readFile(path)
	lines=read.split("\n")[1:]
	processedList=[]
	#lines longer then 20 assumed to be sequences
	for line in lines:
		if len(line)>20:
			delims=["    ","   ","  "," "]
			array=[]
			for delim in delims:
				if(len(line.split(delim))>1):
					array=line.split(delim)
					break

			processedList.append(array[1])
	return processedList

#generate all the directories needed for the given path
def generateDirectories(path):
	folders=path.split("/")
	curdir=""
	for folder in folders:
		curdir=os.path.join(curdir,folder)
		if not os.path.exists(curdir):
			os.mkdir(curdir)

def generateDirectoriesMult(paths):
	for path in paths:
		generateDirectories(path)

#processFusedGenes functions

#takes the protein, taxa, and sequence information and produce a FASTA format string for that sequence
def toFASTA(prot, taxa, seq):
	return ">"+prot+ " ["+taxa+"]\n"+seq+"\n\n"
	
#read the fusion event log and produce a dictionary to easily access the contents
def readFusionEventLog(path):
	f=open(path,"r")
	content=f.read()
	f.close()

	fusionDict={}

	lines=content.split("\n")
	for line in lines:
		array=line.split("\t")
		
		# if this line is not a header
		if (not "#" in line) and (len(line)!=0):
			fusionDict[int(array[0])]=array

	return fusionDict

#A simple function to generate a name for each test case base on the parameters
def name(model,seqLen,numFamily, numFusionEvent,totalEvolutionTime, numGeneration):
	name="M_"+str(model.replace("-",""))+"_SeqL_"+str(seqLen)+"_NFam_"+str(numFamily)+"_NFusions_"+str(numFusionEvent)+"_TEvo_"+str(totalEvolutionTime)+"_NGen_"+str(numGeneration)
	return name