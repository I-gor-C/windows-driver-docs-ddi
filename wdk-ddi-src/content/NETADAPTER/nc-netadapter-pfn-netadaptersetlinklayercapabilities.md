---
UID: NC.netadapter.PFN_NETADAPTERSETLINKLAYERCAPABILITIES
title: PFN_NETADAPTERSETLINKLAYERCAPABILITIES
author: windows-driver-content
description: 
ms.assetid: 80ef0fda-c3b2-4469-8e49-408f520e927e
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

# PFN_NETADAPTERSETLINKLAYERCAPABILITIES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETADAPTERSETLINKLAYERCAPABILITIES PfnNetadaptersetlinklayercapabilities; 

// Definition

WDFAPI PfnNetadaptersetlinklayercapabilities 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETADAPTER Adapter
	PNET_ADAPTER_LINK_LAYER_CAPABILITIES LinkLayerCapabilities
)
{...}

PFN_NETADAPTERSETLINKLAYERCAPABILITIES 


```

## -parameters

### -param DriverGlobals: 
### -param Adapter: 
### -param LinkLayerCapabilities: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also