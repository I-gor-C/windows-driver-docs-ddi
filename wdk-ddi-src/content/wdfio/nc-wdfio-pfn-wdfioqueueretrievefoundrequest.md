---
UID: NC.wdfio.PFN_WDFIOQUEUERETRIEVEFOUNDREQUEST
title: PFN_WDFIOQUEUERETRIEVEFOUNDREQUEST
author: windows-driver-content
description: 
ms.assetid: 31e2d97f-fa7b-4223-b5bd-9996cd0ab32c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfio.h
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

# PFN_WDFIOQUEUERETRIEVEFOUNDREQUEST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOQUEUERETRIEVEFOUNDREQUEST PfnWdfioqueueretrievefoundrequest; 

// Definition

WDFAPI PfnWdfioqueueretrievefoundrequest 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFQUEUE Queue
	WDFREQUEST FoundRequest
	WDFREQUEST *OutRequest
)
{...}

PFN_WDFIOQUEUERETRIEVEFOUNDREQUEST 


```

## -parameters

### -param DriverGlobals: 
### -param Queue: 
### -param FoundRequest: 
### -param *OutRequest: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also