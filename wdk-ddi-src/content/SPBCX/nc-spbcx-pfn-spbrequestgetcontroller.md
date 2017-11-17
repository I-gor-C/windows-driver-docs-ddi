---
UID: NC.spbcx.PFN_SPBREQUESTGETCONTROLLER
title: PFN_SPBREQUESTGETCONTROLLER
author: windows-driver-content
description: 
ms.assetid: f66e87b5-f122-41f0-b55c-2fef85f60e74
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: spbcx.h
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

# PFN_SPBREQUESTGETCONTROLLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SPBREQUESTGETCONTROLLER PfnSpbrequestgetcontroller; 

// Definition

WDFAPI PfnSpbrequestgetcontroller 
(
	PSPB_DRIVER_GLOBALS DriverGlobals
	SPBREQUEST SpbRequest
)
{...}

PFN_SPBREQUESTGETCONTROLLER 


```

## -parameters

### -param DriverGlobals: 
### -param SpbRequest: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also