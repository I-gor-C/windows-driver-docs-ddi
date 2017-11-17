---
UID: NC.wdfverifier.PFN_WDFGETTRIAGEINFO
title: *PFN_WDFGETTRIAGEINFO
author: windows-driver-content
description: 
ms.assetid: 41acfb22-9754-4f8b-b865-3cafbeee9069
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfverifier.h
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

# *PFN_WDFGETTRIAGEINFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFGETTRIAGEINFO *PfnWdfgettriageinfo; 

// Definition

PVOID *PfnWdfgettriageinfo 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
)
{...}

*PFN_WDFGETTRIAGEINFO 


```

## -parameters

### -param DriverGlobals: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also