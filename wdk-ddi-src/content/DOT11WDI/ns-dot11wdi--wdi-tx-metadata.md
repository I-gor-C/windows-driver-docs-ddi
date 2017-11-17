---
UID: NS.dot11wdi._WDI_TX_METADATA
title: WDI_TX_METADATA
author: windows-driver-content
description: The WDI_TX_METADATA structure defines the TX metadata.
old-location: netvista\wdi_tx_metadata.htm
ms.assetid: 21833980-0098-43c2-822c-9d8292f7120a
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_TX_METADATA
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
ms.keywords: WDI_TX_METADATA, WDI_TX_METADATA, *PWDI_TX_METADATA
req.iface: 
---

# WDI_TX_METADATA structure



## -description
<p>The 
  WDI_TX_METADATA structure defines the TX metadata.</p>


## -syntax

````
typedef struct _WDI_TX_METADATA {
  WDI_PORT_ID               PortID;
  WDI_PEER_ID               PeerID;
  WDI_EXTENDED_TID          ExTID;
  BOOLEAN                   IsUnicast;
  BOOLEAN                   bAllowLegacyRates;
  UINT16                    Ethertype;
  BOOLEAN                   bTxCompleteRequired;
  UINT8                     PnLength;
  UINT16                    TxCost;
  WDI_EXEMPTION_ACTION_TYPE ExemptionAction;
  WDI_TXRX_MPDU_PN          MpduPn;
  UINT64                    ReplayIHVReserved0;
  UINT64                    ReplayIHVReserved1;
  UINT16                    SeqCtl;
  UINT16                    wPad;
} WDI_TX_METADATA, *PWDI_TX_METADATA;
````


## -struct-fields
<dl>

### -field <b>PortID</b>

<dd>
<p>Port ID of the frame.</p>
</dd>

### -field <b>PeerID</b>

<dd>
<p>Peer ID of the frame (only if <b>TargetPriorityQueueing</b> is false).</p>
</dd>

### -field <b>ExTID</b>

<dd>
<p>Extended TID of the frame (only if <b>TargetPriorityQueueing</b> is false).</p>
</dd>

### -field <b>IsUnicast</b>

<dd>
<p>Specifies if the frame is for a unicast recipient address.</p>
</dd>

### -field <b>bAllowLegacyRates</b>

<dd>
<p>Specifies if legacy rates should be used for transmitting the frame.</p>
</dd>

### -field <b>Ethertype</b>

<dd>
<p>Specifies the Ethertype of the frame.</p>
</dd>

### -field <b>bTxCompleteRequired</b>

<dd>
<p>Specifies if an <a href="https://msdn.microsoft.com/A38BA15D-FDD8-41D1-87ED-2CABC1926962">NdisWdiTxSendCompleteIndication</a> is required for this frame.</p>
</dd>

### -field <b>PnLength</b>

<dd>
<p>Specifies the PnLength for the frame. This is only applicable to Requeued/Replayed TX frames.  Otherwise, set to zero.</p>
</dd>

### -field <b>TxCost</b>

<dd>
<p>Specifies the number of credits required to dequeue the frame.</p>
</dd>

### -field <b>ExemptionAction</b>

<dd>
<p>Specifies the <a href="https://msdn.microsoft.com/library/windows/hardware/dn897820">WDI_EXEMPTION_ACTION_TYPE</a> value for this frame.</p>
</dd>

### -field <b>MpduPn</b>

<dd>
<p>Specifies the MpduPn for the frame. This is only applicable to Requeued/Replayed TX frames.  Otherwise, set to zero.</p>
</dd>

### -field <b>ReplayIHVReserved0</b>

<dd>
<p>Reserved for use by the IHV miniport for Requeued/Replayed TX frames. This is only applicable to Requeued/Replayed TX frames.  Otherwise, set to zero.  </p>
</dd>

### -field <b>ReplayIHVReserved1</b>

<dd>
<p>Reserved for use by the IHV miniport for Requeued/Replayed TX frames. This is only applicable to Requeued/Replayed TX frames.  Otherwise, set to zero.  </p>
</dd>

### -field <b>SeqCtl</b>

<dd>
<p>Specifies the SeqCtl (if necessary). This is only applicable to Requeued/Replayed TX frames.  Otherwise, set to zero.</p>
</dd>

### -field <b>wPad</b>

<dd>
<p>Reserved.</p>
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
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn897820">WDI_EXEMPTION_ACTION_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn898187">WDI_TXRX_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WDI_TX_METADATA structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
