---
UID: NS.dbghelp._IMAGEHLP_MODULE64
title: IMAGEHLP_MODULE64
author: windows-driver-content
description: 
ms.assetid: 3e086eca-db7e-4118-a715-4f04c53f1ecb
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMAGEHLP_MODULE64, IMAGEHLP_MODULE64, *PIMAGEHLP_MODULE64
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

# IMAGEHLP_MODULE64 structure

## -description



## -struct-fields

### -field DWORD SizeOfStruct			
 	
### -field DWORD64 BaseOfImage			
 	
### -field DWORD ImageSize			
 	
### -field DWORD TimeDateStamp			
 	
### -field DWORD CheckSum			
 	
### -field DWORD NumSyms			
 	
### -field SYM_TYPE SymType			
 	
### -field CHAR [32] ModuleName			
 	
### -field CHAR [256] ImageName			
 	
### -field CHAR [256] LoadedImageName			
 	
### -field CHAR [256] LoadedPdbName			
 	
### -field DWORD CVSig			
 	
### -field CHAR [MAX_PATH * 3] CVData			
 	
### -field DWORD PdbSig			
 	
### -field GUID PdbSig70			
 	
### -field DWORD PdbAge			
 	
### -field BOOL PdbUnmatched			
 	
### -field BOOL DbgUnmatched			
 	
### -field BOOL LineNumbers			
 	
### -field BOOL GlobalSymbols			
 	
### -field BOOL TypeInfo			
 	
### -field BOOL SourceIndexed			
 	
### -field BOOL Publics			
 	
### -field DWORD MachineType			
 	
### -field DWORD Reserved			
 	
## -remarks

## -see-also