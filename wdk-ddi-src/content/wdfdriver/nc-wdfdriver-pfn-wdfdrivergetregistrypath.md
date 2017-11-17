---
UID: NC.wdfdriver.PFN_WDFDRIVERGETREGISTRYPATH
title: PFN_WDFDRIVERGETREGISTRYPATH
author: windows-driver-content
description: 
ms.assetid: 6cef6d64-04d9-48ff-a63b-e9e21897def6
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdriver.h
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

# PFN_WDFDRIVERGETREGISTRYPATH callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDRIVERGETREGISTRYPATH PfnWdfdrivergetregistrypath; 

// Definition

WDFAPI PfnWdfdrivergetregistrypath 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDRIVER Driver
)
{...}

PFN_WDFDRIVERGETREGISTRYPATH 


```

## -parameters

### -param DriverGlobals: 
### -param Driver: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also