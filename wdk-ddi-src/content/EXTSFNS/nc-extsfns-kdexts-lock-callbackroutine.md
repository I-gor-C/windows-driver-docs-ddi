---
UID: NC.extsfns.KDEXTS_LOCK_CALLBACKROUTINE
title: KDEXTS_LOCK_CALLBACKROUTINE
author: windows-driver-content
description: 
ms.assetid: 0c0f2cb1-e8a9-434d-8eef-7cecc10092f5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# KDEXTS_LOCK_CALLBACKROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

KDEXTS_LOCK_CALLBACKROUTINE KdextsLockCallbackroutine; 

// Definition

HRESULT KdextsLockCallbackroutine 
(
	PKDEXTS_LOCK_INFO pLock
	PVOID Context
)
{...}

KDEXTS_LOCK_CALLBACKROUTINE 


```

## -parameters

### -param pLock: 
### -param Context: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also