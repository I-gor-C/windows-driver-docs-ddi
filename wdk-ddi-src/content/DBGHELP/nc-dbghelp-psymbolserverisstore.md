---
UID: NC.dbghelp.PSYMBOLSERVERISSTORE
title: PSYMBOLSERVERISSTORE
author: windows-driver-content
description: 
ms.assetid: c78545d1-7e28-4402-b444-054869884810
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

# PSYMBOLSERVERISSTORE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERISSTORE Psymbolserverisstore; 

// Definition

BOOL Psymbolserverisstore 
(
	 PCSTR
)
{...}

PSYMBOLSERVERISSTORE 


```

## -parameters

### -param PCSTR: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also