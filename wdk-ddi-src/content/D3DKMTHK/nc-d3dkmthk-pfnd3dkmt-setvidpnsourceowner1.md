---
UID: NC.d3dkmthk.PFND3DKMT_SETVIDPNSOURCEOWNER1
title: PFND3DKMT_SETVIDPNSOURCEOWNER1
author: windows-driver-content
description: 
ms.assetid: 34cb933b-48d8-445e-8ee7-439df4a0cf7d
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

# PFND3DKMT_SETVIDPNSOURCEOWNER1 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_SETVIDPNSOURCEOWNER1 Pfnd3dkmtSetvidpnsourceowner1; 

// Definition

NTSTATUS Pfnd3dkmtSetvidpnsourceowner1 
(
	CONST D3DKMT_SETVIDPNSOURCEOWNER1 *
)
{...}

PFND3DKMT_SETVIDPNSOURCEOWNER1 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also