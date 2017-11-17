---
UID: NC.ufxclient.UFX_DEVICE_NOTIFY_HARDWARE_READY
title: UFX_DEVICE_NOTIFY_HARDWARE_READY
author: windows-driver-content
description: 
ms.assetid: e66d85e0-76b7-44e1-8cb6-68187845fe19
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

# UFX_DEVICE_NOTIFY_HARDWARE_READY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_DEVICE_NOTIFY_HARDWARE_READY UfxDeviceNotifyHardwareReady; 

// Definition

VOID UfxDeviceNotifyHardwareReady 
(
	PUFX_GLOBALS 
	UFXDEVICE 
)
{...}

UFX_DEVICE_NOTIFY_HARDWARE_READY PFN_UFX_DEVICE_NOTIFY_HARDWARE_READY


```

## -parameters

### -param : 
### -param : 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also