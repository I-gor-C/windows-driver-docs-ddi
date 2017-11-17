---
UID: NC.wdfchildlist.PFN_WDFCHILDLISTGETDEVICE
title: PFN_WDFCHILDLISTGETDEVICE
author: windows-driver-content
description: 
ms.assetid: f2ddd181-7c80-47d0-9884-e16d4afd6fee
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfchildlist.h
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

# PFN_WDFCHILDLISTGETDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCHILDLISTGETDEVICE PfnWdfchildlistgetdevice; 

// Definition

WDFAPI PfnWdfchildlistgetdevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCHILDLIST ChildList
)
{...}

PFN_WDFCHILDLISTGETDEVICE 


```

## -parameters

### -param DriverGlobals: 
### -param ChildList: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also