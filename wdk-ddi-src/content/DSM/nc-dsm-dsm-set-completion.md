---
UID: NC.dsm.DSM_SET_COMPLETION
title: DSM_SET_COMPLETION
author: windows-driver-content
description: 
ms.assetid: 63641177-e259-4df7-b5c4-e8f421d4e66f
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

# DSM_SET_COMPLETION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_SET_COMPLETION DsmSetCompletion; 

// Definition

VOID DsmSetCompletion 
(
	IN PVOID DsmContext
	IN PVOID DsmId
	IN PIRP Irp
	IN PSCSI_REQUEST_BLOCK Srb
	IN OUT PDSM_COMPLETION_INFO DsmCompletion
)
{...}

DSM_SET_COMPLETION 


```

## -parameters

### -param DsmContext: 
### -param DsmId: 
### -param Irp: 
### -param Srb: 
### -param DsmCompletion: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also