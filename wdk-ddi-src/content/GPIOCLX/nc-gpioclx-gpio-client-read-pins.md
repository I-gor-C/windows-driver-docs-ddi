---
UID: NC.gpioclx.GPIO_CLIENT_READ_PINS
title: GPIO_CLIENT_READ_PINS
author: windows-driver-content
description: 
ms.assetid: 44bedc4a-297c-4799-89d8-01425434bf19
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

# GPIO_CLIENT_READ_PINS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLIENT_READ_PINS GpioClientReadPins; 

// Definition

NTSTATUS GpioClientReadPins 
(
	PVOID Context
	PGPIO_READ_PINS_PARAMETERS ReadParameters
)
{...}

GPIO_CLIENT_READ_PINS PGPIO_CLIENT_READ_PINS


```

## -parameters

### -param Context: 
### -param ReadParameters: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also