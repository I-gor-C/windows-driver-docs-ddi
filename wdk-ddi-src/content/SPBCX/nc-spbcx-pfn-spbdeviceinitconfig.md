---
UID: NC.spbcx.PFN_SPBDEVICEINITCONFIG
title: PFN_SPBDEVICEINITCONFIG
author: windows-driver-content
description: 
ms.assetid: 62c7153d-c72a-4e6d-a534-d891f6f31512
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: spbcx.h
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

# PFN_SPBDEVICEINITCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SPBDEVICEINITCONFIG PfnSpbdeviceinitconfig; 

// Definition

WDFAPI PfnSpbdeviceinitconfig 
(
	PSPB_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE_INIT *DeviceInit
)
{...}

PFN_SPBDEVICEINITCONFIG 


```

## -parameters

### -param DriverGlobals: 
### -param *DeviceInit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also