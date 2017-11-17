---
UID: NC.ufxclient.UFX_DEVICE_NOTIFY_RESUME
title: UFX_DEVICE_NOTIFY_RESUME
author: windows-driver-content
description: 
ms.assetid: ddde808e-3dc7-42b8-a1dd-6b7cba4577a5
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

# UFX_DEVICE_NOTIFY_RESUME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_DEVICE_NOTIFY_RESUME UfxDeviceNotifyResume; 

// Definition

VOID UfxDeviceNotifyResume 
(
	PUFX_GLOBALS 
	UFXDEVICE 
)
{...}

UFX_DEVICE_NOTIFY_RESUME PFN_UFX_DEVICE_NOTIFY_RESUME


```

## -parameters

### -param : 
### -param : 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also