---
UID: NC.wdfrequest.PFN_WDFREQUESTRETRIEVEACTIVITYID
title: PFN_WDFREQUESTRETRIEVEACTIVITYID
author: windows-driver-content
description: 
ms.assetid: dcc3f117-8c2b-4257-bce6-a0729f9600d2
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

# PFN_WDFREQUESTRETRIEVEACTIVITYID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTRETRIEVEACTIVITYID PfnWdfrequestretrieveactivityid; 

// Definition

WDFAPI PfnWdfrequestretrieveactivityid 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	LPGUID ActivityId
)
{...}

PFN_WDFREQUESTRETRIEVEACTIVITYID 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param ActivityId: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also