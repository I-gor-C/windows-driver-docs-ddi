---
UID: NC.d3dkmthk.PFND3DKMT_SETDISPLAYPRIVATEDRIVERFORMAT
title: PFND3DKMT_SETDISPLAYPRIVATEDRIVERFORMAT
author: windows-driver-content
description: 
ms.assetid: 614c0542-f8de-44c8-a348-fea1bfdd93c3
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

# PFND3DKMT_SETDISPLAYPRIVATEDRIVERFORMAT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_SETDISPLAYPRIVATEDRIVERFORMAT Pfnd3dkmtSetdisplayprivatedriverformat; 

// Definition

NTSTATUS Pfnd3dkmtSetdisplayprivatedriverformat 
(
	CONST D3DKMT_SETDISPLAYPRIVATEDRIVERFORMAT *
)
{...}

PFND3DKMT_SETDISPLAYPRIVATEDRIVERFORMAT 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also