---
UID: NC.dbghelp.PSYMBOLSERVERPINGPROCW
title: PSYMBOLSERVERPINGPROCW
author: windows-driver-content
description: 
ms.assetid: 712530ba-b45d-49e1-9b83-dd170d0470be
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

# PSYMBOLSERVERPINGPROCW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERPINGPROCW Psymbolserverpingprocw; 

// Definition

BOOL Psymbolserverpingprocw 
(
	 PCWSTR
)
{...}

PSYMBOLSERVERPINGPROCW 


```

## -parameters

### -param PCWSTR: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also