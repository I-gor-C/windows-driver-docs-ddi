---
UID: NC.wdfrequest.PFN_WDFREQUESTSETACTIVITYID
title: PFN_WDFREQUESTSETACTIVITYID
author: windows-driver-content
description: 
ms.assetid: f3cbd900-23b2-4173-b431-2c810f363333
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

# PFN_WDFREQUESTSETACTIVITYID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTSETACTIVITYID PfnWdfrequestsetactivityid; 

// Definition

WDFAPI PfnWdfrequestsetactivityid 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	LPGUID ActivityId
)
{...}

PFN_WDFREQUESTSETACTIVITYID 


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