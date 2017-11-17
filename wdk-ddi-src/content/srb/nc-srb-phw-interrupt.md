---
UID: NC.srb.PHW_INTERRUPT
title: PHW_INTERRUPT
author: windows-driver-content
description: 
ms.assetid: 0d7e6e6f-d15a-4563-8e37-9219f2f36fe3
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

# PHW_INTERRUPT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHW_INTERRUPT PhwInterrupt; 

// Definition

BOOLEAN PhwInterrupt 
(
	PVOID DeviceExtension
)
{...}

PHW_INTERRUPT 


```

## -parameters

### -param DeviceExtension: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also