---
UID: NS.ntddndis._NDIS_RECEIVE_FILTER_INFO_ARRAY
title: NDIS_RECEIVE_FILTER_INFO_ARRAY
author: windows-driver-content
description: The NDIS_RECEIVE_FILTER_INFO_ARRAY structure specifies a list of receive filters that are currently configured on a miniport driver.
old-location: netvista\ndis_receive_filter_info_array.htm
old-project: netvista
ms.assetid: 32896b46-1143-4598-ad15-2eb4dbdea6e8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_RECEIVE_FILTER_INFO_ARRAY, NDIS_RECEIVE_FILTER_INFO_ARRAY, *PNDIS_RECEIVE_FILTER_INFO_ARRAY
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
req.alt-api: NDIS_RECEIVE_FILTER_INFO_ARRAY
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

# NDIS_RECEIVE_FILTER_INFO_ARRAY structure



## -description
<p>
<p>The <b>NDIS_RECEIVE_FILTER_INFO_ARRAY</b> structure specifies a list of receive filters that are currently configured on a miniport driver.</p>
</p>
<p>The <b>NDIS_RECEIVE_FILTER_INFO_ARRAY</b> structure specifies a list of receive filters that are currently configured on a miniport driver.</p>
<p>NDIS receive filters are used in the following NDIS interfaces:</p>
<p>
<a href="NULL">NDIS Packet Coalescing</a>. For more information about how to use receive filters in this interface, see <a href="NULL">Managing Packet Coalescing Receive Filters</a>.</p>
<p>
<a href="NULL">Single Root I/O Virtualization (SR-IOV)</a>. For more information about how to use receive filters in this interface, see <a href="NULL">Setting a Receive Filter on a Virtual Port</a>.</p>
<p>
<a href="NULL">Virtual Machine Queue (VMQ)</a>. For more information about how to use receive filters in this interface, see <a href="NULL">Setting and Clearing VMQ Filters</a>.</p>


## -syntax

````
typedef struct _NDIS_RECEIVE_FILTER_INFO_ARRAY {
  NDIS_OBJECT_HEADER       Header;
  NDIS_RECEIVE_QUEUE_ID    QueueId;
  ULONG                    FirstElementOffset;
  ULONG                    NumElements;
  ULONG                    ElementSize;
#if (NDIS_SUPPORT_NDIS630)
  ULONG                    Flags;
  NDIS_NIC_SWITCH_VPORT_ID VPortId;
#endif 
} NDIS_RECEIVE_FILTER_INFO_ARRAY, *PNDIS_RECEIVE_FILTER_INFO_ARRAY;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_RECEIVE_FILTER_INFO_ARRAY</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_RECEIVE_FILTER_INFO_ARRAY</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_SIZEOF_RECEIVE_FILTER_INFO_ARRAY_REVISION_2"></a><a id="ndis_sizeof_receive_filter_info_array_revision_2"></a>NDIS_SIZEOF_RECEIVE_FILTER_INFO_ARRAY_REVISION_2

<dd>
<p>Added members for NDIS 6.30.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_RECEIVE_FILTER_INFO_ARRAY_REVISION_2.</p>
</dd>

### -field <a id="NDIS_SIZEOF_RECEIVE_FILTER_INFO_ARRAY_REVISION_1"></a><a id="ndis_sizeof_receive_filter_info_array_revision_1"></a>NDIS_SIZEOF_RECEIVE_FILTER_INFO_ARRAY_REVISION_1

<dd>
<p>Original version for NDIS 6.20.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_RECEIVE_FILTER_INFO_ARRAY_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>QueueId</b>

<dd>
<p>A receive queue identifier. This identifier is an
     integer between zero and the number of queues that the network adapter supports. A value of NDIS_DEFAULT_RECEIVE_QUEUE_ID specifies
     the default receive queue.</p>
<div class="alert"><b>Note</b>  Miniport drivers that support <a href="NULL">NDIS packet coalescing</a> or SR-IOV interface must set the <b>QueueId</b> member to NDIS_DEFAULT_RECEIVE_QUEUE_ID.</div>
<div> </div>
</dd>

### -field <b>FirstElementOffset</b>

<dd>
<p>The offset, in bytes, to the first element in an array of elements that follow this structure. The offset is measured from the start of the <b>NDIS_RECEIVE_FILTER_INFO_ARRAY</b> structure up to the beginning of the first element. Each element in the array is an <a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-info.md">NDIS_RECEIVE_FILTER_INFO</a> structure.

</p>
<div class="alert"><b>Note</b>  If <b>NumElements</b> is set to zero, this member is ignored.  </div>
<div> </div>
</dd>

### -field <b>NumElements</b>

<dd>
<p>The number of elements in the array.</p>
</dd>

### -field <b>ElementSize</b>

<dd>
<p>The size, in bytes, of each element in the array.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A  bitwise OR of the following flags: </p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_FILTER_INFO_ARRAY_VPORT_ID_SPECIFIED"></a><a id="ndis_receive_filter_info_array_vport_id_specified"></a>NDIS_RECEIVE_FILTER_INFO_ARRAY_VPORT_ID_SPECIFIED

<dd>
<p>If this flag is set, information is requested about receive filters that are configured on the virtual port (VPort) specified by the <b>VPortId</b> member.</p>
<div class="alert"><b>Note</b>  This flag is only valid for the SR-IOV interface.</div>
<div> </div>
</dd>
</dl>
</dd>

### -field <b>VPortId</b>

<dd>
<p>The virtual port (VPort) identifier on which receive filters are being queried. The VPort identifier must be one of the following values:</p>
<ul>
<li>
<p>

The identifier of a VPort that was previously allocated through an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>.

</p>
</li>
<li>
<p>A value of NDIS_DEFAULT_VPORT_ID that specifies the default VPort on the NIC switch.

</p>
</li>
</ul>
<p>A NIC switch is supported by network adapters for the SR-IOV interface. The NIC switch can be configured to have one or more VPorts.</p>
<div class="alert"><b>Note</b>  The <b>VPortId</b> member is only valid if the NDIS_RECEIVE_FILTER_INFO_ARRAY_VPORT_ID_SPECIFIED flag is set in <b>Flags</b>. 
</div>
<div> </div>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_RECEIVE_FILTER_INFO_ARRAY</b> structure is used in the 
    OID request of <a href="netvista.oid_receive_filter_enum_filters">
    OID_RECEIVE_FILTER_ENUM_FILTERS</a>. This OID request enumerates the receive filters on a VMQ  or SR-IOV receive queue. Each
    element in the array that follows the <b>NDIS_RECEIVE_FILTER_INFO_ARRAY</b> structure is an 
    <a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-info.md">
    NDIS_RECEIVE_FILTER_INFO</a> structure.</p>

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
<a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-info.md">NDIS_RECEIVE_FILTER_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569787">OID_RECEIVE_FILTER_ENUM_FILTERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RECEIVE_FILTER_INFO_ARRAY structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
