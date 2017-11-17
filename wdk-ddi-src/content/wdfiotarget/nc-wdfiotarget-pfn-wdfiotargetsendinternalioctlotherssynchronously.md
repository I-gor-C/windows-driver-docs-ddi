---
UID: NC.wdfiotarget.PFN_WDFIOTARGETSENDINTERNALIOCTLOTHERSSYNCHRONOUSLY
title: PFN_WDFIOTARGETSENDINTERNALIOCTLOTHERSSYNCHRONOUSLY
author: windows-driver-content
description: 
ms.assetid: 24c704b2-520a-4c87-8048-8fcc1b731910
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

# PFN_WDFIOTARGETSENDINTERNALIOCTLOTHERSSYNCHRONOUSLY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETSENDINTERNALIOCTLOTHERSSYNCHRONOUSLY PfnWdfiotargetsendinternalioctlotherssynchronously; 

// Definition

WDFAPI PfnWdfiotargetsendinternalioctlotherssynchronously 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
	WDFREQUEST Request
	ULONG IoctlCode
	PWDF_MEMORY_DESCRIPTOR OtherArg1
	PWDF_MEMORY_DESCRIPTOR OtherArg2
	PWDF_MEMORY_DESCRIPTOR OtherArg4
	PWDF_REQUEST_SEND_OPTIONS RequestOptions
	PULONG_PTR BytesReturned
)
{...}

PFN_WDFIOTARGETSENDINTERNALIOCTLOTHERSSYNCHRONOUSLY 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 
### -param Request: 
### -param IoctlCode: 
### -param OtherArg1: 
### -param OtherArg2: 
### -param OtherArg4: 
### -param RequestOptions: 
### -param BytesReturned: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also