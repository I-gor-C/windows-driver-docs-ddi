---
UID: NC.d3dkmthk.PFND3DKMT_QUERYREMOTEVIDPNSOURCEFROMGDIDISPLAYNAME
title: PFND3DKMT_QUERYREMOTEVIDPNSOURCEFROMGDIDISPLAYNAME
author: windows-driver-content
description: 
ms.assetid: 747cf0e4-9b28-4943-84a7-45486e7e6982
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

# PFND3DKMT_QUERYREMOTEVIDPNSOURCEFROMGDIDISPLAYNAME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_QUERYREMOTEVIDPNSOURCEFROMGDIDISPLAYNAME Pfnd3dkmtQueryremotevidpnsourcefromgdidisplayname; 

// Definition

NTSTATUS Pfnd3dkmtQueryremotevidpnsourcefromgdidisplayname 
(
	D3DKMT_QUERYREMOTEVIDPNSOURCEFROMGDIDISPLAYNAME *
)
{...}

PFND3DKMT_QUERYREMOTEVIDPNSOURCEFROMGDIDISPLAYNAME 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also