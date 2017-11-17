---
UID: NC.netadapter.PFN_NETADAPTERGETNETLUID
title: PFN_NETADAPTERGETNETLUID
author: windows-driver-content
description: 
ms.assetid: bce0bee2-eb7b-48cc-8be1-3d5c3a8a9790
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

# PFN_NETADAPTERGETNETLUID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETADAPTERGETNETLUID PfnNetadaptergetnetluid; 

// Definition

WDFAPI PfnNetadaptergetnetluid 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETADAPTER Adapter
)
{...}

PFN_NETADAPTERGETNETLUID 


```

## -parameters

### -param DriverGlobals: 
### -param Adapter: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also