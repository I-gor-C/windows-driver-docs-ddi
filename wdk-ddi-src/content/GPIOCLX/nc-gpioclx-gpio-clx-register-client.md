---
UID: NC.gpioclx.GPIO_CLX_REGISTER_CLIENT
title: GPIO_CLX_REGISTER_CLIENT
author: windows-driver-content
description: 
ms.assetid: 0fba2eea-c2d2-457a-a74d-6c686ead1536
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

# GPIO_CLX_REGISTER_CLIENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GPIO_CLX_REGISTER_CLIENT GpioClxRegisterClient; 

// Definition

NTSTATUS GpioClxRegisterClient 
(
	WDFDRIVER Driver
	PGPIO_CLIENT_REGISTRATION_PACKET RegistrationPacket
	PUNICODE_STRING RegistryPath
)
{...}

GPIO_CLX_REGISTER_CLIENT PGPIO_CLX_REGISTER_CLIENT


```

## -parameters

### -param Driver: 
### -param RegistrationPacket: 
### -param RegistryPath: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also