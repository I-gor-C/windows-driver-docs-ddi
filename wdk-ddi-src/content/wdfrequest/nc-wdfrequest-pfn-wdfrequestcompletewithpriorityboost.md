---
UID: NC.wdfrequest.PFN_WDFREQUESTCOMPLETEWITHPRIORITYBOOST
title: PFN_WDFREQUESTCOMPLETEWITHPRIORITYBOOST
author: windows-driver-content
description: 
ms.assetid: 71f618fe-b5fc-4c78-92f3-cb3ce774c708
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

# PFN_WDFREQUESTCOMPLETEWITHPRIORITYBOOST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTCOMPLETEWITHPRIORITYBOOST PfnWdfrequestcompletewithpriorityboost; 

// Definition

WDFAPI PfnWdfrequestcompletewithpriorityboost 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	NTSTATUS Status
	CCHAR PriorityBoost
)
{...}

PFN_WDFREQUESTCOMPLETEWITHPRIORITYBOOST 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param Status: 
### -param PriorityBoost: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also