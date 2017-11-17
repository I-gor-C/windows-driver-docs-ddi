---
UID: NC.gpioclx.GPIO_CLIENT_READ_PINS_MASK
title: GPIO_CLIENT_READ_PINS_MASK
author: windows-driver-content
description: 
ms.assetid: 20816785-4d5d-488d-bef4-db97ce6232ef
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

# GPIO_CLIENT_READ_PINS_MASK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLIENT_READ_PINS_MASK GpioClientReadPinsMask; 

// Definition

NTSTATUS GpioClientReadPinsMask 
(
	PVOID Context
	PGPIO_READ_PINS_MASK_PARAMETERS ReadParameters
)
{...}

GPIO_CLIENT_READ_PINS_MASK PGPIO_CLIENT_READ_PINS_MASK


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