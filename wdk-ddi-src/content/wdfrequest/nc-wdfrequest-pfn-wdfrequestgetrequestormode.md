---
UID: NC.wdfrequest.PFN_WDFREQUESTGETREQUESTORMODE
title: PFN_WDFREQUESTGETREQUESTORMODE
author: windows-driver-content
description: 
ms.assetid: e2d6f7e4-1de1-4854-b725-3899dee73cd0
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

# PFN_WDFREQUESTGETREQUESTORMODE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTGETREQUESTORMODE PfnWdfrequestgetrequestormode; 

// Definition

WDFAPI PfnWdfrequestgetrequestormode 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
)
{...}

PFN_WDFREQUESTGETREQUESTORMODE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also