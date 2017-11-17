---
UID: NC.wdfrequest.PFN_WDFREQUESTRETRIEVEUNSAFEUSERINPUTBUFFER
title: PFN_WDFREQUESTRETRIEVEUNSAFEUSERINPUTBUFFER
author: windows-driver-content
description: 
ms.assetid: c66574cf-2679-4050-b0a3-8914a4530e61
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

# PFN_WDFREQUESTRETRIEVEUNSAFEUSERINPUTBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTRETRIEVEUNSAFEUSERINPUTBUFFER PfnWdfrequestretrieveunsafeuserinputbuffer; 

// Definition

WDFAPI PfnWdfrequestretrieveunsafeuserinputbuffer 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	size_t MinimumRequiredLength
	PVOID *InputBuffer
	size_t *Length
)
{...}

PFN_WDFREQUESTRETRIEVEUNSAFEUSERINPUTBUFFER 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param MinimumRequiredLength: 
### -param *InputBuffer: 
### -param *Length: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also