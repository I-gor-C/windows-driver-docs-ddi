---
UID: NC.wdfdevice.PFN_WDFDEVICEGETHARDWAREREGISTERMAPPEDADDRESS
title: PFN_WDFDEVICEGETHARDWAREREGISTERMAPPEDADDRESS
author: windows-driver-content
description: 
ms.assetid: 2cd65b34-a9a9-4dc1-9358-a2630da4e591
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

# PFN_WDFDEVICEGETHARDWAREREGISTERMAPPEDADDRESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEGETHARDWAREREGISTERMAPPEDADDRESS PfnWdfdevicegethardwareregistermappedaddress; 

// Definition

WDFAPI PfnWdfdevicegethardwareregistermappedaddress 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PVOID PseudoBaseAddress
)
{...}

PFN_WDFDEVICEGETHARDWAREREGISTERMAPPEDADDRESS 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param PseudoBaseAddress: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also