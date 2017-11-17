---
UID: NC.extsfns.PGET_DEVICE_OBJECT_INFO
title: PGET_DEVICE_OBJECT_INFO
author: windows-driver-content
description: 
ms.assetid: 463807dc-1ff9-473e-a928-266ae73aff9c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# PGET_DEVICE_OBJECT_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_DEVICE_OBJECT_INFO PgetDeviceObjectInfo; 

// Definition

HRESULT PgetDeviceObjectInfo 
(
	IN PDEBUG_CLIENT Client
	IN ULONG64 DeviceObject
	OUT PDEBUG_DEVICE_OBJECT_INFO pDevObjInfo
)
{...}

PGET_DEVICE_OBJECT_INFO 


```

## -parameters

### -param Client: 
### -param DeviceObject: 
### -param pDevObjInfo: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also