---
UID: NC.wdfrequest.PFN_WDFREQUESTGETCOMPLETIONPARAMS
title: PFN_WDFREQUESTGETCOMPLETIONPARAMS
author: windows-driver-content
description: 
ms.assetid: 3ce91949-0336-42af-9533-7ca5ff01384b
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

# PFN_WDFREQUESTGETCOMPLETIONPARAMS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTGETCOMPLETIONPARAMS PfnWdfrequestgetcompletionparams; 

// Definition

WDFAPI PfnWdfrequestgetcompletionparams 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	PWDF_REQUEST_COMPLETION_PARAMS Params
)
{...}

PFN_WDFREQUESTGETCOMPLETIONPARAMS 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param Params: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also