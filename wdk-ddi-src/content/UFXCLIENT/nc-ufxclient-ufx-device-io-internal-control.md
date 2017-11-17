---
UID: NC.ufxclient.UFX_DEVICE_IO_INTERNAL_CONTROL
title: UFX_DEVICE_IO_INTERNAL_CONTROL
author: windows-driver-content
description: 
ms.assetid: acdefc1e-e272-4fdb-bb65-a85d97e23d38
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ufxclient.h
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

# UFX_DEVICE_IO_INTERNAL_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_DEVICE_IO_INTERNAL_CONTROL UfxDeviceIoInternalControl; 

// Definition

BOOLEAN UfxDeviceIoInternalControl 
(
	PUFX_GLOBALS 
	UFXDEVICE 
	WDFREQUEST 
	size_t 
	size_t 
	ULONG 
)
{...}

UFX_DEVICE_IO_INTERNAL_CONTROL PFN_UFX_DEVICE_IO_INTERNAL_CONTROL


```

## -parameters

### -param : 
### -param : 
### -param : 
### -param : 
### -param : 
### -param : 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also