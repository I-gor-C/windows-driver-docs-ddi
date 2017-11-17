import json
import pdb
import re
import os
import sys
import glob
from distutils.dir_util import copy_tree
import globalVals

def returnNoExtension(headerName):
    headerDotHLess=headerName
    if(headerDotHLess.endswith(".hpp")):
        headerDotHLess=headerDotHLess[:-4]
    elif(headerDotHLess.endswith(".h")):
        headerDotHLess=headerDotHLess[:-2]
    # NOTE THESE ARE THE BAD CASES BELOW
    elif(headerDotHLess.endswith(".idl")):
        pass
    elif headerDotHLess.endswith(".w"):
        pass
    else:
        print("HEADER NOT FOUND")
        pdb.set_trace()
    return headerDotHLess
allProjects=glob.glob(os.path.join(os.path.abspath(globalVals.twoDirUp()),("wdk-ddi-src\\content"))+"\~*")
allHeaders= set(glob.glob(os.path.join(os.path.abspath(globalVals.twoDirUp()),("wdk-ddi-src\\content"))+"\*"))- set(allProjects)

# Determine what projects to look at.
if len(sys.argv)>=2:
    projects=[sys.argv[1]]
else:
    projects=allProjects


with open('../OwnerInfo/links.json') as linksJson:
    linksDict = json.load(linksJson)

with open('../OwnerInfo/owners.json') as ownersJson:
    ownersDict = json.load(ownersJson)


projectToHeaders=dict()
for header in ownersDict:

    if ownersDict[header]['project'] not in projectToHeaders:
        projectToHeaders[ownersDict[header]['project']]=[]
    projectToHeaders[ownersDict[header]['project']].append(header)



# Note this may differ
for _project in projects:

    projectS=os.path.basename(_project)[1:].lower()

    headerTechTypeApiDict=dict()
    headerTypeApiDict=dict()
    # if projectS not in headerTechTypeApiDict:
    #     headerTechTypeApiDict[projectS]=dict()
    # else:
    #     #SHOULD NOT ALREADY EXIST
    #     pdb.set_trace()

    headers=[]

    if projectS in projectToHeaders:
        headers=projectToHeaders[projectS]



    ## TODO Make the portal for the header
    for header in headers:

        headerDotHLess=returnNoExtension(header)

        # NOTE Determine if project is multi level
        projectInHeader=""

        if header in ownersDict:
            projectInHeader=ownersDict[header]['project']

        currHeaderDir=os.path.join(os.path.abspath(globalVals.twoDirUp()),"wdk-ddi-src","content",headerDotHLess)
        if(not os.path.exists(currHeaderDir)):
            print(currHeaderDir+" does not exist.")
            continue

        allNonPortalMdFilesInCurrHeader=set(glob.glob(os.path.join(currHeaderDir,"*")))-set(glob.glob(os.path.join(currHeaderDir,"~PORTAL~*")))

        #NOTE GOTTA FIND WHICH ONES IN THERE HEADERS BELONG TO WHAT
        if header not in headerTechTypeApiDict:
            headerTechTypeApiDict[header]=dict()
            headerTypeApiDict[header]=dict()
        else:
            #SHOULD NOT ALREADY EXIST
            pdb.set_trace()

        # NOTE This
        for aNonPortalMd in list(allNonPortalMdFilesInCurrHeader):
            if os.path.basename(aNonPortalMd).startswith("~") or os.path.basename(aNonPortalMd).startswith("__P"):
                continue
            inYaml=False
            yamlDict=dict()
            with open(aNonPortalMd,encoding="utf8") as fBuffer:
                for line in fBuffer:
                    if(line.startswith("---")):
                        inYaml=not inYaml
                    elif(inYaml):
                        splitLine=line.split(":")
                        try:
                            yamlDict[splitLine[0]]=splitLine[1].strip()
                        except IndexError as identifier:
                            #NOTE THis occurs when the YAML block has multi line comments.
                            pass
                        
                    elif(line.startswith("# ")):

                        yamlDict["pretty"]=line[2:].strip()
                        break
            #NOTE Might have to change the windows-devices


            if yamlDict["ms.technology"] not in headerTechTypeApiDict[header]:
                headerTechTypeApiDict[header][yamlDict["ms.technology"]]=dict()
            if yamlDict["ms.topic"] not in headerTechTypeApiDict[header][yamlDict["ms.technology"]]:
                headerTechTypeApiDict[header][yamlDict["ms.technology"]][yamlDict["ms.topic"]]=[]
            headerTechTypeApiDict[header][yamlDict["ms.technology"]][yamlDict["ms.topic"]].append([yamlDict['pretty'],aNonPortalMd,yamlDict['description']])

            if yamlDict["ms.topic"] not in headerTypeApiDict[header]:
                headerTypeApiDict[header][yamlDict["ms.topic"]]=[]
            headerTypeApiDict[header][yamlDict["ms.topic"]].append([yamlDict['pretty'],aNonPortalMd,yamlDict['description']])

        headerPortalPath=os.path.join(currHeaderDir,str("~PORTAL~"+headerDotHLess+".md"))
        # if(os.path.exists(headerPortalPath)):

        print (headerPortalPath)

        with open(headerPortalPath, "w",encoding="utf-8") as fBuffer:
            # Title: "<header name>"
            # This <header name> is used by <friendly name1>, <friendly name2>. For more information, see
            #
            # -[Friendly name1](URL)
            # -[Friendly name2](URL)

            # %$Note:&% Get the URL and friendly name from the Tech JSON.

            linesInHeaderFile=["# "+headerDotHLess.title()+".h header\n", "\n"]
            linesInHeaderFile.append("\nThis header is used by ")
            # Build a list of technologies, identified by currTech, that are used by this header file
            techList={}
            for currTech in headerTechTypeApiDict[header]:
                # pdb.set_trace()
                if currTech=="windows-devices":
                    continue
                    # pass
                # Get the friendly name of currTech, if it is available
                if currTech in linksDict:
                    techList[currTech]=linksDict[currTech]['Long Title']
                else:
                    techList[currTech]=currTech

            # Build the list of technologies
            if techList:
                techListKeys = ", ".join(techList.values())

                linesInHeaderFile.append(techListKeys + ". For more information, see\n")
                # Build [Friendlyname](URL)
                for key in techList:
                    linesInHeaderFile.append("- [%s](..content/_%s)\n" % (techList[key], key))
            else:
                linesInHeaderFile.append("unknown technology.\n")

            # Build the list of programming interfaces
            linesInHeaderFile.append("\n"+ headerDotHLess.title()+".h contain these programming interfaces:\n\n")
            apiByTypeDict = {"function":["\n## Functions\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "callback":["\n## Callback functions\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "struct":["\n## Structures\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "ioctl":["\n## I/O control codes\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "enum":["\n## Enumerations\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "interface":["\n## Interfaces\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "macro":["\n## Macros\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "unknown":["\n## Unknown types\n\n| Title   | Description   |\n| ---- |:---- |\n"]}
            for topicType in headerTypeApiDict[header]:
               # The topicType should be one of the keys in the apiByTypeDict
                if topicType in apiByTypeDict:
                    # Keep inserting the APIs in the list of apiByTypeDict[topicType], where
                    # topicType is a key (function, struct, callback, etc)
                    for topic in headerTypeApiDict[header][topicType]:
                        if(not topic[2]):
                            topic[2]="TBD"
                        apiByTypeDict[topicType].append("| ["+topic[0]+"](" +os.path.basename(topic[1])+") | "+topic[2] +" |\n")
                # For the unlikely case, where the API type is not a key in apiByTypeDict. Put these APIs in unknown.
                else:
                    for topic in headerTypeApiDict[header][topicType]:
                        if(not topic[2]):
                            topic[2]="TBD"
                        apiByTypeDict["unknown"].append("| ["+topic[0]+"](" +os.path.basename(topic[1])+") | "+topic[2] +" |\n")

            # Sort and print the programming interfaces
            for apiType in apiByTypeDict:
                if (len(apiByTypeDict[apiType]) > 1):
                    # Let's sort each apiType in apiByTypeDict
                    apiByTypeDict[apiType][1:] = sorted(apiByTypeDict[apiType][1:])
                    for i in range(len(apiByTypeDict[apiType])):
                        linesInHeaderFile.append(apiByTypeDict[apiType][i])

            fBuffer.writelines(linesInHeaderFile)





    # TODO Work on the things here

    # Get the friendly name of projectS
    if projectS in linksDict:
        friendly = linksDict[projectS]['Long Title']
    else:
        friendly = projectS.title()

    # Print the title and intro
    linesInProjectFile=["# "+friendly+"\n\n",
                "Overview of the " +friendly+" technology.\n\n"
                ]

    # Check if there are headers associated with the projectS technology,
    # and if there are, print the list of headers.
    if headerTechTypeApiDict:
        linesInProjectFile.append("To develop "+friendly+", you need these headers:\n\n")
        for eachHeader in headerTechTypeApiDict:
            # Create a link to the header
            headerDotHLess=returnNoExtension(eachHeader)
            currHeaderOut=os.path.join("..\\",headerDotHLess,str("~PORTAL~"+headerDotHLess+".md"))
            linesInProjectFile.append(" * ["+eachHeader+"](" +currHeaderOut+")\n" )
    else:
        linesInProjectFile.append("The "+friendly+" technology is not associated with any headers.\n")

    # Insert the OP conceptual link
    if projectS in linksDict:
        linesInProjectFile.append("\nFor the programming guide, see ["+friendly+"]("+linksDict[projectS]['conceptualPath']+").\n")
    else:
        linesInProjectFile.append("\n\n")

    # Build a dictionary of key api types, and values as lists
    apiTypeDict = {"function":["\n## Functions\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "callback":["\n## Callback functions\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "struct":["\n## Structures\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "enum":["\n## Enumerations\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "ioctl":["\n## I/O control codes\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "interface":["\n## Interfaces\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "macro":["\n## Macros\n\n| Title   | Description   |\n| ---- |:---- |\n"],
                "unknown":["\n## Unknown types\n\n| Title   | Description   |\n| ---- |:---- |\n"]}

    # API types are identified here as currTech
    for eachHeader in headerTechTypeApiDict:
        if projectS not in headerTechTypeApiDict[eachHeader]:
            continue
        for currTech in headerTechTypeApiDict[eachHeader][projectS]:
            # Build the table of the APIs by type=currTech
            for currApi in headerTechTypeApiDict[eachHeader][projectS][currTech]:
                if(not currApi[2]):
                    currApi[2]="TBD"
                apiTypeDict[currTech].append("| ["+currApi[0]+"](" +os.path.join("..\\",returnNoExtension(eachHeader),os.path.basename(currApi[1]))+") | "+currApi[2] +" |\n")

    # Sort and print the APIs for each type.
    for apiType in apiTypeDict:
        if (len(apiTypeDict[apiType]) > 1):
            # sort the items in the list except for first item
            apiTypeDict[apiType][1:] = sorted(apiTypeDict[apiType][1:])
            for i in range(len(apiTypeDict[apiType])):
                linesInProjectFile.append(apiTypeDict[apiType][i])

    techPortalPath = os.path.join(_project,str("~PORTAL~"+projectS+".md"))

    with open(techPortalPath, "w",encoding="utf-8") as fBuffer:
        fBuffer.writelines(linesInProjectFile)
