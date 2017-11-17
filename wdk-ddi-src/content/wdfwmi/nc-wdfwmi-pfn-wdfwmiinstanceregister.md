---
UID: NC.wdfwmi.PFN_WDFWMIINSTANCEREGISTER
title: PFN_WDFWMIINSTANCEREGISTER
author: windows-driver-content
description: 
ms.assetid: 180f39b5-25aa-456d-b9a2-c8c162fe6233
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfwmi.h
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

# PFN_WDFWMIINSTANCEREGISTER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWMIINSTANCEREGISTER PfnWdfwmiinstanceregister; 

// Definition

WDFAPI PfnWdfwmiinstanceregister 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFWMIINSTANCE WmiInstance
)
{...}

PFN_WDFWMIINSTANCEREGISTER 


```

## -parameters

### -param DriverGlobals: 
### -param WmiInstance: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also