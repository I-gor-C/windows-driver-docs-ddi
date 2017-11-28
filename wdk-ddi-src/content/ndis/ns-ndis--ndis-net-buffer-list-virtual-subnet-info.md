---
UID: NS.ndis._NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO
title: NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO
author: windows-driver-content
description: Defines the group network virtualization information for a network buffer list (NBL).
old-location: netvista\ndis_net_buffer_list_virtual_subnet_info.htm
old-project: netvista
ms.assetid: E87F9FC0-D408-43D2-A09F-F921617CF3DA
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO, NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO, *PNDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO structure



## -description
<p>Defines the group network virtualization information for a network buffer list (NBL).</p>


## -syntax

````
typedef struct _NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO {
  union {
    struct {
      UINT32 VirtualSubnetId  :32;
      UINT32 ReservedVsidBits  :8;
      UINT32 Reserved;
    };
    PVOID  Value;
  };
} NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO, *PNDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO;
````


## -struct-fields
<dl>

### -field ( <i>unnamed struct</i> )

<dd>
<p>A member in the union that is contained in <b>NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO</b>. Ethernet
      miniport drivers use 
      this member to access the originating virtual switch port ID for the network buffer list. 
      This member is a bit field with the following members:</p>
<dl>

### -field <b>VirtualSubnetId</b>

<dd>
<p>The originating virtual switch port ID for the network buffer list.</p>
</dd>

### -field <b>ReservedVsidBits</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>
</dl>
</dd>

### -field <b>Value</b>

<dd>
<p>A member in the union that is contained in <b>NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO</b>. 
      <b>Value</b> contains a pointer value that is type-compatible with the 
      <b>NetBufferListInfo</b> member in the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. (See the <b>VirtualSubnetInfo</b> constant in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566569">NDIS_NET_BUFFER_LIST_INFO</a> enumeration.)</p>
</dd>
</dl>

## -remarks
<p>This structure is used in the <b>NetBufferListInfo</b> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>

<p>In NDIS 6.40 (Windows Server 2012 R2) and later, a <b>VirtualSubnetId</b> can be configured on a VM network adapter port as an external virtual subnet to support a third-party network virtualization solution. A Hyper-V extensible Switch forwarding extension may then modify the packet headers, as required, during forwarding. Packets that are being modified must be cloned, and their <b>ParentNetBufferList</b> pointers must be set to the original NBL.</p>

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
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="NULL">Cloning Packet Traffic</a>
</dt>
<dt>
<a href="NULL">Forwarding Extensions</a>
</dt>
<dt>
<a href="NULL">Overview of the Hyper-V Extensible Switch</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383677">NDIS_ISOLATION_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566569">NDIS_NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
