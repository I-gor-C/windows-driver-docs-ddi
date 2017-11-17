---
UID: NC.wdfusb.PFN_WDFUSBTARGETPIPESENDURBSYNCHRONOUSLY
title: PFN_WDFUSBTARGETPIPESENDURBSYNCHRONOUSLY
author: windows-driver-content
description: 
ms.assetid: 87046c62-9609-4c96-9452-10758ce597b5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfusb.h
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

# PFN_WDFUSBTARGETPIPESENDURBSYNCHRONOUSLY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETPIPESENDURBSYNCHRONOUSLY PfnWdfusbtargetpipesendurbsynchronously; 

// Definition

WDFAPI PfnWdfusbtargetpipesendurbsynchronously 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBPIPE Pipe
	WDFREQUEST Request
	PWDF_REQUEST_SEND_OPTIONS RequestOptions
	PURB Urb
)
{...}

PFN_WDFUSBTARGETPIPESENDURBSYNCHRONOUSLY 


```

## -parameters

### -param DriverGlobals: 
### -param Pipe: 
### -param Request: 
### -param RequestOptions: 
### -param Urb: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also