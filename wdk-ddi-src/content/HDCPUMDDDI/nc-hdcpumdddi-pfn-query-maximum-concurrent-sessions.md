---
UID: NC.hdcpumdddi.PFN_QUERY_MAXIMUM_CONCURRENT_SESSIONS
title: PFN_QUERY_MAXIMUM_CONCURRENT_SESSIONS
author: windows-driver-content
description: 
ms.assetid: 74b2b30a-9221-4e95-a982-35a895769901
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hdcpumdddi.h
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

# PFN_QUERY_MAXIMUM_CONCURRENT_SESSIONS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_QUERY_MAXIMUM_CONCURRENT_SESSIONS PfnQueryMaximumConcurrentSessions; 

// Definition

VOID PfnQueryMaximumConcurrentSessions 
(
	UINT *pcSessions
)
{...}

PFN_QUERY_MAXIMUM_CONCURRENT_SESSIONS 


```

## -parameters

### -param *pcSessions: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also