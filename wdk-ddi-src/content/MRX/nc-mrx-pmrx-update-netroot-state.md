---
UID: NC.mrx.PMRX_UPDATE_NETROOT_STATE
title: PMRX_UPDATE_NETROOT_STATE
author: windows-driver-content
description: 
ms.assetid: ad8a573d-45b8-4c42-985f-f355a7fc314a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mrx.h
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

# PMRX_UPDATE_NETROOT_STATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_UPDATE_NETROOT_STATE PmrxUpdateNetrootState; 

// Definition

NTSTATUS PmrxUpdateNetrootState 
(
	IN OUT PMRX_NET_ROOT NetRoot
)
{...}

PMRX_UPDATE_NETROOT_STATE 


```

## -parameters

### -param NetRoot: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also