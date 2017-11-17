---
UID: NC.bthsdpddi.PCREATENODEUINT8
title: PCREATENODEUINT8
author: windows-driver-content
description: 
ms.assetid: 64ef337d-8e18-428d-8c1f-866d677bcff4
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

# PCREATENODEUINT8 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODEUINT8 Pcreatenodeuint8; 

// Definition

PSDP_NODE Pcreatenodeuint8 
(
	UCHAR ucVal
	ULONG tag
)
{...}

PCREATENODEUINT8 


```

## -parameters

### -param ucVal: 
### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also