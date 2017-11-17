---
UID: NC.d3dkmthk.PFND3DKMT_CREATEOUTPUTDUPL
title: PFND3DKMT_CREATEOUTPUTDUPL
author: windows-driver-content
description: 
ms.assetid: 2eae93f2-7a19-44da-be9b-e70ecb708218
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

# PFND3DKMT_CREATEOUTPUTDUPL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_CREATEOUTPUTDUPL Pfnd3dkmtCreateoutputdupl; 

// Definition

NTSTATUS Pfnd3dkmtCreateoutputdupl 
(
	CONST D3DKMT_CREATE_OUTPUTDUPL *
)
{...}

PFND3DKMT_CREATEOUTPUTDUPL 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also