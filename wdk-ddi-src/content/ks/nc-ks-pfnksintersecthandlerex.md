---
UID: NC.ks.PFNKSINTERSECTHANDLEREX
title: PFNKSINTERSECTHANDLEREX
author: windows-driver-content
description: 
ms.assetid: f4f8fdb1-39a0-45a8-9e13-46976d3329ab
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSINTERSECTHANDLEREX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSINTERSECTHANDLEREX Pfnksintersecthandlerex; 

// Definition

NTSTATUS Pfnksintersecthandlerex 
(
	PVOID Context
	PIRP Irp
	PKSP_PIN Pin
	PKSDATARANGE DataRange
	PKSDATARANGE MatchingDataRange
	ULONG DataBufferSize
	PVOID Data
	PULONG DataSize
)
{...}

PFNKSINTERSECTHANDLEREX 


```

## -parameters

### -param Context: 
### -param Irp: 
### -param Pin: 
### -param DataRange: 
### -param MatchingDataRange: 
### -param DataBufferSize: 
### -param Data: 
### -param DataSize: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also