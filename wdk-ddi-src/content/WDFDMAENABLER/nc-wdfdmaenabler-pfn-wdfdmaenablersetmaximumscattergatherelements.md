---
UID: NC.wdfdmaenabler.PFN_WDFDMAENABLERSETMAXIMUMSCATTERGATHERELEMENTS
title: PFN_WDFDMAENABLERSETMAXIMUMSCATTERGATHERELEMENTS
author: windows-driver-content
description: 
ms.assetid: 6eaa2345-c21a-4864-b9fe-d168981ae4b9
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

# PFN_WDFDMAENABLERSETMAXIMUMSCATTERGATHERELEMENTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMAENABLERSETMAXIMUMSCATTERGATHERELEMENTS PfnWdfdmaenablersetmaximumscattergatherelements; 

// Definition

WDFAPI PfnWdfdmaenablersetmaximumscattergatherelements 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMAENABLER DmaEnabler
	size_t MaximumFragments
)
{...}

PFN_WDFDMAENABLERSETMAXIMUMSCATTERGATHERELEMENTS 


```

## -parameters

### -param DriverGlobals: 
### -param DmaEnabler: 
### -param MaximumFragments: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also