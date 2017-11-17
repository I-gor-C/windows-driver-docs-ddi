---
UID: NC.wdfcompaniontarget.PFN_WDFCOMPANIONTARGETWDMGETCOMPANIONPROCESS
title: PFN_WDFCOMPANIONTARGETWDMGETCOMPANIONPROCESS
author: windows-driver-content
description: 
ms.assetid: 16c6bf01-f9e1-4b90-8c8e-09a33dd14ed1
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfcompaniontarget.h
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

# PFN_WDFCOMPANIONTARGETWDMGETCOMPANIONPROCESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOMPANIONTARGETWDMGETCOMPANIONPROCESS PfnWdfcompaniontargetwdmgetcompanionprocess; 

// Definition

WDFAPI PfnWdfcompaniontargetwdmgetcompanionprocess 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCOMPANIONTARGET CompanionTarget
)
{...}

PFN_WDFCOMPANIONTARGETWDMGETCOMPANIONPROCESS 


```

## -parameters

### -param DriverGlobals: 
### -param CompanionTarget: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also