---
UID: NC.gpioclx.GPIO_CLIENT_QUERY_ACTIVE_INTERRUPTS
title: GPIO_CLIENT_QUERY_ACTIVE_INTERRUPTS
author: windows-driver-content
description: 
ms.assetid: 906511ee-a97f-458e-b890-313f3d024f99
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

# GPIO_CLIENT_QUERY_ACTIVE_INTERRUPTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLIENT_QUERY_ACTIVE_INTERRUPTS GpioClientQueryActiveInterrupts; 

// Definition

NTSTATUS GpioClientQueryActiveInterrupts 
(
	PVOID Context
	PGPIO_QUERY_ACTIVE_INTERRUPTS_PARAMETERS QueryActiveParameters
)
{...}

GPIO_CLIENT_QUERY_ACTIVE_INTERRUPTS PGPIO_CLIENT_QUERY_ACTIVE_INTERRUPTS


```

## -parameters

### -param Context: 
### -param QueryActiveParameters: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also