---
UID: NC.dbgeng.PDEBUG_STACK_PROVIDER_FREESTACKSYMFRAMES
title: PDEBUG_STACK_PROVIDER_FREESTACKSYMFRAMES
author: windows-driver-content
description: 
ms.assetid: d528d86c-7454-4d47-a728-4882a94787c1
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dbgeng.h
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

# PDEBUG_STACK_PROVIDER_FREESTACKSYMFRAMES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEBUG_STACK_PROVIDER_FREESTACKSYMFRAMES PdebugStackProviderFreestacksymframes; 

// Definition

HRESULT PdebugStackProviderFreestacksymframes 
(
	PSTACK_SYM_FRAME_INFO StackSymFrames
)
{...}

PDEBUG_STACK_PROVIDER_FREESTACKSYMFRAMES 


```

## -parameters

### -param StackSymFrames: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also