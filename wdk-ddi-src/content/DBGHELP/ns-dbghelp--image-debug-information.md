---
UID: NS.dbghelp._IMAGE_DEBUG_INFORMATION
title: IMAGE_DEBUG_INFORMATION
author: windows-driver-content
description: 
ms.assetid: dd6295a8-66c8-4601-a129-43cac169f916
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMAGE_DEBUG_INFORMATION, IMAGE_DEBUG_INFORMATION, *PIMAGE_DEBUG_INFORMATION
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

# IMAGE_DEBUG_INFORMATION structure

## -description



## -struct-fields

### -field LIST_ENTRY List			
 	
### -field DWORD ReservedSize			
 	
### -field PVOID ReservedMappedBase			
 	
### -field USHORT ReservedMachine			
 	
### -field USHORT ReservedCharacteristics			
 	
### -field DWORD ReservedCheckSum			
 	
### -field DWORD ImageBase			
 	
### -field DWORD SizeOfImage			
 	
### -field DWORD ReservedNumberOfSections			
 	
### -field PIMAGE_SECTION_HEADER ReservedSections			
 	
### -field DWORD ReservedExportedNamesSize			
 	
### -field PSTR ReservedExportedNames			
 	
### -field DWORD ReservedNumberOfFunctionTableEntries			
 	
### -field PIMAGE_FUNCTION_ENTRY ReservedFunctionTableEntries			
 	
### -field DWORD ReservedLowestFunctionStartingAddress			
 	
### -field DWORD ReservedHighestFunctionEndingAddress			
 	
### -field DWORD ReservedNumberOfFpoTableEntries			
 	
### -field PFPO_DATA ReservedFpoTableEntries			
 	
### -field DWORD SizeOfCoffSymbols			
 	
### -field PIMAGE_COFF_SYMBOLS_HEADER CoffSymbols			
 	
### -field DWORD ReservedSizeOfCodeViewSymbols			
 	
### -field PVOID ReservedCodeViewSymbols			
 	
### -field PSTR ImageFilePath			
 	
### -field PSTR ImageFileName			
 	
### -field PSTR ReservedDebugFilePath			
 	
### -field DWORD ReservedTimeDateStamp			
 	
### -field BOOL ReservedRomImage			
 	
### -field PIMAGE_DEBUG_DIRECTORY ReservedDebugDirectory			
 	
### -field DWORD ReservedNumberOfDebugDirectories			
 	
### -field DWORD ReservedOriginalFunctionTableBaseAddress			
 	
### -field DWORD [2] Reserved			
 	
## -remarks

## -see-also