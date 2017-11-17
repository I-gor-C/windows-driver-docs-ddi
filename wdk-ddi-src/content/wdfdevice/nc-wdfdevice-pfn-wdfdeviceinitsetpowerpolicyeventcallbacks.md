---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETPOWERPOLICYEVENTCALLBACKS
title: PFN_WDFDEVICEINITSETPOWERPOLICYEVENTCALLBACKS
author: windows-driver-content
description: 
ms.assetid: 894bbe28-81e4-41a8-a4f4-bbc10e7ba556
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

# PFN_WDFDEVICEINITSETPOWERPOLICYEVENTCALLBACKS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETPOWERPOLICYEVENTCALLBACKS PfnWdfdeviceinitsetpowerpolicyeventcallbacks; 

// Definition

WDFAPI PfnWdfdeviceinitsetpowerpolicyeventcallbacks 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PWDF_POWER_POLICY_EVENT_CALLBACKS PowerPolicyEventCallbacks
)
{...}

PFN_WDFDEVICEINITSETPOWERPOLICYEVENTCALLBACKS 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param PowerPolicyEventCallbacks: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also