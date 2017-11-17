---
UID: NC.wdfcompanion.PFN_WDFDEVICEINITSETCOMPANIONEVENTCALLBACKS
title: PFN_WDFDEVICEINITSETCOMPANIONEVENTCALLBACKS
author: windows-driver-content
description: 
ms.assetid: 5ade58b9-69a7-412a-9f9d-19c291bfa1f3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfcompanion.h
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

# PFN_WDFDEVICEINITSETCOMPANIONEVENTCALLBACKS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETCOMPANIONEVENTCALLBACKS PfnWdfdeviceinitsetcompanioneventcallbacks; 

// Definition

WDFAPI PfnWdfdeviceinitsetcompanioneventcallbacks 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PWDF_COMPANION_EVENT_CALLBACKS CompanionEventCallbacks
)
{...}

PFN_WDFDEVICEINITSETCOMPANIONEVENTCALLBACKS 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param CompanionEventCallbacks: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also