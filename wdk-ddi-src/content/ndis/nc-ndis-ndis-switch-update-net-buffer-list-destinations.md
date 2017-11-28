---
UID: NC.ndis.NDIS_SWITCH_UPDATE_NET_BUFFER_LIST_DESTINATIONS
title: NDIS_SWITCH_UPDATE_NET_BUFFER_LIST_DESTINATIONS
author: windows-driver-content
description: The Hyper-V extensible switch extension calls the UpdateNetBufferListDestinations function to commit modifications that the extension made to a packet that contains multiple extensible switch destination ports.
old-location: netvista\UpdateNetBufferListDestinations.htm
old-project: netvista
ms.assetid: 9A740524-0FC1-4585-8059-F678D4777F66
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
req.alt-api: UpdateNetBufferListDestinations
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

# NDIS_SWITCH_UPDATE_NET_BUFFER_LIST_DESTINATIONS callback



## -description
<p>
<p>The Hyper-V extensible switch extension calls the <i>UpdateNetBufferListDestinations</i> function to commit modifications that the extension made to a packet that contains multiple extensible switch destination ports. The function saves these modifications to the out-of-band (OOB) extensible switch forwarding context of the packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. </p>
</p>
<p>The Hyper-V extensible switch extension calls the <i>UpdateNetBufferListDestinations</i> function to commit modifications that the extension made to a packet that contains multiple extensible switch destination ports. The function saves these modifications to the out-of-band (OOB) extensible switch forwarding context of the packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. </p>


## -prototype

````
NDIS_SWITCH_UPDATE_NET_BUFFER_LIST_DESTINATIONS UpdateNetBufferListDestinations;

NDIS_STATUS UpdateNetBufferListDestinations(
  _In_    NDIS_SWITCH_CONTEXT                       NdisSwitchContext,
  _Inout_ PNET_BUFFER_LIST                          NetBufferList,
  _In_    UINT32                                    NumberOfNewDestinations,
  _In_    PNDIS_SWITCH_FORWARDING_DESTINATION_ARRAY Destinations
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisSwitchContext</i> [in]

<dd>
<p>An NDIS_SWITCH_CONTEXT value that contains the handle of the extensible switch module to which the Hyper-V extensible switch extension is attached. When the extension calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>,  this handle is returned through the <i>NdisSwitchContext</i> parameter.</p>
</dd>

### -param <i>NetBufferList</i> [in, out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure for a single packet.</p>
<div class="alert"><b>Note</b>  This structure must contain  an extensible switch forwarding context. If the extension created or cloned the  packet, it must have previously allocated this structure by calling the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function.</div>
<div> </div>
</dd>

### -param <i>NumberOfNewDestinations</i> [in]

<dd>
<p>A UINT32 value that specifies the number of new destination ports that were added to the packet.</p>
</dd>

### -param <i>Destinations</i> [in]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> structure. This structure specifies the extensible switch destination ports of the packet.</p>
<div class="alert"><b>Note</b>  The extension received this structure through a previous call to the <a href="netvista.GetNetBufferListDestinations">GetNetBufferListDestinations</a> function.</div>
<div> </div>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns NDIS_STATUS_SUCCESS. Otherwise, it returns an NDIS_STATUS_<i>Xxx</i> error code that is defined in Ndis.h.

</p>

## -remarks
<p>The extensible switch extension calls the <a href="netvista.GetNetBufferListDestinations">GetNetBufferListDestinations</a> function to obtain an array of the extensible switch destination ports for a packet. If the function returns successfully, the array is obtained through the <i>Destinations</i> parameter, which contains a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> structure. Each element in this array is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598224">NDIS_SWITCH_PORT_DESTINATION</a> structure that specifies a destination port for the packet.</p>

<p>After the extension obtains the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> structure, the extension can do the following:</p>

<p>Add additional <a href="https://msdn.microsoft.com/library/windows/hardware/hh598224">NDIS_SWITCH_PORT_DESTINATION</a> elements in the array.</p>

<p>For more information, see <a href="NULL">Adding Extensible Switch Destination Port Data to a Packet</a>.</p>

<p>Modify existing <a href="https://msdn.microsoft.com/library/windows/hardware/hh598224">NDIS_SWITCH_PORT_DESTINATION</a> elements of the array to exclude a packet from being forwarded to a specified port.</p>

<p>For more information, see <a href="NULL">Excluding Packet Delivery to Extensible Switch Destination Ports</a>.</p>

<p>If the extension adds or modifies destination ports in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> structure, the extension must call the <i>UpdateNetBufferListDestinations</i> function to commit those changes to the packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>

<p>If the call to <i>UpdateNetBufferListDestinations</i> returns NDIS_STATUS_SUCCESS, the extensible switch interface guarantees that the extensible switch port and network adapter connection that are referenced in the destination ports will not be deleted until the packet's send or receive operation is completed. </p>

<p>Also, after the changes for destination ports have been committed, destination ports cannot be removed, and only the <b>IsExcluded</b>  member of a destination port's <a href="https://msdn.microsoft.com/library/windows/hardware/hh598224">NDIS_SWITCH_PORT_DESTINATION</a> structure can be changed. For more information, see <a href="NULL">Excluding Packet Delivery to Extensible Switch Destination Ports</a>.</p>

<p>For more information about the extensible switch forwarding context, see <a href="NULL">Hyper-V Extensible Switch Forwarding Context</a>.</p>

<p>The extensible switch extension calls the <a href="netvista.GetNetBufferListDestinations">GetNetBufferListDestinations</a> function to obtain an array of the extensible switch destination ports for a packet. If the function returns successfully, the array is obtained through the <i>Destinations</i> parameter, which contains a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> structure. Each element in this array is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598224">NDIS_SWITCH_PORT_DESTINATION</a> structure that specifies a destination port for the packet.</p>

<p>After the extension obtains the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> structure, the extension can do the following:</p>

<p>Add additional <a href="https://msdn.microsoft.com/library/windows/hardware/hh598224">NDIS_SWITCH_PORT_DESTINATION</a> elements in the array.</p>

<p>For more information, see <a href="NULL">Adding Extensible Switch Destination Port Data to a Packet</a>.</p>

<p>Modify existing <a href="https://msdn.microsoft.com/library/windows/hardware/hh598224">NDIS_SWITCH_PORT_DESTINATION</a> elements of the array to exclude a packet from being forwarded to a specified port.</p>

<p>For more information, see <a href="NULL">Excluding Packet Delivery to Extensible Switch Destination Ports</a>.</p>

<p>If the extension adds or modifies destination ports in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> structure, the extension must call the <i>UpdateNetBufferListDestinations</i> function to commit those changes to the packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>

<p>If the call to <i>UpdateNetBufferListDestinations</i> returns NDIS_STATUS_SUCCESS, the extensible switch interface guarantees that the extensible switch port and network adapter connection that are referenced in the destination ports will not be deleted until the packet's send or receive operation is completed. </p>

<p>Also, after the changes for destination ports have been committed, destination ports cannot be removed, and only the <b>IsExcluded</b>  member of a destination port's <a href="https://msdn.microsoft.com/library/windows/hardware/hh598224">NDIS_SWITCH_PORT_DESTINATION</a> structure can be changed. For more information, see <a href="NULL">Excluding Packet Delivery to Extensible Switch Destination Ports</a>.</p>

<p>For more information about the extensible switch forwarding context, see <a href="NULL">Hyper-V Extensible Switch Forwarding Context</a>.</p>

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
<a href="netvista.GetNetBufferListDestinations">GetNetBufferListDestinations</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598224">NDIS_SWITCH_PORT_DESTINATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561830">NdisFOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598264">OID_SWITCH_NIC_DELETE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_UPDATE_NET_BUFFER_LIST_DESTINATIONS callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
