---
UID: NC.dbghelp.PSYMBOLSERVERPROC
title: PSYMBOLSERVERPROC
author: windows-driver-content
description: 
ms.assetid: ccf08a52-3f9e-40b5-a8df-20afe1a532f3
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

# PSYMBOLSERVERPROC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERPROC Psymbolserverproc; 

// Definition

BOOL Psymbolserverproc 
(
	 PCSTR
	 PCSTR
	 PVOID
	 DWORD
	 DWORD
	 PSTR
)
{...}

PSYMBOLSERVERPROC 


```

## -parameters

### -param PCSTR: 
### -param PCSTR: 
### -param PVOID: 
### -param DWORD: 
### -param DWORD: 
### -param PSTR: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also