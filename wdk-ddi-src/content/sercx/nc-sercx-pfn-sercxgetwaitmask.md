---
UID: NC.sercx.PFN_SERCXGETWAITMASK
title: PFN_SERCXGETWAITMASK
author: windows-driver-content
description: 
ms.assetid: 45ea7aee-5bd9-42d2-9dfc-cc88b4758cc6
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

# PFN_SERCXGETWAITMASK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCXGETWAITMASK PfnSercxgetwaitmask; 

// Definition

WDFAPI PfnSercxgetwaitmask 
(
	PSER_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
)
{...}

PFN_SERCXGETWAITMASK 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also