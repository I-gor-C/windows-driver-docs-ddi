---
UID: NC.icm.PBMCALLBACKFN
title: PBMCALLBACKFN
author: windows-driver-content
description: 
ms.assetid: bb2bb7e3-0fcb-49c7-945e-e47206485f3c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: icm.h
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

# PBMCALLBACKFN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PBMCALLBACKFN Pbmcallbackfn; 

// Definition

BOOL Pbmcallbackfn 
(
	 ULONG
	 ULONG
	 LPARAM
)
{...}

PBMCALLBACKFN 


```

## -parameters

### -param ULONG: 
### -param ULONG: 
### -param LPARAM: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also