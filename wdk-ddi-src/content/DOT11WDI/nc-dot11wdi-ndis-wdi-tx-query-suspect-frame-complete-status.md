---
UID: NC.dot11wdi.NDIS_WDI_TX_QUERY_SUSPECT_FRAME_COMPLETE_STATUS
title: NDIS_WDI_TX_QUERY_SUSPECT_FRAME_COMPLETE_STATUS
author: windows-driver-content
description: 
ms.assetid: f946a466-b396-4eb6-bb6a-6c9cbb99237d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dot11wdi.h
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

# NDIS_WDI_TX_QUERY_SUSPECT_FRAME_COMPLETE_STATUS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_WDI_TX_QUERY_SUSPECT_FRAME_COMPLETE_STATUS NdisWdiTxQuerySuspectFrameCompleteStatus; 

// Definition

void NdisWdiTxQuerySuspectFrameCompleteStatus 
(
	NDIS_HANDLE NdisMiniportDataPathHandle
	UINT64 SuspectFrameContext
	PNET_BUFFER_LIST pNBL
	BOOLEAN *pIsTransferCompleteNeeded
	BOOLEAN *pIsSendCompleteNeeded
	NDIS_STATUS *pWifiStatus
)
{...}

NDIS_WDI_TX_QUERY_SUSPECT_FRAME_COMPLETE_STATUS 


```

## -parameters

### -param NdisMiniportDataPathHandle: 
### -param SuspectFrameContext: 
### -param pNBL: 
### -param *pIsTransferCompleteNeeded: 
### -param *pIsSendCompleteNeeded: 
### -param *pWifiStatus: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also