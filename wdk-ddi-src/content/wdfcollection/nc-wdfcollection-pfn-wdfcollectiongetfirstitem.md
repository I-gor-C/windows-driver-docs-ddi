---
UID: NC.wdfcollection.PFN_WDFCOLLECTIONGETFIRSTITEM
title: PFN_WDFCOLLECTIONGETFIRSTITEM
author: windows-driver-content
description: 
ms.assetid: b75b2f3c-3692-40e9-88dc-a5c6e9e5bd88
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

# PFN_WDFCOLLECTIONGETFIRSTITEM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOLLECTIONGETFIRSTITEM PfnWdfcollectiongetfirstitem; 

// Definition

WDFAPI PfnWdfcollectiongetfirstitem 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCOLLECTION Collection
)
{...}

PFN_WDFCOLLECTIONGETFIRSTITEM 


```

## -parameters

### -param DriverGlobals: 
### -param Collection: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also