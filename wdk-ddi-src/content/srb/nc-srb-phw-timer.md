---
UID: NC.srb.PHW_TIMER
title: PHW_TIMER
author: windows-driver-content
description: 
ms.assetid: fad805f6-91d5-4e19-892a-14d16303dcac
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: srb.h
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

# PHW_TIMER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHW_TIMER PhwTimer; 

// Definition

VOID PhwTimer 
(
	PVOID DeviceExtension
)
{...}

PHW_TIMER 


```

## -parameters

### -param DeviceExtension: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also