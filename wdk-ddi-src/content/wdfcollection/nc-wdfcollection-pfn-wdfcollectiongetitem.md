---
UID: NC.wdfcollection.PFN_WDFCOLLECTIONGETITEM
title: PFN_WDFCOLLECTIONGETITEM
author: windows-driver-content
description: 
ms.assetid: 6304ed95-d14f-45e6-93f5-f1ae0829233c
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

# PFN_WDFCOLLECTIONGETITEM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOLLECTIONGETITEM PfnWdfcollectiongetitem; 

// Definition

WDFAPI PfnWdfcollectiongetitem 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCOLLECTION Collection
	ULONG Index
)
{...}

PFN_WDFCOLLECTIONGETITEM 


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