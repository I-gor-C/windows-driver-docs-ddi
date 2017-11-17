---
UID: NC.wdm.SET_VIRTUAL_DEVICE_DATA
title: SET_VIRTUAL_DEVICE_DATA
author: windows-driver-content
description: 
ms.assetid: a721ecf6-a60c-4463-90ad-cec2f086f358
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

# SET_VIRTUAL_DEVICE_DATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SET_VIRTUAL_DEVICE_DATA SetVirtualDeviceData; 

// Definition

ULONG SetVirtualDeviceData 
(
	PVOID Context
	USHORT VirtualFunction
	PVOID Buffer
	ULONG Offset
	ULONG Length
)
{...}

SET_VIRTUAL_DEVICE_DATA PSET_VIRTUAL_DEVICE_DATA


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