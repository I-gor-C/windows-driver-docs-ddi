---
UID: NC.strmini.PHW_RESET_ADAPTER
title: PHW_RESET_ADAPTER
author: windows-driver-content
description: 
ms.assetid: 91042c22-275b-405d-89a6-62d4fae54cfd
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: strmini.h
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

# PHW_RESET_ADAPTER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHW_RESET_ADAPTER PhwResetAdapter; 

// Definition

BOOLEAN PhwResetAdapter 
(
	IN PVOID DeviceExtension
)
{...}

PHW_RESET_ADAPTER 


```

## -parameters

### -param DeviceExtension: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also