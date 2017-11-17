---
UID: NC.dsm.DSM_INTERPRET_ERROR
title: DSM_INTERPRET_ERROR
author: windows-driver-content
description: 
ms.assetid: 626100c4-f26e-4010-82dd-0301b3c57594
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsm.h
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

# DSM_INTERPRET_ERROR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_INTERPRET_ERROR DsmInterpretError; 

// Definition

ULONG DsmInterpretError 
(
	IN PVOID DsmContext
	IN PVOID DsmId
	IN PSCSI_REQUEST_BLOCK Srb
	IN OUT PNTSTATUS Status
	OUT PBOOLEAN Retry
)
{...}

DSM_INTERPRET_ERROR 


```

## -parameters

### -param DsmContext: 
### -param DsmId: 
### -param Srb: 
### -param Status: 
### -param Retry: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also