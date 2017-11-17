---
UID: NC.wdm.GET_D3COLD_CAPABILITY
title: GET_D3COLD_CAPABILITY
author: windows-driver-content
description: 
ms.assetid: 06637f91-f389-43d9-9aa2-12a9eb4a02e5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# GET_D3COLD_CAPABILITY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GET_D3COLD_CAPABILITY GetD3coldCapability; 

// Definition

NTSTATUS GetD3coldCapability 
(
	PVOID Context
	PBOOLEAN D3ColdSupported
)
{...}

GET_D3COLD_CAPABILITY PGET_D3COLD_CAPABILITY


```

## -parameters

### -param Context: 
### -param D3ColdSupported: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also