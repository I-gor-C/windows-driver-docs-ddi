---
UID: NC.wdfrequest.PFN_WDFREQUESTCREATEFROMIRP
title: PFN_WDFREQUESTCREATEFROMIRP
author: windows-driver-content
description: 
ms.assetid: 010642ac-a6e0-4ad6-9eaf-bab270a9c9a4
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

# PFN_WDFREQUESTCREATEFROMIRP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTCREATEFROMIRP PfnWdfrequestcreatefromirp; 

// Definition

WDFAPI PfnWdfrequestcreatefromirp 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDF_OBJECT_ATTRIBUTES RequestAttributes
	PIRP Irp
	BOOLEAN RequestFreesIrp
	WDFREQUEST *Request
)
{...}

PFN_WDFREQUESTCREATEFROMIRP 


```

## -parameters

### -param DriverGlobals: 
### -param RequestAttributes: 
### -param Irp: 
### -param RequestFreesIrp: 
### -param *Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also