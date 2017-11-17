---
UID: NC.bthsdpddi.PCREATENODESTRING
title: PCREATENODESTRING
author: windows-driver-content
description: 
ms.assetid: 95fcbdb8-be12-462b-9bdf-3439828afdfe
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

# PCREATENODESTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODESTRING Pcreatenodestring; 

// Definition

PSDP_NODE Pcreatenodestring 
(
	PCHAR string
	ULONG stringLength
	ULONG tag
)
{...}

PCREATENODESTRING 


```

## -parameters

### -param string: 
### -param stringLength: 
### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also