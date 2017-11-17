---
UID: NC.mrx.PMRX_GET_CONNECTION_ID
title: PMRX_GET_CONNECTION_ID
author: windows-driver-content
description: 
ms.assetid: 48e230d1-c9e1-46ab-b735-ceee9b834122
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

# PMRX_GET_CONNECTION_ID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_GET_CONNECTION_ID PmrxGetConnectionId; 

// Definition

NTSTATUS PmrxGetConnectionId 
(
	IN OUT PRX_CONTEXT RxContext
	IN OUT PRX_CONNECTION_ID UniqueId
)
{...}

PMRX_GET_CONNECTION_ID 


```

## -parameters

### -param RxContext: 
### -param UniqueId: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also