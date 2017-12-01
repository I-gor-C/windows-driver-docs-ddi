---
UID: NS.ntddndis._NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS
title: NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS
author: windows-driver-content
description: The NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS structure specifies the receive filtering features that are enabled or disabled on a network adapter.NDIS receive filters are used in the following NDIS interfaces:NDIS Packet Coalescing.
old-location: netvista\ndis_receive_filter_global_parameters.htm
old-project: netvista
ms.assetid: 4ec36054-ba61-4862-b185-7473a6806804
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS, NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS, *PNDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS
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

# NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS structure



## -description
<p>The <b>NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS</b> structure specifies the receive filtering features that are
  enabled or disabled on a network adapter.</p>
<p>NDIS receive filters are used in the following NDIS interfaces:</p>
<p>
<a href="NULL">NDIS Packet Coalescing</a>. For more information about how to use receive filters in this interface, see <a href="NULL">Managing Packet Coalescing Receive Filters</a>.</p>
<p>
<a href="NULL">Single Root I/O Virtualization (SR-IOV)</a>. For more information about how to use receive filters in this interface, see <a href="NULL">Setting a Receive Filter on a Virtual Port</a>.</p>
<p>
<a href="NULL">Virtual Machine Queue (VMQ)</a>. For more information about how to use receive filters in this interface, see <a href="NULL">Setting and Clearing VMQ Filters</a>.</p>


## -syntax

````
typedef struct _NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  ULONG              Flags;
  ULONG              EnabledFilterTypes;
  ULONG              EnabledQueueTypes;
} NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS, *PNDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS</b> structure. The driver sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT.</p>
<p>To indicate the version of the <b>NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS</b> structure, the driver sets the 
     <b>Revision</b> member to one of the following values:</p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS_REVISION_1"></a><a id="ndis_receive_filter_global_parameters_revision_1"></a>NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS_REVISION_1

<dd>
<p>Original version for NDIS 6.20.</p>
<p>The driver sets the 
        <b>Size</b> member to NDIS_SIZEOF_RECEIVE_FILTER_GLOBAL_PARAMETERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>EnabledFilterTypes</b>

<dd>
<p>A  bitwise OR of flags for types of enabled receive filters. The
     following filter type flag is valid.
     </p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_FILTER_VMQ_FILTERS_ENABLED"></a><a id="ndis_receive_filter_vmq_filters_enabled"></a>NDIS_RECEIVE_FILTER_VMQ_FILTERS_ENABLED

<dd>
<p>Specifies that VMQ filters are enabled.</p>
<div class="alert"><b>Note</b>  The miniport driver should set this flag if the miniport driver is enabled to use the SR-IOV interface. For more information on how these interfaces are enabled, see <a href="netvista.handling_sr-iov__vmq__and_rss_standardized_inf_keywords">Handling SR-IOV, VMQ, and RSS Standardized INF Keywords</a>.</div>
<div> </div>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_PACKET_COALESCING_FILTERS_ENABLED"></a><a id="ndis_receive_filter_packet_coalescing_filters_enabled"></a>NDIS_RECEIVE_FILTER_PACKET_COALESCING_FILTERS_ENABLED

<dd>
<p>Specifies that NDIS packet coalescing receive filters are enabled.</p>
</dd>
</dl>
</dd>

### -field <b>EnabledQueueTypes</b>

<dd>
<p>A  bitwise OR of flags for types of enabled receive queues. The
     following queue type flag is valid.
     </p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_FILTER_VM_QUEUES_ENABLED"></a><a id="ndis_receive_filter_vm_queues_enabled"></a>NDIS_RECEIVE_FILTER_VM_QUEUES_ENABLED

<dd>
<p>Specifies that virtual machine (VM) queues are enabled.  VM queues are used in the VMQ and SR-IOV interface.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS</b> structure is used in the 
    <a href="netvista.oid_receive_filter_global_parameters">
    OID_RECEIVE_FILTER_GLOBAL_PARAMETERS</a> query OID to obtain the current global receive filter
    settings.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.20 and later.</p>
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
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.oid_receive_filter_global_parameters">
   OID_RECEIVE_FILTER_GLOBAL_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
