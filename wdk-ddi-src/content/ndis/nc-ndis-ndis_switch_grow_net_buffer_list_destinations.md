---
UID: NC.ndis.NDIS_SWITCH_GROW_NET_BUFFER_LIST_DESTINATIONS
title: NDIS_SWITCH_GROW_NET_BUFFER_LIST_DESTINATIONS
author: windows-driver-content
description: The GrowNetBufferListDestinations function adds space for additional Hyper-V extensible switch destination ports to a packet that is specified by a NET_BUFFER_LIST structure.
old-location: netvista\grownetbufferlistdestinations.htm
old-project: netvista
ms.assetid: 9A79F41F-566F-4844-BF1A-E8889E6FDCE8
ms.author: windowsdriverdev
ms.date: 12/8/2017
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
---

# NDIS_SWITCH_GROW_NET_BUFFER_LIST_DESTINATIONS callback



## -description

The <i>GrowNetBufferListDestinations</i> function adds space for additional Hyper-V extensible switch destination ports to a packet that is specified by a <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure.



The <i>GrowNetBufferListDestinations</i> function adds space for additional Hyper-V extensible switch destination ports to a packet that is specified by a <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure.



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

### -param NdisSwitchContext [in]

An NDIS_SWITCH_CONTEXT value that contains the handle of the extensible switch module to which the Hyper-V extensible switch extension is attached. When the extension calls <a href="netvista.ndisfgetoptionalswitchhandlers">NdisFGetOptionalSwitchHandlers</a>,  this handle is returned through the <i>NdisSwitchContext</i> parameter.


### -param NetBufferLists [in, out]

A pointer to a linked list of <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures.  

<div class="alert"><b>Note</b>  This structure must contain  an extensible switch forwarding context. If the extension created or cloned the  packet, it must have previously allocated this structure by calling the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function. For more information about the extensible switch forwarding context, see <a href="netvista.hyper_v_extensible_switch_forwarding_context">Hyper-V Extensible Switch Forwarding Context</a>.</div>
<div> </div>

### -param NumberOfNewDestinations [in]

A UINT32 value that specifies the number of new destination ports to be  added for the packet.


### -param Destinations [out]

A pointer to an <a href="netvista.ndis_switch_forwarding_destination_array">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> structure. This structure specifies the extensible switch destination ports of the packet.


## -returns
If the call succeeds, the function returns NDIS_STATUS_SUCCESS. Otherwise, it returns an NDIS_STATUS_<i>Xxx</i> error code that is defined in Ndis.h.




## -remarks
The extensible switch extension calls the <i>GrowNetBufferListDestinations</i> function to add space for destination ports for a packet. Port destinations are specified through an <a href="netvista.ndis_switch_forwarding_destination_array">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> structure.

For more information on how to add destination ports to a packet, see <a href="netvista.adding_extensible_switch_destination_port_data_to_a_packet">Adding Extensible Switch Destination Port Data to a Packet</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported in NDIS 6.30 and later.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

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
<a href="netvista.ndis_switch_forwarding_destination_array">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a>
</dt>
<dt>
<a href="netvista.ndis_switch_port_destination">NDIS_SWITCH_PORT_DESTINATION</a>
</dt>
<dt>
<a href="netvista.ndisfgetoptionalswitchhandlers">NdisFGetOptionalSwitchHandlers</a>
</dt>
<dt>
<a href="netvista.net_buffer">NET_BUFFER</a>
</dt>
<dt>
<a href="netvista.net_buffer_list">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="netvista.UpdateNetBufferListDestinations">UpdateNetBufferListDestinations</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_GROW_NET_BUFFER_LIST_DESTINATIONS callback function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

