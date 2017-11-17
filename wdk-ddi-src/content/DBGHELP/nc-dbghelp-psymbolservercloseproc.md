---
UID: NC.dbghelp.PSYMBOLSERVERCLOSEPROC
title: PSYMBOLSERVERCLOSEPROC
author: windows-driver-content
description: 
ms.assetid: a1d64c9c-09df-46b8-9478-057a6f6db332
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

# PSYMBOLSERVERCLOSEPROC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERCLOSEPROC Psymbolservercloseproc; 

// Definition

BOOL Psymbolservercloseproc 
(
	 VOID
)
{...}

PSYMBOLSERVERCLOSEPROC 


```

## -parameters

### -param VOID: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also