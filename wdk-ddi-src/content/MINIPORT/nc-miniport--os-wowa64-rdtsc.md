---
UID: NC.miniport._os_wowa64_rdtsc
title: _os_wowa64_rdtsc
author: windows-driver-content
description: 
ms.assetid: 590d3a7d-6212-458e-b482-abc2403a0780
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: miniport.h
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

# _os_wowa64_rdtsc callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

_os_wowa64_rdtsc OsWowa64Rdtsc; 

// Definition

ULONG64 OsWowa64Rdtsc 
(
)
{...}

_os_wowa64_rdtsc 


```

## -parameters




## -returns

Returns ULONG64 that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also