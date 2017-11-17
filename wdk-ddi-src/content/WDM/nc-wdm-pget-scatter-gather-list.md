---
UID: NC.wdm.PGET_SCATTER_GATHER_LIST
title: PGET_SCATTER_GATHER_LIST
author: windows-driver-content
description: 
ms.assetid: 17259ea3-6fa0-443f-9836-319190057a42
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

# PGET_SCATTER_GATHER_LIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_SCATTER_GATHER_LIST PgetScatterGatherList; 

// Definition

NTSTATUS PgetScatterGatherList 
(
	PDMA_ADAPTER DmaAdapter
	PDEVICE_OBJECT DeviceObject
	PMDL Mdl
	PVOID CurrentVa
	ULONG Length
	PDRIVER_LIST_CONTROL ExecutionRoutine
	PVOID Context
	BOOLEAN WriteToDevice
)
{...}

PGET_SCATTER_GATHER_LIST 


```

## -parameters

### -param DmaAdapter: 
### -param DeviceObject: 
### -param Mdl: 
### -param CurrentVa: 
### -param Length: 
### -param ExecutionRoutine: 
### -param Context: 
### -param WriteToDevice: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also