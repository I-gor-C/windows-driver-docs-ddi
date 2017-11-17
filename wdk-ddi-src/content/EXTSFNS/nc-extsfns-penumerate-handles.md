---
UID: NC.extsfns.PENUMERATE_HANDLES
title: PENUMERATE_HANDLES
author: windows-driver-content
description: 
ms.assetid: a8793ce0-888a-4aa1-8ea4-c4acee948362
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# PENUMERATE_HANDLES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PENUMERATE_HANDLES PenumerateHandles; 

// Definition

HRESULT PenumerateHandles 
(
	PDEBUG_CLIENT Client
	ULONG64 Process
	ULONG64 HandleToDump
	ULONG Flags
	KDEXT_DUMP_HANDLE_CALLBACK Callback
	PVOID Context
)
{...}

PENUMERATE_HANDLES 


```

## -parameters

### -param Client: 
### -param Process: 
### -param HandleToDump: 
### -param Flags: 
### -param Callback: 
### -param Context: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also