---
UID: NC.gpioclx.GPIO_CLIENT_QUERY_SET_CONTROLLER_INFORMATION
title: GPIO_CLIENT_QUERY_SET_CONTROLLER_INFORMATION
author: windows-driver-content
description: 
ms.assetid: d7105c07-f95e-40f8-830e-155695e98e25
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

# GPIO_CLIENT_QUERY_SET_CONTROLLER_INFORMATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLIENT_QUERY_SET_CONTROLLER_INFORMATION GpioClientQuerySetControllerInformation; 

// Definition

NTSTATUS GpioClientQuerySetControllerInformation 
(
	PVOID Context
	PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT InputBuffer
	PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT OutputBuffer
)
{...}

GPIO_CLIENT_QUERY_SET_CONTROLLER_INFORMATION PGPIO_CLIENT_QUERY_SET_CONTROLLER_INFORMATION


```

## -parameters

### -param Context: 
### -param InputBuffer: 
### -param OutputBuffer: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also