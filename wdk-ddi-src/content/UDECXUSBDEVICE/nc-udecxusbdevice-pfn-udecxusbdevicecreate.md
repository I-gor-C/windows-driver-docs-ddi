---
UID: NC.udecxusbdevice.PFN_UDECXUSBDEVICECREATE
title: *PFN_UDECXUSBDEVICECREATE
author: windows-driver-content
description: 
ms.assetid: effc93f6-aec4-4ba7-8ea0-50a7fae060ae
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

# *PFN_UDECXUSBDEVICECREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBDEVICECREATE *PfnUdecxusbdevicecreate; 

// Definition

NTSTATUS *PfnUdecxusbdevicecreate 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	PUDECXUSBDEVICE_INIT *UdecxUsbDeviceInit
	PWDF_OBJECT_ATTRIBUTES Attributes
	UDECXUSBDEVICE *UdecxUsbDevice
)
{...}

*PFN_UDECXUSBDEVICECREATE 


```

## -parameters

### -param DriverGlobals: 
### -param *UdecxUsbDeviceInit: 
### -param Attributes: 
### -param *UdecxUsbDevice: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also