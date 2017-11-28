---
UID: NS.ntddndis._NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD
title: NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD
author: windows-driver-content
description: The NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD structure contains the offload support state for receive segment coalescing (RSC).
old-location: netvista\ndis_tcp_recv_seg_coalesce_offload.htm
old-project: netvista
ms.assetid: F474ABFA-D811-4C03-868A-E7C23BAE2017
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD, NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD, *PNDIS_TCP_RECV_SEG_COALESCE_OFFLOAD
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD
req.alt-loc: Ntddndis.h
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
req.iface: 
---

# NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD structure



## -description
<p>The <b>NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD</b>  structure contains the offload support state for receive segment coalescing (RSC).</p>


## -syntax

````
typedef struct _NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD {
  struct {
    BOOLEAN Enabled;
  } IPv4;
  struct {
    BOOLEAN Enabled;
  } IPv6;
} NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD, *PNDIS_TCP_RECV_SEG_COALESCE_OFFLOAD;
````


## -struct-fields
<dl>

### -field <b>IPv4</b>

<dd>
<dl>

### -field <b>Enabled</b>

<dd>
<p>A BOOLEAN value that is set to TRUE if RSC processing on IPv4 traffic is supported. Otherwise, this member is FALSE.</p>
</dd>
</dl>
</dd>

### -field <b>IPv6</b>

<dd>
<dl>

### -field <b>Enabled</b>

<dd>
<p>A BOOLEAN value that is set to TRUE if RSC processing on IPv6 traffic is supported. Otherwise, this member is FALSE.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>A miniport driver advertises support for receive segment coalescing (RSC) in the Rsc member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566599">NDIS_OFFLOAD</a> structure that it passes to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a> function. </p>

<p>The miniport driver can set the <b>IPv4.Enabled</b> member or the <b>IPv6.Enabled</b> member or both in the <b>NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD</b> structure to TRUE if it supports RSC for these protocols. The miniport driver must support RSC for 802.3 encapsulation or greater, and can support any other encapsulations. If the miniport driver does not support RSC for some encapsulation, the received packets of that encapsulation type must be indicated up the stack normally. </p>

<p>To determine if a miniport driver supports RSC, NDIS drivers and other applications can query the  <a href="https://msdn.microsoft.com/library/windows/hardware/ff569806">OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES</a> OID which returns the NDIS_OFFLOAD structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566599">NDIS_OFFLOAD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569806">OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
