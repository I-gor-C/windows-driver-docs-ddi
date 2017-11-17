---
UID: NC.wdfrequest.PFN_WDFREQUESTCREATE
title: PFN_WDFREQUESTCREATE
author: windows-driver-content
description: 
ms.assetid: bbf4ebff-fb44-4178-979f-1b989e8cf7f8
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

# PFN_WDFREQUESTCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTCREATE PfnWdfrequestcreate; 

// Definition

WDFAPI PfnWdfrequestcreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDF_OBJECT_ATTRIBUTES RequestAttributes
	WDFIOTARGET IoTarget
	WDFREQUEST *Request
)
{...}

PFN_WDFREQUESTCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param RequestAttributes: 
### -param IoTarget: 
### -param *Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also