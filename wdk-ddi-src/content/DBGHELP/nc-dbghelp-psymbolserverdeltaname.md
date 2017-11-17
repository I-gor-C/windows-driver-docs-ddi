---
UID: NC.dbghelp.PSYMBOLSERVERDELTANAME
title: PSYMBOLSERVERDELTANAME
author: windows-driver-content
description: 
ms.assetid: 023267ec-1224-4769-8d06-2a139264f438
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

# PSYMBOLSERVERDELTANAME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERDELTANAME Psymbolserverdeltaname; 

// Definition

BOOL Psymbolserverdeltaname 
(
	 PCSTR
	 PVOID
	 DWORD
	 DWORD
	 PVOID
	 DWORD
	 DWORD
	 PSTR
	 size_t
)
{...}

PSYMBOLSERVERDELTANAME 


```

## -parameters

### -param PCSTR: 
### -param PVOID: 
### -param DWORD: 
### -param DWORD: 
### -param PVOID: 
### -param DWORD: 
### -param DWORD: 
### -param PSTR: 
### -param size_t: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also