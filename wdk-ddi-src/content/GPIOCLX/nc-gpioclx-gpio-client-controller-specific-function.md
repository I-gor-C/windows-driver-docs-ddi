---
UID: NC.gpioclx.GPIO_CLIENT_CONTROLLER_SPECIFIC_FUNCTION
title: GPIO_CLIENT_CONTROLLER_SPECIFIC_FUNCTION
author: windows-driver-content
description: 
ms.assetid: ed6cde26-5221-4f99-b6b2-6c71e11473d4
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

# GPIO_CLIENT_CONTROLLER_SPECIFIC_FUNCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLIENT_CONTROLLER_SPECIFIC_FUNCTION GpioClientControllerSpecificFunction; 

// Definition

NTSTATUS GpioClientControllerSpecificFunction 
(
	PVOID Context
	PGPIO_CLIENT_CONTROLLER_SPECIFIC_FUNCTION_PARAMETERS Parameters
)
{...}

GPIO_CLIENT_CONTROLLER_SPECIFIC_FUNCTION PGPIO_CLIENT_CONTROLLER_SPECIFIC_FUNCTION


```

## -parameters

### -param Context: 
### -param Parameters: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also