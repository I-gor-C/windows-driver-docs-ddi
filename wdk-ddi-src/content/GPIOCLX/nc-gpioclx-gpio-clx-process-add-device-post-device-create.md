---
UID: NC.gpioclx.GPIO_CLX_PROCESS_ADD_DEVICE_POST_DEVICE_CREATE
title: GPIO_CLX_PROCESS_ADD_DEVICE_POST_DEVICE_CREATE
author: windows-driver-content
description: 
ms.assetid: 8b37191d-39f4-4f33-b3e2-0dc127d3b0ab
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

# GPIO_CLX_PROCESS_ADD_DEVICE_POST_DEVICE_CREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLX_PROCESS_ADD_DEVICE_POST_DEVICE_CREATE GpioClxProcessAddDevicePostDeviceCreate; 

// Definition

NTSTATUS GpioClxProcessAddDevicePostDeviceCreate 
(
	WDFDRIVER Driver
	WDFDEVICE Device
)
{...}

GPIO_CLX_PROCESS_ADD_DEVICE_POST_DEVICE_CREATE PGPIO_CLX_PROCESS_ADD_DEVICE_POST_DEVICE_CREATE


```

## -parameters

### -param Driver: 
### -param Device: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also