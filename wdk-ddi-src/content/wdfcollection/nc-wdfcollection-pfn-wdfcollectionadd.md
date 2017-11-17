---
UID: NC.wdfcollection.PFN_WDFCOLLECTIONADD
title: PFN_WDFCOLLECTIONADD
author: windows-driver-content
description: 
ms.assetid: 00fc227c-2b18-4324-abed-3de55718ec21
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

# PFN_WDFCOLLECTIONADD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOLLECTIONADD PfnWdfcollectionadd; 

// Definition

WDFAPI PfnWdfcollectionadd 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCOLLECTION Collection
	WDFOBJECT Object
)
{...}

PFN_WDFCOLLECTIONADD 


```

## -parameters

### -param DriverGlobals: 
### -param Collection: 
### -param Object: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also