---
UID: NC.d3dkmthk.PFND3DKMT_GETDEVICESTATE
title: PFND3DKMT_GETDEVICESTATE
author: windows-driver-content
description: 
ms.assetid: 658edd9b-5b13-4123-bc16-5d6b908ac6aa
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

# PFND3DKMT_GETDEVICESTATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_GETDEVICESTATE Pfnd3dkmtGetdevicestate; 

// Definition

NTSTATUS Pfnd3dkmtGetdevicestate 
(
	D3DKMT_GETDEVICESTATE *
)
{...}

PFND3DKMT_GETDEVICESTATE 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also