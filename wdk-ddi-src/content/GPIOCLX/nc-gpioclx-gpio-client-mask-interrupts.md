---
UID: NC.gpioclx.GPIO_CLIENT_MASK_INTERRUPTS
title: GPIO_CLIENT_MASK_INTERRUPTS
author: windows-driver-content
description: 
ms.assetid: 3fea98d6-6900-4cb4-b243-0bb9598e275d
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

# GPIO_CLIENT_MASK_INTERRUPTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLIENT_MASK_INTERRUPTS GpioClientMaskInterrupts; 

// Definition

NTSTATUS GpioClientMaskInterrupts 
(
	PVOID Context
	PGPIO_MASK_INTERRUPT_PARAMETERS MaskParameters
)
{...}

GPIO_CLIENT_MASK_INTERRUPTS PGPIO_CLIENT_MASK_INTERRUPTS


```

## -parameters

### -param Context: 
### -param MaskParameters: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also