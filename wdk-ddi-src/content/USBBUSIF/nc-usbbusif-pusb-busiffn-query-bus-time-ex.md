---
UID: NC.usbbusif.PUSB_BUSIFFN_QUERY_BUS_TIME_EX
title: PUSB_BUSIFFN_QUERY_BUS_TIME_EX
author: windows-driver-content
description: 
ms.assetid: e160c0de-66bc-4519-b53f-8a5326d3a54e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: usbbusif.h
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

# PUSB_BUSIFFN_QUERY_BUS_TIME_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PUSB_BUSIFFN_QUERY_BUS_TIME_EX PusbBusiffnQueryBusTimeEx; 

// Definition

NTSTATUS PusbBusiffnQueryBusTimeEx 
(
	PVOID 
	PULONG 
)
{...}

PUSB_BUSIFFN_QUERY_BUS_TIME_EX 


```

## -parameters

### -param : 
### -param : 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also