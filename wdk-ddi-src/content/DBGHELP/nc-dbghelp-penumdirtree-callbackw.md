---
UID: NC.dbghelp.PENUMDIRTREE_CALLBACKW
title: PENUMDIRTREE_CALLBACKW
author: windows-driver-content
description: 
ms.assetid: 515e090e-95fa-4ea4-99d3-ec08e6d0625d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dbghelp.h
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

# PENUMDIRTREE_CALLBACKW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PENUMDIRTREE_CALLBACKW PenumdirtreeCallbackw; 

// Definition

BOOL PenumdirtreeCallbackw 
(
	PCWSTR FilePath
	PVOID CallerData
)
{...}

PENUMDIRTREE_CALLBACKW 


```

## -parameters

### -param FilePath: 
### -param CallerData: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also