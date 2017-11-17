---
UID: NC.wdftimer.PFN_WDFTIMERGETPARENTOBJECT
title: PFN_WDFTIMERGETPARENTOBJECT
author: windows-driver-content
description: 
ms.assetid: 061186b5-a5f9-4dd8-b8d3-3936be956434
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdftimer.h
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

# PFN_WDFTIMERGETPARENTOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFTIMERGETPARENTOBJECT PfnWdftimergetparentobject; 

// Definition

WDFAPI PfnWdftimergetparentobject 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFTIMER Timer
)
{...}

PFN_WDFTIMERGETPARENTOBJECT 


```

## -parameters

### -param DriverGlobals: 
### -param Timer: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also