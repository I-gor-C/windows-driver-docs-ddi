---
UID: NC.wdfpdo.PFN_WDFPDOINITALLOCATE
title: PFN_WDFPDOINITALLOCATE
author: windows-driver-content
description: 
ms.assetid: fee94775-8b97-4168-805b-1058dffabefc
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfpdo.h
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

# PFN_WDFPDOINITALLOCATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDOINITALLOCATE PfnWdfpdoinitallocate; 

// Definition

WDFAPI PfnWdfpdoinitallocate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE ParentDevice
)
{...}

PFN_WDFPDOINITALLOCATE 


```

## -parameters

### -param DriverGlobals: 
### -param ParentDevice: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also