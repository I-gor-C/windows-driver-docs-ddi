---
UID: NC.ndkpi.NDK_FN_DISCONNECT_EX
title: NDK_FN_DISCONNECT_EX
author: windows-driver-content
description: 
ms.assetid: 9a938a4a-aaca-4e57-8812-1a13536b32b8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndkpi.h
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

# NDK_FN_DISCONNECT_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDK_FN_DISCONNECT_EX NdkFnDisconnectEx; 

// Definition

NTSTATUS NdkFnDisconnectEx 
(
	NDK_CONNECTOR *pNdkConnector
	BOOLEAN Abortive
	NDK_FN_REQUEST_COMPLETION RequestCompletion
	PVOID RequestContext
)
{...}

NDK_FN_DISCONNECT_EX 


```

## -parameters

### -param *pNdkConnector: 
### -param Abortive: 
### -param RequestCompletion: 
### -param RequestContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also