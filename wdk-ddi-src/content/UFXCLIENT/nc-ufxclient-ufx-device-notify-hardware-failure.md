---
UID: NC.ufxclient.UFX_DEVICE_NOTIFY_HARDWARE_FAILURE
title: UFX_DEVICE_NOTIFY_HARDWARE_FAILURE
author: windows-driver-content
description: 
ms.assetid: d00f6f6d-051b-4369-aa08-abbaddc4e720
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

# UFX_DEVICE_NOTIFY_HARDWARE_FAILURE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_DEVICE_NOTIFY_HARDWARE_FAILURE UfxDeviceNotifyHardwareFailure; 

// Definition

VOID UfxDeviceNotifyHardwareFailure 
(
	PUFX_GLOBALS 
	UFXDEVICE 
	PUFX_HARDWARE_FAILURE_CONTEXT 
)
{...}

UFX_DEVICE_NOTIFY_HARDWARE_FAILURE PFN_UFX_DEVICE_NOTIFY_HARDWARE_FAILURE


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