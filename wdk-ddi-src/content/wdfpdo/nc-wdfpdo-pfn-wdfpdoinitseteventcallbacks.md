---
UID: NC.wdfpdo.PFN_WDFPDOINITSETEVENTCALLBACKS
title: PFN_WDFPDOINITSETEVENTCALLBACKS
author: windows-driver-content
description: 
ms.assetid: 5cea816b-0573-4b0b-bf77-b7f84ac0b96b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfpdo.h
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

# PFN_WDFPDOINITSETEVENTCALLBACKS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDOINITSETEVENTCALLBACKS PfnWdfpdoinitseteventcallbacks; 

// Definition

WDFAPI PfnWdfpdoinitseteventcallbacks 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PWDF_PDO_EVENT_CALLBACKS DispatchTable
)
{...}

PFN_WDFPDOINITSETEVENTCALLBACKS 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param DispatchTable: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also