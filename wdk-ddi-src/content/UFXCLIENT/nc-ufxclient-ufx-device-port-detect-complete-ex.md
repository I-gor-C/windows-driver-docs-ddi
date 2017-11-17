---
UID: NC.ufxclient.UFX_DEVICE_PORT_DETECT_COMPLETE_EX
title: UFX_DEVICE_PORT_DETECT_COMPLETE_EX
author: windows-driver-content
description: 
ms.assetid: 86dc05bf-5cae-4279-ae7a-8868d3b04acf
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

# UFX_DEVICE_PORT_DETECT_COMPLETE_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_DEVICE_PORT_DETECT_COMPLETE_EX UfxDevicePortDetectCompleteEx; 

// Definition

VOID UfxDevicePortDetectCompleteEx 
(
	PUFX_GLOBALS 
	UFXDEVICE 
	USBFN_PORT_TYPE 
	USBFN_ACTION 
)
{...}

UFX_DEVICE_PORT_DETECT_COMPLETE_EX PFN_UFX_DEVICE_PORT_DETECT_COMPLETE_EX


```

## -parameters

### -param : 
### -param : 
### -param : 
### -param : 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also