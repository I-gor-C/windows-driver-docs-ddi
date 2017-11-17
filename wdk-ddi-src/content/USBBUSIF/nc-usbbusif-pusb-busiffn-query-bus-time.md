---
UID: NC.usbbusif.PUSB_BUSIFFN_QUERY_BUS_TIME
title: PUSB_BUSIFFN_QUERY_BUS_TIME
author: windows-driver-content
description: 
ms.assetid: 55839648-4a77-421a-8124-c7928da8a7dc
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

# PUSB_BUSIFFN_QUERY_BUS_TIME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PUSB_BUSIFFN_QUERY_BUS_TIME PusbBusiffnQueryBusTime; 

// Definition

NTSTATUS PusbBusiffnQueryBusTime 
(
	PVOID 
	PULONG 
)
{...}

PUSB_BUSIFFN_QUERY_BUS_TIME 


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