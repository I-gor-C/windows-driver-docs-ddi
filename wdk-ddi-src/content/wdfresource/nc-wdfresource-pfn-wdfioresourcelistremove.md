---
UID: NC.wdfresource.PFN_WDFIORESOURCELISTREMOVE
title: PFN_WDFIORESOURCELISTREMOVE
author: windows-driver-content
description: 
ms.assetid: a2b5704e-3880-46db-8a40-d9a75742b2f2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfresource.h
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

# PFN_WDFIORESOURCELISTREMOVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIORESOURCELISTREMOVE PfnWdfioresourcelistremove; 

// Definition

WDFAPI PfnWdfioresourcelistremove 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIORESLIST ResourceList
	ULONG Index
)
{...}

PFN_WDFIORESOURCELISTREMOVE 


```

## -parameters

### -param DriverGlobals: 
### -param ResourceList: 
### -param Index: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also