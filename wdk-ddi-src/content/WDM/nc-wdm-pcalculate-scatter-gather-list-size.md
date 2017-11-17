---
UID: NC.wdm.PCALCULATE_SCATTER_GATHER_LIST_SIZE
title: PCALCULATE_SCATTER_GATHER_LIST_SIZE
author: windows-driver-content
description: 
ms.assetid: 6908c345-73f8-4b05-b911-6d3d8678ba42
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PCALCULATE_SCATTER_GATHER_LIST_SIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCALCULATE_SCATTER_GATHER_LIST_SIZE PcalculateScatterGatherListSize; 

// Definition

NTSTATUS PcalculateScatterGatherListSize 
(
	PDMA_ADAPTER DmaAdapter
	OPTIONAL PMDL Mdl
	PVOID CurrentVa
	ULONG Length
	PULONG ScatterGatherListSize
	OPTIONAL PULONG pNumberOfMapRegisters
)
{...}

PCALCULATE_SCATTER_GATHER_LIST_SIZE 


```

## -parameters

### -param DmaAdapter: 
### -param Mdl: 
### -param CurrentVa: 
### -param Length: 
### -param ScatterGatherListSize: 
### -param pNumberOfMapRegisters: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also