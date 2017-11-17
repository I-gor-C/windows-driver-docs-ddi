---
UID: NC.systemrng.PENTROPY_SOURCE_CALLBACK_FUNCTION
title: PENTROPY_SOURCE_CALLBACK_FUNCTION
author: windows-driver-content
description: 
ms.assetid: f85cc0e5-c277-4f4d-987c-9c6f61c5e750
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: systemrng.h
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

# PENTROPY_SOURCE_CALLBACK_FUNCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PENTROPY_SOURCE_CALLBACK_FUNCTION PentropySourceCallbackFunction; 

// Definition

NTSTATUS PentropySourceCallbackFunction 
(
	ENTROPY_SOURCE_HANDLE hEntropySource
	PVOID context
)
{...}

PENTROPY_SOURCE_CALLBACK_FUNCTION 


```

## -parameters

### -param hEntropySource: 
### -param context: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also