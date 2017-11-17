---
UID: NC.ntddk.EXPAND_STACK_CALLOUT
title: EXPAND_STACK_CALLOUT
author: windows-driver-content
description: 
ms.assetid: 8fad00b6-72d2-4b68-878a-d849cfb6adef
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# EXPAND_STACK_CALLOUT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXPAND_STACK_CALLOUT ExpandStackCallout; 

// Definition

VOID() ExpandStackCallout 
(
	PVOID Parameter
)
{...}

EXPAND_STACK_CALLOUT PEXPAND_STACK_CALLOUT


```

## -parameters

### -param Parameter: 



## -returns

Returns VOID() that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also