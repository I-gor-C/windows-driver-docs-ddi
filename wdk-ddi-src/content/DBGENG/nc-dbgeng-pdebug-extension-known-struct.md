---
UID: NC.dbgeng.PDEBUG_EXTENSION_KNOWN_STRUCT
title: PDEBUG_EXTENSION_KNOWN_STRUCT
author: windows-driver-content
description: 
ms.assetid: ef86f44d-de8a-452b-886c-51db219370ce
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

# PDEBUG_EXTENSION_KNOWN_STRUCT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEBUG_EXTENSION_KNOWN_STRUCT PdebugExtensionKnownStruct; 

// Definition

HRESULT PdebugExtensionKnownStruct 
(
	ULONG Flags
	ULONG64 Offset
	PSTR TypeName
	PSTR Buffer
	PULONG BufferChars
)
{...}

PDEBUG_EXTENSION_KNOWN_STRUCT 


```

## -parameters

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