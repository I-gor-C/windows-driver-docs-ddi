---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETPOWERNOTPAGEABLE
title: PFN_WDFDEVICEINITSETPOWERNOTPAGEABLE
author: windows-driver-content
description: 
ms.assetid: b2376155-6e18-4c01-a823-e352f7f80b1c
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

# PFN_WDFDEVICEINITSETPOWERNOTPAGEABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETPOWERNOTPAGEABLE PfnWdfdeviceinitsetpowernotpageable; 

// Definition

WDFAPI PfnWdfdeviceinitsetpowernotpageable 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
)
{...}

PFN_WDFDEVICEINITSETPOWERNOTPAGEABLE 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also