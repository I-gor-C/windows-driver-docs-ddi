---
UID: NC.sercx.EVT_SERCX2_CUSTOM_RECEIVE_TRANSACTION_QUERY_PROGRESS
title: EVT_SERCX2_CUSTOM_RECEIVE_TRANSACTION_QUERY_PROGRESS
author: windows-driver-content
description: 
ms.assetid: 381cbe0f-2ac5-4f21-bfc0-f3d9e9435bb2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sercx.h
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

# EVT_SERCX2_CUSTOM_RECEIVE_TRANSACTION_QUERY_PROGRESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_SERCX2_CUSTOM_RECEIVE_TRANSACTION_QUERY_PROGRESS EvtSercx2CustomReceiveTransactionQueryProgress; 

// Definition

VOID EvtSercx2CustomReceiveTransactionQueryProgress 
(
	SERCX2CUSTOMRECEIVETRANSACTION CustomReceiveTransaction
)
{...}

EVT_SERCX2_CUSTOM_RECEIVE_TRANSACTION_QUERY_PROGRESS PFN_SERCX2_CUSTOM_RECEIVE_TRANSACTION_QUERY_PROGRESS


```

## -parameters

### -param CustomReceiveTransaction: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also