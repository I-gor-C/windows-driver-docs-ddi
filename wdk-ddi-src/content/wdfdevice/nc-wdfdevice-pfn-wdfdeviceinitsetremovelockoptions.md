---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETREMOVELOCKOPTIONS
title: PFN_WDFDEVICEINITSETREMOVELOCKOPTIONS
author: windows-driver-content
description: 
ms.assetid: 43f342c2-00f4-4b5c-a64f-2f0484703e38
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

# PFN_WDFDEVICEINITSETREMOVELOCKOPTIONS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETREMOVELOCKOPTIONS PfnWdfdeviceinitsetremovelockoptions; 

// Definition

WDFAPI PfnWdfdeviceinitsetremovelockoptions 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PWDF_REMOVE_LOCK_OPTIONS Options
)
{...}

PFN_WDFDEVICEINITSETREMOVELOCKOPTIONS 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param Options: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also