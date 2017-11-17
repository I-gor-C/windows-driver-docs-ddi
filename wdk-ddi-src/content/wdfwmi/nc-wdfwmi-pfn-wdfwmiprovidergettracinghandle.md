---
UID: NC.wdfwmi.PFN_WDFWMIPROVIDERGETTRACINGHANDLE
title: PFN_WDFWMIPROVIDERGETTRACINGHANDLE
author: windows-driver-content
description: 
ms.assetid: 9ae8ac67-a171-45bf-885c-f15f4b79f882
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfwmi.h
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

# PFN_WDFWMIPROVIDERGETTRACINGHANDLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWMIPROVIDERGETTRACINGHANDLE PfnWdfwmiprovidergettracinghandle; 

// Definition

WDFAPI PfnWdfwmiprovidergettracinghandle 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFWMIPROVIDER WmiProvider
)
{...}

PFN_WDFWMIPROVIDERGETTRACINGHANDLE 


```

## -parameters

### -param DriverGlobals: 
### -param WmiProvider: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also