---
UID: NC.netadapter.EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN
title: EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN
author: windows-driver-content
description: 
ms.assetid: 56253c9d-7713-4990-9bb9-603e1d4c0387
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

# EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN EvtNetAdapterPreviewWakePattern; 

// Definition

NTSTATUS EvtNetAdapterPreviewWakePattern 
(
	NETADAPTER Adapter
	NETPOWERSETTINGS ExistingPowerSettings
	NDIS_PM_WOL_PACKET WakePatternType
	PNDIS_PM_WOL_PATTERN PatternToBeAdded
)
{...}

EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN PFN_NET_ADAPTER_PREVIEW_WAKE_PATTERN


```

## -parameters

### -param Adapter: 
### -param ExistingPowerSettings: 
### -param WakePatternType: 
### -param PatternToBeAdded: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also