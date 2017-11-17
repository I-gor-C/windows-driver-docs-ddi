---
UID: NC.wdfcollection.PFN_WDFCOLLECTIONGETLASTITEM
title: PFN_WDFCOLLECTIONGETLASTITEM
author: windows-driver-content
description: 
ms.assetid: e4166d75-4d6e-4e98-85b3-26a3b5fd447f
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

# PFN_WDFCOLLECTIONGETLASTITEM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOLLECTIONGETLASTITEM PfnWdfcollectiongetlastitem; 

// Definition

WDFAPI PfnWdfcollectiongetlastitem 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCOLLECTION Collection
)
{...}

PFN_WDFCOLLECTIONGETLASTITEM 


```

## -parameters

### -param DriverGlobals: 
### -param Collection: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also