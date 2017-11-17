---
UID: NC.wdm.PMAP_TRANSFER_EX
title: PMAP_TRANSFER_EX
author: windows-driver-content
description: 
ms.assetid: 1214ffef-d1e4-418b-9424-4cf46f709c32
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

# PMAP_TRANSFER_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMAP_TRANSFER_EX PmapTransferEx; 

// Definition

NTSTATUS PmapTransferEx 
(
	PDMA_ADAPTER DmaAdapter
	PMDL Mdl
	PVOID MapRegisterBase
	ULONGLONG Offset
	ULONG DeviceOffset
	PULONG Length
	BOOLEAN WriteToDevice
	PSCATTER_GATHER_LIST ScatterGatherBuffer
	ULONG ScatterGatherBufferLength
	PDMA_COMPLETION_ROUTINE DmaCompletionRoutine
	PVOID CompletionContext
)
{...}

PMAP_TRANSFER_EX 


```

## -parameters

### -param DmaAdapter: 
### -param Mdl: 
### -param MapRegisterBase: 
### -param Offset: 
### -param DeviceOffset: 
### -param Length: 
### -param WriteToDevice: 
### -param ScatterGatherBuffer: 
### -param ScatterGatherBufferLength: 
### -param DmaCompletionRoutine: 
### -param CompletionContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also