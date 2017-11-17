---
UID: NC.usbcamdi.PCAM_FREE_BW_ROUTINE_EX
title: PCAM_FREE_BW_ROUTINE_EX
author: windows-driver-content
description: 
ms.assetid: 6b5cec02-91c7-467e-ace4-9c4914aff81d
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

# PCAM_FREE_BW_ROUTINE_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCAM_FREE_BW_ROUTINE_EX PcamFreeBwRoutineEx; 

// Definition

NTSTATUS PcamFreeBwRoutineEx 
(
	PDEVICE_OBJECT BusDeviceObject
	PVOID DeviceContext
	ULONG STreamNumber
)
{...}

PCAM_FREE_BW_ROUTINE_EX 


```

## -parameters

### -param BusDeviceObject: 
### -param DeviceContext: 
### -param STreamNumber: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also