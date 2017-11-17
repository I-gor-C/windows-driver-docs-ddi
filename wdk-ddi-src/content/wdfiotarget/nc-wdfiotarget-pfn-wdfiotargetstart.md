---
UID: NC.wdfiotarget.PFN_WDFIOTARGETSTART
title: PFN_WDFIOTARGETSTART
author: windows-driver-content
description: 
ms.assetid: b9a3dc70-85bd-48e3-a559-61c8c499f8ab
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

# PFN_WDFIOTARGETSTART callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETSTART PfnWdfiotargetstart; 

// Definition

WDFAPI PfnWdfiotargetstart 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
)
{...}

PFN_WDFIOTARGETSTART 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also