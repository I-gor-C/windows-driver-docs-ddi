---
UID: NC.ndkrss.NDK_FN_GET_RSS_PROCESSOR_INFO
title: NDK_FN_GET_RSS_PROCESSOR_INFO
author: windows-driver-content
description: 
ms.assetid: 3934857d-c89c-448a-8a15-ba7c0a257cd4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndkrss.h
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

# NDK_FN_GET_RSS_PROCESSOR_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDK_FN_GET_RSS_PROCESSOR_INFO NdkFnGetRssProcessorInfo; 

// Definition

NDIS_STATUS NdkFnGetRssProcessorInfo 
(
	NDK_ADAPTER *pNdkAdapter
	PNDIS_RSS_PROCESSOR_INFO RssProcessorInfo
	PSIZE_T Size
)
{...}

NDK_FN_GET_RSS_PROCESSOR_INFO 


```

## -parameters

### -param *pNdkAdapter: 
### -param RssProcessorInfo: 
### -param Size: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also