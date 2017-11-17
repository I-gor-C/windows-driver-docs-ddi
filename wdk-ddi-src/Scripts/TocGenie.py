import json
import pdb
import re
import os
import sys
import glob
from distutils.dir_util import copy_tree
import globalVals

standaloneVer=True
scrappyOutputDir=globalVals.scrappyOutputDir

if len(sys.argv)>=2:
    standaloneVer=False
    scrappyOutputDir=sys.argv[1]
def removeWhiteSpace(match):
    return match.group(0).replace("_","").replace(" ","")

def convertTo(someInp):
    return re.sub('([A-Z]|[a-z])(\s|_)',removeWhiteSpace,someInp)
#a simple class for storing a project's information
class Project():
    def __init__(self, toc_name):
        self.toc_name = toc_name
        #self.xml_files = []
        #self.md_files = []
        self.header_info = []



# NOTE: the pretty_name_file must be comprised of project mappings in the form: projName = human readable name
# for example:
# bltooth = bluetooth
# p_mb = mobile broadband

def build_map(pretty_name_file, stub_output_path, md_location_path):
    all_files_list=set()
    found_files=dict()
    output_string=""
    project_dict = {}
    msdn_to_info_dict = {}
    project_api_dict = {}

    output_path = "content"
    with open(pretty_name_file, 'r', encoding="utf8")as f:
        for line in f:
            
            search = line.replace("\n","").split(";")
            original_name = search[0]
            # toc name is what will appear in the final TOC
            pretty_name = search[1]
            
            # instantiate object to store project info
            project_dict[original_name] = (pretty_name)

    all_headers_stubby= glob.glob(os.path.join(os.path.abspath(globalVals.twoDirUp()),("wdk-ddi-src/content"))+"\*")
    
    for a_header_stubby in all_headers_stubby:
        if(os.path.basename(a_header_stubby).startswith("~")):
            continue
        baseProject=os.path.basename(os.path.abspath(a_header_stubby))
        baseWdkPath=os.path.join(os.path.abspath(globalVals.twoDirUp()),("wdk-ddi-src/content"),baseProject)
        
        output_md_files=glob.glob(os.path.abspath(a_header_stubby)+"/*.md")
        print("Mapping "+str(baseProject)+" to wdk-ddi")
        # #pdb.set_trace()
        # copy_tree(os.path.abspath(a_header_stubby), baseWdkPath)
        # pdb.set_trace()
        for output_md_file in output_md_files:
            #pdb.set_trace()
            
            with open(output_md_file, 'r',encoding='utf-8') as a_md_file:
                msdn_id=None
                uid=None
                title=None
                actualProjectName=None
                header=None
                for line in a_md_file:
                    if(line.startswith("ms.assetid: ")):
                        msdn_id=line.split(": ")[1].strip()
                    elif line.startswith("ms.technology: "):
                        actualProjectName=line.split(": ")[1].strip().lower()
                    elif line.startswith("req.header:"):
                        header=line.split(": ")[1].strip()
                    elif(line.startswith("UID: ")):
                        uid=line.split(": ")[1].strip()
                    elif(line.startswith("# ") and msdn_id and uid):
                        title=line.replace("# ","").replace("\n","")
                if actualProjectName=='windows-devices':
                    actualProjectName="TBD"
                if(actualProjectName!="TBD"):
                    try:
                        actualProjectName= project_dict[actualProjectName]
                    except KeyError as e:

                        print(actualProjectName+ "not found in the mapping. Skipping Pretty title")           
                    
                        

                if(actualProjectName not in msdn_to_info_dict):
                    msdn_to_info_dict[actualProjectName]={}
                
                header=header.title().replace(".H",".h")
                if(header not in msdn_to_info_dict[actualProjectName]):
                    msdn_to_info_dict[actualProjectName][header]=[] 
               
                msdn_to_info_dict[actualProjectName][header].append("["+str(title)+"]("+str(output_path)+"\\"+
                str(os.path.basename(os.path.dirname(output_md_file)))+"\\"+str(os.path.basename(output_md_file))+")" )
                
                # msdn_to_info_dict[msdn_id.upper()]=[uid,os.path.basename(os.path.dirname(output_md_file)),name,os.path.basename(output_md_file)]
        #pdb.set_trace()
                        #msdn_to_info_dict[k].append(v)
                        #except KeyError:
                         
    ## NOTE This portion creates the Title to its Project and XML association

    for project in sorted(msdn_to_info_dict):
        
        if(project in msdn_to_info_dict):
            output_string+="# "+project+"\n"
            
        for header in sorted(msdn_to_info_dict[project]):
            output_string+="## "+header+"\n"
            for api in sorted(msdn_to_info_dict[project][header]):
                output_string+="### "+api+"\n"
   
    # finds the headers for a project and attaches them to the project objects in the main dictionary

    return output_string

def build_map_seperate_projects(pretty_name_file, stub_output_path, md_location_path):
    all_files_list=set()
    found_files=dict()
    output_string=""
    project_dict = {}
    msdn_to_info_dict = {}
    project_api_dict = {}

    output_path = "content"
    with open(pretty_name_file, 'r', encoding="utf8")as f:
        for line in f:
            
            search = line.replace("\n","").split(";")
            original_name = search[0]
            # toc name is what will appear in the final TOC
            pretty_name = search[1]
            
            # instantiate object to store project info
            project_dict[original_name] = (pretty_name)

    all_headers_stubby= glob.glob(os.path.join(os.path.abspath(globalVals.twoDirUp()),("wdk-ddi-src/content"))+"\*")
    
    for a_header_stubby in all_headers_stubby:
        if(os.path.basename(a_header_stubby).startswith("~")):
            continue
        baseProject=os.path.basename(os.path.abspath(a_header_stubby))
        baseWdkPath=os.path.join(os.path.abspath(globalVals.twoDirUp()),("wdk-ddi-src/content"),baseProject)
        
        output_md_files=glob.glob(os.path.abspath(a_header_stubby)+"/*.md")
        print("Mapping "+str(baseProject)+" to wdk-ddi")
        # #pdb.set_trace()
        # copy_tree(os.path.abspath(a_header_stubby), baseWdkPath)
        # pdb.set_trace()
        for output_md_file in output_md_files:
            #pdb.set_trace()
            if os.path.basename(output_md_file).startswith("~") or os.path.basename(output_md_file).startswith("_"):
                continue
            with open(output_md_file, 'r',encoding='utf-8') as a_md_file:
                msdn_id=None
                uid=None
                title=None
                actualProjectName=None
                header=None
                for line in a_md_file:
                    if(line.startswith("ms.assetid: ")):
                        msdn_id=line.split(": ")[1].strip()
                    elif line.startswith("ms.technology: "):
                        actualProjectName=line.split(": ")[1].strip().lower()
                    elif line.startswith("req.header:"):
                        header=line.split(": ")[1].strip()
                    elif(line.startswith("UID: ")):
                        uid=line.split(": ")[1].strip()
                    elif(line.startswith("# ") and msdn_id and uid):
                        title=line.replace("# ","").replace("\n","")
                if actualProjectName=='windows-devices':
                    actualProjectName="TBD"
                # NOTE This version does not want the pretty titles    
                # if(actualProjectName!="TBD"):
                #     try:
                #         actualProjectName= project_dict[actualProjectName]
                #     except KeyError as e:
                #         print(actualProjectName+ "not found in the mapping. Skipping Pretty title")           
                    

                if(actualProjectName not in msdn_to_info_dict):
                    msdn_to_info_dict[actualProjectName]={}
                try:
                    header=header.title().replace(".H",".h")
                except AttributeError as identifier:
                    pdb.set_trace()
                
                if(header not in msdn_to_info_dict[actualProjectName]):
                    msdn_to_info_dict[actualProjectName][header]=[] 
               
                msdn_to_info_dict[actualProjectName][header].append("["+str(title)+"]("+str(output_path)+"\\"+
                str(os.path.basename(os.path.dirname(output_md_file)))+"\\"+str(os.path.basename(output_md_file))+")" )
                
                # msdn_to_info_dict[msdn_id.upper()]=[uid,os.path.basename(os.path.dirname(output_md_file)),name,os.path.basename(output_md_file)]
        #pdb.set_trace()
                        #msdn_to_info_dict[k].append(v)
                        #except KeyError:
                         
    ## NOTE This portion creates the Title to its Project and XML association
    
    for project in sorted(msdn_to_info_dict):

        actualProjectName=project

        if(project!="TBD"):
            try:
                actualProjectName= project_dict[project]
            except KeyError as e:
                print(project+ "not found in the mapping. Skipping Pretty title")
                      
        output_string="# "+actualProjectName+"\n"
        
        for header in sorted(msdn_to_info_dict[project]):
            output_string+="## "+header+"\n"
            for api in sorted(msdn_to_info_dict[project][header]):
                output_string+="### "+api+"\n"
        print("writing TOC file for "+str(project))
        
        dirForCurrToc=os.path.join(globalVals.wdkDdiDir,"content",str("~"+str(project) ) )
        if not os.path.exists(dirForCurrToc):
            os.makedirs(dirForCurrToc)
        with open(os.path.join(dirForCurrToc,"TOC.md"), "w") as f:
            for line in output_string:
                f.write(line)

    # finds the headers for a project and attaches them to the project objects in the main dictionary



#name file contains the project names as they should appear in the TOC
name_file = os.path.join(globalVals.oneDirUp(),"Scripts\\PrettyTitles\\Pretty.txt")
#json file contains mapping of headers to their respective projects
# json_file = os.path.join(globalVals.pageTypeOutput,'ProjectHeaderAPI.json')

toc_lines = []
stub_files_location = globalVals.stubOutputDir
if standaloneVer:
    build_map_seperate_projects(name_file, stub_files_location, stub_files_location)
else:
    toc_dict = build_map(name_file, stub_files_location, stub_files_location)
    if not os.path.exists("Cache\\"):
        os.makedirs("Cache\\")
    with open("Cache\\TOC_Sample.md", "w") as f:
        for line in toc_dict:
            f.write(line)
    with open(os.path.join(globalVals.wdkDdiDir,"TOC.md"), "w") as f:
        for line in toc_dict:
            f.write(line)
