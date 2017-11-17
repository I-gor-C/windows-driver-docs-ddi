---
UID: NC.wdfiotarget.PFN_WDFIOTARGETCREATE
title: PFN_WDFIOTARGETCREATE
author: windows-driver-content
description: 
ms.assetid: 781e73c2-5514-4f89-8e0f-16da18c7afde
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfiotarget.h
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

# PFN_WDFIOTARGETCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETCREATE PfnWdfiotargetcreate; 

// Definition

WDFAPI PfnWdfiotargetcreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_OBJECT_ATTRIBUTES IoTargetAttributes
	WDFIOTARGET *IoTarget
)
{...}

PFN_WDFIOTARGETCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param IoTargetAttributes: 
### -param *IoTarget: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also