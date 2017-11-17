---
UID: NC.dbghelp.PSYMBOLSERVERPINGPROC
title: PSYMBOLSERVERPINGPROC
author: windows-driver-content
description: 
ms.assetid: 7e4b05b7-35a8-4a1a-bebb-eb12ece036a9
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

# PSYMBOLSERVERPINGPROC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERPINGPROC Psymbolserverpingproc; 

// Definition

BOOL Psymbolserverpingproc 
(
	 PCSTR
)
{...}

PSYMBOLSERVERPINGPROC 


```

## -parameters

### -param PCSTR: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also