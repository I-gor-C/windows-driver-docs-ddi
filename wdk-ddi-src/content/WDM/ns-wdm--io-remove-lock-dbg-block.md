---
UID: NS.wdm._IO_REMOVE_LOCK_DBG_BLOCK
title: IO_REMOVE_LOCK_DBG_BLOCK
author: windows-driver-content
description: 
ms.assetid: d01bc06d-d2ae-4187-bc42-acb09c493c94
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IO_REMOVE_LOCK_DBG_BLOCK, IO_REMOVE_LOCK_DBG_BLOCK
req.header: wdm.h
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

# IO_REMOVE_LOCK_DBG_BLOCK structure

## -description



## -struct-fields

### -field LONG Signature			
 	
### -field ULONG HighWatermark			
 	
### -field LONGLONG MaxLockedTicks			
 	
### -field LONG AllocateTag			
 	
### -field LIST_ENTRY LockList			
 	
### -field KSPIN_LOCK Spin			
 	
### -field __volatile LONG LowMemoryCount			
 	
### -field ULONG [4] Reserved1			
 	
### -field PVOID Reserved2			
 	
### -field PIO_REMOVE_LOCK_TRACKING_BLOCK Blocks			
 	
## -remarks

## -see-also