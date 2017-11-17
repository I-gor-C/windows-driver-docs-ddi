---
UID: NC.wdfrequest.PFN_WDFREQUESTFORWARDTOIOQUEUE
title: PFN_WDFREQUESTFORWARDTOIOQUEUE
author: windows-driver-content
description: 
ms.assetid: 1432ce1b-a5cf-4fb6-b441-92ec03f77d0f
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

# PFN_WDFREQUESTFORWARDTOIOQUEUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTFORWARDTOIOQUEUE PfnWdfrequestforwardtoioqueue; 

// Definition

WDFAPI PfnWdfrequestforwardtoioqueue 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	WDFQUEUE DestinationQueue
)
{...}

PFN_WDFREQUESTFORWARDTOIOQUEUE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param DestinationQueue: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also