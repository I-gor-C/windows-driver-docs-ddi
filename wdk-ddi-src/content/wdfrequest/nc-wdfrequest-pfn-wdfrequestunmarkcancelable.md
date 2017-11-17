---
UID: NC.wdfrequest.PFN_WDFREQUESTUNMARKCANCELABLE
title: PFN_WDFREQUESTUNMARKCANCELABLE
author: windows-driver-content
description: 
ms.assetid: a927bf71-ae62-41fd-be98-a0241e6a0070
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

# PFN_WDFREQUESTUNMARKCANCELABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTUNMARKCANCELABLE PfnWdfrequestunmarkcancelable; 

// Definition

WDFAPI PfnWdfrequestunmarkcancelable 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
)
{...}

PFN_WDFREQUESTUNMARKCANCELABLE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also