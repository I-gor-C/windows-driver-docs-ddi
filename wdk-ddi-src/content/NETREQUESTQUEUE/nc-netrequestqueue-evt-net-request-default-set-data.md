---
UID: NC.netrequestqueue.EVT_NET_REQUEST_DEFAULT_SET_DATA
title: EVT_NET_REQUEST_DEFAULT_SET_DATA
author: windows-driver-content
description: 
ms.assetid: 2b51fa9b-ff46-4516-ad88-473b9abde822
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netrequestqueue.h
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

# EVT_NET_REQUEST_DEFAULT_SET_DATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_NET_REQUEST_DEFAULT_SET_DATA EvtNetRequestDefaultSetData; 

// Definition

VOID EvtNetRequestDefaultSetData 
(
	NETREQUESTQUEUE RequestQueue
	NETREQUEST Request
	NDIS_OID Oid
	PVOID InputBuffer
	UINT InputBufferLength
)
{...}

EVT_NET_REQUEST_DEFAULT_SET_DATA PFN_NET_REQUEST_DEFAULT_SET_DATA


```

## -parameters

### -param RequestQueue: 
### -param Request: 
### -param Oid: 
### -param InputBuffer: 
### -param InputBufferLength: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also