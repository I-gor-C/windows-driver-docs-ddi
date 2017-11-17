---
UID: NC.udecxwdfdevice.PFN_UDECXWDFDEVICERESETCOMPLETE
title: *PFN_UDECXWDFDEVICERESETCOMPLETE
author: windows-driver-content
description: 
ms.assetid: ccd37420-383d-428f-9cf3-c4a4c3adbcfa
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

# *PFN_UDECXWDFDEVICERESETCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXWDFDEVICERESETCOMPLETE *PfnUdecxwdfdeviceresetcomplete; 

// Definition

VOID *PfnUdecxwdfdeviceresetcomplete 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE UdeWdfDevice
)
{...}

*PFN_UDECXWDFDEVICERESETCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param UdeWdfDevice: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also