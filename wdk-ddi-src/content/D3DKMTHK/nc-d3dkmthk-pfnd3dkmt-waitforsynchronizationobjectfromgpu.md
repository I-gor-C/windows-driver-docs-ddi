---
UID: NC.d3dkmthk.PFND3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMGPU
title: PFND3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMGPU
author: windows-driver-content
description: 
ms.assetid: ab5efd4a-cea6-4a28-ba51-5e7427ce710a
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

# PFND3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMGPU callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMGPU Pfnd3dkmtWaitforsynchronizationobjectfromgpu; 

// Definition

NTSTATUS Pfnd3dkmtWaitforsynchronizationobjectfromgpu 
(
	CONST D3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMGPU *
)
{...}

PFND3DKMT_WAITFORSYNCHRONIZATIONOBJECTFROMGPU 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also