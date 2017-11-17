---
UID: NC.wdfrequest.PFN_WDFREQUESTGETPARAMETERS
title: PFN_WDFREQUESTGETPARAMETERS
author: windows-driver-content
description: 
ms.assetid: 856c728f-b394-46e5-b7fc-3d3247590b1f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfrequest.h
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

# PFN_WDFREQUESTGETPARAMETERS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTGETPARAMETERS PfnWdfrequestgetparameters; 

// Definition

WDFAPI PfnWdfrequestgetparameters 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	PWDF_REQUEST_PARAMETERS Parameters
)
{...}

PFN_WDFREQUESTGETPARAMETERS 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param Parameters: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also