---
UID: NC.gpioclx.GPIO_CLIENT_ENABLE_INTERRUPT
title: GPIO_CLIENT_ENABLE_INTERRUPT
author: windows-driver-content
description: 
ms.assetid: 16ba6d7d-8f6c-4014-a7a5-75bc044e8370
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

# GPIO_CLIENT_ENABLE_INTERRUPT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLIENT_ENABLE_INTERRUPT GpioClientEnableInterrupt; 

// Definition

NTSTATUS GpioClientEnableInterrupt 
(
	PVOID Context
	PGPIO_ENABLE_INTERRUPT_PARAMETERS EnableParameters
)
{...}

GPIO_CLIENT_ENABLE_INTERRUPT PGPIO_CLIENT_ENABLE_INTERRUPT


```

## -parameters

### -param Context: 
### -param EnableParameters: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also