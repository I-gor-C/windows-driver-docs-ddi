---
UID: NC.d3dkmthk.PFND3DKMT_PRESENTMULTIPLANEOVERLAY3
title: PFND3DKMT_PRESENTMULTIPLANEOVERLAY3
author: windows-driver-content
description: 
ms.assetid: 111a2b7f-398d-4f8a-8c0f-0d281af5b69c
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

# PFND3DKMT_PRESENTMULTIPLANEOVERLAY3 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_PRESENTMULTIPLANEOVERLAY3 Pfnd3dkmtPresentmultiplaneoverlay3; 

// Definition

NTSTATUS Pfnd3dkmtPresentmultiplaneoverlay3 
(
	CONST D3DKMT_PRESENT_MULTIPLANE_OVERLAY3 *
)
{...}

PFND3DKMT_PRESENTMULTIPLANEOVERLAY3 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also