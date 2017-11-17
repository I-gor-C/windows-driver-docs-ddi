---
UID: NC.hidpi.PHIDP_INSERT_SCANCODES
title: PHIDP_INSERT_SCANCODES
author: windows-driver-content
description: 
ms.assetid: 9f103276-3854-41c4-a79c-f21192b35f26
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hidpi.h
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

# PHIDP_INSERT_SCANCODES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHIDP_INSERT_SCANCODES PhidpInsertScancodes; 

// Definition

BOOLEAN PhidpInsertScancodes 
(
	PVOID Context
	PCHAR NewScanCodes
	ULONG Length
)
{...}

PHIDP_INSERT_SCANCODES 


```

## -parameters

### -param Context: 
### -param NewScanCodes: 
### -param Length: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also