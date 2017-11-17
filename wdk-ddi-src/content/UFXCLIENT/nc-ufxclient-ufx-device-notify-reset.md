---
UID: NC.ufxclient.UFX_DEVICE_NOTIFY_RESET
title: UFX_DEVICE_NOTIFY_RESET
author: windows-driver-content
description: 
ms.assetid: a41dae24-7138-4875-8ba3-a0f470d1e870
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

# UFX_DEVICE_NOTIFY_RESET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_DEVICE_NOTIFY_RESET UfxDeviceNotifyReset; 

// Definition

VOID UfxDeviceNotifyReset 
(
	PUFX_GLOBALS 
	UFXDEVICE 
	USB_DEVICE_SPEED 
)
{...}

UFX_DEVICE_NOTIFY_RESET PFN_UFX_DEVICE_NOTIFY_RESET


```

## -parameters

### -param : 
### -param : 
### -param : 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also