---
UID: NC.ntifs.RTL_FREE_STRING_ROUTINE
title: RTL_FREE_STRING_ROUTINE
author: windows-driver-content
description: 
ms.assetid: ef361dac-1f12-4eb2-af16-b4ea3bdf9fe5
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

# RTL_FREE_STRING_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RTL_FREE_STRING_ROUTINE RtlFreeStringRoutine; 

// Definition

VOID RtlFreeStringRoutine 
(
	__drv_freesMem(Mem)PVOID Buffer
)
{...}

RTL_FREE_STRING_ROUTINE PRTL_FREE_STRING_ROUTINE


```

## -parameters

### -param Buffer: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also