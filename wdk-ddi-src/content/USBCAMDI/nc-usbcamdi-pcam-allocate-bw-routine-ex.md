---
UID: NC.usbcamdi.PCAM_ALLOCATE_BW_ROUTINE_EX
title: PCAM_ALLOCATE_BW_ROUTINE_EX
author: windows-driver-content
description: 
ms.assetid: 604dcb36-ac05-4383-a389-59ac32f4c814
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: usbcamdi.h
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

# PCAM_ALLOCATE_BW_ROUTINE_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCAM_ALLOCATE_BW_ROUTINE_EX PcamAllocateBwRoutineEx; 

// Definition

NTSTATUS PcamAllocateBwRoutineEx 
(
	PDEVICE_OBJECT BusDeviceObject
	PVOID DeviceContext
	PULONG RawFrameLength
	PVOID Format
	ULONG StreamNumber
)
{...}

PCAM_ALLOCATE_BW_ROUTINE_EX 


```

## -parameters

### -param BusDeviceObject: 
### -param DeviceContext: 
### -param RawFrameLength: 
### -param Format: 
### -param StreamNumber: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also