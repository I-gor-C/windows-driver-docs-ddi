---
UID: NC.udecxusbdevice.PFN_UDECXUSBDEVICEPLUGIN
title: *PFN_UDECXUSBDEVICEPLUGIN
author: windows-driver-content
description: 
ms.assetid: 88c60bd4-6550-43d4-b94f-0d1450ff3708
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxusbdevice.h
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

# *PFN_UDECXUSBDEVICEPLUGIN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBDEVICEPLUGIN *PfnUdecxusbdeviceplugin; 

// Definition

NTSTATUS *PfnUdecxusbdeviceplugin 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	UDECXUSBDEVICE UdecxUsbDevice
	PUDECX_USB_DEVICE_PLUG_IN_OPTIONS Options
)
{...}

*PFN_UDECXUSBDEVICEPLUGIN 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxUsbDevice: 
### -param Options: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also