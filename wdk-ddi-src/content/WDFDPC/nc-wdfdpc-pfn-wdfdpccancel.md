---
UID: NC.wdfdpc.PFN_WDFDPCCANCEL
title: *PFN_WDFDPCCANCEL
author: windows-driver-content
description: 
ms.assetid: d86845b1-2a20-4960-b21c-36c81425c82b
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

# *PFN_WDFDPCCANCEL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFDPCCANCEL *PfnWdfdpccancel; 

// Definition

BOOLEAN *PfnWdfdpccancel 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDPC Dpc
	BOOLEAN Wait
)
{...}

*PFN_WDFDPCCANCEL 


```

## -parameters

### -param DriverGlobals: 
### -param Dpc: 
### -param Wait: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also