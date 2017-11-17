---
UID: NC.wdfrequest.PFN_WDFREQUESTGETREQUESTORPROCESSID
title: PFN_WDFREQUESTGETREQUESTORPROCESSID
author: windows-driver-content
description: 
ms.assetid: 1bb00a80-480c-463f-a328-71da45ad7fc9
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

# PFN_WDFREQUESTGETREQUESTORPROCESSID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTGETREQUESTORPROCESSID PfnWdfrequestgetrequestorprocessid; 

// Definition

WDFAPI PfnWdfrequestgetrequestorprocessid 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
)
{...}

PFN_WDFREQUESTGETREQUESTORPROCESSID 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also