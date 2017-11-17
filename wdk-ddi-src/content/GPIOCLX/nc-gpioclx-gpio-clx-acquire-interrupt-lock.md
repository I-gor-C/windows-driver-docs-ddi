---
UID: NC.gpioclx.GPIO_CLX_ACQUIRE_INTERRUPT_LOCK
title: GPIO_CLX_ACQUIRE_INTERRUPT_LOCK
author: windows-driver-content
description: 
ms.assetid: 1b0d2534-c845-44f8-9d38-3e910602eaba
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

# GPIO_CLX_ACQUIRE_INTERRUPT_LOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLX_ACQUIRE_INTERRUPT_LOCK GpioClxAcquireInterruptLock; 

// Definition

VOID GpioClxAcquireInterruptLock 
(
	PVOID Context
	BANK_ID BankId
)
{...}

GPIO_CLX_ACQUIRE_INTERRUPT_LOCK PGPIO_CLX_ACQUIRE_INTERRUPT_LOCK


```

## -parameters

### -param Context: 
### -param BankId: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also