---
UID: NC.dbghelp.PSYMBOLSERVERSETOPTIONSPROC
title: PSYMBOLSERVERSETOPTIONSPROC
author: windows-driver-content
description: 
ms.assetid: 144fe47a-d8d2-47a1-a846-ead3af333abd
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

# PSYMBOLSERVERSETOPTIONSPROC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERSETOPTIONSPROC Psymbolserversetoptionsproc; 

// Definition

BOOL Psymbolserversetoptionsproc 
(
	 UINT_PTR
	 ULONG64
)
{...}

PSYMBOLSERVERSETOPTIONSPROC 


```

## -parameters

### -param UINT_PTR: 
### -param ULONG64: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also