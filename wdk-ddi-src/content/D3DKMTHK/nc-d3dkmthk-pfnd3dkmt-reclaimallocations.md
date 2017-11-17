---
UID: NC.d3dkmthk.PFND3DKMT_RECLAIMALLOCATIONS
title: PFND3DKMT_RECLAIMALLOCATIONS
author: windows-driver-content
description: 
ms.assetid: 9b26f0fe-2406-4706-a672-007fe6e0c640
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

# PFND3DKMT_RECLAIMALLOCATIONS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_RECLAIMALLOCATIONS Pfnd3dkmtReclaimallocations; 

// Definition

NTSTATUS Pfnd3dkmtReclaimallocations 
(
	CONST D3DKMT_RECLAIMALLOCATIONS *
)
{...}

PFND3DKMT_RECLAIMALLOCATIONS 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also