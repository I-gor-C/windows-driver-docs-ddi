---
UID: NC.printoem.PFNGETINFO
title: PFNGETINFO
author: windows-driver-content
description: 
ms.assetid: d43dc138-f574-4e8c-9c2d-4be60f9f5644
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: printoem.h
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

# PFNGETINFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNGETINFO Pfngetinfo; 

// Definition

BOOL Pfngetinfo 
(
	_UNIFONTOBJ *
	 DWORD
	 PVOID
	 DWORD
	 PDWORD
)
{...}

PFNGETINFO 


```

## -parameters

### -param *: 
### -param DWORD: 
### -param PVOID: 
### -param DWORD: 
### -param PDWORD: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also