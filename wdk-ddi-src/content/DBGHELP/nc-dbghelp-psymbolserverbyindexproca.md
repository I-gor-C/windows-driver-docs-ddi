---
UID: NC.dbghelp.PSYMBOLSERVERBYINDEXPROCA
title: PSYMBOLSERVERBYINDEXPROCA
author: windows-driver-content
description: 
ms.assetid: a9173e84-54cc-4872-bf0b-0bf6472758a0
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

# PSYMBOLSERVERBYINDEXPROCA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERBYINDEXPROCA Psymbolserverbyindexproca; 

// Definition

BOOL Psymbolserverbyindexproca 
(
	 PCSTR
	 PCSTR
	 PCSTR
	 PSTR
)
{...}

PSYMBOLSERVERBYINDEXPROCA 


```

## -parameters

### -param PCSTR: 
### -param PCSTR: 
### -param PCSTR: 
### -param PSTR: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also