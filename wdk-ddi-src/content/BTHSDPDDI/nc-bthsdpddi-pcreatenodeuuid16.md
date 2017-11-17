---
UID: NC.bthsdpddi.PCREATENODEUUID16
title: PCREATENODEUUID16
author: windows-driver-content
description: 
ms.assetid: efe040a2-c328-4e89-bb9a-cf3996d95028
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

# PCREATENODEUUID16 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODEUUID16 Pcreatenodeuuid16; 

// Definition

PSDP_NODE Pcreatenodeuuid16 
(
	USHORT usVal
	ULONG tag
)
{...}

PCREATENODEUUID16 


```

## -parameters

### -param usVal: 
### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also