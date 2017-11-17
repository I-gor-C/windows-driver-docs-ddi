---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETIOTYPEEX
title: PFN_WDFDEVICEINITSETIOTYPEEX
author: windows-driver-content
description: 
ms.assetid: 5b37dd80-3a65-4d65-8c2d-073e839adba2
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

# PFN_WDFDEVICEINITSETIOTYPEEX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETIOTYPEEX PfnWdfdeviceinitsetiotypeex; 

// Definition

WDFAPI PfnWdfdeviceinitsetiotypeex 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PWDF_IO_TYPE_CONFIG IoTypeConfig
)
{...}

PFN_WDFDEVICEINITSETIOTYPEEX 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param IoTypeConfig: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also