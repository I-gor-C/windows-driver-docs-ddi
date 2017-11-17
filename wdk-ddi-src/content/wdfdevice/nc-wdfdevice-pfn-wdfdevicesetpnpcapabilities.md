---
UID: NC.wdfdevice.PFN_WDFDEVICESETPNPCAPABILITIES
title: PFN_WDFDEVICESETPNPCAPABILITIES
author: windows-driver-content
description: 
ms.assetid: 851adddb-a92c-4416-99f1-ae38345a6c42
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

# PFN_WDFDEVICESETPNPCAPABILITIES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICESETPNPCAPABILITIES PfnWdfdevicesetpnpcapabilities; 

// Definition

WDFAPI PfnWdfdevicesetpnpcapabilities 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_DEVICE_PNP_CAPABILITIES PnpCapabilities
)
{...}

PFN_WDFDEVICESETPNPCAPABILITIES 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param PnpCapabilities: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also