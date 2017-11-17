---
UID: NC.d3dkmthk.PFND3DKMT_CREATEOVERLAY
title: PFND3DKMT_CREATEOVERLAY
author: windows-driver-content
description: 
ms.assetid: 0116802e-1587-490f-8ed1-de7ce40391ed
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

# PFND3DKMT_CREATEOVERLAY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_CREATEOVERLAY Pfnd3dkmtCreateoverlay; 

// Definition

NTSTATUS Pfnd3dkmtCreateoverlay 
(
	D3DKMT_CREATEOVERLAY *
)
{...}

PFND3DKMT_CREATEOVERLAY 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also