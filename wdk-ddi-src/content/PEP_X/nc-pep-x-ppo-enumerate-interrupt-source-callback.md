---
UID: NC.pep_x.PPO_ENUMERATE_INTERRUPT_SOURCE_CALLBACK
title: PPO_ENUMERATE_INTERRUPT_SOURCE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 4a317a71-6a41-42b3-87ee-55c85a6bf475
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: pep_x.h
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

# PPO_ENUMERATE_INTERRUPT_SOURCE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PPO_ENUMERATE_INTERRUPT_SOURCE_CALLBACK PpoEnumerateInterruptSourceCallback; 

// Definition

BOOLEAN PpoEnumerateInterruptSourceCallback 
(
	PVOID CallbackContext
	PPEP_UNMASKED_INTERRUPT_INFORMATION InterruptInformation
)
{...}

PPO_ENUMERATE_INTERRUPT_SOURCE_CALLBACK 


```

## -parameters

### -param CallbackContext: 
### -param InterruptInformation: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also