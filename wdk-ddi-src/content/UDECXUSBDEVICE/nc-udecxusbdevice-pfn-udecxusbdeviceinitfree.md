---
UID: NC.udecxusbdevice.PFN_UDECXUSBDEVICEINITFREE
title: *PFN_UDECXUSBDEVICEINITFREE
author: windows-driver-content
description: 
ms.assetid: 853b0c29-346a-4a58-a591-7f09dbbf3aca
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

# *PFN_UDECXUSBDEVICEINITFREE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBDEVICEINITFREE *PfnUdecxusbdeviceinitfree; 

// Definition

VOID *PfnUdecxusbdeviceinitfree 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	PUDECXUSBDEVICE_INIT UdecxUsbDeviceInit
)
{...}

*PFN_UDECXUSBDEVICEINITFREE 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxUsbDeviceInit: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also