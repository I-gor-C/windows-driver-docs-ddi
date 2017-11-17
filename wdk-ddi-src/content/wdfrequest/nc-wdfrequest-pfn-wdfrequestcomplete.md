---
UID: NC.wdfrequest.PFN_WDFREQUESTCOMPLETE
title: PFN_WDFREQUESTCOMPLETE
author: windows-driver-content
description: 
ms.assetid: 2df4e6c8-4f11-4f2f-ab03-a705eb44cb5a
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

# PFN_WDFREQUESTCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTCOMPLETE PfnWdfrequestcomplete; 

// Definition

WDFAPI PfnWdfrequestcomplete 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	NTSTATUS Status
)
{...}

PFN_WDFREQUESTCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param Status: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also