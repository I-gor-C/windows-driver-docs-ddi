---
UID: NC.dbghelp.SYMADDSOURCESTREAM~r1
title: SYMADDSOURCESTREAM
author: windows-driver-content
description: 
ms.assetid: 8b90f4b7-8f16-4868-badb-ddf2145d1750
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

# SYMADDSOURCESTREAM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SYMADDSOURCESTREAM Symaddsourcestream; 

// Definition

BOOL Symaddsourcestream 
(
	 HANDLE
	 ULONG64
	 PCSTR
	 PBYTE
	 size_t
)
{...}

SYMADDSOURCESTREAM 


```

## -parameters

### -param HANDLE: 
### -param ULONG64: 
### -param PCSTR: 
### -param PBYTE: 
### -param size_t: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also