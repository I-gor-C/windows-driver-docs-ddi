---
UID: NC.dbghelp.PENUMDIRTREE_CALLBACK
title: PENUMDIRTREE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 0562f160-b3b8-415c-ab1b-95d47aaf60a2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dbghelp.h
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

# PENUMDIRTREE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PENUMDIRTREE_CALLBACK PenumdirtreeCallback; 

// Definition

BOOL PenumdirtreeCallback 
(
	PCSTR FilePath
	PVOID CallerData
)
{...}

PENUMDIRTREE_CALLBACK 


```

## -parameters

### -param FilePath: 
### -param CallerData: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also