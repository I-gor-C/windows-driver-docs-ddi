---
UID: NS.dbghelp._LOADED_IMAGE
title: LOADED_IMAGE
author: windows-driver-content
description: 
ms.assetid: 7126da74-a2a9-475b-af07-f1bcc8896bbc
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: LOADED_IMAGE, LOADED_IMAGE, *PLOADED_IMAGE
req.header: dbghelp.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# LOADED_IMAGE structure

## -description



## -struct-fields

### -field PSTR ModuleName			
 	
### -field HANDLE hFile			
 	
### -field PUCHAR MappedAddress			
 	
### -field PIMAGE_NT_HEADERS64 FileHeader			
 	
### -field PIMAGE_NT_HEADERS32 FileHeader			
 	
### -field PIMAGE_SECTION_HEADER LastRvaSection			
 	
### -field ULONG NumberOfSections			
 	
### -field PIMAGE_SECTION_HEADER Sections			
 	
### -field ULONG Characteristics			
 	
### -field BOOLEAN fSystemImage			
 	
### -field BOOLEAN fDOSImage			
 	
### -field BOOLEAN fReadOnly			
 	
### -field UCHAR Version			
 	
### -field LIST_ENTRY Links			
 	
### -field ULONG SizeOfImage			
 	
## -remarks

## -see-also