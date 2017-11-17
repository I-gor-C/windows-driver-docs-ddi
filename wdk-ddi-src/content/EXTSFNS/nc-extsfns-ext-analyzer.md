---
UID: NC.extsfns.EXT_ANALYZER
title: EXT_ANALYZER
author: windows-driver-content
description: 
ms.assetid: 07156a23-064c-424d-a757-9f42c2980277
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

# EXT_ANALYZER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXT_ANALYZER ExtAnalyzer; 

// Definition

HRESULT ExtAnalyzer 
(
	PDEBUG_CLIENT Client
	PSTR BucketSuffix
	ULONG cbBucketSuffix
	PSTR DebugText
	ULONG cbDebugText
	PULONG Flags
	PDEBUG_FAILURE_ANALYSIS pAnalysis
)
{...}

EXT_ANALYZER 


```

## -parameters

### -param Client: 
### -param BucketSuffix: 
### -param cbBucketSuffix: 
### -param DebugText: 
### -param cbDebugText: 
### -param Flags: 
### -param pAnalysis: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also