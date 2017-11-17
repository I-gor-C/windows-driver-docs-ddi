import json
import pdb
import re
import glob, os

## Get a dir two parents up (Compatible with Python 2.x) 
def twoDirUp():
    return os.path.abspath(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir), os.pardir))
## Get a dir one parent up  (Compatible with Python 2.x)
def oneDirUp():
    return os.path.abspath(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))    

global currPath
currPath=os.path.dirname(os.path.abspath(__file__))

global inputBaseDir
global outputBaseDir
global resourcesBaseDir
global dataLogsDir
global tocOutputDir
global linkDbDir
global generateHeaderTocOutput
global generateTocOutput
global headerCsvInputDir
global headerCsvOutputDir
global skeletonLogs
global stubOutputDir
global stubbyPath
global pageTypeDir
global pageTypeMissingDir
global pageTypeOutput
global offlineHeaderDir
global remoteDirBase
global scrappyOutputDir
global wdkDdiDir

inputBaseDir=str(oneDirUp())+"\\Input\\"
outputBaseDir=str(oneDirUp())+"\\Output\\"
resourcesBaseDir=oneDirUp()+"\\Resources\\"
dataLogsDir=outputBaseDir+'DataLogs\\'
## TODO Fix location of tocOutputDir and linkDbDir to be consistent with rest of dirs
tocOutputDir=oneDirUp()+'\\TOCOutput\\'
linkDbDir=oneDirUp()+"\\LinkDb\\"
generateHeaderTocOutput=outputBaseDir+'GenerateHeaderTocOutput\\'
generateTocOutput=outputBaseDir+'GenerateTocOutput\\'
headerCsvInputDir=str(oneDirUp())+"\\Input\\CSVS\\"
headerCsvOutputDir=outputBaseDir+"HeaderCsvOutput\\"
skeletonLogs=str(currPath)+"\\SkeletonLogs"
stubOutputDir=outputBaseDir+"StubFilesOutput\\"
# scrappyOutputDir=outputBaseDir+"ScrappyFilesOutput\\"
scrappyOutputDir=twoDirUp()+"\\wdk-ddi\\wdk-ddi-src\\content\\"
stubbyPath=oneDirUp()+"\\Stubby\\"
pageTypeDir=outputBaseDir+"PageTypeOutput\\IndividualProjects\\"
pageTypeMissingDir=outputBaseDir+"GenerateMissingHeaderListOutput\\"
pageTypeOutput=outputBaseDir+"PageTypeOutput\\"
offlineHeaderDir=os.path.join(inputBaseDir,"Headers")

remoteDirBase=os.path.abspath('\\\\WDGCP-WKFLOW01\\Win32SharedDrop\\Latest')
wdkDdiDir=os.path.join(twoDirUp(),"wdk-ddi-src")
# wdkDdiDir=os.path.join(globalVals.twoDirUp(),"wdk-ddi\\wdk-ddi-src")
# remoteDirBase=str(oneDirUp())+"\\TempCsv\\"
