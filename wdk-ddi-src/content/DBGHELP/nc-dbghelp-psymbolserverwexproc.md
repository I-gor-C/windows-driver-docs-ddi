---
UID: NC.dbghelp.PSYMBOLSERVERWEXPROC
title: PSYMBOLSERVERWEXPROC
author: windows-driver-content
description: 
ms.assetid: f45dc8fd-cd45-4db2-9b26-08d03b6e18d0
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

# PSYMBOLSERVERWEXPROC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERWEXPROC Psymbolserverwexproc; 

// Definition

BOOL Psymbolserverwexproc 
(
	 PCWSTR
	 PCWSTR
	 PVOID
	 DWORD
	 DWORD
	 PWSTR
	 PSYMSRV_EXTENDED_OUTPUT_DATA
)
{...}

PSYMBOLSERVERWEXPROC 


```

## -parameters

### -param PCWSTR: 
### -param PCWSTR: 
### -param PVOID: 
### -param DWORD: 
### -param DWORD: 
### -param PWSTR: 
### -param PSYMSRV_EXTENDED_OUTPUT_DATA: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also