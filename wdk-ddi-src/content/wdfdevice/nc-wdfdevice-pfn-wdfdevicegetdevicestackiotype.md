---
UID: NC.wdfdevice.PFN_WDFDEVICEGETDEVICESTACKIOTYPE
title: PFN_WDFDEVICEGETDEVICESTACKIOTYPE
author: windows-driver-content
description: 
ms.assetid: 606279a3-64c6-4677-8248-b2be96589f80
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

# PFN_WDFDEVICEGETDEVICESTACKIOTYPE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEGETDEVICESTACKIOTYPE PfnWdfdevicegetdevicestackiotype; 

// Definition

WDFAPI PfnWdfdevicegetdevicestackiotype 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	WDF_DEVICE_IO_TYPE *ReadWriteIoType
	WDF_DEVICE_IO_TYPE *IoControlIoType
)
{...}

PFN_WDFDEVICEGETDEVICESTACKIOTYPE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param *ReadWriteIoType: 
### -param *IoControlIoType: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also