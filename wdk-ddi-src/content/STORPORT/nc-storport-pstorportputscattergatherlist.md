---
UID: NC.storport.PStorPortPutScatterGatherList
title: PStorPortPutScatterGatherList
author: windows-driver-content
description: 
ms.assetid: 52f20d83-c6a5-4638-ab49-6193338e9edd
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

# PStorPortPutScatterGatherList callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PStorPortPutScatterGatherList Pstorportputscattergatherlist; 

// Definition

VOID Pstorportputscattergatherlist 
(
	PVOID HwDeviceExtension
	PSTOR_SCATTER_GATHER_LIST ScatterGatherList
	BOOLEAN WriteToDevice
)
{...}

PStorPortPutScatterGatherList 


```

## -parameters

### -param HwDeviceExtension: 
### -param ScatterGatherList: 
### -param WriteToDevice: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also