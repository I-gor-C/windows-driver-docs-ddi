---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICERETRIEVECONFIGDESCRIPTOR
title: PFN_WDFUSBTARGETDEVICERETRIEVECONFIGDESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 62a99e1c-3403-40b3-98c8-bde4b40fd0df
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

# PFN_WDFUSBTARGETDEVICERETRIEVECONFIGDESCRIPTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICERETRIEVECONFIGDESCRIPTOR PfnWdfusbtargetdeviceretrieveconfigdescriptor; 

// Definition

WDFAPI PfnWdfusbtargetdeviceretrieveconfigdescriptor 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	PVOID ConfigDescriptor
	PUSHORT ConfigDescriptorLength
)
{...}

PFN_WDFUSBTARGETDEVICERETRIEVECONFIGDESCRIPTOR 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param ConfigDescriptor: 
### -param ConfigDescriptorLength: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also