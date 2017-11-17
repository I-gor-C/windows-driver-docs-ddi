---
UID: NC.wdfrequest.PFN_WDFREQUESTSTOPACKNOWLEDGE
title: PFN_WDFREQUESTSTOPACKNOWLEDGE
author: windows-driver-content
description: 
ms.assetid: 2b18ac4c-58ad-45c3-bc3f-c4f1b0fbf471
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

# PFN_WDFREQUESTSTOPACKNOWLEDGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTSTOPACKNOWLEDGE PfnWdfrequeststopacknowledge; 

// Definition

WDFAPI PfnWdfrequeststopacknowledge 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	BOOLEAN Requeue
)
{...}

PFN_WDFREQUESTSTOPACKNOWLEDGE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param Requeue: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also