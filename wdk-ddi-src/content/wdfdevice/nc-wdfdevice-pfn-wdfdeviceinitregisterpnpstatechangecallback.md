---
UID: NC.wdfdevice.PFN_WDFDEVICEINITREGISTERPNPSTATECHANGECALLBACK
title: PFN_WDFDEVICEINITREGISTERPNPSTATECHANGECALLBACK
author: windows-driver-content
description: 
ms.assetid: c1d5fbc5-69c9-4f73-83bc-5f80f226ef9f
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

# PFN_WDFDEVICEINITREGISTERPNPSTATECHANGECALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITREGISTERPNPSTATECHANGECALLBACK PfnWdfdeviceinitregisterpnpstatechangecallback; 

// Definition

WDFAPI PfnWdfdeviceinitregisterpnpstatechangecallback 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	WDF_DEVICE_PNP_STATE PnpState
	PFN_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION EvtDevicePnpStateChange
	ULONG CallbackTypes
)
{...}

PFN_WDFDEVICEINITREGISTERPNPSTATECHANGECALLBACK 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param PnpState: 
### -param EvtDevicePnpStateChange: 
### -param CallbackTypes: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also