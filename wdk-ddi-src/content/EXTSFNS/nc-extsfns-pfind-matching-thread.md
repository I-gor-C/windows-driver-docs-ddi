---
UID: NC.extsfns.PFIND_MATCHING_THREAD
title: PFIND_MATCHING_THREAD
author: windows-driver-content
description: 
ms.assetid: 957ce40b-5457-4529-9fd7-49d6bf836623
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

# PFIND_MATCHING_THREAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFIND_MATCHING_THREAD PfindMatchingThread; 

// Definition

HRESULT PfindMatchingThread 
(
	PDEBUG_CLIENT Client
	PKDEXT_THREAD_FIND_PARAMS ThreadInfo
)
{...}

PFIND_MATCHING_THREAD 


```

## -parameters

### -param Client: 
### -param ThreadInfo: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also