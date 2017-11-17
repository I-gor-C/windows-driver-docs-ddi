---
UID: NC.wdm.PO_FX_COMPONENT_ACTIVE_CONDITION_CALLBACK
title: PO_FX_COMPONENT_ACTIVE_CONDITION_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 69a8222d-94bc-4086-b57a-7055667fa290
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

# PO_FX_COMPONENT_ACTIVE_CONDITION_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PO_FX_COMPONENT_ACTIVE_CONDITION_CALLBACK PoFxComponentActiveConditionCallback; 

// Definition

VOID PoFxComponentActiveConditionCallback 
(
	PVOID Context
	ULONG Component
)
{...}

PO_FX_COMPONENT_ACTIVE_CONDITION_CALLBACK PPO_FX_COMPONENT_ACTIVE_CONDITION_CALLBACK


```

## -parameters

### -param Context: 
### -param Component: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also