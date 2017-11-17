---
UID: NS.dot11wdi._NDIS_MINIPORT_WDI_DATA_HANDLERS
title: NDIS_MINIPORT_WDI_DATA_HANDLERS
author: windows-driver-content
description: The NDIS_MINIPORT_WDI_DATA_HANDLERS structure specifies the entry points for the IHV miniport datapath handlers.
old-location: netvista\ndis_miniport_wdi_data_handlers.htm
ms.assetid: DBDB5F08-9988-4D9B-A731-DA65BBA67813
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: NDIS_MINIPORT_WDI_DATA_HANDLERS, NDIS_MINIPORT_WDI_DATA_HANDLERS, *PNDIS_MINIPORT_WDI_DATA_HANDLERS
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

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_MINIPORT_WDI_DATA_HANDLERS structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_MINIPORT_WDI_DATA_HANDLERS.
     </p>
<p>To indicate the version of the NDIS_MINIPORT_WDI_DATA_HANDLERS structure, set the 
     <b>Revision</b> member to the following value:</p>
<p></p>
<dl>

### -field <a id="NDIS_OBJECT_TYPE_MINIPORT_WDI_DATA_HANDLERS_REVISION_1"></a><a id="ndis_object_type_miniport_wdi_data_handlers_revision_1"></a>NDIS_OBJECT_TYPE_MINIPORT_WDI_DATA_HANDLERS_REVISION_1

<dd>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_MINIPORT_WDI_DATA_HANDLERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>TxAbortHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/FA6BEAE9-5D48-463E-A398-518737D78867">MiniportWdiTxAbort</a> handler function.</p>
</dd>

### -field <b>TxTargetDescInitHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/EAFE6F7D-6820-4626-863D-C28FBFFCE6A0">MiniportWdiTxTargetDescInit</a> handler function.</p>
</dd>

### -field <b>TxTargetDescDeInitHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/C7C6C175-5E9D-4C6B-8A6B-F903DDE4DC78">MiniportWdiTxTargetDescDeInit</a> handler function.</p>
</dd>

### -field <b>TxDataSendHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/A9EB1E8C-BD10-450F-9F4B-CD19C8AF13EA">MiniportWdiTxDataSend</a> handler function.</p>
</dd>

### -field <b>TxTalSendHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/42489ADA-78BF-4EBF-A6EC-5484F82C46ED">MiniportWdiTxTalSend</a> handler function.</p>
</dd>

### -field <b>TxTalSendCompleteHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/347B069F-76B6-42D5-9613-7D0214C2FEDB">MiniportWdiTxTalSendComplete</a> handler function.</p>
</dd>

### -field <b>TxTalQueueInOrderHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/E82E19EA-4336-49DE-9CE4-DFBA0A347DFE">MiniportWdiTxTalQueueInOrder</a> handler function.</p>
</dd>

### -field <b>TxPeerBacklogHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/49DC9034-9A50-4B0F-B7F7-A06147D1046F">MiniportWdiTxPeerBacklog</a> handler function.</p>
</dd>

### -field <b>RxStopHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/AAFECA64-07D7-43E6-ABFB-C0C85A9C03CD">MiniportWdiRxStop</a> handler function.</p>
</dd>

### -field <b>RxFlushHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/76945A84-A6DB-4753-B04E-32249359B8C6">MiniportWdiRxFlush</a> handler function.</p>
</dd>

### -field <b>RxRestartHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/465716C7-A157-4B06-BAE2-F18A08126040">MiniportWdiRxRestart</a> handler function.</p>
</dd>

### -field <b>RxGetMpdusHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/195F4143-4889-4788-BAF5-2F1ED6E4E50A">MiniportWdiRxGetMpdus</a> handler function.</p>
</dd>

### -field <b>RxReturnFramesHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/BF2DB7C6-97F9-454B-8DED-E8CC21A4F07F">MiniportWdiRxReturnFrames</a> handler function.</p>
</dd>

### -field <b>RxResumeHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/483C59C3-8F9C-48A5-B5E4-34A60BAE1B1A">MiniportWdiRxResume</a> handler function.</p>
</dd>

### -field <b>RxThrottleHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/A5985C6D-3768-4ACE-B52B-3D3494334114">MiniportWdiRxThrottle</a> handler function.</p>
</dd>

### -field <b>RxPpduRssiHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/34C34C42-E5E1-44F6-AC81-ADC77206DED0">MiniportWdiRxPpduRssi</a> handler function.</p>
</dd>

### -field <b>TalTxRxStartHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/6F88F4B1-8D2A-41CC-8D60-C1CF91ED072A">MiniportWdiTalTxRxStart</a> handler function.</p>
</dd>

### -field <b>TalTxRxStopHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/21841DC6-B95F-4372-BBD1-EA195832A118">MiniportWdiTalTxRxStop</a> handler function.</p>
</dd>

### -field <b>TalTxRxAddPortHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/D3006A0B-B0E0-4FEA-864A-FA4B75594FB0">MiniportWdiTalTxRxAddPort</a> handler function.</p>
</dd>

### -field <b>TalTxRxDeletePortHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/3DB6AC6F-2A6F-43E1-B98D-B4E5C8A87845">MiniportWdiTalTxRxDeletePort</a> handler function.</p>
</dd>

### -field <b>TalTxRxSetPortOpModeHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/86F3005E-8BB3-4309-AFDE-7FA6E0427BFD">MiniportWdiTalTxRxSetPortOpMode</a> handler function.</p>
</dd>

### -field <b>TalTxRxResetPortHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/BB584FC9-8048-42F4-AFA9-7BF6790EDD69">MiniportWdiTalTxRxResetPort</a> handler function.</p>
</dd>

### -field <b>TalTxRxPeerConfigHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/48BB554D-A19E-46C0-8278-690A686A731D">MiniportWdiTalTxRxPeerConfig</a> handler function.</p>
</dd>

### -field <b>TalTxRxPeerDeleteConfirmHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/993C600F-E2FA-46D7-AE66-77048B481660">MiniportWdiTalTxRxPeerDeleteConfirm</a> handler function.</p>
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