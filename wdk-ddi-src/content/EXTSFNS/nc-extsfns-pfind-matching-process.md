---
UID: NC.extsfns.PFIND_MATCHING_PROCESS
title: PFIND_MATCHING_PROCESS
author: windows-driver-content
description: 
ms.assetid: 09c29d8b-2e8c-4db2-82c9-3257dd5c8568
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

# PFIND_MATCHING_PROCESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFIND_MATCHING_PROCESS PfindMatchingProcess; 

// Definition

HRESULT PfindMatchingProcess 
(
	PDEBUG_CLIENT Client
	PKDEXT_PROCESS_FIND_PARAMS ProcessInfo
	PULONG64 Process
)
{...}

PFIND_MATCHING_PROCESS 


```

## -parameters

### -param Client: 
### -param ProcessInfo: 
### -param Process: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also