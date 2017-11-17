---
UID: NC.classpnp.PCLASS_TICK
title: PCLASS_TICK
author: windows-driver-content
description: 
ms.assetid: 7ea3b7a6-a3b2-4035-833e-787a0b55d473
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: classpnp.h
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

# PCLASS_TICK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_TICK PclassTick; 

// Definition

VOID PclassTick 
(
	PDEVICE_OBJECT DeviceObject
)
{...}

PCLASS_TICK 


```

## -parameters

### -param DeviceObject: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also