---
UID: NC.udecxwdfdevice.PFN_UDECXWDFDEVICETRYHANDLEUSERIOCTL
title: *PFN_UDECXWDFDEVICETRYHANDLEUSERIOCTL
author: windows-driver-content
description: 
ms.assetid: 4623e44c-a961-4093-af08-fbf405e5fc1d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxwdfdevice.h
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

# *PFN_UDECXWDFDEVICETRYHANDLEUSERIOCTL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXWDFDEVICETRYHANDLEUSERIOCTL *PfnUdecxwdfdevicetryhandleuserioctl; 

// Definition

BOOLEAN *PfnUdecxwdfdevicetryhandleuserioctl 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE UdecxWdfDevice
	WDFREQUEST Request
)
{...}

*PFN_UDECXWDFDEVICETRYHANDLEUSERIOCTL 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxWdfDevice: 
### -param Request: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also