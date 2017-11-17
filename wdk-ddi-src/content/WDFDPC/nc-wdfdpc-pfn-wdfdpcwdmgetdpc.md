---
UID: NC.wdfdpc.PFN_WDFDPCWDMGETDPC
title: PFN_WDFDPCWDMGETDPC
author: windows-driver-content
description: 
ms.assetid: 503c1812-1bf3-4914-b0e2-569994c37364
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

# PFN_WDFDPCWDMGETDPC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDPCWDMGETDPC PfnWdfdpcwdmgetdpc; 

// Definition

WDFAPI PfnWdfdpcwdmgetdpc 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDPC Dpc
)
{...}

PFN_WDFDPCWDMGETDPC 


```

## -parameters

### -param DriverGlobals: 
### -param Dpc: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also