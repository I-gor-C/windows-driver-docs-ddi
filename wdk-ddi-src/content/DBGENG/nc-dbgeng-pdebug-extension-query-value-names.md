---
UID: NC.dbgeng.PDEBUG_EXTENSION_QUERY_VALUE_NAMES
title: PDEBUG_EXTENSION_QUERY_VALUE_NAMES
author: windows-driver-content
description: 
ms.assetid: 6eaa7bde-9bfd-45ba-ad2a-622757b30b58
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

# PDEBUG_EXTENSION_QUERY_VALUE_NAMES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEBUG_EXTENSION_QUERY_VALUE_NAMES PdebugExtensionQueryValueNames; 

// Definition

HRESULT PdebugExtensionQueryValueNames 
(
	PDEBUG_CLIENT Client
	ULONG Flags
	PWSTR Buffer
	ULONG BufferChars
	PULONG BufferNeeded
)
{...}

PDEBUG_EXTENSION_QUERY_VALUE_NAMES 


```

## -parameters

### -param Client: 
### -param Flags: 
### -param Buffer: 
### -param BufferChars: 
### -param BufferNeeded: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also