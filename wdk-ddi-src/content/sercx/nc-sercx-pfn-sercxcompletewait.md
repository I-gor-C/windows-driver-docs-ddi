---
UID: NC.sercx.PFN_SERCXCOMPLETEWAIT
title: PFN_SERCXCOMPLETEWAIT
author: windows-driver-content
description: 
ms.assetid: 2b8a29fd-31f1-4eb7-9b83-468e441c163f
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

# PFN_SERCXCOMPLETEWAIT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCXCOMPLETEWAIT PfnSercxcompletewait; 

// Definition

WDFAPI PfnSercxcompletewait 
(
	PSER_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	ULONG Event
)
{...}

PFN_SERCXCOMPLETEWAIT 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Event: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also