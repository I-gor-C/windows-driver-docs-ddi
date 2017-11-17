---
UID: NS.ntifs.PUSN_RECORD_V4
title: PUSN_RECORD_V4
author: windows-driver-content
description: 
ms.assetid: 384328a6-1722-4732-88ab-ac8973f4fb66
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PUSN_RECORD_V4, USN_RECORD_V4, *PUSN_RECORD_V4
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

# PUSN_RECORD_V4 structure

## -description



## -struct-fields

### -field USN_RECORD_COMMON_HEADER Header			
 	
### -field FILE_ID_128 FileReferenceNumber			
 	
### -field FILE_ID_128 ParentFileReferenceNumber			
 	
### -field USN Usn			
 	
### -field ULONG Reason			
 	
### -field ULONG SourceInfo			
 	
### -field ULONG RemainingExtents			
 	
### -field USHORT NumberOfExtents			
 	
### -field USHORT ExtentSize			
 	
### -field USN_RECORD_EXTENT [1] Extents			
 	
## -remarks

## -see-also