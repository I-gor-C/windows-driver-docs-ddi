---
UID: NC.wdm.PTM_RM_NOTIFICATION
title: PTM_RM_NOTIFICATION
author: windows-driver-content
description: 
ms.assetid: 2f273733-27d7-425b-b5f1-75cad17b3e1e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
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

# PTM_RM_NOTIFICATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PTM_RM_NOTIFICATION PtmRmNotification; 

// Definition

NTSTATUS PtmRmNotification 
(
	PKENLISTMENT EnlistmentObject
	PVOID RMContext
	PVOID TransactionContext
	ULONG TransactionNotification
	PLARGE_INTEGER TmVirtualClock
	ULONG ArgumentLength
	PVOID Argument
)
{...}

PTM_RM_NOTIFICATION 


```

## -parameters

### -param EnlistmentObject: 
### -param RMContext: 
### -param TransactionContext: 
### -param TransactionNotification: 
### -param TmVirtualClock: 
### -param ArgumentLength: 
### -param Argument: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also