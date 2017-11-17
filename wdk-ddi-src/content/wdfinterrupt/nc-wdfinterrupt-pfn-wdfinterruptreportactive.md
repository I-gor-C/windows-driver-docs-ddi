---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTREPORTACTIVE
title: PFN_WDFINTERRUPTREPORTACTIVE
author: windows-driver-content
description: 
ms.assetid: 426cfaec-4263-4c68-a2d8-422732db53de
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfinterrupt.h
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

# PFN_WDFINTERRUPTREPORTACTIVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFINTERRUPTREPORTACTIVE PfnWdfinterruptreportactive; 

// Definition

WDFAPI PfnWdfinterruptreportactive 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFINTERRUPT Interrupt
)
{...}

PFN_WDFINTERRUPTREPORTACTIVE 


```

## -parameters

### -param DriverGlobals: 
### -param Interrupt: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also