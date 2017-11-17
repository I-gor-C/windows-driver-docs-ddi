---
UID: NC.dbghelp.PSYMBOLSERVERGETINDEXSTRINGW
title: PSYMBOLSERVERGETINDEXSTRINGW
author: windows-driver-content
description: 
ms.assetid: 3b815ebc-dec8-42e0-8746-cc8f60899c08
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

# PSYMBOLSERVERGETINDEXSTRINGW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERGETINDEXSTRINGW Psymbolservergetindexstringw; 

// Definition

BOOL Psymbolservergetindexstringw 
(
	 PVOID
	 DWORD
	 DWORD
	 PWSTR
	 size_t
)
{...}

PSYMBOLSERVERGETINDEXSTRINGW 


```

## -parameters

### -param PVOID: 
### -param DWORD: 
### -param DWORD: 
### -param PWSTR: 
### -param size_t: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also