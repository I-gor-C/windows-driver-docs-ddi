---
UID: NC.netadapter.PFN_NETADAPTERGETPOWERSETTINGS
title: PFN_NETADAPTERGETPOWERSETTINGS
author: windows-driver-content
description: 
ms.assetid: cd5972fb-fe9b-45b6-933a-44a0cb0552bb
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

# PFN_NETADAPTERGETPOWERSETTINGS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETADAPTERGETPOWERSETTINGS PfnNetadaptergetpowersettings; 

// Definition

WDFAPI PfnNetadaptergetpowersettings 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETADAPTER Adapter
)
{...}

PFN_NETADAPTERGETPOWERSETTINGS 


```

## -parameters

### -param DriverGlobals: 
### -param Adapter: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also