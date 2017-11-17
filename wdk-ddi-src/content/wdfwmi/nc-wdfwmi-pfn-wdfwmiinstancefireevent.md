---
UID: NC.wdfwmi.PFN_WDFWMIINSTANCEFIREEVENT
title: PFN_WDFWMIINSTANCEFIREEVENT
author: windows-driver-content
description: 
ms.assetid: ed88d864-221a-4dff-a5b8-d504f0e2fa27
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

# PFN_WDFWMIINSTANCEFIREEVENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWMIINSTANCEFIREEVENT PfnWdfwmiinstancefireevent; 

// Definition

WDFAPI PfnWdfwmiinstancefireevent 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFWMIINSTANCE WmiInstance
	ULONG EventDataSize
	PVOID EventData
)
{...}

PFN_WDFWMIINSTANCEFIREEVENT 


```

## -parameters

### -param DriverGlobals: 
### -param WmiInstance: 
### -param EventDataSize: 
### -param EventData: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also