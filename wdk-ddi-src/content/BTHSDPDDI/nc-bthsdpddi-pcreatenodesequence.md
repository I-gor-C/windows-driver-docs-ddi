---
UID: NC.bthsdpddi.PCREATENODESEQUENCE
title: PCREATENODESEQUENCE
author: windows-driver-content
description: 
ms.assetid: d2ab82ec-f9c2-48f0-9908-9e7f5c80062b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: bthsdpddi.h
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

# PCREATENODESEQUENCE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODESEQUENCE Pcreatenodesequence; 

// Definition

PSDP_NODE Pcreatenodesequence 
(
	ULONG tag
)
{...}

PCREATENODESEQUENCE 


```

## -parameters

### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also