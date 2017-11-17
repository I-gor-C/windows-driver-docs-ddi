---
UID: NC.d3dkmthk.PFND3DKMT_OPENKEYEDMUTEX
title: PFND3DKMT_OPENKEYEDMUTEX
author: windows-driver-content
description: 
ms.assetid: aa34d7bc-086a-439f-9d25-f57d15c8bd60
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmthk.h
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

# PFND3DKMT_OPENKEYEDMUTEX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_OPENKEYEDMUTEX Pfnd3dkmtOpenkeyedmutex; 

// Definition

NTSTATUS Pfnd3dkmtOpenkeyedmutex 
(
	D3DKMT_OPENKEYEDMUTEX *
)
{...}

PFND3DKMT_OPENKEYEDMUTEX 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also