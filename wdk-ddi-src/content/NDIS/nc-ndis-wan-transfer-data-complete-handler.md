---
UID: NC.ndis.WAN_TRANSFER_DATA_COMPLETE_HANDLER
title: WAN_TRANSFER_DATA_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: 83a01c93-5717-4558-a80e-47c5d9e30ce0
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

# WAN_TRANSFER_DATA_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

WAN_TRANSFER_DATA_COMPLETE_HANDLER WanTransferDataCompleteHandler; 

// Definition

VOID WanTransferDataCompleteHandler 
(
	 VOID
)
{...}

WAN_TRANSFER_DATA_COMPLETE_HANDLER 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also