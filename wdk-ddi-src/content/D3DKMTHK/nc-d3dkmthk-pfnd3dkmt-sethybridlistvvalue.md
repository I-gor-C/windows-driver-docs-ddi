---
UID: NC.d3dkmthk.PFND3DKMT_SETHYBRIDLISTVVALUE
title: PFND3DKMT_SETHYBRIDLISTVVALUE
author: windows-driver-content
description: 
ms.assetid: c3ec2f49-a32b-4d6d-97ac-b5c4fab6dad3
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

# PFND3DKMT_SETHYBRIDLISTVVALUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_SETHYBRIDLISTVVALUE Pfnd3dkmtSethybridlistvvalue; 

// Definition

NTSTATUS Pfnd3dkmtSethybridlistvvalue 
(
	D3DKMT_HYBRID_LIST *
)
{...}

PFND3DKMT_SETHYBRIDLISTVVALUE 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also