---
UID: NC.wdm.GET_VIRTUAL_DEVICE_DATA
title: GET_VIRTUAL_DEVICE_DATA
author: windows-driver-content
description: 
ms.assetid: 8763e55a-a114-4be7-a4fd-a9b80836d96c
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

# GET_VIRTUAL_DEVICE_DATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GET_VIRTUAL_DEVICE_DATA GetVirtualDeviceData; 

// Definition

ULONG GetVirtualDeviceData 
(
	PVOID Context
	USHORT VirtualFunction
	PVOID Buffer
	ULONG Offset
	ULONG Length
)
{...}

GET_VIRTUAL_DEVICE_DATA PGET_VIRTUAL_DEVICE_DATA


```

## -parameters

### -param Context: 
### -param VirtualFunction: 
### -param Buffer: 
### -param Offset: 
### -param Length: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also