---
UID: NC.wdfcollection.PFN_WDFCOLLECTIONREMOVEITEM
title: PFN_WDFCOLLECTIONREMOVEITEM
author: windows-driver-content
description: 
ms.assetid: 7290b7c2-82fd-4025-9ad5-1fb6d0de0ff0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfcollection.h
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

# PFN_WDFCOLLECTIONREMOVEITEM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOLLECTIONREMOVEITEM PfnWdfcollectionremoveitem; 

// Definition

WDFAPI PfnWdfcollectionremoveitem 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCOLLECTION Collection
	ULONG Index
)
{...}

PFN_WDFCOLLECTIONREMOVEITEM 


```

## -parameters

### -param DriverGlobals: 
### -param Collection: 
### -param Index: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also