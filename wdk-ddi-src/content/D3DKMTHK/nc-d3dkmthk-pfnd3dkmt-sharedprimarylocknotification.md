---
UID: NC.d3dkmthk.PFND3DKMT_SHAREDPRIMARYLOCKNOTIFICATION
title: PFND3DKMT_SHAREDPRIMARYLOCKNOTIFICATION
author: windows-driver-content
description: 
ms.assetid: 0e21781a-2983-44cb-88b8-8093cee68e2e
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

# PFND3DKMT_SHAREDPRIMARYLOCKNOTIFICATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_SHAREDPRIMARYLOCKNOTIFICATION Pfnd3dkmtSharedprimarylocknotification; 

// Definition

NTSTATUS Pfnd3dkmtSharedprimarylocknotification 
(
	CONST D3DKMT_SHAREDPRIMARYLOCKNOTIFICATION *
)
{...}

PFND3DKMT_SHAREDPRIMARYLOCKNOTIFICATION 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also