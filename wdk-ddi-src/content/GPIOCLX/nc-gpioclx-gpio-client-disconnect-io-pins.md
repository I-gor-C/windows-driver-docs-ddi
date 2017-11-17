---
UID: NC.gpioclx.GPIO_CLIENT_DISCONNECT_IO_PINS
title: GPIO_CLIENT_DISCONNECT_IO_PINS
author: windows-driver-content
description: 
ms.assetid: 7b52fa39-7727-4137-a8f6-9af52d63470d
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

# GPIO_CLIENT_DISCONNECT_IO_PINS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLIENT_DISCONNECT_IO_PINS GpioClientDisconnectIoPins; 

// Definition

NTSTATUS GpioClientDisconnectIoPins 
(
	PVOID Context
	PGPIO_DISCONNECT_IO_PINS_PARAMETERS DisconnectParameters
)
{...}

GPIO_CLIENT_DISCONNECT_IO_PINS PGPIO_CLIENT_DISCONNECT_IO_PINS


```

## -parameters

### -param Context: 
### -param DisconnectParameters: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also