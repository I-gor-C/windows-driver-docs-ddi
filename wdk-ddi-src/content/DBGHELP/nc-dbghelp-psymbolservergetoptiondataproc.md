---
UID: NC.dbghelp.PSYMBOLSERVERGETOPTIONDATAPROC
title: PSYMBOLSERVERGETOPTIONDATAPROC
author: windows-driver-content
description: 
ms.assetid: fcaf1317-6be4-456b-b3c5-441ce40efa36
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

# PSYMBOLSERVERGETOPTIONDATAPROC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERGETOPTIONDATAPROC Psymbolservergetoptiondataproc; 

// Definition

BOOL Psymbolservergetoptiondataproc 
(
	 UINT_PTR
	 PULONG64
)
{...}

PSYMBOLSERVERGETOPTIONDATAPROC 


```

## -parameters

### -param UINT_PTR: 
### -param PULONG64: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also