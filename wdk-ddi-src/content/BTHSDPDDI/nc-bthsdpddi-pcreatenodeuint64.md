---
UID: NC.bthsdpddi.PCREATENODEUINT64
title: PCREATENODEUINT64
author: windows-driver-content
description: 
ms.assetid: 2dfcf7e9-de28-4fe3-ae4d-4af373dd172e
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

# PCREATENODEUINT64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODEUINT64 Pcreatenodeuint64; 

// Definition

PSDP_NODE Pcreatenodeuint64 
(
	ULONGLONG ullVal
	ULONG tag
)
{...}

PCREATENODEUINT64 


```

## -parameters

### -param ullVal: 
### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also