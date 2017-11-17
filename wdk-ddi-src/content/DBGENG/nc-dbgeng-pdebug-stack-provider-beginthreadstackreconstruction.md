---
UID: NC.dbgeng.PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION
title: PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION
author: windows-driver-content
description: 
ms.assetid: 786d8845-57c8-44e1-bdb5-b05e906e803a
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

# PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION PdebugStackProviderBeginthreadstackreconstruction; 

// Definition

HRESULT PdebugStackProviderBeginthreadstackreconstruction 
(
	ULONG StreamType
	PVOID MiniDumpStreamBuffer
	ULONG BufferSize
)
{...}

PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION 


```

## -parameters

### -param StreamType: 
### -param MiniDumpStreamBuffer: 
### -param BufferSize: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also