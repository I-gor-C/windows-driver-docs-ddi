---
UID: NC.wdm.GET_SET_DEVICE_DATA
title: GET_SET_DEVICE_DATA
author: windows-driver-content
description: 
ms.assetid: a30f5fc4-ab96-4800-98d4-a838f938784f
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

# GET_SET_DEVICE_DATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GET_SET_DEVICE_DATA GetSetDeviceData; 

// Definition

_IRQL_requires_same_ ULONG GetSetDeviceData 
(
	PVOID Context
	ULONG DataType
	PVOID Buffer
	ULONG Offset
	ULONG Length
)
{...}

GET_SET_DEVICE_DATA PGET_SET_DEVICE_DATA


```

## -parameters

### -param Context: 
### -param DataType: 
### -param Buffer: 
### -param Offset: 
### -param Length: 



## -returns

Returns _IRQL_requires_same_ ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also