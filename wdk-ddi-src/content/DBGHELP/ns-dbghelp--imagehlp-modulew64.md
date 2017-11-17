---
UID: NS.dbghelp._IMAGEHLP_MODULEW64
title: IMAGEHLP_MODULEW64
author: windows-driver-content
description: 
ms.assetid: 341443ea-b233-4bb4-b808-cc469506bf50
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMAGEHLP_MODULEW64, IMAGEHLP_MODULEW64, *PIMAGEHLP_MODULEW64
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

# IMAGEHLP_MODULEW64 structure

## -description



## -struct-fields

### -field DWORD SizeOfStruct			
 	
### -field DWORD64 BaseOfImage			
 	
### -field DWORD ImageSize			
 	
### -field DWORD TimeDateStamp			
 	
### -field DWORD CheckSum			
 	
### -field DWORD NumSyms			
 	
### -field SYM_TYPE SymType			
 	
### -field WCHAR [32] ModuleName			
 	
### -field WCHAR [256] ImageName			
 	
### -field WCHAR [256] LoadedImageName			
 	
### -field WCHAR [256] LoadedPdbName			
 	
### -field DWORD CVSig			
 	
### -field WCHAR [MAX_PATH * 3] CVData			
 	
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