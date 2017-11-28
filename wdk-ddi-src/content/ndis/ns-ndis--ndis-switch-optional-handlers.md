---
UID: NS.ndis._NDIS_SWITCH_OPTIONAL_HANDLERS
title: NDIS_SWITCH_OPTIONAL_HANDLERS
author: windows-driver-content
description: The NDIS_SWITCH_OPTIONAL_HANDLERS structure specifies the pointers to the Hyper-V extensible switch handler functions. These functions can be called by an extensible switch extension.
old-location: netvista\ndis_switch_optional_handlers.htm
old-project: netvista
ms.assetid: aa8367c7-8366-4601-8c2a-4d96df5cfcd8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_SWITCH_OPTIONAL_HANDLERS, NDIS_SWITCH_OPTIONAL_HANDLERS, *PNDIS_SWITCH_OPTIONAL_HANDLERS
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
req.alt-api: NDIS_SWITCH_OPTIONAL_HANDLERS
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
req.irql: See Remarks section
req.iface: 
---

# NDIS_SWITCH_OPTIONAL_HANDLERS structure



## -description
<p>The <b>NDIS_SWITCH_OPTIONAL_HANDLERS</b> structure specifies the pointers to the Hyper-V extensible switch handler functions. These functions can be called by an extensible switch extension.</p>


## -syntax

````
typedef struct _NDIS_SWITCH_OPTIONAL_HANDLERS {
  NDIS_OBJECT_HEADER                                              Header;
  NDIS_SWITCH_ALLOCATE_NET_BUFFER_LIST_FORWARDING_CONTEXT_HANDLER AllocateNetBufferListForwardingContext;
  NDIS_SWITCH_FREE_NET_BUFFER_LIST_FORWARDING_CONTEXT_HANDLER     FreeNetBufferListForwardingContext;
  NDIS_SWITCH_SET_NET_BUFFER_LIST_SOURCE_HANDLER                  SetNetBufferListSource;
  NDIS_SWITCH_ADD_NET_BUFFER_LIST_DESTINATION_HANDLER             AddNetBufferListDestination;
  NDIS_SWITCH_GROW_NET_BUFFER_LIST_DESTINATIONS_HANDLER           GrowNetBufferListDestinations;
  NDIS_SWITCH_GET_NET_BUFFER_LIST_DESTINATIONS_HANDLER            GetNetBufferListDestinations;
  NDIS_SWITCH_UPDATE_NET_BUFFER_LIST_DESTINATIONS_HANDLER         UpdateNetBufferListDestinations;
  NDIS_SWITCH_COPY_NET_BUFFER_LIST_INFO_HANDLER                   CopyNetBufferListInfo;
  NDIS_SWITCH_REFERENCE_SWITCH_NIC_HANDLER                        ReferenceSwitchNic;
  NDIS_SWITCH_DEREFERENCE_SWITCH_NIC_HANDLER                      DereferenceSwitchNic;
  NDIS_SWITCH_REFERENCE_SWITCH_PORT_HANDLER                       ReferenceSwitchPort;
  NDIS_SWITCH_DEREFERENCE_SWITCH_PORT_HANDLER                     DereferenceSwitchPort;
  NDIS_SWITCH_REPORT_FILTERED_NET_BUFFER_LISTS_HANDLER            ReportFilteredNetBufferLists;
} NDIS_SWITCH_OPTIONAL_HANDLERS, *PNDIS_SWITCH_OPTIONAL_HANDLERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_SWITCH_OPTIONAL_HANDLERS</b> structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The <b>Type</b> member of <b>Header</b> must be set to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_SWITCH_OPTIONAL_HANDLERS</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_SWITCH_OPTIONAL_HANDLERS_REVISION_1"></a><a id="ndis_switch_optional_handlers_revision_1"></a>NDIS_SWITCH_OPTIONAL_HANDLERS_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NDIS_SWITCH_NIC_ARRAY_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>AllocateNetBufferListForwardingContext</b>

<dd>
<p>A pointer to the <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> function.</p>
</dd>

### -field <b>FreeNetBufferListForwardingContext</b>

<dd>
<p>A pointer to the <a href="netvista.FreeNetBufferListForwardingContext">FreeNetBufferListForwardingContext</a> function.</p>
</dd>

### -field <b>SetNetBufferListSource</b>

<dd>
<p>A pointer to the <a href="..\ndis\nc-ndis-ndis-switch-set-net-buffer-list-source.md">SetNetBufferListSource</a> function.</p>
</dd>

### -field <b>AddNetBufferListDestination</b>

<dd>
<p>A pointer to the <a href="netvista.AddNetBufferListDestination">AddNetBufferListDestination</a> function.</p>
</dd>

### -field <b>GrowNetBufferListDestinations</b>

<dd>
<p>A pointer to the <a href="..\ndis\nc-ndis-ndis-switch-grow-net-buffer-list-destinations.md">GrowNetBufferListDestinations</a> function.</p>
</dd>

### -field <b>GetNetBufferListDestinations</b>

<dd>
<p>A pointer to the <a href="netvista.GetNetBufferListDestinations">GetNetBufferListDestinations</a> function.</p>
</dd>

### -field <b>UpdateNetBufferListDestinations</b>

<dd>
<p>A pointer to the <a href="netvista.UpdateNetBufferListDestinations">UpdateNetBufferListDestinations</a> function.</p>
</dd>

### -field <b>CopyNetBufferListInfo</b>

<dd>
<p>A pointer to the <a href="netvista.CopyNetBufferListInfo">CopyNetBufferListInfo</a> function.</p>
</dd>

### -field <b>ReferenceSwitchNic</b>

<dd>
<p>A pointer to the <a href="netvista.ReferenceSwitchNic">ReferenceSwitchNic</a> function.</p>
</dd>

### -field <b>DereferenceSwitchNic</b>

<dd>
<p>A pointer to the <a href="netvista.DereferenceSwitchNic">DereferenceSwitchNic</a> function.</p>
</dd>

### -field <b>ReferenceSwitchPort</b>

<dd>
<p>A pointer to the <a href="netvista.ReferenceSwitchPort">ReferenceSwitchPort</a> function.</p>
</dd>

### -field <b>DereferenceSwitchPort</b>

<dd>
<p>A pointer to the <a href="netvista.DereferenceSwitchPort">DereferenceSwitchPort</a> function.</p>
</dd>

### -field <b>ReportFilteredNetBufferLists</b>

<dd>
<p>A pointer to the <a href="..\ndis\nc-ndis-ndis-switch-report-filtered-net-buffer-lists.md">ReportFilteredNetBufferLists</a> function.</p>
</dd>
</dl>

## -remarks
<p>The extensible switch handler functions provide support for filtering and forwarding actions that are performed by an extensible switch extension. These actions include the following:</p>

<p>
<ul>
<li>
<p>Allocate or free  the forwarding context. This data is stored in the out-of-band (OOB) data of a packet's  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. For more information about the forwarding context, see <a href="NULL">Hyper-V Extensible Switch Forwarding Context</a>.</p>
</li>
<li>
<p>Get or set the destination ports that are contained in a packet's forwarding context.</p>
</li>
<li>
<p>Add destination ports to a packet's forwarding context.</p>
</li>
</ul>
</p>

<p>Allocate or free  the forwarding context. This data is stored in the out-of-band (OOB) data of a packet's  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. For more information about the forwarding context, see <a href="NULL">Hyper-V Extensible Switch Forwarding Context</a>.</p>

<p>Get or set the destination ports that are contained in a packet's forwarding context.</p>

<p>Add destination ports to a packet's forwarding context.</p>

<p>When the extensible switch extension calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>, the <i>NdisSwitchHandlers</i> parameter contains a pointer to an  <b>NDIS_SWITCH_OPTIONAL_HANDLERS</b> structure. An extensible switch extension typically calls <b>NdisFGetOptionalSwitchHandlers</b> from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a> function.</p>

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
<dt><b></b></dt>
<dt>
<a href="netvista.AddNetBufferListDestination">AddNetBufferListDestination</a>
</dt>
<dt>
<a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a>
</dt>
<dt>
<a href="netvista.CopyNetBufferListInfo">CopyNetBufferListInfo</a>
</dt>
<dt>
<a href="netvista.DereferenceSwitchNic">DereferenceSwitchNic</a>
</dt>
<dt>
<a href="netvista.DereferenceSwitchPort">DereferenceSwitchPort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a>
</dt>
<dt>
<a href="netvista.FreeNetBufferListForwardingContext">FreeNetBufferListForwardingContext</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-ndis-switch-grow-net-buffer-list-destinations.md">GrowNetBufferListDestinations</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="netvista.ReferenceSwitchNic">ReferenceSwitchNic</a>
</dt>
<dt>
<a href="netvista.ReferenceSwitchPort">ReferenceSwitchPort</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-ndis-switch-report-filtered-net-buffer-lists.md">ReportFilteredNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-ndis-switch-set-net-buffer-list-source.md">SetNetBufferListSource</a>
</dt>
<dt>
<a href="netvista.UpdateNetBufferListDestinations">UpdateNetBufferListDestinations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_OPTIONAL_HANDLERS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
