---
UID: NC.dbgeng.PDEBUG_EXTENSION_INITIALIZE
title: PDEBUG_EXTENSION_INITIALIZE
author: windows-driver-content
description: 
ms.assetid: 38616f27-681a-481d-8781-75fe9d45e788
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

# PDEBUG_EXTENSION_INITIALIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEBUG_EXTENSION_INITIALIZE PdebugExtensionInitialize; 

// Definition

HRESULT PdebugExtensionInitialize 
(
	PULONG Version
	PULONG Flags
)
{...}

PDEBUG_EXTENSION_INITIALIZE 


```

## -parameters

### -param Version: 
### -param Flags: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also