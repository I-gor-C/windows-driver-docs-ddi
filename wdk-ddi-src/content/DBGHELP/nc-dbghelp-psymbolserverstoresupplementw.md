---
UID: NC.dbghelp.PSYMBOLSERVERSTORESUPPLEMENTW
title: PSYMBOLSERVERSTORESUPPLEMENTW
author: windows-driver-content
description: 
ms.assetid: 6ede5b83-38cf-43a1-b129-32716ea80ee8
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

# PSYMBOLSERVERSTORESUPPLEMENTW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERSTORESUPPLEMENTW Psymbolserverstoresupplementw; 

// Definition

BOOL Psymbolserverstoresupplementw 
(
	 PCWSTR
	 PCWSTR
	 PCWSTR
	 PWSTR
	 size_t
	 DWORD
)
{...}

PSYMBOLSERVERSTORESUPPLEMENTW 


```

## -parameters

### -param PCWSTR: 
### -param PCWSTR: 
### -param PCWSTR: 
### -param PWSTR: 
### -param size_t: 
### -param DWORD: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also