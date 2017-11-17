---
UID: NC.ursdevice.PFN_URSSETPOHANDLE
title: PFN_URSSETPOHANDLE
author: windows-driver-content
description: 
ms.assetid: 1b3cd242-9c90-4a04-bd25-44cc6363b2d9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ursdevice.h
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

# PFN_URSSETPOHANDLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_URSSETPOHANDLE PfnUrssetpohandle; 

// Definition

WDFAPI PfnUrssetpohandle 
(
	PURS_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	POHANDLE PoHandle
)
{...}

PFN_URSSETPOHANDLE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param PoHandle: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also