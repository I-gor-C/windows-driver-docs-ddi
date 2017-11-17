---
UID: NS.fcb._NON_PAGED_FCB
title: NON_PAGED_FCB
author: windows-driver-content
description: 
ms.assetid: ae4e0f20-2c2e-4acb-b1e4-832ec60b1634
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NON_PAGED_FCB, NON_PAGED_FCB, *PNON_PAGED_FCB
req.header: fcb.h
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

# NON_PAGED_FCB structure

## -description



## -struct-fields

### -field NODE_TYPE_CODE NodeTypeCode			
 	
### -field NODE_BYTE_SIZE NodeByteSize			
 	
### -field SECTION_OBJECT_POINTERS SectionObjectPointers			
 	
### -field ERESOURCE HeaderResource			
 	
### -field ERESOURCE PagingIoResource			
 	
### -field FAST_MUTEX FileSizeLock			
 	
### -field LIST_ENTRY TransitionWaitList			
 	
### -field ULONG OutstandingAsyncWrites			
 	
### -field PKEVENT OutstandingAsyncEvent			
 	
### -field KEVENT TheActualEvent			
 	
### -field PVOID [2] MiniRdrContext			
 	
### -field FAST_MUTEX AdvancedFcbHeaderMutex			
 	
### -field ERESOURCE BufferedLocksResource			
 	
### -field PFCB FcbBackPointer			
 	
## -remarks

## -see-also