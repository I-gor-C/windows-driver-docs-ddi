---
UID: NC.ks.PFNKSCANCELPINNEDMDL
title: PFNKSCANCELPINNEDMDL
author: windows-driver-content
description: 
ms.assetid: bc8447cd-8781-4dd9-a2a8-47a66e9ee3a0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSCANCELPINNEDMDL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSCANCELPINNEDMDL Pfnkscancelpinnedmdl; 

// Definition

VOID Pfnkscancelpinnedmdl 
(
	 GUID
	 PVOID
	 PVOID
)
{...}

PFNKSCANCELPINNEDMDL 


```

## -parameters

### -param GUID: 
### -param PVOID: 
### -param PVOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also