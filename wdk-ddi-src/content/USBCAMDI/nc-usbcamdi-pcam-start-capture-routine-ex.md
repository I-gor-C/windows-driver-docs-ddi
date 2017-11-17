---
UID: NC.usbcamdi.PCAM_START_CAPTURE_ROUTINE_EX
title: PCAM_START_CAPTURE_ROUTINE_EX
author: windows-driver-content
description: 
ms.assetid: 597b84d7-d7d4-4f22-af8d-39114ef77375
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

# PCAM_START_CAPTURE_ROUTINE_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCAM_START_CAPTURE_ROUTINE_EX PcamStartCaptureRoutineEx; 

// Definition

NTSTATUS PcamStartCaptureRoutineEx 
(
	PDEVICE_OBJECT BusDeviceObject
	PVOID DeviceContext
	ULONG StreamNumber
)
{...}

PCAM_START_CAPTURE_ROUTINE_EX 


```

## -parameters

### -param BusDeviceObject: 
### -param DeviceContext: 
### -param StreamNumber: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also