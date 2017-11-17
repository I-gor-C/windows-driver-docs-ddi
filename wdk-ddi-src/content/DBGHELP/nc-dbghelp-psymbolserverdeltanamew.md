---
UID: NC.dbghelp.PSYMBOLSERVERDELTANAMEW
title: PSYMBOLSERVERDELTANAMEW
author: windows-driver-content
description: 
ms.assetid: 3567b25d-9112-4ea7-92df-b9908b20a135
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

# PSYMBOLSERVERDELTANAMEW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERDELTANAMEW Psymbolserverdeltanamew; 

// Definition

BOOL Psymbolserverdeltanamew 
(
	 PCWSTR
	 PVOID
	 DWORD
	 DWORD
	 PVOID
	 DWORD
	 DWORD
	 PWSTR
	 size_t
)
{...}

PSYMBOLSERVERDELTANAMEW 


```

## -parameters

### -param PCWSTR: 
### -param PVOID: 
### -param DWORD: 
### -param DWORD: 
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