---
UID: NC.ndis.FILTER_CANCEL_SEND_NET_BUFFER_LISTS
title: FILTER_CANCEL_SEND_NET_BUFFER_LISTS
author: windows-driver-content
description: 
ms.assetid: 050d3394-006c-4275-8432-71303f923400
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

# FILTER_CANCEL_SEND_NET_BUFFER_LISTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

FILTER_CANCEL_SEND_NET_BUFFER_LISTS FilterCancelSendNetBufferLists; 

// Definition

VOID FilterCancelSendNetBufferLists 
(
	NDIS_HANDLE FilterModuleContext
	PVOID CancelId
)
{...}

FILTER_CANCEL_SEND_NET_BUFFER_LISTS PFILTER_CANCEL_SEND_NET_BUFFER_LISTS


```

## -parameters

### -param FilterModuleContext: 
### -param CancelId: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also