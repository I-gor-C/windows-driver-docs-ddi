---
UID: NC.gpioclx.GPIO_CLIENT_UNMASK_INTERRUPT
title: GPIO_CLIENT_UNMASK_INTERRUPT
author: windows-driver-content
description: 
ms.assetid: 6abd96d8-1a02-4fe3-b0fe-1c78b82907d7
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

# GPIO_CLIENT_UNMASK_INTERRUPT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLIENT_UNMASK_INTERRUPT GpioClientUnmaskInterrupt; 

// Definition

NTSTATUS GpioClientUnmaskInterrupt 
(
	PVOID Context
	PGPIO_ENABLE_INTERRUPT_PARAMETERS InterruptParameters
)
{...}

GPIO_CLIENT_UNMASK_INTERRUPT PGPIO_CLIENT_UNMASK_INTERRUPT


```

## -parameters

### -param Context: 
### -param InterruptParameters: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also