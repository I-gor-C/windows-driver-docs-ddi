---
UID: NC.bthsdpddi.PCREATENODEUINT16
title: PCREATENODEUINT16
author: windows-driver-content
description: 
ms.assetid: 18709279-faa7-4f6f-822d-2e857be8e7d6
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

# PCREATENODEUINT16 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODEUINT16 Pcreatenodeuint16; 

// Definition

PSDP_NODE Pcreatenodeuint16 
(
	USHORT usVal
	ULONG tag
)
{...}

PCREATENODEUINT16 


```

## -parameters

### -param usVal: 
### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also