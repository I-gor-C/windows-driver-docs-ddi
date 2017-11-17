---
UID: NC.ntddk.pKdGetAcpiTablePhase0
title: pKdGetAcpiTablePhase0
author: windows-driver-content
description: 
ms.assetid: 8b8a6d82-e1cf-40e4-a218-f8e373d06fd7
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# pKdGetAcpiTablePhase0 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pKdGetAcpiTablePhase0 Pkdgetacpitablephase0; 

// Definition

PVOID Pkdgetacpitablephase0 
(
	_LOADER_PARAMETER_BLOCK *LoaderBlock
	ULONG Signature
)
{...}

pKdGetAcpiTablePhase0 


```

## -parameters

### -param *LoaderBlock: 
### -param Signature: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also