---
UID: NC.dbgeng.PDEBUG_STACK_PROVIDER_RECONSTRUCTSTACK
title: PDEBUG_STACK_PROVIDER_RECONSTRUCTSTACK
author: windows-driver-content
description: 
ms.assetid: eb74eda6-4b79-435b-a549-a29eed8fdfac
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

# PDEBUG_STACK_PROVIDER_RECONSTRUCTSTACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEBUG_STACK_PROVIDER_RECONSTRUCTSTACK PdebugStackProviderReconstructstack; 

// Definition

HRESULT PdebugStackProviderReconstructstack 
(
	ULONG SystemThreadId
	PDEBUG_STACK_FRAME_EX NativeFrames
	ULONG CountNativeFrames
	PSTACK_SYM_FRAME_INFO *StackSymFrames
	PULONG StackSymFramesFilled
)
{...}

PDEBUG_STACK_PROVIDER_RECONSTRUCTSTACK 


```

## -parameters

### -param SystemThreadId: 
### -param NativeFrames: 
### -param CountNativeFrames: 
### -param *StackSymFrames: 
### -param StackSymFramesFilled: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also