---
UID: NC.wdfcompanion.PFN_WDFCOMPANIONCREATE
title: PFN_WDFCOMPANIONCREATE
author: windows-driver-content
description: 
ms.assetid: 7c0a8132-7eab-4944-8e78-aafc89b4df29
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfcompanion.h
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

# PFN_WDFCOMPANIONCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOMPANIONCREATE PfnWdfcompanioncreate; 

// Definition

WDFAPI PfnWdfcompanioncreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT *DeviceInit
	PWDF_OBJECT_ATTRIBUTES DeviceAttributes
	WDFCOMPANION *Companion
)
{...}

PFN_WDFCOMPANIONCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param *DeviceInit: 
### -param DeviceAttributes: 
### -param *Companion: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also