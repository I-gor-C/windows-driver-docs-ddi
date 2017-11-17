---
UID: NC.wudfwdm.PO_FX_COMPONENT_CRITICAL_TRANSITION_CALLBACK
title: PO_FX_COMPONENT_CRITICAL_TRANSITION_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 331538a0-89a7-48f4-ac34-2ede3ff6b516
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wudfwdm.h
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

# PO_FX_COMPONENT_CRITICAL_TRANSITION_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PO_FX_COMPONENT_CRITICAL_TRANSITION_CALLBACK PoFxComponentCriticalTransitionCallback; 

// Definition

VOID PoFxComponentCriticalTransitionCallback 
(
	PVOID Context
	ULONG Component
	BOOLEAN Active
)
{...}

PO_FX_COMPONENT_CRITICAL_TRANSITION_CALLBACK PPO_FX_COMPONENT_CRITICAL_TRANSITION_CALLBACK


```

## -parameters

### -param Context: 
### -param Component: 
### -param Active: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also