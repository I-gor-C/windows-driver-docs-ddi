---
UID: NC.ndis.WM_TRANSFER_DATA_HANDLER
title: WM_TRANSFER_DATA_HANDLER
author: windows-driver-content
description: 
ms.assetid: db7f590e-fdb8-463a-b9db-c059c0b06f97
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndis.h
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

# WM_TRANSFER_DATA_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

WM_TRANSFER_DATA_HANDLER WmTransferDataHandler; 

// Definition

NDIS_STATUS WmTransferDataHandler 
(
	 VOID
)
{...}

WM_TRANSFER_DATA_HANDLER 


```

## -parameters

### -param VOID: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also