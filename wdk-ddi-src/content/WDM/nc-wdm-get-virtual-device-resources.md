---
UID: NC.wdm.GET_VIRTUAL_DEVICE_RESOURCES
title: GET_VIRTUAL_DEVICE_RESOURCES
author: windows-driver-content
description: 
ms.assetid: 12d3c2e9-9cf2-48f6-8f45-24807c5ef4cb
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

# GET_VIRTUAL_DEVICE_RESOURCES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GET_VIRTUAL_DEVICE_RESOURCES GetVirtualDeviceResources; 

// Definition

VOID GetVirtualDeviceResources 
(
	PVOID Context
	PUINT8 CapturedBusNumbers
)
{...}

GET_VIRTUAL_DEVICE_RESOURCES PGET_VIRTUAL_DEVICE_RESOURCES


```

## -parameters

### -param Context: 
### -param CapturedBusNumbers: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also