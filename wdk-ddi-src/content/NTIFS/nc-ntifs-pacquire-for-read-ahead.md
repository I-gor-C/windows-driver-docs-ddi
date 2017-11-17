---
UID: NC.ntifs.PACQUIRE_FOR_READ_AHEAD
title: PACQUIRE_FOR_READ_AHEAD
author: windows-driver-content
description: 
ms.assetid: c1267f89-c6c2-4f60-9aed-153aa80d15b9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntifs.h
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

# PACQUIRE_FOR_READ_AHEAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PACQUIRE_FOR_READ_AHEAD PacquireForReadAhead; 

// Definition

BOOLEAN PacquireForReadAhead 
(
	PVOID Context
	BOOLEAN Wait
)
{...}

PACQUIRE_FOR_READ_AHEAD 


```

## -parameters

### -param Context: 
### -param Wait: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also