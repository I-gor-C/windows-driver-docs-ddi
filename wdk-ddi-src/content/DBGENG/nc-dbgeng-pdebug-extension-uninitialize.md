---
UID: NC.dbgeng.PDEBUG_EXTENSION_UNINITIALIZE
title: PDEBUG_EXTENSION_UNINITIALIZE
author: windows-driver-content
description: 
ms.assetid: b67ce1fb-9941-4b17-bbd5-4e4d9e37d7ca
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

# PDEBUG_EXTENSION_UNINITIALIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEBUG_EXTENSION_UNINITIALIZE PdebugExtensionUninitialize; 

// Definition

void PdebugExtensionUninitialize 
(
	 void
)
{...}

PDEBUG_EXTENSION_UNINITIALIZE 


```

## -parameters

### -param void: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also