---
UID: NC.wdfio.PFN_WDFIOQUEUERETRIEVEREQUESTBYFILEOBJECT
title: PFN_WDFIOQUEUERETRIEVEREQUESTBYFILEOBJECT
author: windows-driver-content
description: 
ms.assetid: 4f301378-1030-4d5f-a844-b0c6461311fd
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

# PFN_WDFIOQUEUERETRIEVEREQUESTBYFILEOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOQUEUERETRIEVEREQUESTBYFILEOBJECT PfnWdfioqueueretrieverequestbyfileobject; 

// Definition

WDFAPI PfnWdfioqueueretrieverequestbyfileobject 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFQUEUE Queue
	WDFFILEOBJECT FileObject
	WDFREQUEST *OutRequest
)
{...}

PFN_WDFIOQUEUERETRIEVEREQUESTBYFILEOBJECT 


```

## -parameters

### -param DriverGlobals: 
### -param Queue: 
### -param FileObject: 
### -param *OutRequest: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also