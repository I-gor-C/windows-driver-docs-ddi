---
UID: NC.dsm.DSM_COMPLETION_ROUTINE
title: DSM_COMPLETION_ROUTINE
author: windows-driver-content
description: 
ms.assetid: c15a271d-200d-4ef5-8a75-d6d7d3be5eb1
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

# DSM_COMPLETION_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_COMPLETION_ROUTINE DsmCompletionRoutine; 

// Definition

VOID DsmCompletionRoutine 
(
	IN PVOID DsmId
	IN PIRP Irp
	IN PSCSI_REQUEST_BLOCK Srb
	IN PVOID DsmContext
)
{...}

DSM_COMPLETION_ROUTINE 


```

## -parameters

### -param DsmId: 
### -param Irp: 
### -param Srb: 
### -param DsmContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also