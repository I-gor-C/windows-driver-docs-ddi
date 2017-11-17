---
UID: NC.dbghelp.PSYMBOLSERVERSTOREFILE
title: PSYMBOLSERVERSTOREFILE
author: windows-driver-content
description: 
ms.assetid: e5c785c1-5f00-460b-aa5b-63a6194ba5cc
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

# PSYMBOLSERVERSTOREFILE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERSTOREFILE Psymbolserverstorefile; 

// Definition

BOOL Psymbolserverstorefile 
(
	 PCSTR
	 PCSTR
	 PVOID
	 DWORD
	 DWORD
	 PSTR
	 size_t
	 DWORD
)
{...}

PSYMBOLSERVERSTOREFILE 


```

## -parameters

### -param PCSTR: 
### -param PCSTR: 
### -param PVOID: 
### -param DWORD: 
### -param DWORD: 
### -param PSTR: 
### -param size_t: 
### -param DWORD: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also