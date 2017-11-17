---
UID: NC.wdfrequest.PFN_WDFREQUESTRETRIEVEUNSAFEUSEROUTPUTBUFFER
title: PFN_WDFREQUESTRETRIEVEUNSAFEUSEROUTPUTBUFFER
author: windows-driver-content
description: 
ms.assetid: d9d31882-d0f6-4931-a7a0-3eb7329f80f1
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

# PFN_WDFREQUESTRETRIEVEUNSAFEUSEROUTPUTBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTRETRIEVEUNSAFEUSEROUTPUTBUFFER PfnWdfrequestretrieveunsafeuseroutputbuffer; 

// Definition

WDFAPI PfnWdfrequestretrieveunsafeuseroutputbuffer 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	size_t MinimumRequiredLength
	PVOID *OutputBuffer
	size_t *Length
)
{...}

PFN_WDFREQUESTRETRIEVEUNSAFEUSEROUTPUTBUFFER 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param MinimumRequiredLength: 
### -param *OutputBuffer: 
### -param *Length: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also