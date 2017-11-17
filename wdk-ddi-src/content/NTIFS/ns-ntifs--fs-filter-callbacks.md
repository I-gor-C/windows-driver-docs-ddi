---
UID: NS.ntifs._FS_FILTER_CALLBACKS
title: FS_FILTER_CALLBACKS
author: windows-driver-content
description: 
ms.assetid: fe11057e-86b3-4fdc-a1db-0a507ecc6c87
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: FS_FILTER_CALLBACKS, FS_FILTER_CALLBACKS, *PFS_FILTER_CALLBACKS
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

# FS_FILTER_CALLBACKS structure

## -description



## -struct-fields

### -field ULONG SizeOfFsFilterCallbacks			
 	
### -field ULONG Reserved			
 	
### -field PFS_FILTER_CALLBACK PreAcquireForSectionSynchronization			
 	
### -field PFS_FILTER_COMPLETION_CALLBACK PostAcquireForSectionSynchronization			
 	
### -field PFS_FILTER_CALLBACK PreReleaseForSectionSynchronization			
 	
### -field PFS_FILTER_COMPLETION_CALLBACK PostReleaseForSectionSynchronization			
 	
### -field PFS_FILTER_CALLBACK PreAcquireForCcFlush			
 	
### -field PFS_FILTER_COMPLETION_CALLBACK PostAcquireForCcFlush			
 	
### -field PFS_FILTER_CALLBACK PreReleaseForCcFlush			
 	
### -field PFS_FILTER_COMPLETION_CALLBACK PostReleaseForCcFlush			
 	
### -field PFS_FILTER_CALLBACK PreAcquireForModifiedPageWriter			
 	
### -field PFS_FILTER_COMPLETION_CALLBACK PostAcquireForModifiedPageWriter			
 	
### -field PFS_FILTER_CALLBACK PreReleaseForModifiedPageWriter			
 	
### -field PFS_FILTER_COMPLETION_CALLBACK PostReleaseForModifiedPageWriter			
 	
### -field PFS_FILTER_CALLBACK PreQueryOpen			
 	
### -field PFS_FILTER_COMPLETION_CALLBACK PostQueryOpen			
 	
## -remarks

## -see-also