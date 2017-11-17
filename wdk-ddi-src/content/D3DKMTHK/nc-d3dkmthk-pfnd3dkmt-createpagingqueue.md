---
UID: NC.d3dkmthk.PFND3DKMT_CREATEPAGINGQUEUE
title: PFND3DKMT_CREATEPAGINGQUEUE
author: windows-driver-content
description: 
ms.assetid: 2b8425d3-dce2-429f-8a80-b85822b5b29f
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

# PFND3DKMT_CREATEPAGINGQUEUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_CREATEPAGINGQUEUE Pfnd3dkmtCreatepagingqueue; 

// Definition

NTSTATUS Pfnd3dkmtCreatepagingqueue 
(
	D3DKMT_CREATEPAGINGQUEUE *
)
{...}

PFND3DKMT_CREATEPAGINGQUEUE 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also