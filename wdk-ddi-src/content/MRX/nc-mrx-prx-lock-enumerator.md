---
UID: NC.mrx.PRX_LOCK_ENUMERATOR
title: PRX_LOCK_ENUMERATOR
author: windows-driver-content
description: 
ms.assetid: 0cb3f891-f15a-452d-acd4-0f057a4e505c
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

# PRX_LOCK_ENUMERATOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRX_LOCK_ENUMERATOR PrxLockEnumerator; 

// Definition

BOOLEAN PrxLockEnumerator 
(
	IN OUT PMRX_SRV_OPEN SrvOpen
	IN OUT PVOID *ContinuationHandle
	OUT PLARGE_INTEGER FileOffset
	OUT PLARGE_INTEGER LockRange
	OUT PBOOLEAN IsLockExclusive
)
{...}

PRX_LOCK_ENUMERATOR 


```

## -parameters

### -param SrvOpen: 
### -param *ContinuationHandle: 
### -param FileOffset: 
### -param LockRange: 
### -param IsLockExclusive: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also