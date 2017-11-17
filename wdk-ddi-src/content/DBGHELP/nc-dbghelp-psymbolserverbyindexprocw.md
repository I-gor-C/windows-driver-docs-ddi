---
UID: NC.dbghelp.PSYMBOLSERVERBYINDEXPROCW
title: PSYMBOLSERVERBYINDEXPROCW
author: windows-driver-content
description: 
ms.assetid: 90a0d026-944e-4092-a3af-fb99f0de2be7
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

# PSYMBOLSERVERBYINDEXPROCW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERBYINDEXPROCW Psymbolserverbyindexprocw; 

// Definition

BOOL Psymbolserverbyindexprocw 
(
	 PCWSTR
	 PCWSTR
	 PCWSTR
	 PWSTR
)
{...}

PSYMBOLSERVERBYINDEXPROCW 


```

## -parameters

### -param PCWSTR: 
### -param PCWSTR: 
### -param PCWSTR: 
### -param PWSTR: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also