---
UID: NC.ucxclass.PFN_UCXINITIALIZEDEVICEINIT
title: PFN_UCXINITIALIZEDEVICEINIT
author: windows-driver-content
description: 
ms.assetid: e2cad686-36e5-493c-bf65-21552fbda855
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxclass.h
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

# PFN_UCXINITIALIZEDEVICEINIT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXINITIALIZEDEVICEINIT PfnUcxinitializedeviceinit; 

// Definition

WDFAPI PfnUcxinitializedeviceinit 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
)
{...}

PFN_UCXINITIALIZEDEVICEINIT 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also