---
UID: NC.extsfns.PENUMERATE_SYSTEM_LOCKS
title: PENUMERATE_SYSTEM_LOCKS
author: windows-driver-content
description: 
ms.assetid: c9afa64d-d6ba-4a50-8220-1e0a35c2e653
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

# PENUMERATE_SYSTEM_LOCKS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PENUMERATE_SYSTEM_LOCKS PenumerateSystemLocks; 

// Definition

HRESULT PenumerateSystemLocks 
(
	PDEBUG_CLIENT Client
	ULONG Flags
	KDEXTS_LOCK_CALLBACKROUTINE Callback
	PVOID Context
)
{...}

PENUMERATE_SYSTEM_LOCKS 


```

## -parameters

### -param Client: 
### -param Flags: 
### -param Callback: 
### -param Context: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also