---
UID: NS.ntifs.PUSN_RECORD_V3
title: PUSN_RECORD_V3
author: windows-driver-content
description: 
ms.assetid: c111f203-c3fb-431b-bd0d-1cb4818bbebb
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PUSN_RECORD_V3, USN_RECORD_V3, *PUSN_RECORD_V3
req.header: ntifs.h
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

# PUSN_RECORD_V3 structure

## -description



## -struct-fields

### -field ULONG RecordLength			
 	
### -field USHORT MajorVersion			
 	
### -field USHORT MinorVersion			
 	
### -field FILE_ID_128 FileReferenceNumber			
 	
### -field FILE_ID_128 ParentFileReferenceNumber			
 	
### -field USN Usn			
 	
### -field LARGE_INTEGER TimeStamp			
 	
### -field ULONG Reason			
 	
### -field ULONG SourceInfo			
 	
### -field ULONG SecurityId			
 	
### -field ULONG FileAttributes			
 	
### -field USHORT FileNameLength			
 	
### -field USHORT FileNameOffset			
 	
### -field WCHAR [1] FileName			
 	
## -remarks

## -see-also