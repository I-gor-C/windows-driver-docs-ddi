---
UID: NC.mrx.PMRX_IS_LOCK_REALIZABLE
title: PMRX_IS_LOCK_REALIZABLE
author: windows-driver-content
description: 
ms.assetid: 5d535445-9c5c-4bb8-9501-b1ae00364534
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mrx.h
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

# PMRX_IS_LOCK_REALIZABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_IS_LOCK_REALIZABLE PmrxIsLockRealizable; 

// Definition

NTSTATUS PmrxIsLockRealizable 
(
	IN OUT PMRX_FCB Fcb
	IN PLARGE_INTEGER ByteOffset
	IN PLARGE_INTEGER Length
	IN ULONG LowIoLockFlags
)
{...}

PMRX_IS_LOCK_REALIZABLE 


```

## -parameters

### -param Fcb: 
### -param ByteOffset: 
### -param Length: 
### -param LowIoLockFlags: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also