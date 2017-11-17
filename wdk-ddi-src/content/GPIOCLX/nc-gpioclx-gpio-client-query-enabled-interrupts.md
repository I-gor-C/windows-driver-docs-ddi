---
UID: NC.gpioclx.GPIO_CLIENT_QUERY_ENABLED_INTERRUPTS
title: GPIO_CLIENT_QUERY_ENABLED_INTERRUPTS
author: windows-driver-content
description: 
ms.assetid: 6c3dcca0-c81b-4eef-b549-fa7937406bc2
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

# GPIO_CLIENT_QUERY_ENABLED_INTERRUPTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLIENT_QUERY_ENABLED_INTERRUPTS GpioClientQueryEnabledInterrupts; 

// Definition

NTSTATUS GpioClientQueryEnabledInterrupts 
(
	PVOID Context
	PGPIO_QUERY_ENABLED_INTERRUPTS_PARAMETERS QueryEnabledParameters
)
{...}

GPIO_CLIENT_QUERY_ENABLED_INTERRUPTS PGPIO_CLIENT_QUERY_ENABLED_INTERRUPTS


```

## -parameters

### -param Context: 
### -param QueryEnabledParameters: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also