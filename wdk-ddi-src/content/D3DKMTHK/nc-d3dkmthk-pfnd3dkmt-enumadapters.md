---
UID: NC.d3dkmthk.PFND3DKMT_ENUMADAPTERS
title: PFND3DKMT_ENUMADAPTERS
author: windows-driver-content
description: 
ms.assetid: 4380fa5b-9f20-4ddb-99ad-cae0231d270c
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

# PFND3DKMT_ENUMADAPTERS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_ENUMADAPTERS Pfnd3dkmtEnumadapters; 

// Definition

NTSTATUS Pfnd3dkmtEnumadapters 
(
	CONST D3DKMT_ENUMADAPTERS *
)
{...}

PFND3DKMT_ENUMADAPTERS 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also