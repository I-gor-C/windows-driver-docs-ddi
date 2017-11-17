---
UID: NC.bthsdpddi.PCREATENODEURL
title: PCREATENODEURL
author: windows-driver-content
description: 
ms.assetid: a347fdde-35ae-4ef2-853b-2d3993a44a66
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

# PCREATENODEURL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODEURL Pcreatenodeurl; 

// Definition

PSDP_NODE Pcreatenodeurl 
(
	PCHAR url
	ULONG urlLength
	ULONG tag
)
{...}

PCREATENODEURL 


```

## -parameters

### -param url: 
### -param urlLength: 
### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also