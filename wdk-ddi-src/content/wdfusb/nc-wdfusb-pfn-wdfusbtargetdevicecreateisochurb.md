---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICECREATEISOCHURB
title: PFN_WDFUSBTARGETDEVICECREATEISOCHURB
author: windows-driver-content
description: 
ms.assetid: c9712d15-a2c0-40b8-b5db-bdb3edb57377
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfusb.h
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

# PFN_WDFUSBTARGETDEVICECREATEISOCHURB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICECREATEISOCHURB PfnWdfusbtargetdevicecreateisochurb; 

// Definition

WDFAPI PfnWdfusbtargetdevicecreateisochurb 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	PWDF_OBJECT_ATTRIBUTES Attributes
	ULONG NumberOfIsochPackets
	WDFMEMORY *UrbMemory
	PURB *Urb
)
{...}

PFN_WDFUSBTARGETDEVICECREATEISOCHURB 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param Attributes: 
### -param NumberOfIsochPackets: 
### -param *UrbMemory: 
### -param *Urb: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also