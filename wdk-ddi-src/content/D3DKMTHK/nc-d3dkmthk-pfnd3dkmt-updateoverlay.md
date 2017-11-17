---
UID: NC.d3dkmthk.PFND3DKMT_UPDATEOVERLAY
title: PFND3DKMT_UPDATEOVERLAY
author: windows-driver-content
description: 
ms.assetid: 1afc2019-f107-4398-bd23-e46f2948c5f0
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

# PFND3DKMT_UPDATEOVERLAY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_UPDATEOVERLAY Pfnd3dkmtUpdateoverlay; 

// Definition

NTSTATUS Pfnd3dkmtUpdateoverlay 
(
	CONST D3DKMT_UPDATEOVERLAY *
)
{...}

PFND3DKMT_UPDATEOVERLAY 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also