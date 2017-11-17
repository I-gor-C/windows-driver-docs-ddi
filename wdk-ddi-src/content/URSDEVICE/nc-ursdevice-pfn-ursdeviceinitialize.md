---
UID: NC.ursdevice.PFN_URSDEVICEINITIALIZE
title: PFN_URSDEVICEINITIALIZE
author: windows-driver-content
description: 
ms.assetid: 57132e1a-f22a-454a-8262-152e60789701
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ursdevice.h
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

# PFN_URSDEVICEINITIALIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_URSDEVICEINITIALIZE PfnUrsdeviceinitialize; 

// Definition

WDFAPI PfnUrsdeviceinitialize 
(
	PURS_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PURS_CONFIG Config
)
{...}

PFN_URSDEVICEINITIALIZE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Config: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also