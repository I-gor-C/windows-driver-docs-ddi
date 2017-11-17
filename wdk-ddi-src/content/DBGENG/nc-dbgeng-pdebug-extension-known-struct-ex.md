---
UID: NC.dbgeng.PDEBUG_EXTENSION_KNOWN_STRUCT_EX
title: PDEBUG_EXTENSION_KNOWN_STRUCT_EX
author: windows-driver-content
description: 
ms.assetid: 216fb863-35a4-4a3c-b03d-d4f4d7184ef7
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

# PDEBUG_EXTENSION_KNOWN_STRUCT_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEBUG_EXTENSION_KNOWN_STRUCT_EX PdebugExtensionKnownStructEx; 

// Definition

HRESULT PdebugExtensionKnownStructEx 
(
	PDEBUG_CLIENT Client
	ULONG Flags
	ULONG64 Offset
	PCSTR TypeName
	PSTR Buffer
	PULONG BufferChars
)
{...}

PDEBUG_EXTENSION_KNOWN_STRUCT_EX 


```

## -parameters

### -param Client: 
### -param Flags: 
### -param Offset: 
### -param TypeName: 
### -param Buffer: 
### -param BufferChars: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also