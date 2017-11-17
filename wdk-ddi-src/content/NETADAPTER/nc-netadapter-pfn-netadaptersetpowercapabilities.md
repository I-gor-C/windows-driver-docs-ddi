---
UID: NC.netadapter.PFN_NETADAPTERSETPOWERCAPABILITIES
title: PFN_NETADAPTERSETPOWERCAPABILITIES
author: windows-driver-content
description: 
ms.assetid: 5dcba2ba-a3bc-4b8c-b11d-78d7492f946d
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

# PFN_NETADAPTERSETPOWERCAPABILITIES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETADAPTERSETPOWERCAPABILITIES PfnNetadaptersetpowercapabilities; 

// Definition

WDFAPI PfnNetadaptersetpowercapabilities 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETADAPTER Adapter
	PNET_ADAPTER_POWER_CAPABILITIES PowerCapabilities
)
{...}

PFN_NETADAPTERSETPOWERCAPABILITIES 


```

## -parameters

### -param DriverGlobals: 
### -param Adapter: 
### -param PowerCapabilities: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also