---
UID: NC.ntddk.pKdUnmapVirtualAddress
title: pKdUnmapVirtualAddress
author: windows-driver-content
description: 
ms.assetid: 886a6a2d-bc44-4982-9b24-c507128fcce0
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

# pKdUnmapVirtualAddress callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pKdUnmapVirtualAddress Pkdunmapvirtualaddress; 

// Definition

VOID Pkdunmapvirtualaddress 
(
	PVOID VirtualAddress
	ULONG NumberPages
	BOOLEAN FlushCurrentTLB
)
{...}

pKdUnmapVirtualAddress 


```

## -parameters

### -param VirtualAddress: 
### -param NumberPages: 
### -param FlushCurrentTLB: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also