---
UID: NC.gpioclx.GPIO_CLIENT_STOP_CONTROLLER
title: GPIO_CLIENT_STOP_CONTROLLER
author: windows-driver-content
description: 
ms.assetid: 1c4cb060-d794-4519-9dea-2fee11fc011b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: gpioclx.h
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

# GPIO_CLIENT_STOP_CONTROLLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLIENT_STOP_CONTROLLER GpioClientStopController; 

// Definition

NTSTATUS GpioClientStopController 
(
	PVOID Context
	BOOLEAN SaveContext
	WDF_POWER_DEVICE_STATE TargetState
)
{...}

GPIO_CLIENT_STOP_CONTROLLER PGPIO_CLIENT_STOP_CONTROLLER


```

## -parameters

### -param Context: 
### -param SaveContext: 
### -param TargetState: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also