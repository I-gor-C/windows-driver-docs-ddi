---
UID: NS.namcache._NAME_CACHE_CONTROL_
title: NAME_CACHE_CONTROL_
author: windows-driver-content
description: 
ms.assetid: 4752f3d2-824b-427a-a3c4-b912a101e09f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NAME_CACHE_CONTROL_, NAME_CACHE_CONTROL, *PNAME_CACHE_CONTROL
req.header: namcache.h
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

# NAME_CACHE_CONTROL_ structure

## -description



## -struct-fields

### -field FAST_MUTEX NameCacheLock			
 	
### -field LIST_ENTRY ActiveList			
 	
### -field LIST_ENTRY FreeList			
 	
### -field __volatile ULONG EntryCount			
 	
### -field ULONG MaximumEntries			
 	
### -field ULONG MRxNameCacheSize			
 	
### -field ULONG NumberActivates			
 	
### -field ULONG NumberChecks			
 	
### -field ULONG NumberNameHits			
 	
### -field ULONG NumberNetOpsSaved			
 	
### -field ULONG [4] Spare			
 	
## -remarks

## -see-also