---
UID: NC.ucxcontroller.PFN_UCXCONTROLLERNEEDSRESET
title: PFN_UCXCONTROLLERNEEDSRESET
author: windows-driver-content
description: 
ms.assetid: a267a5ac-e83b-4ca0-a42a-3c192564465d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxcontroller.h
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

# PFN_UCXCONTROLLERNEEDSRESET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXCONTROLLERNEEDSRESET PfnUcxcontrollerneedsreset; 

// Definition

WDFAPI PfnUcxcontrollerneedsreset 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXCONTROLLER Controller
)
{...}

PFN_UCXCONTROLLERNEEDSRESET 


```

## -parameters

### -param DriverGlobals: 
### -param Controller: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also