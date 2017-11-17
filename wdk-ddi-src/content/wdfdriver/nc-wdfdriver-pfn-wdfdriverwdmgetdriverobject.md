---
UID: NC.wdfdriver.PFN_WDFDRIVERWDMGETDRIVEROBJECT
title: PFN_WDFDRIVERWDMGETDRIVEROBJECT
author: windows-driver-content
description: 
ms.assetid: 0865f596-1652-4a85-bf3c-8c255609fb59
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdriver.h
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

# PFN_WDFDRIVERWDMGETDRIVEROBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDRIVERWDMGETDRIVEROBJECT PfnWdfdriverwdmgetdriverobject; 

// Definition

WDFAPI PfnWdfdriverwdmgetdriverobject 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDRIVER Driver
)
{...}

PFN_WDFDRIVERWDMGETDRIVEROBJECT 


```

## -parameters

### -param DriverGlobals: 
### -param Driver: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also