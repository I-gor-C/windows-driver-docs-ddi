---
UID: NC.wdm.PTM_PROPAGATE_ROUTINE
title: PTM_PROPAGATE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: e7bb81db-41a0-4887-b15e-78c2026fc27c
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

# PTM_PROPAGATE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PTM_PROPAGATE_ROUTINE PtmPropagateRoutine; 

// Definition

NTSTATUS PtmPropagateRoutine 
(
	PVOID PropagationCookie
	PVOID CallbackData
	NTSTATUS PropagationStatus
	GUID TransactionGuid
)
{...}

PTM_PROPAGATE_ROUTINE 


```

## -parameters

### -param PropagationCookie: 
### -param CallbackData: 
### -param PropagationStatus: 
### -param TransactionGuid: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also