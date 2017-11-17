---
UID: NC.wdfdmaenabler.PFN_WDFDMAENABLERGETMAXIMUMLENGTH
title: PFN_WDFDMAENABLERGETMAXIMUMLENGTH
author: windows-driver-content
description: 
ms.assetid: 4769be9f-a328-49ca-8cdf-7a26e4788d86
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

# PFN_WDFDMAENABLERGETMAXIMUMLENGTH callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMAENABLERGETMAXIMUMLENGTH PfnWdfdmaenablergetmaximumlength; 

// Definition

WDFAPI PfnWdfdmaenablergetmaximumlength 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMAENABLER DmaEnabler
)
{...}

PFN_WDFDMAENABLERGETMAXIMUMLENGTH 


```

## -parameters

### -param DriverGlobals: 
### -param DmaEnabler: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also