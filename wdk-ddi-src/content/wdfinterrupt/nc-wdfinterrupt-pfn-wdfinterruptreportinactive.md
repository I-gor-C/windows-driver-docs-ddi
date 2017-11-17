---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTREPORTINACTIVE
title: PFN_WDFINTERRUPTREPORTINACTIVE
author: windows-driver-content
description: 
ms.assetid: 08ec752c-614f-48ef-b931-57c0a93a4e0f
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

# PFN_WDFINTERRUPTREPORTINACTIVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFINTERRUPTREPORTINACTIVE PfnWdfinterruptreportinactive; 

// Definition

WDFAPI PfnWdfinterruptreportinactive 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFINTERRUPT Interrupt
)
{...}

PFN_WDFINTERRUPTREPORTINACTIVE 


```

## -parameters

### -param DriverGlobals: 
### -param Interrupt: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also