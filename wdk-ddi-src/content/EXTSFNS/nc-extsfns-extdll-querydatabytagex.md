---
UID: NC.extsfns.EXTDLL_QUERYDATABYTAGEX
title: EXTDLL_QUERYDATABYTAGEX
author: windows-driver-content
description: 
ms.assetid: 7927caca-b1c9-4783-9fc0-485a258b209f
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

# EXTDLL_QUERYDATABYTAGEX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXTDLL_QUERYDATABYTAGEX ExtdllQuerydatabytagex; 

// Definition

HRESULT ExtdllQuerydatabytagex 
(
	PDEBUG_CLIENT4 Client
	ULONG dwDataTag
	PVOID pQueryInfo
	PBYTE pData
	ULONG cbData
	PBYTE pDataEx
	ULONG cbDataEx
)
{...}

EXTDLL_QUERYDATABYTAGEX 


```

## -parameters

### -param Client: 
### -param dwDataTag: 
### -param pQueryInfo: 
### -param pData: 
### -param cbData: 
### -param pDataEx: 
### -param cbDataEx: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also