---
UID: NC.ks.PFNKSFILTERFACTORYVOID
title: PFNKSFILTERFACTORYVOID
author: windows-driver-content
description: 
ms.assetid: b54bacda-02bc-4960-a826-d4f132b6182e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSFILTERFACTORYVOID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSFILTERFACTORYVOID Pfnksfilterfactoryvoid; 

// Definition

NTSTATUS Pfnksfilterfactoryvoid 
(
	PKSFILTERFACTORY FilterFactory
)
{...}

PFNKSFILTERFACTORYVOID 


```

## -parameters

### -param FilterFactory: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also