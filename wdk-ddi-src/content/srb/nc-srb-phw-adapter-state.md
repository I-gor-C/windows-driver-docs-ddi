---
UID: NC.srb.PHW_ADAPTER_STATE
title: PHW_ADAPTER_STATE
author: windows-driver-content
description: 
ms.assetid: 9dedabb2-4ffc-49d8-83b4-ec4074cec593
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

# PHW_ADAPTER_STATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHW_ADAPTER_STATE PhwAdapterState; 

// Definition

BOOLEAN PhwAdapterState 
(
	PVOID DeviceExtension
	PVOID Context
	BOOLEAN SaveState
)
{...}

PHW_ADAPTER_STATE 


```

## -parameters

### -param DeviceExtension: 
### -param Context: 
### -param SaveState: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also