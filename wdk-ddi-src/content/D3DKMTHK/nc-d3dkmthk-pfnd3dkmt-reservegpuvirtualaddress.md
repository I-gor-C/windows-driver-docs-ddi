---
UID: NC.d3dkmthk.PFND3DKMT_RESERVEGPUVIRTUALADDRESS
title: PFND3DKMT_RESERVEGPUVIRTUALADDRESS
author: windows-driver-content
description: 
ms.assetid: c76f0a5c-120a-49b9-9115-a1604a1504a4
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

# PFND3DKMT_RESERVEGPUVIRTUALADDRESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_RESERVEGPUVIRTUALADDRESS Pfnd3dkmtReservegpuvirtualaddress; 

// Definition

NTSTATUS Pfnd3dkmtReservegpuvirtualaddress 
(
	D3DDDI_RESERVEGPUVIRTUALADDRESS *
)
{...}

PFND3DKMT_RESERVEGPUVIRTUALADDRESS 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also