---
UID: NC.d3dkmthk.PFND3DKMT_SETFSEBLOCK
title: PFND3DKMT_SETFSEBLOCK
author: windows-driver-content
description: 
ms.assetid: a9d457db-397b-4e9b-ba3d-8d84756deb11
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

# PFND3DKMT_SETFSEBLOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_SETFSEBLOCK Pfnd3dkmtSetfseblock; 

// Definition

NTSTATUS Pfnd3dkmtSetfseblock 
(
	CONST D3DKMT_SETFSEBLOCK *
)
{...}

PFND3DKMT_SETFSEBLOCK 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also