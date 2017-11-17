---
UID: NC.ndis.NDIS_SWITCH_SET_NET_BUFFER_LIST_SOURCE
title: NDIS_SWITCH_SET_NET_BUFFER_LIST_SOURCE
author: windows-driver-content
description: The SetNetBufferListSource function sets the Hyper-V extensible switch source port identifier and network adapter index for a packet that is specified by a NET_BUFFER_LIST structure.
old-location: netvista\setnetbufferlistsource.htm
ms.assetid: 6537824A-F521-4916-AAC8-7C0E6E5F7331
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetNetBufferListSource
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: RxNameCacheInitialize
req.iface: 
---

# NDIS_SWITCH_SET_NET_BUFFER_LIST_SOURCE callback



## -description
<p>
<p>The <i>SetNetBufferListSource</i> function sets the Hyper-V extensible switch source port identifier and network adapter index for a packet that is specified by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>
</p>
<p>The <i>SetNetBufferListSource</i> function sets the Hyper-V extensible switch source port identifier and network adapter index for a packet that is specified by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>


## -prototype

````
NDIS_SWITCH_SET_NET_BUFFER_LIST_SOURCE SetNetBufferListSource;

NDIS_STATUS SetNetBufferListSource(
  _In_    NDIS_SWITCH_CONTEXT   NdisSwitchContext,
  _Inout_ PNET_BUFFER_LIST      NetBufferLists,
  _In_    NDIS_SWITCH_PORT_ID   PortId,
  _In_    NDIS_SWITCH_NIC_INDEX NicIndex
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisSwitchContext</i> [in]

<dd>
<p>An NDIS_SWITCH_CONTEXT value that contains the handle of the extensible switch module to which the Hyper-V extensible switch extension is attached. When the extension calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>,  this handle is returned through the <i>NdisSwitchContext</i> parameter.</p>
</dd>

### -param <i>NetBufferLists</i> [in, out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure for a single packet.  </p>
<div class="alert"><b>Note</b>  This structure must contain  an extensible switch forwarding context that was previously allocated by calling the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function. For more information about the extensible switch forwarding context, see <a href="NULL">Hyper-V Extensible Switch Forwarding Context</a>.</div>
<div> </div>
</dd>

### -param <i>PortId</i> [in]

<dd>
<p>An NDIS_SWITCH_PORT_ID value that specifies the unique identifier of the source port on the extensible switch.</p>
</dd>

### -param <i>NicIndex</i> [in]

<dd>
<p>An NDIS_SWITCH_NIC_INDEX value that specifies the index of the network adapter that is connected to the extensible switch port specified by the <i>PortId</i> parameter.</p>
<p>For more information on NDIS_SWITCH_NIC_INDEX values, see <a href="NULL">Network Adapter Index Values</a>.

</p>
<div class="alert"><b>Note</b>  This parameter must specify the index value of a network adapter that is in a connected state. Index values for network adapters that are in a created or disconnected state cannot be specified. For more information about network connection states, see <a href="NULL">Hyper-V Extensible Switch Port and Network Adapter States</a>.</div>
<div> </div>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns NDIS_STATUS_SUCCESS. Otherwise, it returns an NDIS_STATUS_<i>Xxx</i> error code that is defined in Ndis.h.

</p>

## -remarks
<p>The extensible switch extension calls the <i>SetNetBufferListSource</i> function to set the source port identifier and network adapter index in a packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. The extension does this for the following types of packets:</p>

<p>A new packet that the extension has allocated for send or receive operations.</p>

<p>A duplicated packet that the extension had cloned from an original packet that it was filtering. The extension duplicates a packet by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff560705">NdisAllocateCloneNetBufferList</a>.</p>

<p>In both cases, a new or duplicated packet will have its source port identifier set to <b>NDIS_SWITCH_DEFAULT_PORT_ID</b> and its source network adapter index set to <b>NDIS_SWITCH_DEFAULT_NIC_INDEX</b>. The extension  calls the <i>SetNetBufferListSource</i> function to change the source port identifier and network adapter index in a packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>

<p>For example, a packet that has a source port identifier of <b>NDIS_SWITCH_DEFAULT_PORT_ID</b> is trusted and bypasses many extensible switch port policies. These policies include access control lists (ACLs) and quality of service (QoS). If the extension specifies a non-default source port for the packet, this allows the policies for that port to be applied to the packet.</p>

<p>For more information on packet send and receive operations, see <a href="NULL">Filter Module Send and Receive Operations</a>.</p>

<p>The extensible switch extension calls the <i>SetNetBufferListSource</i> function to set the source port identifier and network adapter index in a packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. The extension does this for the following types of packets:</p>

<p>A new packet that the extension has allocated for send or receive operations.</p>

<p>A duplicated packet that the extension had cloned from an original packet that it was filtering. The extension duplicates a packet by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff560705">NdisAllocateCloneNetBufferList</a>.</p>

<p>In both cases, a new or duplicated packet will have its source port identifier set to <b>NDIS_SWITCH_DEFAULT_PORT_ID</b> and its source network adapter index set to <b>NDIS_SWITCH_DEFAULT_NIC_INDEX</b>. The extension  calls the <i>SetNetBufferListSource</i> function to change the source port identifier and network adapter index in a packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>

<p>For example, a packet that has a source port identifier of <b>NDIS_SWITCH_DEFAULT_PORT_ID</b> is trusted and bypasses many extensible switch port policies. These policies include access control lists (ACLs) and quality of service (QoS). If the extension specifies a non-default source port for the packet, this allows the policies for that port to be applied to the packet.</p>

<p>For more information on packet send and receive operations, see <a href="NULL">Filter Module Send and Receive Operations</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560705">NdisAllocateCloneNetBufferList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_SET_NET_BUFFER_LIST_SOURCE callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
