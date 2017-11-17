---
UID: NS.prefix._RX_PREFIX_TABLE
title: RX_PREFIX_TABLE
author: windows-driver-content
description: 
ms.assetid: 9d09d2fb-0e32-45dc-a76a-16d7df3e5ede
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: RX_PREFIX_TABLE, RX_PREFIX_TABLE, *PRX_PREFIX_TABLE
req.header: prefix.h
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

# RX_PREFIX_TABLE structure

## -description



## -struct-fields

### -field NODE_TYPE_CODE NodeTypeCode			
 	
### -field NODE_BYTE_SIZE NodeByteSize			
 	
### -field ULONG Version			
 	
### -field LIST_ENTRY MemberQueue			
 	
### -field ERESOURCE TableLock			
 	
### -field PRX_PREFIX_ENTRY TableEntryForNull			
 	
### -field BOOLEAN CaseInsensitiveMatch			
 	
### -field BOOLEAN IsNetNameTable			
 	
### -field ULONG TableSize			
 	
### -field ULONG Lookups			
 	
### -field ULONG FailedLookups			
 	
### -field ULONG Considers			
 	
### -field ULONG Compares			
 	
### -field LIST_ENTRY [RX_PREFIX_TABLE_DEFAULT_LENGTH] HashBuckets			
 	
## -remarks

## -see-also