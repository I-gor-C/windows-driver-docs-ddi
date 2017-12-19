---
UID: NC.ndis.NDIS_SWITCH_ADD_NET_BUFFER_LIST_DESTINATION
title: NDIS_SWITCH_ADD_NET_BUFFER_LIST_DESTINATION
author: windows-driver-content
description: The AddNetBufferListDestination function adds a single destination port for a packet that is specified by a NET_BUFFER_LIST structure.
old-location: netvista\AddNetBufferListDestination.htm
old-project: NetVista
ms.assetid: 6B8CD868-D2F4-4892-BF6D-DFD7A3984320
ms.author: windowsdriverdev
ms.date: 12/14/2017
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
req.alt-api: AddNetBufferListDestination
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

# NDIS_SWITCH_ADD_NET_BUFFER_LIST_DESTINATION callback



## -description
The <i>AddNetBufferListDestination</i> function adds a single destination port for a packet that is specified by a <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure.



## -prototype

````
NDIS_SWITCH_ADD_NET_BUFFER_LIST_DESTINATION AddNetBufferListDestination;

NDIS_STATUS AddNetBufferListDestination(
  _In_    NDIS_SWITCH_CONTEXT           NdisSwitchContext,
  _Inout_ PNET_BUFFER_LIST              NetBufferList,
  _In_    PNDIS_SWITCH_PORT_DESTINATION Destination
)
{ ... }
````


## -parameters

### -param NdisSwitchContext [in]

An NDIS_SWITCH_CONTEXT value that contains the handle of the extensible switch module to which the Hyper-V extensible switch extension is attached. When the extension calls <a href="netvista.ndisfgetoptionalswitchhandlers">NdisFGetOptionalSwitchHandlers</a>,  this handle is returned through the <i>NdisSwitchContext</i> parameter.


### -param NetBufferList [in, out]

A pointer to a <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure for a packet. 

<div class="alert"><b>Note</b>  This structure must contain  an extensible switch forwarding context. If the extension created or cloned the  packet, it must have previously allocated this structure by calling the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function.</div>
<div> </div>

### -param Destination [in]

A pointer to an <a href="netvista.ndis_switch_port_destination">NDIS_SWITCH_PORT_DESTINATION</a> structure. This structure specifies the destination extensible switch port that the packet will be forwarded to.


## -returns
If the call succeeds, the function returns NDIS_STATUS_SUCCESS. Otherwise, it returns an NDIS_STATUS_<i>Xxx</i> error code that is defined in Ndis.h.




## -remarks
The forwarding extensible switch extension calls <i>AddNetBufferListDestination</i> to define a single extensible switch destination port for a packet. The extension specifies this port by initializing an   <a href="netvista.ndis_switch_port_destination">NDIS_SWITCH_PORT_DESTINATION</a> structure. The extension sets the <i>Destination</i> parameter to a pointer to this structure. For more information on how to specify an extensible switch destination port, see <a href="netvista.managing_hyper_v_extensible_switch_destination_port_data">Managing Hyper-V Extensible Switch Destination Port Data</a>.

The extension must follow these guidelines before it calls <i>AddNetBufferListDestination</i>:

Only forwarding extensions can call <i>AddNetBufferListDestination</i> to add a destination port for a packet. For more information on this type of extension, see <a href="netvista.forwarding_extensions">Forwarding Extensions</a>.

If the forwarding extension is originating a packet with one destination port, the extension must first call the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function. This function allocates the extensible switch forwarding context for the packet. This data contains the extensible switch source and destination ports within the out-of-band (OOB) information for the packet.

For more information about this context, see <a href="netvista.hyper_v_extensible_switch_forwarding_context">Hyper-V Extensible Switch Forwarding Context</a>.

After the extension modifies the destination port information in the <a href="netvista.ndis_switch_port_destination">NDIS_SWITCH_PORT_DESTINATION</a> structure, it calls <i>AddNetBufferListDestination</i> to commit the changes to the <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure for the packet.


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
<a href="netvista.GetNetBufferListDestinations">GetNetBufferListDestinations</a>
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
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NDIS_SWITCH_ADD_NET_BUFFER_LIST_DESTINATION callback function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

