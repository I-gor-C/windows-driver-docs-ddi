---
UID: NC.dsm.DSM_SET_DEVICE_INFO
title: DSM_SET_DEVICE_INFO
author: windows-driver-content
description: 
ms.assetid: 804cf7a6-72ce-4107-8dc9-cc8dbfa81d2b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsm.h
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

# DSM_SET_DEVICE_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_SET_DEVICE_INFO DsmSetDeviceInfo; 

// Definition

NTSTATUS DsmSetDeviceInfo 
(
	IN PVOID DsmContext
	IN PDEVICE_OBJECT TargetObject
	IN PVOID DsmId
	IN OUT PVOID *PathId
)
{...}

DSM_SET_DEVICE_INFO 


```

## -parameters

### -param DsmContext: 
### -param TargetObject: 
### -param DsmId: 
### -param *PathId: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also