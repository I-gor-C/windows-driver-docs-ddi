---
UID: NC.d3dkmthk.PFND3DKMT_QUERYPROCESSOFFERINFO
title: PFND3DKMT_QUERYPROCESSOFFERINFO
author: windows-driver-content
description: 
ms.assetid: e2e6e201-2ce3-4e50-8071-b6c9f22f844a
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

# PFND3DKMT_QUERYPROCESSOFFERINFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_QUERYPROCESSOFFERINFO Pfnd3dkmtQueryprocessofferinfo; 

// Definition

NTSTATUS Pfnd3dkmtQueryprocessofferinfo 
(
	D3DKMT_QUERYPROCESSOFFERINFO *
)
{...}

PFND3DKMT_QUERYPROCESSOFFERINFO 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also