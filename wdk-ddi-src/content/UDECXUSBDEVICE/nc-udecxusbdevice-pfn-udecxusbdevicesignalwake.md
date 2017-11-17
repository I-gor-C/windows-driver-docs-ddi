---
UID: NC.udecxusbdevice.PFN_UDECXUSBDEVICESIGNALWAKE
title: *PFN_UDECXUSBDEVICESIGNALWAKE
author: windows-driver-content
description: 
ms.assetid: e4b0715f-5e7b-4eda-836b-20c20fb3b492
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

# *PFN_UDECXUSBDEVICESIGNALWAKE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBDEVICESIGNALWAKE *PfnUdecxusbdevicesignalwake; 

// Definition

VOID *PfnUdecxusbdevicesignalwake 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	UDECXUSBDEVICE UdecxUsbDevice
)
{...}

*PFN_UDECXUSBDEVICESIGNALWAKE 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxUsbDevice: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also