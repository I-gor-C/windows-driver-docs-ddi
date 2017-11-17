---
UID: NC.usbcamdi.PCAM_STATE_ROUTINE
title: PCAM_STATE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: c9e5e587-95b2-444a-b725-617cc08ddd20
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

# PCAM_STATE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCAM_STATE_ROUTINE PcamStateRoutine; 

// Definition

NTSTATUS PcamStateRoutine 
(
	PDEVICE_OBJECT BusDeviceObject
	PVOID DeviceContext
)
{...}

PCAM_STATE_ROUTINE 


```

## -parameters

### -param BusDeviceObject: 
### -param DeviceContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also