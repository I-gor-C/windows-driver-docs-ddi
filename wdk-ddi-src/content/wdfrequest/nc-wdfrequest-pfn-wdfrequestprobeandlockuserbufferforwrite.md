---
UID: NC.wdfrequest.PFN_WDFREQUESTPROBEANDLOCKUSERBUFFERFORWRITE
title: PFN_WDFREQUESTPROBEANDLOCKUSERBUFFERFORWRITE
author: windows-driver-content
description: 
ms.assetid: a130f07e-6d20-48e8-be66-4be07bf01ce6
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

# PFN_WDFREQUESTPROBEANDLOCKUSERBUFFERFORWRITE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTPROBEANDLOCKUSERBUFFERFORWRITE PfnWdfrequestprobeandlockuserbufferforwrite; 

// Definition

WDFAPI PfnWdfrequestprobeandlockuserbufferforwrite 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	PVOID Buffer
	size_t Length
	WDFMEMORY *MemoryObject
)
{...}

PFN_WDFREQUESTPROBEANDLOCKUSERBUFFERFORWRITE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param Buffer: 
### -param Length: 
### -param *MemoryObject: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also