---
UID: NS.wdbgexts._EXT_FIND_FILE
title: EXT_FIND_FILE
author: windows-driver-content
description: 
ms.assetid: 9d78e1e0-cee9-4eff-83f1-74bdfbeba555
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: EXT_FIND_FILE, EXT_FIND_FILE, *PEXT_FIND_FILE
req.header: wdbgexts.h
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

# EXT_FIND_FILE structure

## -description



## -struct-fields

### -field IN PCWSTR FileName			
 	
### -field IN ULONG64 IndexedSize			
 	
### -field IN ULONG ImageTimeDateStamp			
 	
### -field IN ULONG ImageCheckSum			
 	
### -field IN OPTIONAL PVOID ExtraInfo			
 	
### -field IN ULONG ExtraInfoSize			
 	
### -field IN ULONG Flags			
 	
### -field OUT PVOID FileMapping			
 	
### -field OUT ULONG64 FileMappingSize			
 	
### -field OUT HANDLE FileHandle			
 	
### -field OUT OPTIONAL PWSTR FoundFileName			
 	
### -field OUT ULONG FoundFileNameChars			
 	
## -remarks

## -see-also