---
UID: NC.d3dkmthk.PFND3DKMT_SETSTEREOENABLED
title: PFND3DKMT_SETSTEREOENABLED
author: windows-driver-content
description: 
ms.assetid: b4a6cc68-65bf-4f20-8570-61f8159a6b5b
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

# PFND3DKMT_SETSTEREOENABLED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_SETSTEREOENABLED Pfnd3dkmtSetstereoenabled; 

// Definition

NTSTATUS Pfnd3dkmtSetstereoenabled 
(
	 BOOL
)
{...}

PFND3DKMT_SETSTEREOENABLED 


```

## -parameters

### -param BOOL: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also