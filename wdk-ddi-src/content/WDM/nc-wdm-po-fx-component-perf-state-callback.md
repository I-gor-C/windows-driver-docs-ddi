---
UID: NC.wdm.PO_FX_COMPONENT_PERF_STATE_CALLBACK
title: PO_FX_COMPONENT_PERF_STATE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: dc9f9662-ac7d-4e88-9bef-f5ab6296e61a
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

# PO_FX_COMPONENT_PERF_STATE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PO_FX_COMPONENT_PERF_STATE_CALLBACK PoFxComponentPerfStateCallback; 

// Definition

VOID PoFxComponentPerfStateCallback 
(
	PVOID Context
	ULONG Component
	BOOLEAN Succeeded
	PVOID RequestContext
)
{...}

PO_FX_COMPONENT_PERF_STATE_CALLBACK PPO_FX_COMPONENT_PERF_STATE_CALLBACK


```

## -parameters

### -param Context: 
### -param Component: 
### -param Succeeded: 
### -param RequestContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also