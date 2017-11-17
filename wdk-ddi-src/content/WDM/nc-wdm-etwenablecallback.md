---
UID: NC.wdm.ETWENABLECALLBACK
title: ETWENABLECALLBACK
author: windows-driver-content
description: 
ms.assetid: 66fce0b2-c8c4-4633-879a-a63672efe84d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# ETWENABLECALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ETWENABLECALLBACK Etwenablecallback; 

// Definition

_IRQL_requires_same_ VOID Etwenablecallback 
(
	LPCGUID SourceId
	ULONG ControlCode
	UCHAR Level
	ULONGLONG MatchAnyKeyword
	ULONGLONG MatchAllKeyword
	PEVENT_FILTER_DESCRIPTOR FilterData
	PVOID CallbackContext
)
{...}

ETWENABLECALLBACK PETWENABLECALLBACK


```

## -parameters

### -param SourceId: 
### -param ControlCode: 
### -param Level: 
### -param MatchAnyKeyword: 
### -param MatchAllKeyword: 
### -param FilterData: 
### -param CallbackContext: 



## -returns

Returns _IRQL_requires_same_ VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also