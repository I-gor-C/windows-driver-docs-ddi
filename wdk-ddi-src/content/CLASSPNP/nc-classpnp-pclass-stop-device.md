---
UID: NC.classpnp.PCLASS_STOP_DEVICE
title: PCLASS_STOP_DEVICE
author: windows-driver-content
description: 
ms.assetid: ea760ff2-d150-44b0-ad00-3153e714fca4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: classpnp.h
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

# PCLASS_STOP_DEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_STOP_DEVICE PclassStopDevice; 

// Definition

NTSTATUS PclassStopDevice 
(
	PDEVICE_OBJECT DeviceObject
	UCHAR Type
)
{...}

PCLASS_STOP_DEVICE 


```

## -parameters

### -param DeviceObject: 
### -param Type: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also