---
UID: NC.dsm.DSM_INTERPRET_ERROR_EX
title: DSM_INTERPRET_ERROR_EX
author: windows-driver-content
description: 
ms.assetid: 5a09ff80-0bd7-4f23-b477-0af2852cd04b
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

# DSM_INTERPRET_ERROR_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_INTERPRET_ERROR_EX DsmInterpretErrorEx; 

// Definition

ULONG DsmInterpretErrorEx 
(
	IN PVOID DsmContext
	IN PVOID DsmId
	IN PSCSI_REQUEST_BLOCK Srb
	IN OUT PNTSTATUS Status
	OUT PBOOLEAN Retry
	OUT PLONG RetryInterval
	 ...
)
{...}

DSM_INTERPRET_ERROR_EX 


```

## -parameters

### -param DsmContext: 
### -param DsmId: 
### -param Srb: 
### -param Status: 
### -param Retry: 
### -param RetryInterval: 
### -param ...: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also