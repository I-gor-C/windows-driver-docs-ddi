---
UID: NC.wdfusb.PFN_WDFUSBTARGETPIPEWRITESYNCHRONOUSLY
title: PFN_WDFUSBTARGETPIPEWRITESYNCHRONOUSLY
author: windows-driver-content
description: 
ms.assetid: 5e3944bf-48f2-4efd-9157-a8ab128d8d39
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

# PFN_WDFUSBTARGETPIPEWRITESYNCHRONOUSLY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETPIPEWRITESYNCHRONOUSLY PfnWdfusbtargetpipewritesynchronously; 

// Definition

WDFAPI PfnWdfusbtargetpipewritesynchronously 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBPIPE Pipe
	WDFREQUEST Request
	PWDF_REQUEST_SEND_OPTIONS RequestOptions
	PWDF_MEMORY_DESCRIPTOR MemoryDescriptor
	PULONG BytesWritten
)
{...}

PFN_WDFUSBTARGETPIPEWRITESYNCHRONOUSLY 


```

## -parameters

### -param DriverGlobals: 
### -param Pipe: 
### -param Request: 
### -param RequestOptions: 
### -param MemoryDescriptor: 
### -param BytesWritten: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also