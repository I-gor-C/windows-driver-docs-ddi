---
UID: NC.wdfrequest.PFN_WDFREQUESTRETRIEVEINPUTMEMORY
title: PFN_WDFREQUESTRETRIEVEINPUTMEMORY
author: windows-driver-content
description: 
ms.assetid: 3f3abdff-2863-46a2-8087-13e1eb07c0f5
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

# PFN_WDFREQUESTRETRIEVEINPUTMEMORY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTRETRIEVEINPUTMEMORY PfnWdfrequestretrieveinputmemory; 

// Definition

WDFAPI PfnWdfrequestretrieveinputmemory 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	WDFMEMORY *Memory
)
{...}

PFN_WDFREQUESTRETRIEVEINPUTMEMORY 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param *Memory: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also