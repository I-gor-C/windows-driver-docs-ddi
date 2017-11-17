---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETPNPPOWEREVENTCALLBACKS
title: PFN_WDFDEVICEINITSETPNPPOWEREVENTCALLBACKS
author: windows-driver-content
description: 
ms.assetid: e0e173b6-1514-41fd-b4e3-0f9efa525723
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

# PFN_WDFDEVICEINITSETPNPPOWEREVENTCALLBACKS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETPNPPOWEREVENTCALLBACKS PfnWdfdeviceinitsetpnppowereventcallbacks; 

// Definition

WDFAPI PfnWdfdeviceinitsetpnppowereventcallbacks 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PWDF_PNPPOWER_EVENT_CALLBACKS PnpPowerEventCallbacks
)
{...}

PFN_WDFDEVICEINITSETPNPPOWEREVENTCALLBACKS 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param PnpPowerEventCallbacks: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also