---
UID: NC.wdfrequest.PFN_WDFREQUESTRETRIEVEINPUTBUFFER
title: PFN_WDFREQUESTRETRIEVEINPUTBUFFER
author: windows-driver-content
description: 
ms.assetid: 288a4814-dd52-43b7-9554-ca6139140bf1
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

# PFN_WDFREQUESTRETRIEVEINPUTBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTRETRIEVEINPUTBUFFER PfnWdfrequestretrieveinputbuffer; 

// Definition

WDFAPI PfnWdfrequestretrieveinputbuffer 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	size_t MinimumRequiredLength
	PVOID *Buffer
	size_t *Length
)
{...}

PFN_WDFREQUESTRETRIEVEINPUTBUFFER 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param MinimumRequiredLength: 
### -param *Buffer: 
### -param *Length: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also