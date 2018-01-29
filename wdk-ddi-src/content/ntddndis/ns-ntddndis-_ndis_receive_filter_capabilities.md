---
UID : NS:ntddndis._NDIS_RECEIVE_FILTER_CAPABILITIES
title : _NDIS_RECEIVE_FILTER_CAPABILITIES
author : windows-driver-content
description : The NDIS_RECEIVE_FILTER_CAPABILITIES structure specifies the receive filtering capabilities of a network adapter.
old-location : netvista\ndis_receive_filter_capabilities.htm
old-project : netvista
ms.assetid : aecc1fe0-03f9-44be-9a38-b689eee4c5a6
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : virtual_machine_queue_ref_51c84771-6803-4059-9011-df2d870614a0.xml, NDIS_RECEIVE_FILTER_CAPABILITIES, PNDIS_RECEIVE_FILTER_CAPABILITIES structure pointer [Network Drivers Starting with Windows Vista], NDIS_RECEIVE_FILTER_CAPABILITIES structure [Network Drivers Starting with Windows Vista], PNDIS_RECEIVE_FILTER_CAPABILITIES, ntddndis/NDIS_RECEIVE_FILTER_CAPABILITIES, ntddndis/PNDIS_RECEIVE_FILTER_CAPABILITIES, _NDIS_RECEIVE_FILTER_CAPABILITIES, netvista.ndis_receive_filter_capabilities, *PNDIS_RECEIVE_FILTER_CAPABILITIES
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.20 and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : NDIS_RECEIVE_FILTER_CAPABILITIES, *PNDIS_RECEIVE_FILTER_CAPABILITIES
---

# _NDIS_RECEIVE_FILTER_CAPABILITIES structure
The <b>NDIS_RECEIVE_FILTER_CAPABILITIES</b> structure specifies the  receive filtering capabilities of a
  network adapter.

NDIS receive filters are used in the following NDIS interfaces:
<ul>
<li>

<a href="https://msdn.microsoft.com/500FBF0F-54D9-4675-8E2D-447387DA8798">NDIS Packet Coalescing</a>. For more information about how to use receive filters in this interface, see <a href="https://msdn.microsoft.com/20EA71E0-B880-4891-A12E-76F4C9AB16E6">Managing Packet Coalescing Receive Filters</a>.

</li>
<li>

<a href="https://msdn.microsoft.com/E64DD4F0-D5F8-4FFF-931B-C04C5C42D000">Single Root I/O Virtualization (SR-IOV)</a>. For more information about how to use receive filters in this interface, see <a href="https://msdn.microsoft.com/F0137D59-1701-4DFC-BB30-27E477FC0706">Setting a Receive Filter on a Virtual Port</a>.

</li>
<li>

<a href="https://msdn.microsoft.com/c502c7d6-bdf1-4656-b5a5-339250910f08">Virtual Machine Queue (VMQ)</a>. For more information about how to use receive filters in this interface, see <a href="https://msdn.microsoft.com/bfee8a3c-d2be-4718-beb4-067b66756a41">Setting and Clearing VMQ Filters</a>.

</li>
</ul>

## Syntax
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

## Members


`EnabledFilterTypes`

A bitwise OR of flags that specify the types of receive filters that are enabled. The
     following filter type flag is valid.

`EnabledQueueTypes`

A bitwise OR of flags that specify the types of receive queues that are enabled. The
     following queue type flag is valid.

`Flags`

A bitwise OR of flags. This member is reserved for NDIS.

`Header`

The 
     <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_RECEIVE_FILTER_CAPABILITIES</b> structure. The driver sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT.

To indicate the version of the <b>NDIS_RECEIVE_FILTER_CAPABILITIES</b> structure, the driver sets the 
     <b>Revision</b> member to one of the following values:

`MaxFieldTestsPerPacketCoalescingFilter`

The maximum number of tests on packet header fields that can be specified for a single packet coalescing filter. For more information about packet coalescing, see <a href="https://msdn.microsoft.com/500FBF0F-54D9-4675-8E2D-447387DA8798">NDIS Packet Coalescing</a>.
<div class="alert"><b>Note</b>  Network adapters that support packet coalescing must support five or more packet header fields that can be specified for a single packet coalescing filter. If the adapter does not support packet coalescing, the miniport driver must set this value to zero.</div><div> </div>

`MaxLookaheadSplitSize`

The maximum size, in bytes, that the network adapter supports for lookahead
     packet buffers.
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported. Miniport drivers that support this version of NDIS must set this member to zero.</div><div> </div>

`MaxMacHeaderFilters`

The maximum number of MAC header filters that the miniport driver
     supports.

`MaxPacketCoalescingFilters`

The maximum number of packet coalescing receive filters that are supported by the network adapter.
<div class="alert"><b>Note</b>  Network adapters that support packet coalescing must support ten or more packet coalescing filters. If the adapter does not support packet coalescing, the miniport driver must set this value to zero.</div><div> </div>

`MaxQueueGroups`

This member is reserved for NDIS.

`MaxQueuesPerQueueGroup`

This member is reserved for NDIS.

`MinLookaheadSplitSize`

The minimum size, in bytes, that the network adapter supports for lookahead
     packet buffers.
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported. Miniport drivers that support this version of NDIS must set this member to zero.</div><div> </div>

`NdisReserved`

Reserved. Set to 0.

`NumQueues`

The number of VM queues that the network adapter supports.
<div class="alert"><b>Note</b>  If the miniport driver is enabled to use the SR-IOV interface, it must set this member to zero. When use of the SR-IOV interface is enabled, NDIS uses virtual ports (VPorts) for receive and transmit queues instead of VM queues.
</div><div> </div>

`SupportedARPHeaderFields`

A bitwise OR of flags that specify the types of ARP header fields that a
     miniport driver can inspect. The following flags are defined:

`SupportedFilterTests`

A bitwise OR of flags that specify the test operations that a miniport
     driver supports. The following flags are defined:

`SupportedHeaders`

A bitwise OR of flags that specify the types of network packet headers that
     a miniport driver can inspect. The following flags are defined:

`SupportedIPv4HeaderFields`

A bitwise OR of flags that specify the types of IPv4 header fields that a
     miniport driver can inspect. The following flags are defined:

`SupportedIPv6HeaderFields`

A bitwise OR of flags that specify the types of IPv6 header fields that a
     miniport driver can inspect. The following flags are defined:

`SupportedMacHeaderFields`

A bitwise OR of flags that specify the types of MAC header fields that a
     miniport driver can inspect. The following flags are defined:

`SupportedQueueProperties`

A bitwise OR of flags that specify the VM queue properties that the network adapter supports. The
     following flags are defined:

`SupportedUdpHeaderFields`

A bitwise OR of flags that specify the types of IPv6 header fields that a
     miniport driver can inspect. The following flags are defined:

## Remarks
The <b>NDIS_RECEIVE_FILTER_CAPABILITIES</b> structure is used in the 
    <b>ReceiveFilterCapabilities</b> member of the 
    <mshelp:link keywords="netvista.ndis_miniport_adapter_hardware_assist_attributes" tabindex="0"><b>
    NDIS_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES</b></mshelp:link>, 
    <mshelp:link keywords="netvista.ndis_filter_attach_parameters" tabindex="0"><b>
    NDIS_FILTER_ATTACH_PARAMETERS</b></mshelp:link>, and 
    <a href="..\ndis\ns-ndis-_ndis_bind_parameters.md">NDIS_BIND_PARAMETERS</a> structures and the
    return result of the 
    <mshelp:link keywords="netvista.oid_receive_filter_hardware_capabilities" tabindex="0">
    OID_RECEIVE_FILTER_HARDWARE_CAPABILITIES</mshelp:link> OID query.

Many of the members and flag settings of the <b>NDIS_RECEIVE_FILTER_CAPABILITIES</b> structure are valid only if the miniport driver is enabled to use the VMQ or SR-IOV interface. The miniport driver is enabled to use these interfaces through standardized INF keywords. For more information, see <a href="https://msdn.microsoft.com/EF556563-4097-4388-A563-29FC891AC626">Handling SR-IOV, VMQ, and RSS Standardized INF Keywords</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddndis.h (include Ndis.h) |

## See Also

<a href="..\ndis\ns-ndis-_ndis_bind_parameters.md">NDIS_BIND_PARAMETERS</a>

<mshelp:link keywords="netvista.oid_receive_filter_hardware_capabilities" tabindex="0">
   OID_RECEIVE_FILTER_HARDWARE_CAPABILITIES</mshelp:link>

<a href="..\ntddndis\ns-ntddndis-_ndis_receive_queue_info.md">NDIS_RECEIVE_QUEUE_INFO</a>

<a href="..\ntddndis\ns-ntddndis-_ndis_receive_queue_parameters.md">NDIS_RECEIVE_QUEUE_PARAMETERS</a>

<a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a>

<a href="..\ndis\ns-ndis-_ndis_filter_attach_parameters.md">NDIS_FILTER_ATTACH_PARAMETERS</a>

<mshelp:link keywords="netvista.ndis_miniport_adapter_hardware_assist_attributes" tabindex="0"><b>
   NDIS_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES</b></mshelp:link>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RECEIVE_FILTER_CAPABILITIES structure%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>