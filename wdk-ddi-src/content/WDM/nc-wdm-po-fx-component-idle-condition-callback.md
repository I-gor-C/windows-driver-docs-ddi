---
UID: NC.wdm.PO_FX_COMPONENT_IDLE_CONDITION_CALLBACK
title: PO_FX_COMPONENT_IDLE_CONDITION_CALLBACK
author: windows-driver-content
description: 
ms.assetid: a800e5fb-67c6-4034-8493-7fb317b09c19
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PO_FX_COMPONENT_IDLE_CONDITION_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PO_FX_COMPONENT_IDLE_CONDITION_CALLBACK PoFxComponentIdleConditionCallback; 

// Definition

VOID PoFxComponentIdleConditionCallback 
(
	PVOID Context
	ULONG Component
)
{...}

PO_FX_COMPONENT_IDLE_CONDITION_CALLBACK PPO_FX_COMPONENT_IDLE_CONDITION_CALLBACK


```

## -parameters

### -param Context: 
### -param Component: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also