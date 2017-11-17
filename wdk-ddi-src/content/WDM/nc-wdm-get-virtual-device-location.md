---
UID: NC.wdm.GET_VIRTUAL_DEVICE_LOCATION
title: GET_VIRTUAL_DEVICE_LOCATION
author: windows-driver-content
description: 
ms.assetid: f93e11f3-2093-4780-af06-dc40868c0e0d
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

# GET_VIRTUAL_DEVICE_LOCATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GET_VIRTUAL_DEVICE_LOCATION GetVirtualDeviceLocation; 

// Definition

NTSTATUS GetVirtualDeviceLocation 
(
	PVOID Context
	USHORT VirtualFunction
	PUINT16 SegmentNumber
	PUINT8 BusNumber
	PUINT8 FunctionNumber
)
{...}

GET_VIRTUAL_DEVICE_LOCATION PGET_VIRTUAL_DEVICE_LOCATION


```

## -parameters

### -param Context: 
### -param VirtualFunction: 
### -param SegmentNumber: 
### -param BusNumber: 
### -param FunctionNumber: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also