---
UID: NC.wdfrequest.PFN_WDFREQUESTSEND
title: PFN_WDFREQUESTSEND
author: windows-driver-content
description: 
ms.assetid: 204f905f-972f-4d98-b4de-cbd81b632763
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

# PFN_WDFREQUESTSEND callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTSEND PfnWdfrequestsend; 

// Definition

WDFAPI PfnWdfrequestsend 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	WDFIOTARGET Target
	PWDF_REQUEST_SEND_OPTIONS Options
)
{...}

PFN_WDFREQUESTSEND 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param Target: 
### -param Options: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also