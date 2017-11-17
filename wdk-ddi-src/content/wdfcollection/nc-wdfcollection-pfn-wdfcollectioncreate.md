---
UID: NC.wdfcollection.PFN_WDFCOLLECTIONCREATE
title: PFN_WDFCOLLECTIONCREATE
author: windows-driver-content
description: 
ms.assetid: 039479c6-b6ba-427e-9cb2-60dc31d4cca7
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

# PFN_WDFCOLLECTIONCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOLLECTIONCREATE PfnWdfcollectioncreate; 

// Definition

WDFAPI PfnWdfcollectioncreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDF_OBJECT_ATTRIBUTES CollectionAttributes
	WDFCOLLECTION *Collection
)
{...}

PFN_WDFCOLLECTIONCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param CollectionAttributes: 
### -param *Collection: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also