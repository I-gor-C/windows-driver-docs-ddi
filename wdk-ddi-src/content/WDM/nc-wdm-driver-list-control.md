---
UID: NC.wdm.DRIVER_LIST_CONTROL
title: DRIVER_LIST_CONTROL
author: windows-driver-content
description: 
ms.assetid: 2c6713bd-b4ae-4b93-85b3-be066cf2b12c
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

# DRIVER_LIST_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DRIVER_LIST_CONTROL DriverListControl; 

// Definition

_IRQL_requires_same_ VOID DriverListControl 
(
	_DEVICE_OBJECT * DeviceObject
	_IRP * Irp
	PSCATTER_GATHER_LIST ScatterGather
	PVOID Context
)
{...}

DRIVER_LIST_CONTROL PDRIVER_LIST_CONTROL


```

## -parameters

### -param DeviceObject: 
### -param Irp: 
### -param ScatterGather: 
### -param Context: 



## -returns

Returns _IRQL_requires_same_ VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also