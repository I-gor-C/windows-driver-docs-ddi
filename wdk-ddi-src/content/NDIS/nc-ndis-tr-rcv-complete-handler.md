---
UID: NC.ndis.TR_RCV_COMPLETE_HANDLER
title: TR_RCV_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: ccdb5f50-e600-4cee-8290-2575b9645f49
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

# TR_RCV_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TR_RCV_COMPLETE_HANDLER TrRcvCompleteHandler; 

// Definition

VOID TrRcvCompleteHandler 
(
	PTR_FILTER Filter
)
{...}

TR_RCV_COMPLETE_HANDLER 


```

## -parameters

### -param Filter: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also