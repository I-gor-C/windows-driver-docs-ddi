---
UID: NS.ntddndis._NDIS_RECEIVE_FILTER_FIELD_PARAMETERS
title: NDIS_RECEIVE_FILTER_FIELD_PARAMETERS
author: windows-driver-content
description: The NDIS_RECEIVE_FILTER_FIELD_PARAMETERS structure specifies the filter test criterion for a field in a network packet header.
old-location: netvista\ndis_receive_filter_field_parameters.htm
old-project: netvista
ms.assetid: 3d387fe9-a7cc-4034-b31e-ba1359db2ae1
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_RECEIVE_FILTER_FIELD_PARAMETERS, NDIS_RECEIVE_FILTER_FIELD_PARAMETERS, *PNDIS_RECEIVE_FILTER_FIELD_PARAMETERS
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
req.alt-api: NDIS_RECEIVE_FILTER_FIELD_PARAMETERS
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

# NDIS_RECEIVE_FILTER_FIELD_PARAMETERS structure



## -description
<p>The <b>NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</b> structure specifies the filter test criterion for a field
  in a network packet header.</p>
<p>NDIS receive filters are used in the following NDIS interfaces:</p>
<p>
<a href="netvista.ndis_packet_coalescing">NDIS Packet Coalescing</a>. For more information about how to use receive filters in this interface, see <a href="netvista.managing_packet_coalescing_receive_filters">Managing Packet Coalescing Receive Filters</a>.</p>
<p>
<a href="netvista.single_root_i_o_virtualization__sr-iov_">Single Root I/O Virtualization (SR-IOV)</a>. For more information about how to use receive filters in this interface, see <a href="netvista.setting_a_receive_filter_on_a_virtual_port">Setting a Receive Filter on a Virtual Port</a>.</p>
<p>
<a href="netvista.virtual_machine_queue__vmq__in_ndis_6_20">Virtual Machine Queue (VMQ)</a>. For more information about how to use receive filters in this interface, see <a href="netvista.setting_and_clearing_vmq_filters">Setting and Clearing VMQ Filters</a>.</p>


## -syntax

````
typedef struct _NDIS_RECEIVE_FILTER_FIELD_PARAMETERS {
  NDIS_OBJECT_HEADER       Header;
  ULONG                    Flags;
  NDIS_FRAME_HEADER        FrameHeader;
  NDIS_RECEIVE_FILTER_TEST ReceiveFilterTest;
  union _HEADER_FIELD {
    NDIS_MAC_HEADER_FIELD        MacHeaderField;
    NDIS_ARP_HEADER_FIELD        ArpHeaderField;
    NDIS_IPV4_HEADER_FIELD       IPv4HeaderField;
    NDIS_IPV6_HEADER_FIELD       IPv6HeaderField;
    NDIS_UDP_HEADER_FIELD        UdpHeaderField;
  } HeaderField;
  union _FIELD_VALUE {
    UCHAR   FieldByteValue;
    USHORT  FieldShortValue;
    ULONG   FieldLongValue;
    ULONG64 FieldLong64Value;
    UCHAR   FieldByteArrayValue[16];
  } FieldValue;
  union _RESULT_VALUE {
    UCHAR   ResultByteValue;
    USHORT  ResultShortValue;
    ULONG   ResultLongValue;
    ULONG64 ResultLong64Value;
    UCHAR   ResultByteArrayValue[16];
  } ResultValue;
} NDIS_RECEIVE_FILTER_FIELD_PARAMETERS, *PNDIS_RECEIVE_FILTER_FIELD_PARAMETERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</b> structure. The driver sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT.</p>
<p>To indicate the version of the <b>NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</b> structure, the driver sets the 
     <b>Revision</b> member to one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_RECEIVE_FILTER_FIELD_PARAMETERS_REVISION_2"></a><a id="ndis_receive_filter_field_parameters_revision_2"></a><dl>

### -field NDIS_RECEIVE_FILTER_FIELD_PARAMETERS_REVISION_2


### -field 2

</dl>
</td>
<td width="60%">
<p>Added additional members to the <b>HeaderField</b> union for NDIS 6.30.</p>
<p>The driver sets the 
        <b>Size</b> member to <b>NDIS_SIZEOF_RECEIVE_FILTER_FIELD_PARAMETERS_REVISION_2</b>.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_RECEIVE_FILTER_FIELD_PARAMETERS_REVISION_1"></a><a id="ndis_receive_filter_field_parameters_revision_1"></a><dl>

### -field NDIS_RECEIVE_FILTER_FIELD_PARAMETERS_REVISION_1


### -field 1

</dl>
</td>
<td width="60%">
<p>Original version for NDIS 6.20.</p>
<p>The driver sets the 
        <b>Size</b> member to <b>NDIS_SIZEOF_RECEIVE_FILTER_FIELD_PARAMETERS_REVISION_1</b>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Flags

<dd>
<p>A bitwise OR of flags. The following flags are valid for the 
     <a href="netvista.oid_receive_filter_set_filter">
     OID_RECEIVE_FILTER_SET_FILTER</a> OID.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_RECEIVE_FILTER_FIELD_MAC_HEADER_VLAN_UNTAGGED_OR_ZERO"></a><a id="ndis_receive_filter_field_mac_header_vlan_untagged_or_zero"></a><dl>

### -field NDIS_RECEIVE_FILTER_FIELD_MAC_HEADER_VLAN_UNTAGGED_OR_ZERO


### -field 0x00000001

</dl>
</td>
<td width="60%">
<p>If this flag is set, the network adapter must only indicate received packets that pass the following criteria:</p>
<ul>
<li>
<p>The packet's media access control (MAC) address matches the specified MAC header field test.</p>
</li>
<li>
<p>The packet either does not contain a VLAN tag or has a VLAN tag with an ID of zero. </p>
</li>
</ul>
<p>For more information about this flag, see the Remarks section.</p>
<div class="alert"><b>Note</b>  If an overlying driver sets a MAC address filter and a VLAN identifier filter with an
       OID request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569795">OID_RECEIVE_FILTER_SET_FILTER</a>, it does not set this flag in either of the filter fields. In this
       case, the miniport driver should indicate packets that match both the specified MAC address and the
       VLAN identifier. That is, the miniport driver should not indicate packets with a matching MAC address
       that have a zero VLAN identifier or are untagged packets.</div>
<div> </div>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field FrameHeader

<dd>
<p>The type of header in the network data frame.</p>
</dd>

### -field ReceiveFilterTest

<dd>
<p>The type of test to perform for the receive filter.</p>
</dd>

### -field HeaderField

<dd>
<p>The type of field in a header. The field type (for example,
     <a href="..\ntddndis\ne-ntddndis--ndis-mac-header-field.md">NDIS_MAC_HEADER_FIELD</a>) corresponds to the type of header that is specified in the 
     <b>FrameHeader</b> member.
     </p>
<p>This union contains the following members:</p>
<dl>

### -field MacHeaderField

<dd>
<p>The type of field in a MAC header.</p>
</dd>

### -field ArpHeaderField

<dd>
<p>The type of field in an Address Resolution Protocol (ARP) header.</p>
</dd>

### -field IPv4HeaderField

<dd>
<p>An 
       <a href="..\ntddndis\ne-ntddndis--ndis-ipv4-header-field.md">NDIS_IPV4_HEADER_FIELD</a> enumeration
       value that specifies the type of field in an IP version 4 (IPv4) header.</p>
</dd>

### -field IPv6HeaderField

<dd>
<p>An 
       <a href="..\ntddndis\ne-ntddndis--ndis-ipv6-header-field.md">NDIS_IPV6_HEADER_FIELD</a> enumeration
       value that specifies the type of field in an IP version 6 (IPv6) header.</p>
</dd>

### -field UdpHeaderField

<dd>
<p>The type of field in a User Datagram Protocol
(UDP) header.</p>
</dd>
</dl>
</dd>

### -field FieldValue

<dd>
<p></p>
<p>The value that the miniport adapter compares to the corresponding header field value in incoming packets. The location of the header field value is determined by the field type that is specified in the <b>HeaderField</b> member.</p>
<p>For more information, see the Remarks section.</p>
<p>This union contains the following members:</p>
<dl>

### -field FieldByteValue

<dd>
<p>A <b>UCHAR</b> value to compare with a field in a network packet.</p>
<div class="alert"><b>Note</b>  If the <b>MacHeaderField</b> member specifies an <b>NdisMacHeaderFieldPacketType</b> enumeration value, this member contains an <a href="..\ntddndis\ne-ntddndis--ndis-mac-packet-type.md">NDIS_MAC_PACKET_TYPE</a> enumeration value.</div>
<div> </div>
</dd>

### -field FieldShortValue

<dd>
<p>A <b>USHORT</b> value to compare with a field in a network packet.</p>
</dd>

### -field FieldLongValue

<dd>
<p>A <b>ULONG</b> value to compare with a field in a network packet.</p>
</dd>

### -field FieldLong64Value

<dd>
<p>A <b>ULONG64</b> value to compare with a field in a network packet.</p>
</dd>

### -field FieldByteArrayValue

<dd>
<p>A <b>UCHAR</b> array to compare with a field in a network packet.</p>
</dd>
</dl>
</dd>

### -field ResultValue

<dd>
<p>A union that contains a test result value. </p>
<p>If the <b>ReceiveFilterTest</b> member is set to  <b>NdisReceiveFilterTestMaskEqual</b>, the network adapter first calculates a result from the value in the <b>FieldValue</b> member and the header field value as specified by the <b>HeaderField</b> member. The adapter then compares the calculated result with <b>ResultValue</b>. </p>
<p>For more information, see the Remarks section.</p>
<p>This union contains the following members:</p>
<dl>

### -field ResultByteValue

<dd>
<p>A <b>UCHAR</b> value to compare with a test result.</p>
</dd>

### -field ResultShortValue

<dd>
<p>A <b>USHORT</b> value to compare with a test result.</p>
</dd>

### -field ResultLongValue

<dd>
<p>A <b>ULONG</b> value to compare with a test result.</p>
</dd>

### -field ResultLong64Value

<dd>
<p>A <b>ULONG64</b> value to compare with a test result.</p>
</dd>

### -field ResultByteArrayValue

<dd>
<p>A <b>UCHAR</b> array to compare with a test result.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</b> structure specifies the filter test criterion for one field
    in a possible array of field tests that can be specified with the 
    <a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-parameters.md">
    NDIS_RECEIVE_FILTER_PARAMETERS</a> structure.</p>

<p>The following table describes how the network adapter uses the <b>ReceiveFilterTest</b>, <b>FieldValue</b>, and <b>ResultValue</b> members to perform a filter test on the specified header field value of a received packet.</p>

<p>If the <b>NDIS_RECEIVE_FILTER_FIELD_MAC_HEADER_VLAN_UNTAGGED_OR_ZERO</b> flag is not set and there is no VLAN identifier filter that was configured by an OID set request of
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff569795">OID_RECEIVE_FILTER_SET_FILTER</a>, the miniport driver must do one of the following:</p>

<p>For NDIS 6.20, the miniport driver must return a failed status for the
       OID request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569795">OID_RECEIVE_FILTER_SET_FILTER</a>.</p>

<p>Starting with NDIS 6.30, if the <b>NDIS_RECEIVE_FILTER_FIELD_MAC_HEADER_VLAN_UNTAGGED_OR_ZERO</b> flag is not set and there is no VLAN identifier filter configured by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff569795">OID_RECEIVE_FILTER_SET_FILTER</a> method request, the miniport driver must do either one of the following:</p>

<p>The miniport driver must return a failed status for the
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff569795">OID_RECEIVE_FILTER_SET_FILTER</a> method request.</p>

<p>The miniport driver  must configure the network adapter  to inspect and filter the specified MAC address fields. If a VLAN tag is present in the received packet, the network adapter must remove it from the packet data. The miniport driver must   put the VLAN tag in an <a href="..\ndis\ns-ndis--ndis-net-buffer-list-8021q-info.md">NDIS_NET_BUFFER_LIST_8021Q_INFO</a> that is associated with the packet's <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure.</p>

<p>Starting with NDIS 6.30, if the <b>NDIS_RECEIVE_FILTER_FIELD_MAC_HEADER_VLAN_UNTAGGED_OR_ZERO</b> flag is not set and there is a non-zero VLAN identifier filter that was configured by an OID set request of
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff569795">OID_RECEIVE_FILTER_SET_FILTER</a>, the miniport driver must do the following:</p>

<p>The miniport driver must configure the network adapter  to inspect and filter the specified MAC address and VLAN identifier fields. </p>

<p>If a VLAN tag is present in the received packet, the network adapter must remove it from the packet data. The miniport driver must   put the VLAN tag in an <a href="..\ndis\ns-ndis--ndis-net-buffer-list-8021q-info.md">NDIS_NET_BUFFER_LIST_8021Q_INFO</a> that is associated with the packet's <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure.</p>

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
<a href="..\ntddndis\ne-ntddndis--ndis-arp-header-field.md">NDIS_ARP_HEADER_FIELD</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-frame-header.md">NDIS_FRAME_HEADER</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-ipv4-header-field.md">NDIS_IPV4_HEADER_FIELD</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-ipv6-header-field.md">NDIS_IPV6_HEADER_FIELD</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-udp-header-field.md">NDIS_UDP_HEADER_FIELD</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-mac-header-field.md">NDIS_MAC_HEADER_FIELD</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-mac-packet-type.md">NDIS_MAC_PACKET_TYPE</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-parameters.md">
   NDIS_RECEIVE_FILTER_PARAMETERS</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-receive-filter-test.md">NDIS_RECEIVE_FILTER_TEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569795">OID_RECEIVE_FILTER_SET_FILTER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RECEIVE_FILTER_FIELD_PARAMETERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
