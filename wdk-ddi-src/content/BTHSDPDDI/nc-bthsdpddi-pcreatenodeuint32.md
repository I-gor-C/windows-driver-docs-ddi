---
UID: NC.bthsdpddi.PCREATENODEUINT32
title: PCREATENODEUINT32
author: windows-driver-content
description: 
ms.assetid: 0ac72a69-4a63-4d5c-a264-e4e83b493ce6
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

# PCREATENODEUINT32 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODEUINT32 Pcreatenodeuint32; 

// Definition

PSDP_NODE Pcreatenodeuint32 
(
	ULONG ulVal
	ULONG tag
)
{...}

PCREATENODEUINT32 


```

## -parameters

### -param ulVal: 
### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also