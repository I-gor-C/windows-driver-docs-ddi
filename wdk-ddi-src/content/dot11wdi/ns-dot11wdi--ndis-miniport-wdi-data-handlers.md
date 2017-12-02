---
UID: NS.dot11wdi._NDIS_MINIPORT_WDI_DATA_HANDLERS
title: NDIS_MINIPORT_WDI_DATA_HANDLERS
author: windows-driver-content
description: The NDIS_MINIPORT_WDI_DATA_HANDLERS structure specifies the entry points for the IHV miniport datapath handlers.
old-location: netvista\ndis_miniport_wdi_data_handlers.htm
old-project: netvista
ms.assetid: DBDB5F08-9988-4D9B-A731-DA65BBA67813
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_MINIPORT_WDI_DATA_HANDLERS, NDIS_MINIPORT_WDI_DATA_HANDLERS, *PNDIS_MINIPORT_WDI_DATA_HANDLERS
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
req.alt-api: NDIS_MINIPORT_WDI_DATA_HANDLERS
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

# NDIS_MINIPORT_WDI_DATA_HANDLERS structure



## -description
<p>The NDIS_MINIPORT_WDI_DATA_HANDLERS structure specifies the entry points for the IHV miniport datapath handlers.</p>


## -syntax

````
typedef struct _NDIS_MINIPORT_WDI_DATA_HANDLERS {
  NDIS_OBJECT_HEADER                                Header;
  MINIPORT_WDI_TX_ABORT_HANDLER                     TxAbortHandler;
  MINIPORT_WDI_TX_TARGET_DESC_INIT_HANDLER          TxTargetDescInitHandler;
  MINIPORT_WDI_TX_TARGET_DESC_DEINIT_HANDLER        TxTargetDescDeInitHandler;
  MINIPORT_WDI_TX_DATA_SEND_HANDLER                 TxDataSendHandler;
  MINIPORT_WDI_TX_TAL_SEND_HANDLER                  TxTalSendHandler;
  MINIPORT_WDI_TX_TAL_SEND_COMPLETE_HANDLER         TxTalSendCompleteHandler;
  MINIPORT_WDI_TX_TAL_QUEUE_IN_ORDER_HANDLER        TxTalQueueInOrderHandler;
  MINIPORT_WDI_TX_PEER_BACKLOG_HANDLER              TxPeerBacklogHandler;
  MINIPORT_WDI_RX_STOP_HANDLER                      RxStopHandler;
  MINIPORT_WDI_RX_FLUSH_HANDLER                     RxFlushHandler;
  MINIPORT_WDI_RX_RESTART_HANDLER                   RxRestartHandler;
  MINIPORT_WDI_RX_GET_MPDUS_HANDLER                 RxGetMpdusHandler;
  MINIPORT_WDI_RX_RETURN_FRAMES_HANDLER             RxReturnFramesHandler;
  MINIPORT_WDI_RX_RESUME_HANDLER                    RxResumeHandler;
  MINIPORT_WDI_RX_THROTTLE_HANDLER                  RxThrottleHandler;
  MINIPORT_WDI_RX_PPDU_RSSI_HANDLER                 RxPpduRssiHandler;
  MINIPORT_WDI_TAL_TXRX_START_HANDLER               TalTxRxStartHandler;
  MINIPORT_WDI_TAL_TXRX_STOP_HANDLER                TalTxRxStopHandler;
  MINIPORT_WDI_TAL_TXRX_ADD_PORT_HANDLER            TalTxRxAddPortHandler;
  MINIPORT_WDI_TAL_TXRX_DELETE_PORT_HANDLER         TalTxRxDeletePortHandler;
  MINIPORT_WDI_TAL_TXRX_SET_PORT_OPMODE_HANDLER     TalTxRxSetPortOpModeHandler;
  MINIPORT_WDI_TAL_TXRX_RESET_PORT_HANDLER          TalTxRxResetPortHandler;
  MINIPORT_WDI_TAL_TXRX_PEER_CONFIG_HANDLER         TalTxRxPeerConfigHandler;
  MINIPORT_WDI_TAL_TXRX_PEER_DELETE_CONFIRM_HANDLER TalTxRxPeerDeleteConfirmHandler;
} NDIS_MINIPORT_WDI_DATA_HANDLERS, *PNDIS_MINIPORT_WDI_DATA_HANDLERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_MINIPORT_WDI_DATA_HANDLERS structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_MINIPORT_WDI_DATA_HANDLERS.
     </p>
<p>To indicate the version of the NDIS_MINIPORT_WDI_DATA_HANDLERS structure, set the 
     <b>Revision</b> member to the following value:</p>
<p></p>
<dl>

### -field NDIS_OBJECT_TYPE_MINIPORT_WDI_DATA_HANDLERS_REVISION_1

<dd>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_MINIPORT_WDI_DATA_HANDLERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field TxAbortHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-abort.md">MiniportWdiTxAbort</a> handler function.</p>
</dd>

### -field TxTargetDescInitHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-target-desc-init.md">MiniportWdiTxTargetDescInit</a> handler function.</p>
</dd>

### -field TxTargetDescDeInitHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-target-desc-deinit.md">MiniportWdiTxTargetDescDeInit</a> handler function.</p>
</dd>

### -field TxDataSendHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-data-send.md">MiniportWdiTxDataSend</a> handler function.</p>
</dd>

### -field TxTalSendHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-tal-send.md">MiniportWdiTxTalSend</a> handler function.</p>
</dd>

### -field TxTalSendCompleteHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-tal-send-complete.md">MiniportWdiTxTalSendComplete</a> handler function.</p>
</dd>

### -field TxTalQueueInOrderHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-tal-queue-in-order.md">MiniportWdiTxTalQueueInOrder</a> handler function.</p>
</dd>

### -field TxPeerBacklogHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-peer-backlog.md">MiniportWdiTxPeerBacklog</a> handler function.</p>
</dd>

### -field RxStopHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-rx-stop.md">MiniportWdiRxStop</a> handler function.</p>
</dd>

### -field RxFlushHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-rx-flush.md">MiniportWdiRxFlush</a> handler function.</p>
</dd>

### -field RxRestartHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-rx-restart.md">MiniportWdiRxRestart</a> handler function.</p>
</dd>

### -field RxGetMpdusHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-rx-get-mpdus.md">MiniportWdiRxGetMpdus</a> handler function.</p>
</dd>

### -field RxReturnFramesHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-rx-return-frames.md">MiniportWdiRxReturnFrames</a> handler function.</p>
</dd>

### -field RxResumeHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-rx-resume.md">MiniportWdiRxResume</a> handler function.</p>
</dd>

### -field RxThrottleHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-rx-throttle.md">MiniportWdiRxThrottle</a> handler function.</p>
</dd>

### -field RxPpduRssiHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-rx-ppdu-rssi.md">MiniportWdiRxPpduRssi</a> handler function.</p>
</dd>

### -field TalTxRxStartHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-start.md">MiniportWdiTalTxRxStart</a> handler function.</p>
</dd>

### -field TalTxRxStopHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-stop.md">MiniportWdiTalTxRxStop</a> handler function.</p>
</dd>

### -field TalTxRxAddPortHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-add-port.md">MiniportWdiTalTxRxAddPort</a> handler function.</p>
</dd>

### -field TalTxRxDeletePortHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-delete-port.md">MiniportWdiTalTxRxDeletePort</a> handler function.</p>
</dd>

### -field TalTxRxSetPortOpModeHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-set-port-opmode.md">MiniportWdiTalTxRxSetPortOpMode</a> handler function.</p>
</dd>

### -field TalTxRxResetPortHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-reset-port.md">MiniportWdiTalTxRxResetPort</a> handler function.</p>
</dd>

### -field TalTxRxPeerConfigHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-peer-config.md">MiniportWdiTalTxRxPeerConfig</a> handler function.</p>
</dd>

### -field TalTxRxPeerDeleteConfirmHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-peer-delete-confirm.md">MiniportWdiTalTxRxPeerDeleteConfirm</a> handler function.</p>
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