---
UID: NC.sercx.PFN_SERCXGETREADINTERVALTIMEOUT
title: PFN_SERCXGETREADINTERVALTIMEOUT
author: windows-driver-content
description: 
ms.assetid: aa62e783-1e44-44a5-835e-977b81c65717
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sercx.h
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

# PFN_SERCXGETREADINTERVALTIMEOUT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCXGETREADINTERVALTIMEOUT PfnSercxgetreadintervaltimeout; 

// Definition

WDFAPI PfnSercxgetreadintervaltimeout 
(
	PSER_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
)
{...}

PFN_SERCXGETREADINTERVALTIMEOUT 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also