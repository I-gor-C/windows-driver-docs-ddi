---
UID: NC.udecxusbdevice.PFN_UDECXUSBDEVICEINITALLOCATE
title: *PFN_UDECXUSBDEVICEINITALLOCATE
author: windows-driver-content
description: 
ms.assetid: b0431972-9471-4c99-af39-aeb3bbbdae62
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

# *PFN_UDECXUSBDEVICEINITALLOCATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBDEVICEINITALLOCATE *PfnUdecxusbdeviceinitallocate; 

// Definition

PUDECXUSBDEVICE_INIT *PfnUdecxusbdeviceinitallocate 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE UdecxWdfDevice
)
{...}

*PFN_UDECXUSBDEVICEINITALLOCATE 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxWdfDevice: 



## -returns

Returns PUDECXUSBDEVICE_INIT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also