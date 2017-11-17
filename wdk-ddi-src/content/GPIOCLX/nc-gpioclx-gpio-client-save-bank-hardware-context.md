---
UID: NC.gpioclx.GPIO_CLIENT_SAVE_BANK_HARDWARE_CONTEXT
title: GPIO_CLIENT_SAVE_BANK_HARDWARE_CONTEXT
author: windows-driver-content
description: 
ms.assetid: 0191b96f-a8ba-420f-91bc-f7864cc495fc
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

# GPIO_CLIENT_SAVE_BANK_HARDWARE_CONTEXT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLIENT_SAVE_BANK_HARDWARE_CONTEXT GpioClientSaveBankHardwareContext; 

// Definition

VOID GpioClientSaveBankHardwareContext 
(
	PVOID Context
	PGPIO_SAVE_RESTORE_BANK_HARDWARE_CONTEXT_PARAMETERS Parameters
)
{...}

GPIO_CLIENT_SAVE_BANK_HARDWARE_CONTEXT PGPIO_CLIENT_SAVE_BANK_HARDWARE_CONTEXT


```

## -parameters

### -param Context: 
### -param Parameters: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also