---
UID: NC.d3dkmthk.PFND3DKMT_CHANGESURFACEPOINTER
title: PFND3DKMT_CHANGESURFACEPOINTER
author: windows-driver-content
description: 
ms.assetid: 4bad55d6-6fe8-4b97-aabf-56080a81346a
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

# PFND3DKMT_CHANGESURFACEPOINTER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_CHANGESURFACEPOINTER Pfnd3dkmtChangesurfacepointer; 

// Definition

NTSTATUS Pfnd3dkmtChangesurfacepointer 
(
	CONST D3DKMT_CHANGESURFACEPOINTER *
)
{...}

PFND3DKMT_CHANGESURFACEPOINTER 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also