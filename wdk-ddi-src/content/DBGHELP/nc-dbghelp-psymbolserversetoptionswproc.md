---
UID: NC.dbghelp.PSYMBOLSERVERSETOPTIONSWPROC
title: PSYMBOLSERVERSETOPTIONSWPROC
author: windows-driver-content
description: 
ms.assetid: 8240b389-1cee-464b-85ca-ac945986572d
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

# PSYMBOLSERVERSETOPTIONSWPROC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERSETOPTIONSWPROC Psymbolserversetoptionswproc; 

// Definition

BOOL Psymbolserversetoptionswproc 
(
	 UINT_PTR
	 ULONG64
)
{...}

PSYMBOLSERVERSETOPTIONSWPROC 


```

## -parameters

### -param UINT_PTR: 
### -param ULONG64: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also