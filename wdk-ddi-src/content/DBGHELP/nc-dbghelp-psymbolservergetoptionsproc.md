---
UID: NC.dbghelp.PSYMBOLSERVERGETOPTIONSPROC
title: PSYMBOLSERVERGETOPTIONSPROC
author: windows-driver-content
description: 
ms.assetid: 07ec1e29-79b9-4dcf-a4e7-5e15154de557
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

# PSYMBOLSERVERGETOPTIONSPROC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERGETOPTIONSPROC Psymbolservergetoptionsproc; 

// Definition

UINT_PTR Psymbolservergetoptionsproc 
(
	 
)
{...}

PSYMBOLSERVERGETOPTIONSPROC 


```

## -parameters

### -param : 



## -returns

Returns UINT_PTR that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also