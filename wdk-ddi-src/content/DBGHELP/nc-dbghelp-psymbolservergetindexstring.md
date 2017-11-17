---
UID: NC.dbghelp.PSYMBOLSERVERGETINDEXSTRING
title: PSYMBOLSERVERGETINDEXSTRING
author: windows-driver-content
description: 
ms.assetid: f1891007-5bba-40f1-b98c-fa0ad12d35b0
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

# PSYMBOLSERVERGETINDEXSTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERGETINDEXSTRING Psymbolservergetindexstring; 

// Definition

BOOL Psymbolservergetindexstring 
(
	 PVOID
	 DWORD
	 DWORD
	 PSTR
	 size_t
)
{...}

PSYMBOLSERVERGETINDEXSTRING 


```

## -parameters

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