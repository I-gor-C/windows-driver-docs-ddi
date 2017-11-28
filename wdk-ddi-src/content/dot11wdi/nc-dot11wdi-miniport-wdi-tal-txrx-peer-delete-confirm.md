---
UID: NC.dot11wdi.MINIPORT_WDI_TAL_TXRX_PEER_DELETE_CONFIRM
title: MINIPORT_WDI_TAL_TXRX_PEER_DELETE_CONFIRM
author: windows-driver-content
description: The MiniportWdiTalTxRxPeerDeleteConfirm handler function is invoked after the completion of a PeerDeleteIndication call which did not return success.
old-location: netvista\miniportwditaltxrxpeerdeleteconfirm.htm
old-project: netvista
ms.assetid: 993C600F-E2FA-46D7-AE66-77048B481660
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
req.alt-api: MiniportWdiTalTxRxPeerDeleteConfirm
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

# MINIPORT_WDI_TAL_TXRX_PEER_DELETE_CONFIRM callback



## -description
<p>The 
  MiniportWdiTalTxRxPeerDeleteConfirm handler function is invoked after the completion of a  <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-peer-delete-ind.md">PeerDeleteIndication</a> call which did not return success.  This is called after a successful <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-abort.md">MiniportWdiTxAbort</a> (or <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-abort-confirm.md">TxAbortConfirm</a>) and after all outstanding TX frames for the peer are completed.  After this call, the mapping between the peer Id and MAC address is no longer valid and the peer Id and MAC address may be used for future <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-peer-create-ind.md">PeerCreateIndication</a> calls.</p>
<p>This is a WDI miniport handler inside <a href="https://msdn.microsoft.com/library/windows/hardware/mt297618">NDIS_MINIPORT_WDI_DATA_HANDLERS</a>.</p>


## -prototype

````
MINIPORT_WDI_TAL_TXRX_PEER_DELETE_CONFIRM MiniportWdiTalTxRxPeerDeleteConfirm;

VOID MiniportWdiTalTxRxPeerDeleteConfirm(
  _In_ TAL_TXRX_HANDLE MiniportTalTxRxContext,
  _In_ WDI_PORT_ID     PortId,
  _In_ WDI_PEER_ID     PeerId
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportTalTxRxContext</i> [in]

<dd>
<p>TAL device handle returned by the IHV miniport in <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-initialize.md">MiniportWdiTalTxRxInitialize</a>.</p>
</dd>

### -param <i>PortId</i> [in]

<dd>
<p>Port ID associated with the peer.</p>
</dd>

### -param <i>PeerId</i> [in]

<dd>
<p>Peer ID for the peer.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

<p>To define a MiniportWdiTalTxRxPeerDeleteConfirm function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a MiniportWdiTalTxRxPeerDeleteConfirm function that is named "MyTalTxRxPeerDeleteConfirm", use the <b>MINIPORT_WDI_TAL_TXRX_PEER_DELETE_CONFIRM</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_WDI_TAL_TXRX_PEER_DELETE_CONFIRM</b> function type is defined in the dot11wdi.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_WDI_TAL_TXRX_PEER_DELETE_CONFIRM</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

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
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297618">NDIS_MINIPORT_WDI_DATA_HANDLERS</a>
</dt>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-abort.md">MiniportWdiTxAbort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297625">TAL_TXRX_HANDLE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297658">WDI_PEER_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt269099">WDI_PORT_ID</a>
</dt>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-peer-create-ind.md">PeerCreateIndication</a>
</dt>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-peer-delete-ind.md">PeerDeleteIndication</a>
</dt>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-abort-confirm.md">TxAbortConfirm</a>
</dt>
<dt>
<a href="NULL">WDI general datapath interfaces</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_WDI_TAL_TXRX_PEER_DELETE_CONFIRM callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
