---
UID: NC.dot11wdi.NDIS_WDI_RX_INORDER_DATA_IND
title: NDIS_WDI_RX_INORDER_DATA_IND
author: windows-driver-content
description: The NdisWdiRxInorderDataIndication callback function informs the RxMgr that a list of specified RX frames in the correct order are present.
old-location: netvista\ndiswdirxinorderdataindication.htm
ms.assetid: F2F92DAE-6C13-4EE6-9DE7-B77F5FAFAE60
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisWdiRxInorderDataIndication
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
ms.keywords: SYNTHVOICEPRIORITY_INSTANCE, SYNTHVOICEPRIORITY_INSTANCE, *PSYNTHVOICEPRIORITY_INSTANCE
req.iface: ISynthSinkDMus
---

# NDIS_WDI_RX_INORDER_DATA_IND callback



## -description
<p>The 
  NdisWdiRxInorderDataIndication callback function informs the RxMgr that a list of specified RX frames in the correct order are present.</p>
<p>This is a callback inside <a href="https://msdn.microsoft.com/library/windows/hardware/mt297620">NDIS_WDI_DATA_API</a>.</p>


## -prototype

````
NDIS_WDI_RX_INORDER_DATA_IND NdisWdiRxInorderDataIndication;

VOID NdisWdiRxInorderDataIndication(
  _In_  NDIS_HANDLE                       NdisMiniportDataPathHandle,
  _In_  WDI_RX_INDICATION_LEVEL           IndicationLevel,
  _In_  WDI_PEER_ID                       PeerId,
  _In_  WDI_EXTENDED_TID                  ExTid,
  _In_  PNDIS_RECEIVE_THROTTLE_PARAMETERS pRxThrottleParams,
  _Out_ NDIS_STATUS                       *pWifiStatus
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisMiniportDataPathHandle</i> [in]

<dd>
<p>The NdisMiniportDataPathHandle passed to the IHV miniport in <a href="https://msdn.microsoft.com/C297D681-D43F-4105-9E08-7FF42807E9A0">MiniportWdiTalTxRxInitialize</a>.</p>
</dd>

### -param <i>IndicationLevel</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn926110">WDI_RX_INDICATION_LEVEL</a> enumeration value that specifies the RX indication level.</p>
</dd>

### -param <i>PeerId</i> [in]

<dd>
<p>The peer ID.</p>
</dd>

### -param <i>ExTid</i> [in]

<dd>
<p>The extended TID.</p>
</dd>

### -param <i>pRxThrottleParams</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567241">NDIS_RECEIVE_THROTTLE_PARAMETERS</a> structure.</p>
</dd>

### -param <i>pWifiStatus</i> [out]

<dd>
<p>Status from WDI for the <i>NdisWdiRxInorderDataIndication</i>.  See the <i>Remarks</i> section for more information.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>The RxEngine uses WDI_RX_INDICATION_DISPATCH_FIRST_OF_DPC if this indication is the first data indication <b>NdisWdiRxInorderDataIndication</b>) of a DPC.  Subsequent data indications use WDI_RX_INDICATION_DISPATCH_GENERAL.  If indications are made at passive level, then the RxEngine must use WDI_RX_INDICATION_PASSIVE.  Indications made in the context of <a href="https://msdn.microsoft.com/483C59C3-8F9C-48A5-B5E4-34A60BAE1B1A">MiniportWdiRxResume</a> must use WDI_RX_INDICATION_FROM_RX_RESUME_FRAMES.  This parameter gives the RxMgr information necessary for limiting the lifetime of DPCs.</p>

<p>WDI_RX_INDICATION_FLAG_RESOURCES can be bitwise ORed with the other enum values to cause RxMgr to set NDIS_RECEIVE_FLAG_RESOURCES flags on the data indication.</p>

<p>The RxMgr issues  <a href="https://msdn.microsoft.com/195F4143-4889-4788-BAF5-2F1ED6E4E50A">MiniportWdiRxGetMpdus</a> requests to pull the received data.</p>

<p>If the target is not capable of RX frame classification and uses separate indications for  RX frames from different PeerID/TID pairs, the PeerID is set to a wildcard (0xFFFF) and TID is  set to WDI_EXT_TID_UNKNOWN.</p>

<p>In the case where the target/TAL takes full responsibility for reordering buffer management, it also performs all discard actions. No MPDU status is required.</p>

<p>PNDIS_RECEIVE_THROTTLE_PARAMETERS points to the <i>ReceiveThrottleParameters</i>, which is passed by NDIS for interrupts registered with NDIS.  This only needs to be set for WDI_RX_INDICATION_DISPATCH_FIRST_OF_DPC.  All other data indications should pass NULL, as this parameter is ignored.</p>

<p>If the RxMgr sets the WDI_STATUS to success, the RxEngine can create more data indications in the context of the same DPC.  If the RxMgr sets the WDI_STATUS to pause, the RxEngine must not create data indications until the RxMgr issues a <a href="https://msdn.microsoft.com/483C59C3-8F9C-48A5-B5E4-34A60BAE1B1A">MiniportWdiRxResume</a> and should exit dispatch level as soon as possible.</p>

<p>The RxEngine can choose how to handle incoming data while paused.  If possible, it should just buffer the data.  Dropping data is also acceptable.</p>

<p>The RxMgr tracks the number of frames indicated to NDIS against the limit specified in PNDIS_RECEIVE_THROTTLE_PARAMETERS. The RxMgr also tracks the time spent at dispatch.  When limits are reached, the RxMgr returns NDIS_STATUS_PAUSED.  The RxEngine should return/exit DPC as soon as possible, and must not indicate any more <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures (via <b>NdisWdiRxInorderDataIndication</b>) until RxMgr calls <a href="https://msdn.microsoft.com/483C59C3-8F9C-48A5-B5E4-34A60BAE1B1A">MiniportWdiRxResume</a>.  Any <b>NET_BUFFER_LIST</b> structures that are given to RxMgr (via <a href="https://msdn.microsoft.com/195F4143-4889-4788-BAF5-2F1ED6E4E50A">MiniportWdiRxGetMpdus</a>) and have not been indicated up yet are indicated up to NDIS in a different context to avoid spending too much time at DPC.  Once that backlog has been cleared, RxMgr unpauses the RxEngine by invoking  <i>MiniportWdiRxResume</i>.</p>

<p>The RxEngine uses WDI_RX_INDICATION_DISPATCH_FIRST_OF_DPC if this indication is the first data indication <b>NdisWdiRxInorderDataIndication</b>) of a DPC.  Subsequent data indications use WDI_RX_INDICATION_DISPATCH_GENERAL.  If indications are made at passive level, then the RxEngine must use WDI_RX_INDICATION_PASSIVE.  Indications made in the context of <a href="https://msdn.microsoft.com/483C59C3-8F9C-48A5-B5E4-34A60BAE1B1A">MiniportWdiRxResume</a> must use WDI_RX_INDICATION_FROM_RX_RESUME_FRAMES.  This parameter gives the RxMgr information necessary for limiting the lifetime of DPCs.</p>

<p>WDI_RX_INDICATION_FLAG_RESOURCES can be bitwise ORed with the other enum values to cause RxMgr to set NDIS_RECEIVE_FLAG_RESOURCES flags on the data indication.</p>

<p>The RxMgr issues  <a href="https://msdn.microsoft.com/195F4143-4889-4788-BAF5-2F1ED6E4E50A">MiniportWdiRxGetMpdus</a> requests to pull the received data.</p>

<p>If the target is not capable of RX frame classification and uses separate indications for  RX frames from different PeerID/TID pairs, the PeerID is set to a wildcard (0xFFFF) and TID is  set to WDI_EXT_TID_UNKNOWN.</p>

<p>In the case where the target/TAL takes full responsibility for reordering buffer management, it also performs all discard actions. No MPDU status is required.</p>

<p>PNDIS_RECEIVE_THROTTLE_PARAMETERS points to the <i>ReceiveThrottleParameters</i>, which is passed by NDIS for interrupts registered with NDIS.  This only needs to be set for WDI_RX_INDICATION_DISPATCH_FIRST_OF_DPC.  All other data indications should pass NULL, as this parameter is ignored.</p>

<p>If the RxMgr sets the WDI_STATUS to success, the RxEngine can create more data indications in the context of the same DPC.  If the RxMgr sets the WDI_STATUS to pause, the RxEngine must not create data indications until the RxMgr issues a <a href="https://msdn.microsoft.com/483C59C3-8F9C-48A5-B5E4-34A60BAE1B1A">MiniportWdiRxResume</a> and should exit dispatch level as soon as possible.</p>

<p>The RxEngine can choose how to handle incoming data while paused.  If possible, it should just buffer the data.  Dropping data is also acceptable.</p>

<p>The RxMgr tracks the number of frames indicated to NDIS against the limit specified in PNDIS_RECEIVE_THROTTLE_PARAMETERS. The RxMgr also tracks the time spent at dispatch.  When limits are reached, the RxMgr returns NDIS_STATUS_PAUSED.  The RxEngine should return/exit DPC as soon as possible, and must not indicate any more <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures (via <b>NdisWdiRxInorderDataIndication</b>) until RxMgr calls <a href="https://msdn.microsoft.com/483C59C3-8F9C-48A5-B5E4-34A60BAE1B1A">MiniportWdiRxResume</a>.  Any <b>NET_BUFFER_LIST</b> structures that are given to RxMgr (via <a href="https://msdn.microsoft.com/195F4143-4889-4788-BAF5-2F1ED6E4E50A">MiniportWdiRxGetMpdus</a>) and have not been indicated up yet are indicated up to NDIS in a different context to avoid spending too much time at DPC.  Once that backlog has been cleared, RxMgr unpauses the RxEngine by invoking  <i>MiniportWdiRxResume</i>.</p>

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
<a href="https://msdn.microsoft.com/195F4143-4889-4788-BAF5-2F1ED6E4E50A">MiniportWdiRxGetMpdus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/483C59C3-8F9C-48A5-B5E4-34A60BAE1B1A">MiniportWdiRxResume</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567241">NDIS_RECEIVE_THROTTLE_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297640">WDI_EXTENDED_TID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297658">WDI_PEER_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn926110">WDI_RX_INDICATION_LEVEL</a>
</dt>
<dt>
<a href="NULL">WDI RX path</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WDI_RX_INORDER_DATA_IND callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
