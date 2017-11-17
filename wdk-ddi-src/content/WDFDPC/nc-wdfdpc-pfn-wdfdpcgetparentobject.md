---
UID: NC.wdfdpc.PFN_WDFDPCGETPARENTOBJECT
title: PFN_WDFDPCGETPARENTOBJECT
author: windows-driver-content
description: 
ms.assetid: 76c928b6-82fb-4a33-8b81-1d8acc2f863d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdpc.h
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

# PFN_WDFDPCGETPARENTOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDPCGETPARENTOBJECT PfnWdfdpcgetparentobject; 

// Definition

WDFAPI PfnWdfdpcgetparentobject 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDPC Dpc
)
{...}

PFN_WDFDPCGETPARENTOBJECT 


```

## -parameters

### -param DriverGlobals: 
### -param Dpc: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also