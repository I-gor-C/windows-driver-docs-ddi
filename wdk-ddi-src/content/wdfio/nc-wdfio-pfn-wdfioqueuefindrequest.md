---
UID: NC.wdfio.PFN_WDFIOQUEUEFINDREQUEST
title: PFN_WDFIOQUEUEFINDREQUEST
author: windows-driver-content
description: 
ms.assetid: 77d94ab5-6004-425b-85b5-be76f2173fb8
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

# PFN_WDFIOQUEUEFINDREQUEST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOQUEUEFINDREQUEST PfnWdfioqueuefindrequest; 

// Definition

WDFAPI PfnWdfioqueuefindrequest 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFQUEUE Queue
	WDFREQUEST FoundRequest
	WDFFILEOBJECT FileObject
	PWDF_REQUEST_PARAMETERS Parameters
	WDFREQUEST *OutRequest
)
{...}

PFN_WDFIOQUEUEFINDREQUEST 


```

## -parameters

### -param DriverGlobals: 
### -param Queue: 
### -param FoundRequest: 
### -param FileObject: 
### -param Parameters: 
### -param *OutRequest: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also