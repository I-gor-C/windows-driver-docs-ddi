---
UID: NC.dot11wdi.NDIS_WDI_TX_DEQUEUE_IND
title: NDIS_WDI_TX_DEQUEUE_IND
author: windows-driver-content
description: The NdisWdiTxDequeueIndication callback function is called in the context of a MiniportWdiTxDataSend or MiniportWdiTxTalSend by the IHV miniport to dequeue frames from WDI to the IHV miniport.
old-location: netvista\ndiswditxdequeueindication.htm
old-project: netvista
ms.assetid: ACCB45DA-1233-4276-A0F5-466E50D9377B
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: SYNTHVOICEPRIORITY_INSTANCE, SYNTHVOICEPRIORITY_INSTANCE, *PSYNTHVOICEPRIORITY_INSTANCE
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
req.alt-api: NdisWdiTxDequeueIndication
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
req.irql: 
req.iface: ISynthSinkDMus
---

# NDIS_WDI_TX_DEQUEUE_IND callback



## -description
<p>The 
  NdisWdiTxDequeueIndication callback function is called in the context of a <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-data-send.md">MiniportWdiTxDataSend</a> or <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-tal-send.md">MiniportWdiTxTalSend</a> by the IHV miniport to dequeue frames from WDI to the IHV miniport.</p>
<p>This is a callback inside <a href="..\dot11wdi\ns-dot11wdi--ndis-wdi-data-api.md">NDIS_WDI_DATA_API</a>.</p>


## -prototype

````
NDIS_WDI_TX_DEQUEUE_IND NdisWdiTxDequeueIndication;

VOID NdisWdiTxDequeueIndication(
  _In_  NDIS_HANDLE      NdisMiniportDataPathHandle,
  _In_  UINT32           Quantum,
  _In_  UINT8            MaxNumFrames,
  _In_  UINT16           Credit,
  _Out_ PNET_BUFFER_LIST *ppNBL
)
{ ... }
````


## -parameters
<dl>

### -param NdisMiniportDataPathHandle [in]

<dd>
<p>The NdisMiniportDataPathHandle passed to the IHV miniport in <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-initialize.md">MiniportWdiTalTxRxInitialize</a>.</p>
</dd>

### -param Quantum [in]

<dd>
<p>The quantum. For more information, see the <i>Host - target TX transfer scheduling</i> section in <a href="netvista.wdi_tx_path">WDI TX path</a>.</p>
</dd>

### -param MaxNumFrames [in]

<dd>
<p>Maximum frame count.</p>
</dd>

### -param Credit [in]

<dd>
<p>Credit value. For more information, see <i>The target-credit scheme and the pause/resume mechanism</i> section in <a href="netvista.wdi_tx_path">WDI TX path</a>.</p>
</dd>

### -param ppNBL [out]

<dd>
<p>Pointer to a pointer to a <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> chain dequeued by WDI.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>A subset of the parameters may not be applicable to a device. For instance, the maximum frame count may not apply to a store and forward device (message-based bus interface).</p>

<p>The following parameters are ignored by TxMgr under these circumstances.</p>

<p>The TAL should provide accurate parameters whenever possible to guarantee fairness and avoid overwhelming TIL/target resources.  </p>

<p>If the TAL does not have enough credit to dequeue a maximum cost frame, it should issue an <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-send-pause-ind.md">NdisWdiTxSendPauseIndication</a> instead of an <i>NdisWdiTxDequeueIndication</i>.</p>

<p>The TxMgr may return a list of <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> that exceed the limit of the number of frames, frame cost, or quantum. This only happens if the frames are being requeued/replayed after being send completed with status of Postponed and with identical sequence number, which indicates they were originally transmitted as part of a single A-MSDU.</p>

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
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dot11wdi\ns-dot11wdi--ndis-wdi-data-api.md">NDIS_WDI_DATA_API</a>
</dt>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-dequeue-ind.md">NdisWdiTxDequeueIndication</a>
</dt>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-send-pause-ind.md">NdisWdiTxSendPauseIndication</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="netvista.wdi_tx_path">WDI TX path</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WDI_TX_DEQUEUE_IND callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
