---
UID: NS.dot11wdi._NDIS_WDI_DATA_API
title: NDIS_WDI_DATA_API
author: windows-driver-content
description: The NDIS_WDI_DATA_API structure specifies the entry points for WDI data indications.
old-location: netvista\ndis_wdi_data_api.htm
old-project: netvista
ms.assetid: 8C26D62E-711A-4CE7-BD2B-D78B794C67FB
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_WDI_DATA_API, NDIS_WDI_DATA_API, *PNDIS_WDI_DATA_API
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dot11wdi.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WDI_DATA_API
req.alt-loc: dot11wdi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NDIS_WDI_DATA_API structure



## -description
<p>The 
  NDIS_WDI_DATA_API structure specifies the entry points for WDI data indications.</p>


## -syntax

````
typedef struct _NDIS_WDI_DATA_API {
  NDIS_OBJECT_HEADER                           Header;
  NDIS_WDI_TX_DEQUEUE_IND_HANDLER              TxDequeueIndication;
  NDIS_WDI_TX_TRANSFER_COMPLETE_IND_HANDLER    TxTransferCompleteIndication;
  NDIS_WDI_TX_SEND_COMPLETE_IND_HANDLER        TxSendCompleteIndication;
  NDIS_WDI_TX_QUERY_RA_TID_STATE_HANDLER       TxQueryRATIDState;
  NDIS_WDI_TX_SEND_PAUSE_IND_HANDLER           TxSendPauseIndication;
  NDIS_WDI_TX_SEND_RESTART_IND_HANDLER         TxSendRestartIndication;
  NDIS_WDI_TX_RELEASE_FRAMES_IND_HANDLER       TxReleaseFrameIndication;
  NDIS_WDI_TX_INJECT_FRAME_IND_HANDLER         TxInjectFrameIndication;
  NDIS_WDI_TX_ABORT_CONFIRM_HANDLER            TxAbortConfirm;
  NDIS_WDI_RX_INORDER_DATA_IND_HANDLER         RxInorderDataIndication;
  NDIS_WDI_RX_STOP_CONFIRM_HANDLER             RxStopConfirm;
  NDIS_WDI_RX_FLUSH_CONFIRM_HANDLER            RxFlushConfirm;
  NDIS_WDI_PEER_CREATE_IND_HANDLER             PeerCreateIndication;
  NDIS_WDI_PEER_DELETE_IND_HANDLER             PeerDeleteIndication;
  NDIS_WDI_ALLOCATE_WDI_FRAME_METADATA_HANDLER AllocateWiFiFrameMetaData;
  NDIS_WDI_FREE_WDI_FRAME_METADATA_HANDLER     FreeWiFiFrameMetaData;
} NDIS_WDI_DATA_API, *PNDIS_WDI_DATA_API;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_WDI_DATA_API structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_WDI_DATA_API.
     </p>
<p>To indicate the version of the NDIS_WDI_DATA_API structure, set the 
     <b>Revision</b> member to the following value:</p>
<p></p>
<dl>

### -field <a id="NDIS_OBJECT_TYPE_WDI_DATA_API_REVISION_1"></a><a id="ndis_object_type_wdi_data_api_revision_1"></a>NDIS_OBJECT_TYPE_WDI_DATA_API_REVISION_1

<dd>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_WDI_DATA_API_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>TxDequeueIndication</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-dequeue-ind.md">NdisWdiTxDequeueIndication</a> callback function.</p>
</dd>

### -field <b>TxTransferCompleteIndication</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-transfer-complete-ind.md">NdisWdiTxTransferCompleteIndication</a> callback function.</p>
</dd>

### -field <b>TxSendCompleteIndication</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-send-complete-ind.md">NdisWdiTxSendCompleteIndication</a> callback function.</p>
</dd>

### -field <b>TxQueryRATIDState</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-query-ra-tid-state.md">NdisWdiTxQueryRATIDState</a> callback function.</p>
</dd>

### -field <b>TxSendPauseIndication</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-send-pause-ind.md">NdisWdiTxSendPauseIndication</a> callback function.</p>
</dd>

### -field <b>TxSendRestartIndication</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-send-restart-ind.md">NdisWdiTxSendRestartIndication</a> callback function.</p>
</dd>

### -field <b>TxReleaseFrameIndication</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-release-frames-ind.md">NdisWdiTxReleaseFrameIndication</a> callback function.</p>
</dd>

### -field <b>TxInjectFrameIndication</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-inject-frame-ind.md">NdisWdiTxInjectFrameIndication</a> callback function.</p>
</dd>

### -field <b>TxAbortConfirm</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-abort-confirm.md">NdisWdiTxAbortConfirm</a> callback function.</p>
</dd>

### -field <b>RxInorderDataIndication</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-rx-inorder-data-ind.md">NdisWdiRxInorderDataIndication</a> callback function.</p>
</dd>

### -field <b>RxStopConfirm</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-rx-stop-confirm.md">NdisWdiRxStopConfirm</a> callback function.</p>
</dd>

### -field <b>RxFlushConfirm</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-rx-flush-confirm.md">NdisWdiRxFlushConfirm</a> callback function.</p>
</dd>

### -field <b>PeerCreateIndication</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-peer-create-ind.md">NdisWdiPeerCreateIndication</a> callback function.</p>
</dd>

### -field <b>PeerDeleteIndication</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-peer-delete-ind.md">NdisWdiPeerDeleteIndication</a> callback function.</p>
</dd>

### -field <b>AllocateWiFiFrameMetaData</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-allocate-wdi-frame-metadata.md">NdisWdiAllocateWiFiFrameMetaData</a> callback function.</p>
</dd>

### -field <b>FreeWiFiFrameMetaData</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-free-wdi-frame-metadata.md">NdisWdiFreeWiFiFrameMetaData</a> callback function.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dot11wdi.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>