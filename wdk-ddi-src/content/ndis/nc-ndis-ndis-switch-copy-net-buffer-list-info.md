---
UID: NC.ndis.NDIS_SWITCH_COPY_NET_BUFFER_LIST_INFO
title: NDIS_SWITCH_COPY_NET_BUFFER_LIST_INFO
author: windows-driver-content
description: The Hyper-V extensible switch extension calls the CopyNetBufferListInfo function to copy the out-of-band (OOB) forwarding context from a source packet's NET_BUFFER_LIST structure to a destination packet's NET_BUFFER_LIST structure.
old-location: netvista\CopyNetBufferListInfo.htm
old-project: netvista
ms.assetid: 5CC345FA-C3EF-4122-8E9C-6EA27B20DD5A
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CopyNetBufferListInfo
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
req.iface: 
---

# NDIS_SWITCH_COPY_NET_BUFFER_LIST_INFO callback



## -description
<p>
<p>The Hyper-V extensible switch extension calls the <i>CopyNetBufferListInfo</i> function to copy the out-of-band (OOB) forwarding context from a source packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure to a destination packet's <b>NET_BUFFER_LIST</b> structure. This context includes the extensible switch source port and network adapter information. The extensible switch destination port information can also be copied.</p>
</p>
<p>The Hyper-V extensible switch extension calls the <i>CopyNetBufferListInfo</i> function to copy the out-of-band (OOB) forwarding context from a source packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure to a destination packet's <b>NET_BUFFER_LIST</b> structure. This context includes the extensible switch source port and network adapter information. The extensible switch destination port information can also be copied.</p>


## -prototype

````
NDIS_SWITCH_COPY_NET_BUFFER_LIST_INFO CopyNetBufferListInfo;

NDIS_STATUS CopyNetBufferListInfo(
  _In_    NDIS_SWITCH_CONTEXT NdisSwitchContext,
  _Inout_ PNET_BUFFER_LIST    DestNetBufferList,
  _In_    PNET_BUFFER_LIST    SrcNetBufferList,
  _In_    UINT32              Flags
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisSwitchContext</i> [in]

<dd>
<p>An NDIS_SWITCH_CONTEXT value that contains the handle of the extensible switch module to which the extension is attached. When the extension calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>,  this handle is returned through the <i>NdisSwitchContext</i> parameter.</p>
</dd>

### -param <i>DestNetBufferList</i> [in, out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure for the destination packet to which the extensible switch forwarding context is copied.  </p>
</dd>

### -param <i>SrcNetBufferList</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure for the source packet from which the extensible switch forwarding context is copied. </p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A UINT32 value. When the NDIS_SWITCH_COPY_NBL_INFO_FLAGS_PRESERVE_DESTINATIONS flag is specified, the function copies the extensible switch destination ports from the source packet to the destination packet.</p>
<p>The data that is contained within the source packet's <a href="https://msdn.microsoft.com/library/windows/hardware/hh598211">NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO</a> union is always copied to the extensible switch forwarding context in the destination packet. This data includes the source port identifiers and index of the network adapter connection from which the packet originated. Depending on the number of extensible switch destination ports that are copied to the destination packet, the NumAvailableDestinations member of the <b>NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO</b> union is updated in the destination packet.</p>
<p>For more information about the forwarding context, see <a href="NULL">Hyper-V Extensible Switch Forwarding Context</a>.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns NDIS_STATUS_SUCCESS. Otherwise, it returns an NDIS_STATUS_<i>Xxx</i> error code that is defined in Ndis.h.

</p>

## -remarks
<p>The extensible switch extension calls the <i>CopyNetBufferListInfo</i> function to copy the OOB data from a source packet to a destination packet. This data includes the following:</p>

<p>The data from the <b>NetBufferListInfo</b> array of the source packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh598211">NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO</a> data from the source packet's extensible switch forwarding context.</p>

<p>The data for the extensible switch destination ports from the source packet's extensible switch forwarding context.</p>

<p>Before the extension calls <i>CopyNetBufferListInfo</i>, it must prepare the destination packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure by following these steps:</p>

<p>The extension must first initialize a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure for the destination packet that is derived from the source packet's  <b>NET_BUFFER_LIST</b> structure. </p>

<p>For example, the extension can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560705">NdisAllocateCloneNetBufferList</a> to create a complete copy of the source packet. The extension can also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560707">NdisAllocateFragmentNetBufferList</a> to create a copy of only a fragment of the source packet. For more information, see <a href="netvista.derived_net_buffer_list_structures">Derived NET_BUFFER_LIST Structures</a>.</p>

<p>The extensible switch extension calls the <i>CopyNetBufferListInfo</i> function to copy the OOB data from a source packet to a destination packet. This data includes the following:</p>

<p>The data from the <b>NetBufferListInfo</b> array of the source packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh598211">NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO</a> data from the source packet's extensible switch forwarding context.</p>

<p>The data for the extensible switch destination ports from the source packet's extensible switch forwarding context.</p>

<p>Before the extension calls <i>CopyNetBufferListInfo</i>, it must prepare the destination packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure by following these steps:</p>

<p>The extension must first initialize a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure for the destination packet that is derived from the source packet's  <b>NET_BUFFER_LIST</b> structure. </p>

<p>For example, the extension can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560705">NdisAllocateCloneNetBufferList</a> to create a complete copy of the source packet. The extension can also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560707">NdisAllocateFragmentNetBufferList</a> to create a copy of only a fragment of the source packet. For more information, see <a href="netvista.derived_net_buffer_list_structures">Derived NET_BUFFER_LIST Structures</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560707">NdisAllocateFragmentNetBufferList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598211">NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_COPY_NET_BUFFER_LIST_INFO callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
