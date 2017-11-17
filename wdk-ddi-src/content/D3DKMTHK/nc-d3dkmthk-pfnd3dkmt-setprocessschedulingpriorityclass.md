---
UID: NC.d3dkmthk.PFND3DKMT_SETPROCESSSCHEDULINGPRIORITYCLASS
title: PFND3DKMT_SETPROCESSSCHEDULINGPRIORITYCLASS
author: windows-driver-content
description: 
ms.assetid: c5108e0a-e1dd-4cfd-ab8e-a34b53c3bf9b
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

# PFND3DKMT_SETPROCESSSCHEDULINGPRIORITYCLASS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_SETPROCESSSCHEDULINGPRIORITYCLASS Pfnd3dkmtSetprocessschedulingpriorityclass; 

// Definition

NTSTATUS Pfnd3dkmtSetprocessschedulingpriorityclass 
(
	 HANDLE
	 D3DKMT_SCHEDULINGPRIORITYCLASS
)
{...}

PFND3DKMT_SETPROCESSSCHEDULINGPRIORITYCLASS 


```

## -parameters

### -param HANDLE: 
### -param D3DKMT_SCHEDULINGPRIORITYCLASS: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also