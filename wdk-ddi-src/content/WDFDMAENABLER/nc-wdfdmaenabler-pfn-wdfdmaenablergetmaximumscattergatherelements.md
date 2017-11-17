---
UID: NC.wdfdmaenabler.PFN_WDFDMAENABLERGETMAXIMUMSCATTERGATHERELEMENTS
title: PFN_WDFDMAENABLERGETMAXIMUMSCATTERGATHERELEMENTS
author: windows-driver-content
description: 
ms.assetid: cba92e48-e91b-4391-baca-b1140f6a23ec
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdmaenabler.h
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

# PFN_WDFDMAENABLERGETMAXIMUMSCATTERGATHERELEMENTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMAENABLERGETMAXIMUMSCATTERGATHERELEMENTS PfnWdfdmaenablergetmaximumscattergatherelements; 

// Definition

WDFAPI PfnWdfdmaenablergetmaximumscattergatherelements 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMAENABLER DmaEnabler
)
{...}

PFN_WDFDMAENABLERGETMAXIMUMSCATTERGATHERELEMENTS 


```

## -parameters

### -param DriverGlobals: 
### -param DmaEnabler: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also