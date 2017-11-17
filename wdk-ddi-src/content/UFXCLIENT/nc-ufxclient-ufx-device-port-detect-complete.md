---
UID: NC.ufxclient.UFX_DEVICE_PORT_DETECT_COMPLETE
title: UFX_DEVICE_PORT_DETECT_COMPLETE
author: windows-driver-content
description: 
ms.assetid: 68b8129a-0d45-45f1-ac91-4ee0d17a151e
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

# UFX_DEVICE_PORT_DETECT_COMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_DEVICE_PORT_DETECT_COMPLETE UfxDevicePortDetectComplete; 

// Definition

VOID UfxDevicePortDetectComplete 
(
	PUFX_GLOBALS 
	UFXDEVICE 
	USBFN_PORT_TYPE 
)
{...}

UFX_DEVICE_PORT_DETECT_COMPLETE PFN_UFX_DEVICE_PORT_DETECT_COMPLETE


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