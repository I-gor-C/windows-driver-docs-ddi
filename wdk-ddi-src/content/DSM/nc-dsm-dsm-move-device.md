---
UID: NC.dsm.DSM_MOVE_DEVICE
title: DSM_MOVE_DEVICE
author: windows-driver-content
description: 
ms.assetid: 0480cd83-20f3-4e8b-aa6c-734791911286
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

# DSM_MOVE_DEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_MOVE_DEVICE DsmMoveDevice; 

// Definition

NTSTATUS DsmMoveDevice 
(
	IN PVOID DsmContext
	IN PDSM_IDS DsmIds
	IN PVOID MPIOPath
	IN PVOID SuggestedPath
	IN ULONG Flags
)
{...}

DSM_MOVE_DEVICE 


```

## -parameters

### -param DsmContext: 
### -param DsmIds: 
### -param MPIOPath: 
### -param SuggestedPath: 
### -param Flags: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also