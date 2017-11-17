---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICECREATEURB
title: PFN_WDFUSBTARGETDEVICECREATEURB
author: windows-driver-content
description: 
ms.assetid: d55ab865-b8d0-4029-b8bb-234ca5c15678
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

# PFN_WDFUSBTARGETDEVICECREATEURB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICECREATEURB PfnWdfusbtargetdevicecreateurb; 

// Definition

WDFAPI PfnWdfusbtargetdevicecreateurb 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	PWDF_OBJECT_ATTRIBUTES Attributes
	WDFMEMORY *UrbMemory
	PURB *Urb
)
{...}

PFN_WDFUSBTARGETDEVICECREATEURB 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param Attributes: 
### -param *UrbMemory: 
### -param *Urb: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also