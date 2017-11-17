---
UID: NC.netadapter.PFN_NETADAPTERDRIVERWDMGETHANDLE
title: PFN_NETADAPTERDRIVERWDMGETHANDLE
author: windows-driver-content
description: 
ms.assetid: 93eb1f26-d01b-4cff-b151-49258c7fa180
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

# PFN_NETADAPTERDRIVERWDMGETHANDLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETADAPTERDRIVERWDMGETHANDLE PfnNetadapterdriverwdmgethandle; 

// Definition

WDFAPI PfnNetadapterdriverwdmgethandle 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	WDFDRIVER Driver
)
{...}

PFN_NETADAPTERDRIVERWDMGETHANDLE 


```

## -parameters

### -param DriverGlobals: 
### -param Driver: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also