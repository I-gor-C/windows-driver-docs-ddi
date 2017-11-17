---
UID: NC.d3dkmthk.PFND3DKMT_OUTPUTDUPLPRESENT
title: PFND3DKMT_OUTPUTDUPLPRESENT
author: windows-driver-content
description: 
ms.assetid: d856dbda-134e-45be-92e0-97be1b165da5
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

# PFND3DKMT_OUTPUTDUPLPRESENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_OUTPUTDUPLPRESENT Pfnd3dkmtOutputduplpresent; 

// Definition

NTSTATUS Pfnd3dkmtOutputduplpresent 
(
	CONST D3DKMT_OUTPUTDUPLPRESENT *
)
{...}

PFND3DKMT_OUTPUTDUPLPRESENT 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also