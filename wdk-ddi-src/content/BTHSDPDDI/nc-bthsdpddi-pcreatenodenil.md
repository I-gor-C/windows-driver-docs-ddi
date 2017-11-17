---
UID: NC.bthsdpddi.PCREATENODENIL
title: PCREATENODENIL
author: windows-driver-content
description: 
ms.assetid: aceb3388-48a4-4317-ad28-137c02931494
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

# PCREATENODENIL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODENIL Pcreatenodenil; 

// Definition

PSDP_NODE Pcreatenodenil 
(
	ULONG tag
)
{...}

PCREATENODENIL 


```

## -parameters

### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also