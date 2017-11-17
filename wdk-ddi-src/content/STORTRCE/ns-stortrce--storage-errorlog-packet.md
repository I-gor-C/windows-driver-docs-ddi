---
UID: NS.stortrce._STORAGE_ERRORLOG_PACKET
title: STORAGE_ERRORLOG_PACKET
author: windows-driver-content
description: 
ms.assetid: c997cb55-9399-48e9-838a-d73490972fab
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: STORAGE_ERRORLOG_PACKET, STORAGE_ERRORLOG_PACKET, *PSTORAGE_ERRORLOG_PACKET
req.header: stortrce.h
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

# STORAGE_ERRORLOG_PACKET structure

## -description



## -struct-fields

### -field UCHAR MajorFunctionCode			
 	
### -field UCHAR RetryCount			
 	
### -field USHORT DumpDataSize			
 	
### -field USHORT NumberOfStrings			
 	
### -field USHORT StringOffset			
 	
### -field USHORT EventCategory			
 	
### -field ULONG ErrorCode			
 	
### -field ULONG UniqueErrorValue			
 	
### -field ULONG FinalStatus			
 	
### -field ULONG SequenceNumber			
 	
### -field ULONG IoControlCode			
 	
### -field LARGE_INTEGER DeviceOffset			
 	
### -field ULONG [1] DumpData			
 	
## -remarks

## -see-also