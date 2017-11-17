---
UID: NC.wdfdevice.PFN_WDFDEVICEGETSYSTEMPOWERACTION
title: PFN_WDFDEVICEGETSYSTEMPOWERACTION
author: windows-driver-content
description: 
ms.assetid: 2176545b-cd89-4df5-976d-848cb17a55e8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdevice.h
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

# PFN_WDFDEVICEGETSYSTEMPOWERACTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEGETSYSTEMPOWERACTION PfnWdfdevicegetsystempoweraction; 

// Definition

WDFAPI PfnWdfdevicegetsystempoweraction 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
)
{...}

PFN_WDFDEVICEGETSYSTEMPOWERACTION 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also