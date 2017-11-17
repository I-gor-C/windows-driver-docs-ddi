---
UID: NC.wdfiotarget.PFN_WDFIOTARGETSENDINTERNALIOCTLSYNCHRONOUSLY
title: PFN_WDFIOTARGETSENDINTERNALIOCTLSYNCHRONOUSLY
author: windows-driver-content
description: 
ms.assetid: f356d87e-696e-46fa-aa76-214acfb06532
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

# PFN_WDFIOTARGETSENDINTERNALIOCTLSYNCHRONOUSLY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETSENDINTERNALIOCTLSYNCHRONOUSLY PfnWdfiotargetsendinternalioctlsynchronously; 

// Definition

WDFAPI PfnWdfiotargetsendinternalioctlsynchronously 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
	WDFREQUEST Request
	ULONG IoctlCode
	PWDF_MEMORY_DESCRIPTOR InputBuffer
	PWDF_MEMORY_DESCRIPTOR OutputBuffer
	PWDF_REQUEST_SEND_OPTIONS RequestOptions
	PULONG_PTR BytesReturned
)
{...}

PFN_WDFIOTARGETSENDINTERNALIOCTLSYNCHRONOUSLY 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 
### -param Request: 
### -param IoctlCode: 
### -param InputBuffer: 
### -param OutputBuffer: 
### -param RequestOptions: 
### -param BytesReturned: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also