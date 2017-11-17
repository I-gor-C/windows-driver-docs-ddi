---
UID: NC.bthsdpddi.PCREATENODEUINT128
title: PCREATENODEUINT128
author: windows-driver-content
description: 
ms.assetid: 79c0b24d-0635-4808-a36f-e6bfeb9acd38
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

# PCREATENODEUINT128 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODEUINT128 Pcreatenodeuint128; 

// Definition

PSDP_NODE Pcreatenodeuint128 
(
	PSDP_ULARGE_INTEGER_16 puli16Val
	ULONG tag
)
{...}

PCREATENODEUINT128 


```

## -parameters

### -param puli16Val: 
### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also