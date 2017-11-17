---
UID: NC.spbcx.PFN_SPBREQUESTGETPARAMETERS
title: PFN_SPBREQUESTGETPARAMETERS
author: windows-driver-content
description: 
ms.assetid: 8643cbf8-858a-48d4-9e91-b87ed7881282
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

# PFN_SPBREQUESTGETPARAMETERS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SPBREQUESTGETPARAMETERS PfnSpbrequestgetparameters; 

// Definition

WDFAPI PfnSpbrequestgetparameters 
(
	PSPB_DRIVER_GLOBALS DriverGlobals
	SPBREQUEST SpbRequest
	SPB_REQUEST_PARAMETERS *Parameters
)
{...}

PFN_SPBREQUESTGETPARAMETERS 


```

## -parameters

### -param DriverGlobals: 
### -param SpbRequest: 
### -param *Parameters: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also