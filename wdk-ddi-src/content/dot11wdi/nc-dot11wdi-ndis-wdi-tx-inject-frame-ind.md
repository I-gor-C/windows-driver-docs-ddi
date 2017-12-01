---
UID: NC.dot11wdi.NDIS_WDI_TX_INJECT_FRAME_IND
title: NDIS_WDI_TX_INJECT_FRAME_IND
author: windows-driver-content
description: The NdisWdiTxInjectFrameIndication callback function allows the LE to inject frames through the regular datapath (for example, authentication/association requests/responses, Wi-Fi Direct action frames).
old-location: netvista\ndiswditxinjectframeindication.htm
old-project: netvista
ms.assetid: C384FAFF-E22D-4FA2-8B11-F6C046003C70
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
req.alt-api: NdisWdiTxInjectFrameIndication
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

# NDIS_WDI_TX_INJECT_FRAME_IND callback



## -description
<p>The NdisWdiTxInjectFrameIndication callback function allows the LE to inject frames through the regular datapath (for example, authentication/association requests/responses, Wi-Fi Direct action frames).</p>
<p>This is a callback inside <a href="..\dot11wdi\ns-dot11wdi--ndis-wdi-data-api.md">NDIS_WDI_DATA_API</a>.</p>


## -prototype

````
NDIS_WDI_TX_INJECT_FRAME_IND NdisWdiTxInjectFrameIndication;

VOID NdisWdiTxInjectFrameIndication(
  _In_ NDIS_HANDLE               NdisMiniportDataPathHandle,
  _In_ WDI_PORT_ID               PortId,
  _In_ WDI_PEER_ID               PeerId,
  _In_ WDI_EXTENDED_TID          ExTid,
  _In_ PNET_BUFFER_LIST          pNBL,
  _In_ BOOLEAN                   bIsUnicast,
  _In_ BOOLEAN                   bUseLegacyRates,
  _In_ UINT16                    Ethertype,
  _In_ WDI_EXEMPTION_ACTION_TYPE ExemptionAction
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
<p>The port ID. </p>
</dd>

### -param <i>PeerId</i> [in]

<dd>
<p>The peer ID. When <b>TargetPriorityQueueing</b> is true, this must be set to the wildcard value.</p>
</dd>

### -param <i>ExTid</i> [in]

<dd>
<p>The extended TID.</p>
</dd>

### -param <i>pNBL</i> [in]

<dd>
<p>Pointer to a <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> chain.</p>
</dd>

### -param <i>bIsUnicast</i> [in]

<dd>
<p>Specifies if the frames are to a unicast receiver address.</p>
</dd>

### -param <i>bUseLegacyRates</i> [in]

<dd>
<p>Specifies if legacy rates should be used to send the frames.</p>
</dd>

### -param <i>Ethertype</i> [in]

<dd>
<p>Specifies the Ethertype of the frames.</p>
</dd>

### -param <i>ExemptionAction</i> [in]

<dd>
<p>Specifies the ExemptionAction of the frames.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

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
<a href="..\dot11wdi\ns-dot11wdi--ndis-wdi-data-api.md">NDIS_WDI_DATA_API</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="..\dot11wdi\ne-dot11wdi--wdi-exemption-action-type.md">WDI_EXEMPTION_ACTION_TYPE</a>
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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WDI_TX_INJECT_FRAME_IND callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
