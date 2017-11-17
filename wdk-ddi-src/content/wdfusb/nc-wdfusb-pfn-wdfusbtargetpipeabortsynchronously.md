---
UID: NC.wdfusb.PFN_WDFUSBTARGETPIPEABORTSYNCHRONOUSLY
title: PFN_WDFUSBTARGETPIPEABORTSYNCHRONOUSLY
author: windows-driver-content
description: 
ms.assetid: 0402bfcc-6366-449b-813c-2b8ddd8c4991
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

# PFN_WDFUSBTARGETPIPEABORTSYNCHRONOUSLY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETPIPEABORTSYNCHRONOUSLY PfnWdfusbtargetpipeabortsynchronously; 

// Definition

WDFAPI PfnWdfusbtargetpipeabortsynchronously 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBPIPE Pipe
	WDFREQUEST Request
	PWDF_REQUEST_SEND_OPTIONS RequestOptions
)
{...}

PFN_WDFUSBTARGETPIPEABORTSYNCHRONOUSLY 


```

## -parameters

### -param DriverGlobals: 
### -param Pipe: 
### -param Request: 
### -param RequestOptions: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also