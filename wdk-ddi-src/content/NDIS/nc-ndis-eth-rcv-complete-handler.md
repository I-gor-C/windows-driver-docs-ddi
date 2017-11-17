---
UID: NC.ndis.ETH_RCV_COMPLETE_HANDLER
title: ETH_RCV_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: 5ddb2bdc-5f71-4ca2-b8ef-f9f771d88d00
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

# ETH_RCV_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ETH_RCV_COMPLETE_HANDLER EthRcvCompleteHandler; 

// Definition

VOID EthRcvCompleteHandler 
(
	PETH_FILTER Filter
)
{...}

ETH_RCV_COMPLETE_HANDLER 


```

## -parameters

### -param Filter: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also