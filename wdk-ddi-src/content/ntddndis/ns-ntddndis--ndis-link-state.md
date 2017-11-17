---
UID: NS.ntddndis._NDIS_LINK_STATE
title: NDIS_LINK_STATE
author: windows-driver-content
description: The NDIS_LINK_STATE structure specifies the current link state of a miniport adapter.
old-location: netvista\ndis_link_state.htm
ms.assetid: 01d74e69-55fe-4e2e-94ab-7676f9e33403
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_LINK_STATE
req.alt-loc: ntddndis.h
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
ms.keywords: NDIS_LINK_STATE, NDIS_LINK_STATE, *PNDIS_LINK_STATE
req.iface: 
---

# NDIS_LINK_STATE structure



## -description
<p>The <b>NDIS_LINK_STATE</b> structure specifies the current link state of a miniport adapter.</p>


## -syntax

````
typedef struct _NDIS_LINK_STATE {
  NDIS_OBJECT_HEADER             Header;
  NDIS_MEDIA_CONNECT_STATE       MediaConnectState;
  NDIS_MEDIA_DUPLEX_STATE        MediaDuplexState;
  ULONG64                        XmitLinkSpeed;
  ULONG64                        RcvLinkSpeed;
  NDIS_SUPPORTED_PAUSE_FUNCTIONS PauseFunctions;
  ULONG                          AutoNegotiationFlags;
} NDIS_LINK_STATE, *PNDIS_LINK_STATE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
 <b>NDIS_LINK_STATE</b> structure. Set the 
      <b>Type</b> member of the structure that 
      <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
      <b>Revision</b> member to NDIS_LINK_STATE_REVISION_1, and the 
      <b>Size</b> member to NDIS_SIZEOF_LINK_STATE_REVISION_1.</p>
</dd>

### -field <b>MediaConnectState</b>

<dd>
<p>The media connect state for the miniport adapter. For more information, see  
      <a href="netvista.oid_gen_media_connect_status_ex">
 OID_GEN_MEDIA_CONNECT_STATUS_EX</a> OID.</p>
</dd>

### -field <b>MediaDuplexState</b>

<dd>
<p>The media duplex state for the miniport adapter. For more information, see <a href="netvista.oid_gen_media_duplex_state">
 OID_GEN_MEDIA_DUPLEX_STATE</a> OID.</p>
</dd>

### -field <b>XmitLinkSpeed</b>

<dd>
<p>The current transmit link speed of the miniport adapter in bits per second. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff569594">OID_GEN_LINK_SPEED_EX</a>.
 </p>
<div class="alert"><b>Note</b>  A value of NDIS_LINK_SPEED_UNKNOWN indicates that the
 transmit link speed is unknown.</div>
<div> </div>
</dd>

### -field <b>RcvLinkSpeed</b>

<dd>
<p>The current receive link speed of the miniport adapter in bits per second. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff569594">OID_GEN_LINK_SPEED_EX</a>.

 </p>
<div class="alert"><b>Note</b>  A value of NDIS_LINK_SPEED_UNKNOWN indicates that the
 receive link speed is unknown.</div>
<div> </div>
</dd>

### -field <b>PauseFunctions</b>

<dd>
<p>The type of support for the IEEE 802.3 pause frames. This member must be one of the following
 pause functions:
      </p>
<p></p>
<dl>

### -field <a id="NdisPauseFunctionsUnsupported"></a><a id="ndispausefunctionsunsupported"></a><a id="NDISPAUSEFUNCTIONSUNSUPPORTED"></a><b>NdisPauseFunctionsUnsupported</b>

<dd>
<p>the miniport adapter or link partner does not support pause frames.</p>
</dd>

### -field <a id="NdisPauseFunctionsSendOnly"></a><a id="ndispausefunctionssendonly"></a><a id="NDISPAUSEFUNCTIONSSENDONLY"></a><b>NdisPauseFunctionsSendOnly</b>

<dd>
<p>the miniport adapter and link partner support only sending pause frames from the miniport adapter to the link
 partner.</p>
</dd>

### -field <a id="NdisPauseFunctionsReceiveOnly"></a><a id="ndispausefunctionsreceiveonly"></a><a id="NDISPAUSEFUNCTIONSRECEIVEONLY"></a><b>NdisPauseFunctionsReceiveOnly</b>

<dd>
<p>the miniport adapter and link partner support only sending pause frames from the link partner to the miniport adapter</p>
</dd>

### -field <a id="NdisPauseFunctionsSendAndReceive"></a><a id="ndispausefunctionssendandreceive"></a><a id="NDISPAUSEFUNCTIONSSENDANDRECEIVE"></a><b>NdisPauseFunctionsSendAndReceive</b>

<dd>
<p>the miniport adapter and link partner support sending and receiving pause frames in both transmit and
 receive directions.</p>
</dd>

### -field <a id="NdisPauseFunctionsUnknown"></a><a id="ndispausefunctionsunknown"></a><a id="NDISPAUSEFUNCTIONSUNKNOWN"></a><b>NdisPauseFunctionsUnknown</b>

<dd>
<p>Pause frame negotiation is in progress. The pause frame support that the link partner provides
 is unknown.</p>
</dd>
</dl>
</dd>

### -field <b>AutoNegotiationFlags</b>

<dd>
<p>The auto-negotiation settings for the miniport adapter. This member is created from a bitwise OR
 of the following flags:
      </p>
<p></p>
<dl>

### -field <a id="NDIS_LINK_STATE_XMIT_LINK_SPEED_AUTO_NEGOTIATED"></a><a id="ndis_link_state_xmit_link_speed_auto_negotiated"></a>NDIS_LINK_STATE_XMIT_LINK_SPEED_AUTO_NEGOTIATED

<dd>
<p>the miniport adapter has auto-negotiated the transmit link speed with the link partner.</p>
</dd>

### -field <a id="NDIS_LINK_STATE_RCV_LINK_SPEED_AUTO_NEGOTIATED"></a><a id="ndis_link_state_rcv_link_speed_auto_negotiated"></a>NDIS_LINK_STATE_RCV_LINK_SPEED_AUTO_NEGOTIATED

<dd>
<p>the miniport adapter has auto-negotiated the receive link speed with the link partner.</p>
</dd>

### -field <a id="NDIS_LINK_STATE_DUPLEX_AUTO_NEGOTIATED"></a><a id="ndis_link_state_duplex_auto_negotiated"></a>NDIS_LINK_STATE_DUPLEX_AUTO_NEGOTIATED

<dd>
<p>the miniport adapter has auto-negotiated the duplex state with the link partner.</p>
</dd>

### -field <a id="NDIS_LINK_STATE_PAUSE_FUNCTIONS_AUTO_NEGOTIATED"></a><a id="ndis_link_state_pause_functions_auto_negotiated"></a>NDIS_LINK_STATE_PAUSE_FUNCTIONS_AUTO_NEGOTIATED

<dd>
<p>the miniport adapter has auto-negotiated the pause functions with the link partner.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>Miniport drivers use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567391">NDIS_STATUS_LINK_STATE</a> status indication to notify NDIS and overlying drivers that there has been a change in the physical characteristics of a medium.

When it generates this status indication, the driver sets the 
    <b>StatusBuffer</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff567373">NDIS_STATUS_INDICATION</a> structure to a pointer to an <b>NDIS_LINK_STATE</b> structure.</p>

<p>The miniport driver also returns an <b>NDIS_LINK_STATE</b> structure when it handles an OID query request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569595">OID_GEN_LINK_STATE</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567373">NDIS_STATUS_INDICATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567391">NDIS_STATUS_LINK_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569594">OID_GEN_LINK_SPEED_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569595">OID_GEN_LINK_STATE</a>
</dt>
<dt>
<a href="netvista.oid_gen_media_connect_status_ex">
 OID_GEN_MEDIA_CONNECT_STATUS_EX</a>
</dt>
<dt>
<a href="netvista.oid_gen_media_duplex_state">
 OID_GEN_MEDIA_DUPLEX_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_LINK_STATE structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
