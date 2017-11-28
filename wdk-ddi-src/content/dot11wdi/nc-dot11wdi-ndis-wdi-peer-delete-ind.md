---
UID: NC.dot11wdi.NDIS_WDI_PEER_DELETE_IND
title: NDIS_WDI_PEER_DELETE_IND
author: windows-driver-content
description: The NdisWdiPeerDeleteIndication callback function initiates the removal of the association of between a peer ID and a peer MAC address.
old-location: netvista\ndiswdipeerdeleteindication.htm
old-project: netvista
ms.assetid: A13F2A98-BADA-43B8-A24B-0749C5558C35
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: NdisWdiPeerDeleteIndication
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

# NDIS_WDI_PEER_DELETE_IND callback



## -description
<p>The 
  NdisWdiPeerDeleteIndication callback function initiates the removal of the association of between a peer ID and a peer MAC address. Once this indication is processed, the peer ID can no longer be used  in subsequent Rx indications and the IHV may not inject any Tx frames for this peer.</p>
<p>This is a callback inside <a href="https://msdn.microsoft.com/library/windows/hardware/mt297620">NDIS_WDI_DATA_API</a>.</p>


## -prototype

````
NDIS_WDI_PEER_DELETE_IND NdisWdiPeerDeleteIndication;

VOID NdisWdiPeerDeleteIndication(
  _In_  NDIS_HANDLE NdisMiniportDataPathHandle,
  _In_  WDI_PORT_ID PortId,
  _In_  WDI_PEER_ID PeerId,
  _Out_ NDIS_STATUS *pWifiStatus
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisMiniportDataPathHandle</i> [in]

<dd>
<p>The NdisMiniportDataPathHandle passed to IHV miniport in <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-initialize.md">MiniportWdiTalTxRxInitialize</a>.</p>
</dd>

### -param <i>PortId</i> [in]

<dd>
<p>The port ID.</p>
</dd>

### -param <i>PeerId</i> [in]

<dd>
<p>The peer ID.</p>
</dd>

### -param <i>pWifiStatus</i> [out]

<dd>
<p>Indicates whether the peer deletion completed synchronously (if status is set to <b>NDIS_STATUS_SUCCESS</b>), or whether WDI will issue a <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-peer-delete-confirm.md">MiniportWdiTalTxRxPeerDeleteConfirm</a> when peer deletion completes.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>In PeerQueueing mode, the TxMgr issues a TxAbort for the peer.  If the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-abort.md">MiniportWdiTxAbort</a> completes synchronously and there are no outstanding TX frames for that peer, WDI_STATUS is set to NDIS_STATUS_SUCCESS and the peer deletion is complete (see <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-peer-delete-confirm.md">MiniportWdiTalTxRxPeerDeleteConfirm</a> for  the description of a peer delete completion).  Otherwise, WDI issues a <i>MiniportWdiTalTxRxPeerDeleteConfirm</i> when the TxAbort is completed and there are no outstanding frames for this peer.</p>

<p>In PeerQueueing mode, the TxMgr issues a TxAbort for the peer.  If the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-abort.md">MiniportWdiTxAbort</a> completes synchronously and there are no outstanding TX frames for that peer, WDI_STATUS is set to NDIS_STATUS_SUCCESS and the peer deletion is complete (see <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-peer-delete-confirm.md">MiniportWdiTalTxRxPeerDeleteConfirm</a> for  the description of a peer delete completion).  Otherwise, WDI issues a <i>MiniportWdiTalTxRxPeerDeleteConfirm</i> when the TxAbort is completed and there are no outstanding frames for this peer.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297620">NDIS_WDI_DATA_API</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297618">NDIS_MINIPORT_WDI_DATA_HANDLERS</a>
</dt>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-peer-delete-confirm.md">MiniportWdiTalTxRxPeerDeleteConfirm</a>
</dt>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-abort.md">MiniportWdiTxAbort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297658">WDI_PEER_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt269099">WDI_PORT_ID</a>
</dt>
<dt>
<a href="NULL">WDI general datapath interfaces</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WDI_PEER_DELETE_IND callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
