---
UID: NC.netadapter.EVT_NET_ADAPTER_SET_CAPABILITIES
title: EVT_NET_ADAPTER_SET_CAPABILITIES
author: windows-driver-content
description: 
ms.assetid: 82733eeb-6d73-4176-b296-151daaedfe77
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netadapter.h
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

# EVT_NET_ADAPTER_SET_CAPABILITIES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_NET_ADAPTER_SET_CAPABILITIES EvtNetAdapterSetCapabilities; 

// Definition

NTSTATUS EvtNetAdapterSetCapabilities 
(
	NETADAPTER Adapter
)
{...}

EVT_NET_ADAPTER_SET_CAPABILITIES PFN_NET_ADAPTER_SET_CAPABILITIES


```

## -parameters

### -param Adapter: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also