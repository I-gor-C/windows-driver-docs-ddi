---
UID: NC.d3dkmthk.PFND3DKMT_GETRUNTIMEDATA
title: PFND3DKMT_GETRUNTIMEDATA
author: windows-driver-content
description: 
ms.assetid: b80eec9f-b7bc-43ca-98b3-cd73cee7e12f
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

# PFND3DKMT_GETRUNTIMEDATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_GETRUNTIMEDATA Pfnd3dkmtGetruntimedata; 

// Definition

NTSTATUS Pfnd3dkmtGetruntimedata 
(
	CONST D3DKMT_GETRUNTIMEDATA *
)
{...}

PFND3DKMT_GETRUNTIMEDATA 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also