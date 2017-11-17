---
UID: NC.storport.PStorPortBuildScatterGatherList
title: PStorPortBuildScatterGatherList
author: windows-driver-content
description: 
ms.assetid: 1ea95cb8-8701-44ff-bb22-b0dff82ebd08
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: storport.h
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

# PStorPortBuildScatterGatherList callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PStorPortBuildScatterGatherList Pstorportbuildscattergatherlist; 

// Definition

GETSGSTATUS Pstorportbuildscattergatherlist 
(
	PVOID HwDeviceExtension
	PVOID Mdl
	PVOID CurrentVa
	ULONG Length
	PPOST_SCATTER_GATHER_EXECUTE ExecutionRoutine
	PVOID Context
	BOOLEAN WriteToDevice
	PVOID ScatterGatherBuffer
	ULONG ScatterGatherBufferLength
)
{...}

PStorPortBuildScatterGatherList 


```

## -parameters

### -param HwDeviceExtension: 
### -param Mdl: 
### -param CurrentVa: 
### -param Length: 
### -param ExecutionRoutine: 
### -param Context: 
### -param WriteToDevice: 
### -param ScatterGatherBuffer: 
### -param ScatterGatherBufferLength: 



## -returns

Returns GETSGSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also