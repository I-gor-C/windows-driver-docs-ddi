---
UID: NC.netadapter.PFN_NETADAPTERSETLINKLAYERMTUSIZE
title: PFN_NETADAPTERSETLINKLAYERMTUSIZE
author: windows-driver-content
description: 
ms.assetid: f4493169-eb3f-4071-8411-67743a02fb57
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netadapter.h
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

# PFN_NETADAPTERSETLINKLAYERMTUSIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETADAPTERSETLINKLAYERMTUSIZE PfnNetadaptersetlinklayermtusize; 

// Definition

WDFAPI PfnNetadaptersetlinklayermtusize 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETADAPTER Adapter
	ULONG MtuSize
)
{...}

PFN_NETADAPTERSETLINKLAYERMTUSIZE 


```

## -parameters

### -param DriverGlobals: 
### -param Adapter: 
### -param MtuSize: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also