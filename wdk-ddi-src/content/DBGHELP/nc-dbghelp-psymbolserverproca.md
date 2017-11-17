---
UID: NC.dbghelp.PSYMBOLSERVERPROCA
title: PSYMBOLSERVERPROCA
author: windows-driver-content
description: 
ms.assetid: 6e3ccf62-862b-4145-87d3-a734c70335e4
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

# PSYMBOLSERVERPROCA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERPROCA Psymbolserverproca; 

// Definition

BOOL Psymbolserverproca 
(
	 PCSTR
	 PCSTR
	 PVOID
	 DWORD
	 DWORD
	 PSTR
)
{...}

PSYMBOLSERVERPROCA 


```

## -parameters

### -param PCSTR: 
### -param PCSTR: 
### -param PVOID: 
### -param DWORD: 
### -param DWORD: 
### -param PSTR: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also