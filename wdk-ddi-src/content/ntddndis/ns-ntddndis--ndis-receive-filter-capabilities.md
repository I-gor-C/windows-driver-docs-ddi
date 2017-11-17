---
UID: NS.ntddndis._NDIS_RECEIVE_FILTER_CAPABILITIES
title: NDIS_RECEIVE_FILTER_CAPABILITIES
author: windows-driver-content
description: The NDIS_RECEIVE_FILTER_CAPABILITIES structure specifies the receive filtering capabilities of a network adapter.
old-location: netvista\ndis_receive_filter_capabilities.htm
ms.assetid: aecc1fe0-03f9-44be-9a38-b689eee4c5a6
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_RECEIVE_FILTER_CAPABILITIES
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
ms.keywords: NDIS_RECEIVE_FILTER_CAPABILITIES, NDIS_RECEIVE_FILTER_CAPABILITIES, *PNDIS_RECEIVE_FILTER_CAPABILITIES
req.iface: 
---

# NDIS_RECEIVE_FILTER_CAPABILITIES structure



## -description
<p>The <b>NDIS_RECEIVE_FILTER_CAPABILITIES</b> structure specifies the  receive filtering capabilities of a
  network adapter.</p>
<p>NDIS receive filters are used in the following NDIS interfaces:</p>
<p>
<a href="NULL">NDIS Packet Coalescing</a>. For more information about how to use receive filters in this interface, see <a href="NULL">Managing Packet Coalescing Receive Filters</a>.</p>
<p>
<a href="NULL">Single Root I/O Virtualization (SR-IOV)</a>. For more information about how to use receive filters in this interface, see <a href="NULL">Setting a Receive Filter on a Virtual Port</a>.</p>
<p>
<a href="NULL">Virtual Machine Queue (VMQ)</a>. For more information about how to use receive filters in this interface, see <a href="NULL">Setting and Clearing VMQ Filters</a>.</p>


## -syntax

````
typedef struct _NDIS_RECEIVE_FILTER_CAPABILITIES {
  NDIS_OBJECT_HEADER Header;
  ULONG              Flags;
  ULONG              EnabledFilterTypes;
  ULONG              EnabledQueueTypes;
  ULONG              NumQueues;
  ULONG              SupportedQueueProperties;
  ULONG              SupportedFilterTests;
  ULONG              SupportedHeaders;
  ULONG              SupportedMacHeaderFields;
  ULONG              MaxMacHeaderFilters;
  ULONG              MaxQueueGroups;
  ULONG              MaxQueuesPerQueueGroup;
  ULONG              MinLookaheadSplitSize;
  ULONG              MaxLookaheadSplitSize;
#if NDIS_SUPPORT_NDIS630
  ULONG              SupportedARPHeaderFields;
  ULONG              SupportedIPv4HeaderFields;
  ULONG              SupportedIPv6HeaderFields;
  ULONG              SupportedUdpHeaderFields;
  ULONG              MaxFieldTestsPerPacketCoalescingFilter;
  ULONG              MaxPacketCoalescingFilters;
  ULONG              NdisReserved;
#endif 
} NDIS_RECEIVE_FILTER_CAPABILITIES, *PNDIS_RECEIVE_FILTER_CAPABILITIES;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_RECEIVE_FILTER_CAPABILITIES</b> structure. The driver sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT.</p>
<p>To indicate the version of the <b>NDIS_RECEIVE_FILTER_CAPABILITIES</b> structure, the driver sets the 
     <b>Revision</b> member to one of the following values:</p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_FILTER_CAPABILITIES_REVISION_2"></a><a id="ndis_receive_filter_capabilities_revision_2"></a>NDIS_RECEIVE_FILTER_CAPABILITIES_REVISION_2

<dd>
<p>Added  
        various members for NDIS 6.30 and later.</p>
<p>The driver sets the 
        <b>Size</b> member to NDIS_SIZEOF_RECEIVE_FILTER_CAPABILITIES_REVISION_2.</p>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_CAPABILITIES_REVISION_1"></a><a id="ndis_receive_filter_capabilities_revision_1"></a>NDIS_RECEIVE_FILTER_CAPABILITIES_REVISION_1

<dd>
<p>Original version for NDIS 6.20.</p>
<p>The driver sets the 
        <b>Size</b> member to NDIS_SIZEOF_RECEIVE_FILTER_CAPABILITIES_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>EnabledFilterTypes</b>

<dd>
<p>A bitwise OR of flags that specify the types of receive filters that are enabled. The
     following filter type flag is valid.
     </p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_FILTER_VMQ_FILTERS_ENABLED"></a><a id="ndis_receive_filter_vmq_filters_enabled"></a>NDIS_RECEIVE_FILTER_VMQ_FILTERS_ENABLED

<dd>
<p>Specifies that VMQ filters are enabled.</p>
<div class="alert"><b>Note</b>  The miniport driver should set this flag if the miniport driver is enabled to use the SR-IOV interface.</div>
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
<p>A bitwise OR of flags that specify the types of receive queues that are enabled. The
     following queue type flag is valid.
     </p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_FILTER_VM_QUEUES_ENABLED"></a><a id="ndis_receive_filter_vm_queues_enabled"></a>NDIS_RECEIVE_FILTER_VM_QUEUES_ENABLED

<dd>
<p>Specifies that virtual machine (VM) queues are enabled.  VM queues are used when the miniport driver is enabled to use the VMQ interface.</p>
<div class="alert"><b>Note</b>  The miniport driver must not set this flag if the miniport driver is enabled to only use the SR-IOV interface. For more information on how these interfaces are enabled, see <a href="netvista.handling_sr-iov__vmq__and_rss_standardized_inf_keywords">Handling SR-IOV, VMQ, and RSS Standardized INF Keywords</a>.</div>
<div> </div>
</dd>
</dl>
</dd>

### -field <b>NumQueues</b>

<dd>
<p>The number of VM queues that the network adapter supports.</p>
<div class="alert"><b>Note</b>  If the miniport driver is enabled to use the SR-IOV interface, it must set this member to zero. When use of the SR-IOV interface is enabled, NDIS uses virtual ports (VPorts) for receive and transmit queues instead of VM queues.
</div>
<div> </div>
</dd>

### -field <b>SupportedQueueProperties</b>

<dd>
<p>A bitwise OR of flags that specify the VM queue properties that the network adapter supports. The
     following flags are defined:
     </p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_FILTER_MSI_X_SUPPORTED"></a><a id="ndis_receive_filter_msi_x_supported"></a>NDIS_RECEIVE_FILTER_MSI_X_SUPPORTED

<dd>
<p>The network adapter uses MSI-X for receive queue interrupt generation. This flag is mandatory for miniport drivers that support the VMQ or SR-IOV interface.</p>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_VM_QUEUE_SUPPORTED"></a><a id="ndis_receive_filter_vm_queue_supported"></a>NDIS_RECEIVE_FILTER_VM_QUEUE_SUPPORTED

<dd>
<p>The network adapter provides the minimum requirements to support VM  queue packet filtering. 

The miniport driver must set this flag if it is enabled to use the VMQ or SR-IOV interface.</p>
<p>For more information about VMQ requirements for VM queue packet filtering, see <a href="NULL">Setting and Clearing VMQ Filters</a>.

</p>
<p>For more information about SR-IOV requirements for VM queue packet filtering, see <a href="NULL">Setting a Receive Filter on a Virtual Port</a>.

</p>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_LOOKAHEAD_SPLIT_SUPPORTED"></a><a id="ndis_receive_filter_lookahead_split_supported"></a>NDIS_RECEIVE_FILTER_LOOKAHEAD_SPLIT_SUPPORTED

<dd>
<p>The network adapter supports VM queues that split an incoming received packet at the lookahead
       offset. This offset is equal to or greater than the requested lookahead size. The network adapter uses DMA to transfer the lookahead
       and post-lookahead data to separate shared memory segments.</p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported. Miniport drivers that support this version of NDIS must not set this flag.</div>
<div> </div>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_DYNAMIC_PROCESSOR_AFFINITY_CHANGE_SUPPORTED"></a><a id="ndis_receive_filter_dynamic_processor_affinity_change_supported"></a>NDIS_RECEIVE_FILTER_DYNAMIC_PROCESSOR_AFFINITY_CHANGE_SUPPORTED

<dd>
<p>The  network adapter supports the ability to dynamically change one of the following processor affinity attributes:</p>
<ul>
<li>
<p>The processor affinity of a VM queue in the VMQ interface. The processor affinity is changed through an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569794">OID_RECEIVE_FILTER_QUEUE_PARAMETERS</a>.</p>
</li>
<li>
<p>The processor affinity of a nondefault virtual port (VPort), which was created in the SR-IOV interface and is attached to the PCI Express (PCIe) physical function (PF) of the network adapter. The processor affinity is changed through an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>.</p>
</li>
</ul>
<div class="alert"><b>Note</b>  This flag is supported in NDIS 6.30 and later. Miniport drivers that support the VMQ or SR-IOV interface must set this flag.</div>
<div> </div>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_INTERRUPT_VECTOR_COALESCING_SUPPORTED"></a><a id="ndis_receive_filter_interrupt_vector_coalescing_supported"></a>NDIS_RECEIVE_FILTER_INTERRUPT_VECTOR_COALESCING_SUPPORTED

<dd>
<p>The network adapter supports interrupt coalescing for received packets on any of the following: </p>
<ul>
<li>
<p>Multiple VM queues in the VMQ interface.</p>
</li>
<li>
<p>Multiple VPorts that are attached to the PF in the SR-IOV interface.</p>
</li>
</ul>
<p>If this flag is set, the network adapter must coalesce receive interrupts for VM queues or VPorts that have the same processor affinity.</p>
<div class="alert"><b>Note</b>  This flag is supported in NDIS 6.30 and later. Miniport drivers that support the VMQ or SR-IOV interface must set this flag.</div>
<div> </div>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_IMPLAT_MIN_OF_QUEUES_MODE"></a><a id="ndis_receive_filter_implat_min_of_queues_mode"></a>NDIS_RECEIVE_FILTER_IMPLAT_MIN_OF_QUEUES_MODE

<dd>
<p>Indicates that the number of VM queues available  is the minimum number of queues available from any member of a Load Balancing Failover (LBFO) team. This flag applies to LBFO filters only. This flag is not set for miniports.</p>
</dd>

### -field <a id="_NDIS_RECEIVE_FILTER_IMPLAT_SUM_OF_QUEUES_MODE"></a><a id="_ndis_receive_filter_implat_sum_of_queues_mode"></a> NDIS_RECEIVE_FILTER_IMPLAT_SUM_OF_QUEUES_MODE

<dd>
<p>Indicates that the number of VM queues available is the sum of all the queues available from every member of an LBFO team. This flag applies to LBFO filters only. This flag is not set for miniports.</p>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_PACKET_COALESCING_SUPPORTED_ON_DEFAULT_QUEUE"></a><a id="ndis_receive_filter_packet_coalescing_supported_on_default_queue"></a>NDIS_RECEIVE_FILTER_PACKET_COALESCING_SUPPORTED_ON_DEFAULT_QUEUE

<dd>
<p>The network adapter supports NDIS packet coalescing. Packet coalescing is only supported on the default receive queue of the network adapter. This receive queue has an identifier of NDIS_DEFAULT_RECEIVE_QUEUE_ID.
</p>
<div class="alert"><b>Note</b>  This flag is supported in NDIS 6.30 and later.</div>
<div> </div>
</dd>
</dl>
</dd>

### -field <b>SupportedFilterTests</b>

<dd>
<p>A bitwise OR of flags that specify the test operations that a miniport
     driver supports. The following flags are defined:
     </p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_FILTER_TEST_HEADER_FIELD_EQUAL_SUPPORTED"></a><a id="ndis_receive_filter_test_header_field_equal_supported"></a>NDIS_RECEIVE_FILTER_TEST_HEADER_FIELD_EQUAL_SUPPORTED

<dd>
<p>The network adapter supports testing the selected header field to determine whether it is equal to a
       given value.</p>
<div class="alert"><b>Note</b>  If the miniport driver supports the VMQ or SR-IOV interfaces, it must set this flag.</div>
<div> </div>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_TEST_HEADER_FIELD_MASK_EQUAL_SUPPORTED"></a><a id="ndis_receive_filter_test_header_field_mask_equal_supported"></a>NDIS_RECEIVE_FILTER_TEST_HEADER_FIELD_MASK_EQUAL_SUPPORTED

<dd>
<p>The network adapter supports masking (that is, a bitwise AND) of the selected header field to
       determine whether the result is equal to a specified value.</p>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_TEST_HEADER_FIELD_NOT_EQUAL_SUPPORTED"></a><a id="ndis_receive_filter_test_header_field_not_equal_supported"></a>NDIS_RECEIVE_FILTER_TEST_HEADER_FIELD_NOT_EQUAL_SUPPORTED

<dd>
<p>The network adapter supports testing the selected header field to determine whether it is not equal to a
       specified value.</p>
<div class="alert"><b>Note</b>  This flag is supported in NDIS 6.30 and later.</div>
<div> </div>
</dd>
</dl>
</dd>

### -field <b>SupportedHeaders</b>

<dd>
<p>A bitwise OR of flags that specify the types of network packet headers that
     a miniport driver can inspect. The following flags are defined:
     </p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_FILTER_MAC_HEADER_SUPPORTED"></a><a id="ndis_receive_filter_mac_header_supported"></a>NDIS_RECEIVE_FILTER_MAC_HEADER_SUPPORTED

<dd>
<p>The network adapter can inspect the media access control (MAC) header of a network packet. The <b>SupportedMacHeaderFields</b> member defines the various fields from the MAC header that can be inspected.</p>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_ARP_HEADER_SUPPORTED"></a><a id="ndis_receive_filter_arp_header_supported"></a>NDIS_RECEIVE_FILTER_ARP_HEADER_SUPPORTED

<dd>
<p>The network adapter can inspect the Address Resolution Protocol (ARP) header of a network packet. The <b>SupportedArpHeaderFields</b> member defines the various fields from the ARP header that can be inspected.</p>
<div class="alert"><b>Note</b>  This flag is supported in NDIS 6.30 and later.</div>
<div> </div>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_IPV4_HEADER_SUPPORTED"></a><a id="ndis_receive_filter_ipv4_header_supported"></a>NDIS_RECEIVE_FILTER_IPV4_HEADER_SUPPORTED

<dd>
<p>The network adapter can inspect the IP version 4 (IPv4) header of a network packet. The <b>SupportedIPv4HeaderFields</b> member defines the various fields from the IPv4 header that can be inspected.</p>
<div class="alert"><b>Note</b>  This flag is supported in NDIS 6.30 and later.</div>
<div> </div>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_IPV6_HEADER_SUPPORTED"></a><a id="ndis_receive_filter_ipv6_header_supported"></a>NDIS_RECEIVE_FILTER_IPV6_HEADER_SUPPORTED

<dd>
<p>The network adapter can inspect the IP version 6 (IPv6) header of a network packet. The <b>SupportedIPv6HeaderFields</b> member defines the various fields from the IPv6 header that can be inspected.</p>
<div class="alert"><b>Note</b>  This flag is supported in NDIS 6.30 and later.</div>
<div> </div>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_UDP_HEADER_SUPPORTED"></a><a id="ndis_receive_filter_udp_header_supported"></a>NDIS_RECEIVE_FILTER_UDP_HEADER_SUPPORTED

<dd>
<p>The network adapter can inspect the User Datagram Protocol
(UDP) header of a network packet. The <b>SupportedIPv6HeaderFields</b> member defines the various fields from the UDP header that can be inspected.</p>
<div class="alert"><b>Note</b>  This flag is supported in NDIS 6.30 and later.</div>
<div> </div>
</dd>
</dl>
</dd>

### -field <b>SupportedMacHeaderFields</b>

<dd>
<p>A bitwise OR of flags that specify the types of MAC header fields that a
     miniport driver can inspect. The following flags are defined:
     </p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_FILTER_MAC_HEADER_DEST_ADDR_SUPPORTED"></a><a id="ndis_receive_filter_mac_header_dest_addr_supported"></a>NDIS_RECEIVE_FILTER_MAC_HEADER_DEST_ADDR_SUPPORTED

<dd>
<p>The network adapter supports inspecting and filtering that are based on the destination MAC
       address in the MAC header.</p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, miniport drivers that support the VMQ or SR-IOV interface must set this flag.</div>
<div> </div>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_MAC_HEADER_SOURCE_ADDR_SUPPORTED"></a><a id="ndis_receive_filter_mac_header_source_addr_supported"></a>NDIS_RECEIVE_FILTER_MAC_HEADER_SOURCE_ADDR_SUPPORTED

<dd>
<p>The network adapter supports inspecting and filtering that are based on the source MAC address
       in the MAC header.</p>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_MAC_HEADER_PROTOCOL_SUPPORTED"></a><a id="ndis_receive_filter_mac_header_protocol_supported"></a>NDIS_RECEIVE_FILTER_MAC_HEADER_PROTOCOL_SUPPORTED

<dd>
<p>The network adapter supports inspecting and filtering that are based on the EtherType identifier
       in the MAC header. For example, the EtherType identifier for IPv4 packets is 0x0800.</p>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_MAC_HEADER_VLAN_ID_SUPPORTED"></a><a id="ndis_receive_filter_mac_header_vlan_id_supported"></a>NDIS_RECEIVE_FILTER_MAC_HEADER_VLAN_ID_SUPPORTED

<dd>
<p>The network adapter supports inspecting and filtering that are based on the VLAN identifier in
       the MAC header.</p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, this flag is optional. If the miniport driver does not set this flag, the network adapter should inspect and filter the specified MAC address fields. If a VLAN tag is present in the received packet, the network adapter must remove it from the packet data. The miniport driver must   put the VLAN tag in an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566565">NDIS_NET_BUFFER_LIST_8021Q_INFO</a> structure that is associated with the packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</div>
<div> </div>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_MAC_HEADER_PRIORITY_SUPPORTED"></a><a id="ndis_receive_filter_mac_header_priority_supported"></a>NDIS_RECEIVE_FILTER_MAC_HEADER_PRIORITY_SUPPORTED

<dd>
<p>The network adapter supports inspecting and filtering that are based on the priority tag in the
       MAC header.</p>
</dd>

### -field <a id="NDIS_RECEIVE_FILTER_MAC_HEADER_PACKET_TYPE_SUPPORTED"></a><a id="ndis_receive_filter_mac_header_packet_type_supported"></a>NDIS_RECEIVE_FILTER_MAC_HEADER_PACKET_TYPE_SUPPORTED

<dd>
<p>The network adapter supports inspecting and filtering that are based on the packet type field of the IEEE 802.2 subnetwork access protocol (SNAP) header in an 802.3 MAC header.</p>
<div class="alert"><b>Note</b>  This flag is supported in NDIS 6.30 and later.</div>
<div> </div>
</dd>
</dl>
</dd>

### -field <b>MaxMacHeaderFilters</b>

<dd>
<p>The maximum number of MAC header filters that the miniport driver
     supports.</p>
</dd>

### -field <b>MaxQueueGroups</b>

<dd>
<p>This member is reserved for NDIS.</p>
</dd>

### -field <b>MaxQueuesPerQueueGroup</b>

<dd>
<p>This member is reserved for NDIS.</p>
</dd>

### -field <b>MinLookaheadSplitSize</b>

<dd>
<p>The minimum size, in bytes, that the network adapter supports for lookahead
     packet buffers.</p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported. Miniport drivers that support this version of NDIS must set this member to zero.</div>
<div> </div>
</dd>

### -field <b>MaxLookaheadSplitSize</b>

<dd>
<p>The maximum size, in bytes, that the network adapter supports for lookahead
     packet buffers.</p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported. Miniport drivers that support this version of NDIS must set this member to zero.</div>
<div> </div>
</dd>

### -field <b>SupportedARPHeaderFields</b>

<dd>
<p>A bitwise OR of flags that specify the types of ARP header fields that a
     miniport driver can inspect. The following flags are defined:
     </p>
<p></p>
<dl>

### -field <a id="NDIS_RECEIVE_FILTER_ARP_HEADER_OPERATION_SUPPORTED"></a><a id="ndis_receive_filter_arp_header_operation_supported"></a>NDIS_RECEIVE_FILTER_ARP_HEADER_OPERATION_SUPPORTED

<dd>
<p>The network adapter supports receive filtering on the ARP operation field.</p>
</dd>

### -field <a id="_NDIS_RECEIVE_FILTER_ARP_HEADER_SPA_SUPPORTED"></a><a id="_ndis_receive_filter_arp_header_spa_supported"></a>	NDIS_RECEIVE_FILTER_ARP_HEADER_SPA_SUPPORTED

<dd>
<p>The network adapter supports receive filtering on the ARP source protocol address (SPA) field.</p>
</dd>

### -field <a id="_NDIS_RECEIVE_FILTER_ARP_HEADER_TPA_SUPPORTED"></a><a id="_ndis_receive_filter_arp_header_tpa_supported"></a>	NDIS_RECEIVE_FILTER_ARP_HEADER_TPA_SUPPORTED

<dd>
<p>The network adapter supports receive filtering on the ARP target protocol address (TPA) field.</p>
</dd>
</dl>
</dd>

### -field <b>SupportedIPv4HeaderFields</b>

<dd>
<p>A bitwise OR of flags that specify the types of IPv4 header fields that a
     miniport driver can inspect. The following flags are defined:
     </p>
<p></p>
<dl>

### -field <a id="_NDIS_RECEIVE_FILTER_IPV4_HEADER_PROTOCOL_SUPPORTED"></a><a id="_ndis_receive_filter_ipv4_header_protocol_supported"></a>	NDIS_RECEIVE_FILTER_IPV4_HEADER_PROTOCOL_SUPPORTED

<dd>
<p>The network adapter supports receive filtering on the IPv4 protocol field.</p>
</dd>
</dl>
</dd>

### -field <b>SupportedIPv6HeaderFields</b>

<dd>
<p>A bitwise OR of flags that specify the types of IPv6 header fields that a
     miniport driver can inspect. The following flags are defined:
     </p>
<p></p>
<dl>

### -field <a id="_NDIS_RECEIVE_FILTER_IPV6_HEADER_PROTOCOL_SUPPORTED"></a><a id="_ndis_receive_filter_ipv6_header_protocol_supported"></a>	NDIS_RECEIVE_FILTER_IPV6_HEADER_PROTOCOL_SUPPORTED

<dd>
<p>The network adapter supports receive filtering on the IPv6 protocol field.</p>
</dd>
</dl>
</dd>

### -field <b>SupportedUdpHeaderFields</b>

<dd>
<p>A bitwise OR of flags that specify the types of IPv6 header fields that a
     miniport driver can inspect. The following flags are defined:
     </p>
<p></p>
<dl>

### -field <a id="_NDIS_RECEIVE_FILTER_UDP_HEADER_DEST_PORT_SUPPORTED"></a><a id="_ndis_receive_filter_udp_header_dest_port_supported"></a>	NDIS_RECEIVE_FILTER_UDP_HEADER_DEST_PORT_SUPPORTED

<dd>
<p>The network adapter supports receive filtering on the UDP destination port field.</p>
<div class="alert"><b>Note</b>  If the received UDP packet contains IPv4  options or IPv6 extension headers, the network adapter can automatically drop the  received packet and treat it as if it failed the UDP filter test.</div>
<div> </div>
</dd>
</dl>
</dd>

### -field <b>MaxFieldTestsPerPacketCoalescingFilter</b>

<dd>
<p>The maximum number of tests on packet header fields that can be specified for a single packet coalescing filter. For more information about packet coalescing, see <a href="NULL">NDIS Packet Coalescing</a>.</p>
<div class="alert"><b>Note</b>  Network adapters that support packet coalescing must support five or more packet header fields that can be specified for a single packet coalescing filter. If the adapter does not support packet coalescing, the miniport driver must set this value to zero.</div>
<div> </div>
</dd>

### -field <b>MaxPacketCoalescingFilters</b>

<dd>
<p>The maximum number of packet coalescing receive filters that are supported by the network adapter.</p>
<div class="alert"><b>Note</b>  Network adapters that support packet coalescing must support ten or more packet coalescing filters. If the adapter does not support packet coalescing, the miniport driver must set this value to zero.</div>
<div> </div>
</dd>

### -field <b>NdisReserved</b>

<dd>
<p>Reserved. Set to 0.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_RECEIVE_FILTER_CAPABILITIES</b> structure is used in the 
    <b>ReceiveFilterCapabilities</b> member of the 
    <a href="https://msdn.microsoft.com/b0662a2c-feb6-4d66-89c9-586c2859b78b">
    NDIS_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES</a>, 
    <a href="https://msdn.microsoft.com/d46a1e62-9d03-4ab9-86f6-81b06c04d0f6">
    NDIS_FILTER_ATTACH_PARAMETERS</a>, and 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564832">NDIS_BIND_PARAMETERS</a> structures and the
    return result of the 
    <a href="netvista.oid_receive_filter_hardware_capabilities">
    OID_RECEIVE_FILTER_HARDWARE_CAPABILITIES</a> OID query.</p>

<p>Many of the members and flag settings of the <b>NDIS_RECEIVE_FILTER_CAPABILITIES</b> structure are valid only if the miniport driver is enabled to use the VMQ or SR-IOV interface. The miniport driver is enabled to use these interfaces through standardized INF keywords. For more information, see <a href="netvista.handling_sr-iov__vmq__and_rss_standardized_inf_keywords">Handling SR-IOV, VMQ, and RSS Standardized INF Keywords</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564832">NDIS_BIND_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565481">NDIS_FILTER_ATTACH_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b0662a2c-feb6-4d66-89c9-586c2859b78b">
   NDIS_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567204">NDIS_RECEIVE_QUEUE_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567211">NDIS_RECEIVE_QUEUE_PARAMETERS</a>
</dt>
<dt>
<a href="netvista.oid_receive_filter_hardware_capabilities">
   OID_RECEIVE_FILTER_HARDWARE_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RECEIVE_FILTER_CAPABILITIES structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
