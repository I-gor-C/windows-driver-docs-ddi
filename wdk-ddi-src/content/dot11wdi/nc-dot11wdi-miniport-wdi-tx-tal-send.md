---
UID: NC.dot11wdi.MINIPORT_WDI_TX_TAL_SEND
title: MINIPORT_WDI_TX_TAL_SEND
author: windows-driver-content
description: The MiniportWdiTxTalSend handler function specifies an RA-TID or port queue to transmit from.
old-location: netvista\miniportwditxtalsend.htm
old-project: netvista
ms.assetid: 42489ADA-78BF-4EBF-A6EC-5484F82C46ED
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: MiniportWdiTxTalSend
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

# MINIPORT_WDI_TX_TAL_SEND callback



## -description
<p>The 
  MiniportWdiTxTalSend handler function specifies an RA-TID or port queue to transmit from.  The TxMgr uses this request instead of  <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-data-send.md">MiniportWdiTxDataSend</a> for RA-TID queues with an extended TID in the IHV reserved range. It is issued in the context of a TX thread from the operating system, resume indication, or a work item.</p>
<p>This is a WDI miniport handler inside <a href="..\dot11wdi\ns-dot11wdi--ndis-miniport-wdi-data-handlers.md">NDIS_MINIPORT_WDI_DATA_HANDLERS</a>.</p>


## -prototype

````
MINIPORT_WDI_TX_TAL_SEND MiniportWdiTxTalSend;

VOID MiniportWdiTxTalSend(
  _In_ TAL_TXRX_HANDLE  MiniportTalTxRxContext,
  _In_ WDI_PORT_ID      PortId,
  _In_ WDI_PEER_ID      PeerId,
  _In_ WDI_EXTENDED_TID ExTid,
  _In_ UINT16           NumQueueFrames,
  _In_ UINT32           NumActiveFrames,
  _In_ BOOLEAN          bRobustnessFlag
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
<p>The port ID.</p>
</dd>

### -param <i>PeerId</i> [in]

<dd>
<p>The peer ID.</p>
</dd>

### -param <i>ExTid</i> [in]

<dd>
<p>The Extended TID.</p>
</dd>

### -param <i>NumQueueFrames</i> [in]

<dd>
<p>The queue length, in frames.</p>
</dd>

### -param <i>NumActiveFrames</i> [in]

<dd>
<p>The total number of frames in action (schedulable) queues.</p>
</dd>

### -param <i>bRobustnessFlag</i> [in]

<dd>
<p>The robustness flag. If the robustness flag is set to TRUE, the NIC ensures reliable delivery within a small number of retries by aggressively lowering the TX data rate used for the frame using CTS and/or other mechanisms.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>In port queuing mode, <i>PeerId</i> and <i>ExTid</i> are set to wildcards.
In the context of the send request, the TxEngine issues <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-dequeue-ind.md">NdisWdiTxDequeueIndication</a> to take ownership of a number of frames from the FIFO RA-TID queue and transfer them to the target. If it cannot dequeue any frames, the TxEngine issues <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-send-pause-ind.md">NdisWdiTxSendPauseIndication</a> in the same context instead of <i>NdisWdiTxDequeueIndication</i>.</p>

<p>The TxEngine must issue a transfer complete and send complete indications to return ownership of any frames it dequeues to TxMgr.  If the transfer complete contains a failure code, the TxEngine must not issue a send completion.</p>

<p><i>PeerId</i> is set to wildcard if the port is configured as an access point/Wi-Fi Direct Group Owner and the frame has a group address as the receiver address.</p>

<p>On failure, the TxEngine completes the frame transfers to the target with the appropriate failure status.</p>

<p>To define a MiniportWdiTxTalSend function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a MiniportWdiTxTalSend function that is named "MyTxTalSend", use the <b>MINIPORT_WDI_TX_TAL_SEND</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_WDI_TX_TAL_SEND</b> function type is defined in the dot11wdi.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_WDI_TX_TAL_SEND</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

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
<a href="..\dot11wdi\ns-dot11wdi--ndis-miniport-wdi-data-handlers.md">NDIS_MINIPORT_WDI_DATA_HANDLERS</a>
</dt>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tx-data-send.md">MiniportWdiTxDataSend</a>
</dt>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-dequeue-ind.md">NdisWdiTxDequeueIndication</a>
</dt>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-tx-send-pause-ind.md">NdisWdiTxSendPauseIndication</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297625">TAL_TXRX_HANDLE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297640">WDI_EXTENDED_TID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297658">WDI_PEER_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt269099">WDI_PORT_ID</a>
</dt>
<dt>
<a href="NULL">WDI TX path</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_WDI_TX_TAL_SEND callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
