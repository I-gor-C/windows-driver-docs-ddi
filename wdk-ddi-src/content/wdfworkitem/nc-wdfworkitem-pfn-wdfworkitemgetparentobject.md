---
UID: NC.wdfworkitem.PFN_WDFWORKITEMGETPARENTOBJECT
title: PFN_WDFWORKITEMGETPARENTOBJECT
author: windows-driver-content
description: 
ms.assetid: 35a63dc2-502d-4e42-ba3e-5c0a46590f4a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfworkitem.h
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

# PFN_WDFWORKITEMGETPARENTOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWORKITEMGETPARENTOBJECT PfnWdfworkitemgetparentobject; 

// Definition

WDFAPI PfnWdfworkitemgetparentobject 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFWORKITEM WorkItem
)
{...}

PFN_WDFWORKITEMGETPARENTOBJECT 


```

## -parameters

### -param DriverGlobals: 
### -param WorkItem: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also