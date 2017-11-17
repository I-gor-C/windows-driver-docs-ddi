---
UID: NC.extsfns.EXT_RELOAD_TRIAGER
title: EXT_RELOAD_TRIAGER
author: windows-driver-content
description: 
ms.assetid: 0afab77d-3de3-4e9e-8f43-8e33302ae6f8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# EXT_RELOAD_TRIAGER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXT_RELOAD_TRIAGER ExtReloadTriager; 

// Definition

HRESULT ExtReloadTriager 
(
	PDEBUG_CLIENT4 Client
)
{...}

EXT_RELOAD_TRIAGER 


```

## -parameters

### -param Client: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also