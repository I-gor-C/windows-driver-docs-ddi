---
UID: NC.extsfns.EXTDLL_QUERYDATABYTAG
title: EXTDLL_QUERYDATABYTAG
author: windows-driver-content
description: 
ms.assetid: a8bcbf50-834e-49f9-acc4-b75f8075a6b1
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

# EXTDLL_QUERYDATABYTAG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXTDLL_QUERYDATABYTAG ExtdllQuerydatabytag; 

// Definition

HRESULT ExtdllQuerydatabytag 
(
	PDEBUG_CLIENT4 Client
	ULONG dwDataTag
	PVOID pQueryInfo
	PBYTE pData
	ULONG cbData
)
{...}

EXTDLL_QUERYDATABYTAG 


```

## -parameters

### -param Client: 
### -param dwDataTag: 
### -param pQueryInfo: 
### -param pData: 
### -param cbData: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also