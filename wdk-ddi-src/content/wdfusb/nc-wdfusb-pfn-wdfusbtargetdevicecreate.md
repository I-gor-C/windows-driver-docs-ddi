---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICECREATE
title: PFN_WDFUSBTARGETDEVICECREATE
author: windows-driver-content
description: 
ms.assetid: 69863fe2-217c-4184-9c21-dd8948bdaced
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

# PFN_WDFUSBTARGETDEVICECREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICECREATE PfnWdfusbtargetdevicecreate; 

// Definition

WDFAPI PfnWdfusbtargetdevicecreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_OBJECT_ATTRIBUTES Attributes
	WDFUSBDEVICE *UsbDevice
)
{...}

PFN_WDFUSBTARGETDEVICECREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Attributes: 
### -param *UsbDevice: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also