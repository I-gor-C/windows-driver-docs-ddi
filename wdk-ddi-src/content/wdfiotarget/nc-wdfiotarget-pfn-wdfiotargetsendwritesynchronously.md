---
UID: NC.wdfiotarget.PFN_WDFIOTARGETSENDWRITESYNCHRONOUSLY
title: PFN_WDFIOTARGETSENDWRITESYNCHRONOUSLY
author: windows-driver-content
description: 
ms.assetid: cadec0e6-0196-46d3-bfba-cf2f7e0c89e8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfiotarget.h
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

# PFN_WDFIOTARGETSENDWRITESYNCHRONOUSLY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETSENDWRITESYNCHRONOUSLY PfnWdfiotargetsendwritesynchronously; 

// Definition

WDFAPI PfnWdfiotargetsendwritesynchronously 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
	WDFREQUEST Request
	PWDF_MEMORY_DESCRIPTOR InputBuffer
	PLONGLONG DeviceOffset
	PWDF_REQUEST_SEND_OPTIONS RequestOptions
	PULONG_PTR BytesWritten
)
{...}

PFN_WDFIOTARGETSENDWRITESYNCHRONOUSLY 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 
### -param Request: 
### -param InputBuffer: 
### -param DeviceOffset: 
### -param RequestOptions: 
### -param BytesWritten: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also