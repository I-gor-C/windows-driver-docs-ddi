---
UID: NS.extsfns._KDEXTS_LOCK_INFO
title: KDEXTS_LOCK_INFO
author: windows-driver-content
description: 
ms.assetid: 99940c6c-d010-4b33-ae86-bd9a5a08ea34
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KDEXTS_LOCK_INFO, KDEXTS_LOCK_INFO, *PKDEXTS_LOCK_INFO
req.header: extsfns.h
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

# KDEXTS_LOCK_INFO structure

## -description



## -struct-fields

### -field ULONG SizeOfStruct			
 	
### -field ULONG64 Address			
 	
### -field ULONG64 OwningThread			
 	
### -field BOOL ExclusiveOwned			
 	
### -field ULONG NumOwners			
 	
### -field ULONG ContentionCount			
 	
### -field ULONG NumExclusiveWaiters			
 	
### -field ULONG NumSharedWaiters			
 	
### -field PULONG64 pOwnerThreads			
 	
### -field PULONG64 pWaiterThreads			
 	
## -remarks

## -see-also