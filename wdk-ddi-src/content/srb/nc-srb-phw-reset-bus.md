---
UID: NC.srb.PHW_RESET_BUS
title: PHW_RESET_BUS
author: windows-driver-content
description: 
ms.assetid: 63968426-a00c-492e-bb39-e559bdcd1738
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

# PHW_RESET_BUS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHW_RESET_BUS PhwResetBus; 

// Definition

BOOLEAN PhwResetBus 
(
	PVOID DeviceExtension
	ULONG PathId
)
{...}

PHW_RESET_BUS 


```

## -parameters

### -param DeviceExtension: 
### -param PathId: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also