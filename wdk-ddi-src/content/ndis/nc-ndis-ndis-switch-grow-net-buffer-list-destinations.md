---
UID: NC.ndis.NDIS_SWITCH_GROW_NET_BUFFER_LIST_DESTINATIONS
title: NDIS_SWITCH_GROW_NET_BUFFER_LIST_DESTINATIONS
author: windows-driver-content
description: The GrowNetBufferListDestinations function adds space for additional Hyper-V extensible switch destination ports to a packet that is specified by a NET_BUFFER_LIST structure.
old-location: netvista\grownetbufferlistdestinations.htm
old-project: netvista
ms.assetid: 9A79F41F-566F-4844-BF1A-E8889E6FDCE8
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
req.alt-api: GrowNetBufferListDestinations
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

# NDIS_SWITCH_GROW_NET_BUFFER_LIST_DESTINATIONS callback



## -description
<p>
<p>The <i>GrowNetBufferListDestinations</i> function adds space for additional Hyper-V extensible switch destination ports to a packet that is specified by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>
</p>
<p>The <i>GrowNetBufferListDestinations</i> function adds space for additional Hyper-V extensible switch destination ports to a packet that is specified by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>


## -prototype

````
NDIS_SWITCH_GROW_NET_BUFFER_LIST_DESTINATIONS GrowNetBufferListDestinations;

NDIS_STATUS GrowNetBufferListDestinations(
  _In_    NDIS_SWITCH_CONTEXT                       NdisSwitchContext,
  _Inout_ PNET_BUFFER_LIST                          NetBufferLists,
  _In_    UINT32                                    NumberOfNewDestinations,
  _Out_   PNDIS_SWITCH_FORWARDING_DESTINATION_ARRAY *Destinations
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
<p>A pointer to a linked list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures.  </p>
<div class="alert"><b>Note</b>  This structure must contain  an extensible switch forwarding context. If the extension created or cloned the  packet, it must have previously allocated this structure by calling the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function. For more information about the extensible switch forwarding context, see <a href="NULL">Hyper-V Extensible Switch Forwarding Context</a>.</div>
<div> </div>
</dd>

### -param <i>NumberOfNewDestinations</i> [in]

<dd>
<p>A UINT32 value that specifies the number of new destination ports to be  added for the packet.</p>
</dd>

### -param <i>Destinations</i> [out]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> structure. This structure specifies the extensible switch destination ports of the packet.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns NDIS_STATUS_SUCCESS. Otherwise, it returns an NDIS_STATUS_<i>Xxx</i> error code that is defined in Ndis.h.

</p>

## -remarks
<p>The extensible switch extension calls the <i>GrowNetBufferListDestinations</i> function to add space for destination ports for a packet. Port destinations are specified through an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> structure.</p>

<p>For more information on how to add destination ports to a packet, see <a href="NULL">Adding Extensible Switch Destination Port Data to a Packet</a>.</p>

<p>The extensible switch extension calls the <i>GrowNetBufferListDestinations</i> function to add space for destination ports for a packet. Port destinations are specified through an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> structure.</p>

<p>For more information on how to add destination ports to a packet, see <a href="NULL">Adding Extensible Switch Destination Port Data to a Packet</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598224">NDIS_SWITCH_PORT_DESTINATION</a>
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
<dt>
<a href="netvista.UpdateNetBufferListDestinations">UpdateNetBufferListDestinations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_GROW_NET_BUFFER_LIST_DESTINATIONS callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
