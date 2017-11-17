---
UID: NC.dbgeng.PDEBUG_EXTENSION_CANUNLOAD
title: PDEBUG_EXTENSION_CANUNLOAD
author: windows-driver-content
description: 
ms.assetid: a8d24c38-529d-4688-b820-579f5ad080d8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dbgeng.h
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

# PDEBUG_EXTENSION_CANUNLOAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEBUG_EXTENSION_CANUNLOAD PdebugExtensionCanunload; 

// Definition

HRESULT PdebugExtensionCanunload 
(
	 void
)
{...}

PDEBUG_EXTENSION_CANUNLOAD 


```

## -parameters

### -param void: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also