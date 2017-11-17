---
UID: NS.fcbtable._RX_FCB_TABLE
title: RX_FCB_TABLE
author: windows-driver-content
description: 
ms.assetid: f564f415-e822-498a-9348-4d8027562c19
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: RX_FCB_TABLE, RX_FCB_TABLE, *PRX_FCB_TABLE
req.header: fcbtable.h
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

# RX_FCB_TABLE structure

## -description



## -struct-fields

### -field NODE_TYPE_CODE NodeTypeCode			
 	
### -field NODE_BYTE_SIZE NodeByteSize			
 	
### -field __volatile ULONG Version			
 	
### -field BOOLEAN CaseInsensitiveMatch			
 	
### -field USHORT NumberOfBuckets			
 	
### -field __volatile LONG Lookups			
 	
### -field __volatile LONG FailedLookups			
 	
### -field __volatile LONG Compares			
 	
### -field ERESOURCE TableLock			
 	
### -field PRX_FCB_TABLE_ENTRY TableEntryForNull			
 	
### -field LIST_ENTRY [RX_FCB_TABLE_NUMBER_OF_HASH_BUCKETS] HashBuckets			
 	
## -remarks

## -see-also