---
UID: NC.dbghelp.PSYMBOLSERVERPROCW
title: PSYMBOLSERVERPROCW
author: windows-driver-content
description: 
ms.assetid: 8958aed5-7e76-41fd-a9ad-4f31c974f2b7
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

# PSYMBOLSERVERPROCW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERPROCW Psymbolserverprocw; 

// Definition

BOOL Psymbolserverprocw 
(
	 PCWSTR
	 PCWSTR
	 PVOID
	 DWORD
	 DWORD
	 PWSTR
)
{...}

PSYMBOLSERVERPROCW 


```

## -parameters

### -param PCWSTR: 
### -param PCWSTR: 
### -param PVOID: 
### -param DWORD: 
### -param DWORD: 
### -param PWSTR: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also