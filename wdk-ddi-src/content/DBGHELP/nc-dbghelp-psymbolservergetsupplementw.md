---
UID: NC.dbghelp.PSYMBOLSERVERGETSUPPLEMENTW
title: PSYMBOLSERVERGETSUPPLEMENTW
author: windows-driver-content
description: 
ms.assetid: f244ea02-b038-4af9-b2ce-1499afa80dd5
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

# PSYMBOLSERVERGETSUPPLEMENTW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERGETSUPPLEMENTW Psymbolservergetsupplementw; 

// Definition

BOOL Psymbolservergetsupplementw 
(
	 PCWSTR
	 PCWSTR
	 PCWSTR
	 PWSTR
	 size_t
)
{...}

PSYMBOLSERVERGETSUPPLEMENTW 


```

## -parameters

### -param PCWSTR: 
### -param PCWSTR: 
### -param PCWSTR: 
### -param PWSTR: 
### -param size_t: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also