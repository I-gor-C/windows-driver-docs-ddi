---
UID: NC.dot11wdi.NDIS_WDI_TX_QUERY_RA_TID_STATE
title: NDIS_WDI_TX_QUERY_RA_TID_STATE
author: windows-driver-content
description: The NdisWdiTxQueryRATIDState callback function is used by the TxEngine to query the state of a RA/TID or Port queue.
old-location: netvista\ndiswditxqueryratidstate.htm
old-project: netvista
ms.assetid: 76949336-3349-4869-83C7-60D7D8A6BE24
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
req.alt-api: NdisWdiTxQueryRATIDState
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

# NDIS_WDI_TX_QUERY_RA_TID_STATE callback



## -description
<p>The NdisWdiTxQueryRATIDState callback function is used by the TxEngine to query the state of a RA/TID or Port queue.</p>
<p>This is a callback inside <a href="..\dot11wdi\ns-dot11wdi--ndis-wdi-data-api.md">NDIS_WDI_DATA_API</a>.</p>


## -prototype

````
NDIS_WDI_TX_QUERY_RA_TID_STATE NdisWdiTxQueryRATIDState;

VOID NdisWdiTxQueryRATIDState(
  _In_  NDIS_HANDLE      NdisMiniportDataPathHandle,
  _In_  WDI_PORT_ID      PortId,
  _In_  WDI_PEER_ID      PeerId,
  _In_  WDI_EXTENDED_TID ExTid,
  _Out_ NDIS_STATUS      *pWifiStatus,
  _Out_ PUINT16          pQueueLength
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisMiniportDataPathHandle</i> [in]

<dd>
<p>The NdisMiniportDataPathHandle passed to the IHV miniport in <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-initialize.md">MiniportWdiTalTxRxInitialize</a>.</p>
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
<p>The Extended Traffic ID (TID)</p>
</dd>

### -param <i>pWifiStatus</i> [out]

<dd>
<p>Indicates the result of the query operation.  See the <i>Remarks</i> section for more information.</p>
</dd>

### -param <i>pQueueLength</i> [out]

<dd>
<p>The number of backlogged frames in the specified RA/TID  or Port queue.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>The TxMgr returns a success status if the port and peer are valid. Otherwise, it returns an error status.  In the case of a success status, the <i>QueueLength</i> is set to the number of backlogged frames in the specified RA/TID  or Port queue.</p>

<p>If <b>TargetPriorityQueueing</b> is true, <a href="https://msdn.microsoft.com/library/windows/hardware/mt297658">WDI_PEER_ID</a> must be set to the wildcard peer value.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297640">WDI_EXTENDED_TID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297658">WDI_PEER_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt269099">WDI_PORT_ID</a>
</dt>
<dt>
<a href="netvista.wdi_txrx_capabilities">WDI_TXRX_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WDI_TX_QUERY_RA_TID_STATE callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
