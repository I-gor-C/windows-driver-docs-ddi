---
UID: NC.ucxroothub.PFN_UCXROOTHUBPORTCHANGED
title: PFN_UCXROOTHUBPORTCHANGED
author: windows-driver-content
description: 
ms.assetid: c8b6c1c8-c990-4945-ac9d-0f7eea5d64d2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxroothub.h
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

# PFN_UCXROOTHUBPORTCHANGED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXROOTHUBPORTCHANGED PfnUcxroothubportchanged; 

// Definition

WDFAPI PfnUcxroothubportchanged 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXROOTHUB UcxRootHub
)
{...}

PFN_UCXROOTHUBPORTCHANGED 


```

## -parameters

### -param DriverGlobals: 
### -param UcxRootHub: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also