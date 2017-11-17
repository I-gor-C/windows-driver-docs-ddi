---
UID: NC.wdm.DRIVER_CONTROL
title: DRIVER_CONTROL
author: windows-driver-content
description: 
ms.assetid: eeab1310-4e47-4090-91f9-bd8fc122c521
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

# DRIVER_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DRIVER_CONTROL DriverControl; 

// Definition

_IRQL_requires_same_ IO_ALLOCATION_ACTION DriverControl 
(
	_DEVICE_OBJECT * DeviceObject
	_IRP * Irp
	PVOID MapRegisterBase
	PVOID Context
)
{...}

DRIVER_CONTROL PDRIVER_CONTROL


```

## -parameters

### -param DeviceObject: 
### -param Irp: 
### -param MapRegisterBase: 
### -param Context: 



## -returns

Returns _IRQL_requires_same_ IO_ALLOCATION_ACTION that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also