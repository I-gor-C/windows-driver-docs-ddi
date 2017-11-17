---
UID: NC.wdfrequest.PFN_WDFREQUESTRETRIEVEOUTPUTBUFFER
title: PFN_WDFREQUESTRETRIEVEOUTPUTBUFFER
author: windows-driver-content
description: 
ms.assetid: fe16d075-98a6-405a-9d94-b8ca7a21f930
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

# PFN_WDFREQUESTRETRIEVEOUTPUTBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTRETRIEVEOUTPUTBUFFER PfnWdfrequestretrieveoutputbuffer; 

// Definition

WDFAPI PfnWdfrequestretrieveoutputbuffer 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	size_t MinimumRequiredSize
	PVOID *Buffer
	size_t *Length
)
{...}

PFN_WDFREQUESTRETRIEVEOUTPUTBUFFER 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param MinimumRequiredSize: 
### -param *Buffer: 
### -param *Length: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also