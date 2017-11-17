---
UID: NC.wdfcollection.PFN_WDFCOLLECTIONREMOVE
title: PFN_WDFCOLLECTIONREMOVE
author: windows-driver-content
description: 
ms.assetid: 8eff4922-ad4b-4bde-ac7b-e6beddd5d63c
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

# PFN_WDFCOLLECTIONREMOVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOLLECTIONREMOVE PfnWdfcollectionremove; 

// Definition

WDFAPI PfnWdfcollectionremove 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCOLLECTION Collection
	WDFOBJECT Item
)
{...}

PFN_WDFCOLLECTIONREMOVE 


```

## -parameters

### -param DriverGlobals: 
### -param Collection: 
### -param Item: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also