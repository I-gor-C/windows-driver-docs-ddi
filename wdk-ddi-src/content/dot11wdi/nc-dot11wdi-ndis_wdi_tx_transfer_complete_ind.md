---
UID: NC:dot11wdi.NDIS_WDI_TX_TRANSFER_COMPLETE_IND
title: NDIS_WDI_TX_TRANSFER_COMPLETE_IND
author: windows-driver-content
description: The NdisWdiTxTransferCompleteIndication callback function specifies a list of frame buffers that have been transferred to the target. Frames with different TX Status values are completed in separate indications.
old-location: netvista\ndiswditxtransfercompleteindication.htm
old-project: netvista
ms.assetid: BC66C993-F571-4EB9-8163-65B038ECE754
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: NDIS_WDI_TX_TRANSFER_COMPLETE_IND, NdisWdiTxTransferCompleteIndication, NdisWdiTxTransferCompleteIndication callback function [Network Drivers Starting with Windows Vista], dot11wdi/NdisWdiTxTransferCompleteIndication, netvista.ndiswditxtransfercompleteindication
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	dot11wdi.h
api_name:
-	NdisWdiTxTransferCompleteIndication
product: Windows
targetos: Windows
req.typenames: SYNTH_STATS, *PSYNTH_STATS
---


# NDIS_WDI_TX_TRANSFER_COMPLETE_IND callback function
The NdisWdiTxTransferCompleteIndication callback function specifies a list of frame buffers that have been transferred to the target.
Frames with different TX Status values are completed in separate indications.

If the TX status is a failure code, an <a href="..\dot11wdi\nc-dot11wdi-ndis_wdi_tx_send_complete_ind.md">NdisWdiTxSendCompleteIndication</a> is not indicated for any of the frames in the <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> (NBL) chain.

This is a callback inside <a href="..\dot11wdi\ns-dot11wdi-_ndis_wdi_data_api.md">NDIS_WDI_DATA_API</a>.

## Syntax

```
NDIS_WDI_TX_TRANSFER_COMPLETE_IND NdisWdiTxTransferCompleteInd;

void NdisWdiTxTransferCompleteInd(
  NDIS_HANDLE NdisMiniportDataPathHandle,
  WDI_TX_FRAME_STATUS WifiTxFrameStatus,
  PNET_BUFFER_LIST pNBL
)
{...}
```

## Parameters

`NdisMiniportDataPathHandle`

The NdisMiniportDataPathHandle passed to the IHV miniport in <a href="..\dot11wdi\nc-dot11wdi-miniport_wdi_tal_txrx_initialize.md">MiniportWdiTalTxRxInitialize</a>.

`WifiTxFrameStatus`

The TX status, specified as a <a href="..\dot11wdi\ne-dot11wdi-_wdi_tx_frame_status.md">WDI_TX_FRAME_STATUS</a> value.

`pNBL`

The null-terminated list of frame buffers that have been transferred to the target.


## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | dot11wdi.h |

## See Also

<a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a>



<a href="..\dot11wdi\ne-dot11wdi-_wdi_tx_frame_status.md">WDI_TX_FRAME_STATUS</a>



<a href="..\dot11wdi\ns-dot11wdi-_ndis_wdi_data_api.md">NDIS_WDI_DATA_API</a>



<a href="..\dot11wdi\nc-dot11wdi-ndis_wdi_tx_send_complete_ind.md">NdisWdiTxSendCompleteIndication</a>