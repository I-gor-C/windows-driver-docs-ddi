---
UID: NC.netadapter.EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD
title: EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD
author: windows-driver-content
description: 
ms.assetid: 93edb78a-fcc5-4c4a-a402-a6cf107819f1
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

# EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD EvtNetAdapterPreviewProtocolOffload; 

// Definition

NTSTATUS EvtNetAdapterPreviewProtocolOffload 
(
	NETADAPTER Adapter
	NETPOWERSETTINGS ExistingPowerSettings
	NDIS_PM_PROTOCOL_OFFLOAD_TYPE ProtocolOffloadType
	PNDIS_PM_PROTOCOL_OFFLOAD ProtocolOffloadToBeAdded
)
{...}

EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD PFN_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD


```

## -parameters

### -param Adapter: 
### -param ExistingPowerSettings: 
### -param ProtocolOffloadType: 
### -param ProtocolOffloadToBeAdded: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also