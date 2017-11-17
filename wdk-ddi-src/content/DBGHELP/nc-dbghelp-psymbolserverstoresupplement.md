---
UID: NC.dbghelp.PSYMBOLSERVERSTORESUPPLEMENT
title: PSYMBOLSERVERSTORESUPPLEMENT
author: windows-driver-content
description: 
ms.assetid: 4f27d696-8867-4791-a25c-caed1dd31c63
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

# PSYMBOLSERVERSTORESUPPLEMENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERSTORESUPPLEMENT Psymbolserverstoresupplement; 

// Definition

BOOL Psymbolserverstoresupplement 
(
	 PCSTR
	 PCSTR
	 PCSTR
	 PSTR
	 size_t
	 DWORD
)
{...}

PSYMBOLSERVERSTORESUPPLEMENT 


```

## -parameters

### -param PCSTR: 
### -param PCSTR: 
### -param PCSTR: 
### -param PSTR: 
### -param size_t: 
### -param DWORD: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also