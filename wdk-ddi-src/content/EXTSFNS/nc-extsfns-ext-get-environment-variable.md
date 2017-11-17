---
UID: NC.extsfns.EXT_GET_ENVIRONMENT_VARIABLE
title: EXT_GET_ENVIRONMENT_VARIABLE
author: windows-driver-content
description: 
ms.assetid: 012656ca-11e4-4053-93a3-044a31b5f118
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

# EXT_GET_ENVIRONMENT_VARIABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXT_GET_ENVIRONMENT_VARIABLE ExtGetEnvironmentVariable; 

// Definition

HRESULT ExtGetEnvironmentVariable 
(
	ULONG64 Peb
	PSTR Variable
	PSTR Buffer
	ULONG BufferSize
)
{...}

EXT_GET_ENVIRONMENT_VARIABLE 


```

## -parameters

### -param Peb: 
### -param Variable: 
### -param Buffer: 
### -param BufferSize: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also