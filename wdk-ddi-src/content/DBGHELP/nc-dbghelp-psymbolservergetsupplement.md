---
UID: NC.dbghelp.PSYMBOLSERVERGETSUPPLEMENT
title: PSYMBOLSERVERGETSUPPLEMENT
author: windows-driver-content
description: 
ms.assetid: 0ffab6aa-fea0-4bb3-989a-27ec7064eb45
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

# PSYMBOLSERVERGETSUPPLEMENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERGETSUPPLEMENT Psymbolservergetsupplement; 

// Definition

BOOL Psymbolservergetsupplement 
(
	 PCSTR
	 PCSTR
	 PCSTR
	 PSTR
	 size_t
)
{...}

PSYMBOLSERVERGETSUPPLEMENT 


```

## -parameters

### -param PCSTR: 
### -param PCSTR: 
### -param PCSTR: 
### -param PSTR: 
### -param size_t: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also