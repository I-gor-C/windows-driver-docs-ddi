---
UID: NS.ntddndis._NDIS_NIC_SWITCH_CAPABILITIES
title: NDIS_NIC_SWITCH_CAPABILITIES
author: windows-driver-content
description: The NDIS_NIC_SWITCH_CAPABILITIES structure specifies the capabilities of a NIC switch on the network adapter.
old-location: netvista\ndis_nic_switch_capabilities.htm
old-project: netvista
ms.assetid: bc4b56bd-583f-4b41-b5a7-90958ce65f42
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_NIC_SWITCH_CAPABILITIES, NDIS_NIC_SWITCH_CAPABILITIES, *PNDIS_NIC_SWITCH_CAPABILITIES
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
req.alt-api: NDIS_NIC_SWITCH_CAPABILITIES
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

# NDIS_NIC_SWITCH_CAPABILITIES structure



## -description
<p>The <b>NDIS_NIC_SWITCH_CAPABILITIES</b> structure specifies the capabilities of a NIC switch on the network adapter.</p>


## -syntax

````
typedef struct _NDIS_NIC_SWITCH_CAPABILITIES {
  NDIS_OBJECT_HEADER Header;
  ULONG              Flags;
  ULONG              NdisReserved1;
  ULONG              NumTotalMacAddresses;
  ULONG              NumMacAddressesPerPort;
  ULONG              NumVlansPerPort;
  ULONG              NdisReserved2;
  ULONG              NdisReserved3;
#if (NDIS_SUPPORT_NDIS630)
  ULONG              NicSwitchCapabilities;
  ULONG              MaxNumSwitches;
  ULONG              MaxNumVPorts;
  ULONG              NdisReserved4;
  ULONG              MaxNumVFs;
  ULONG              MaxNumQueuePairs;
  ULONG              NdisReserved5;
  ULONG              NdisReserved6;
  ULONG              NdisReserved7;
  ULONG              MaxNumQueuePairsPerNonDefaultVPort;
  ULONG              NdisReserved8;
  ULONG              NdisReserved9;
  ULONG              NdisReserved10;
  ULONG              NdisReserved11;
  ULONG              NdisReserved12;
  ULONG              MaxNumMacAddresses;
  ULONG              NdisReserved13;
  ULONG              NdisReserved14;
  ULONG              NdisReserved15;
  ULONG              NdisReserved16;
  ULONG              NdisReserved17;
#endif 
#if (NDIS_SUPPORT_NDIS660)
  ULONG              MaxNumRssCapableNonDefaultPFVPorts;
  ULONG              NumberOfIndirectionTableEntriesForDefaultVPort;
  ULONG              NumberOfIndirectionTableEntriesPerNonDefaultPFVPort;
  ULONG              MaxNumQueuePairsForDefaultVPort;
#endif 
} NDIS_NIC_SWITCH_CAPABILITIES, *PNDIS_NIC_SWITCH_CAPABILITIES;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_NIC_SWITCH_CAPABILITIES</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_NIC_SWITCH_CAPABILITIES</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to one of the following values: </p>
<p></p>
<dl>

### -field <a id="NDIS_NIC_SWITCH_CAPABILITIES_REVISION_3"></a><a id="ndis_nic_switch_capabilities_revision_3"></a>NDIS_NIC_SWITCH_CAPABILITIES_REVISION_3

<dd>
<p>Added the RSS interface members for NDIS 6.60.<div class="alert"><b>Note</b>  Revision 3 of this structure is  supported only on Windows Server 2016  and later versions of Windows Server.</div>
<div> </div>
</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NIC_SWITCH_CAPABILITIES_REVISION_3.</p>
</dd>

### -field <a id="NDIS_NIC_SWITCH_CAPABILITIES_REVISION_2"></a><a id="ndis_nic_switch_capabilities_revision_2"></a>NDIS_NIC_SWITCH_CAPABILITIES_REVISION_2

<dd>
<p>Added the single root I/O virtualization (SR-IOV) interface members for NDIS 6.30.<div class="alert"><b>Note</b>  Revision 2 of this structure is  supported only on Windows Server 2012 and later versions of Windows Server.</div>
<div> </div>
</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NIC_SWITCH_CAPABILITIES_REVISION_2.</p>
</dd>

### -field <a id="NDIS_NIC_SWITCH_CAPABILITIES_REVISION_1"></a><a id="ndis_nic_switch_capabilities_revision_1"></a>NDIS_NIC_SWITCH_CAPABILITIES_REVISION_1

<dd>
<p>Original version for NDIS 6.20.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NIC_SWITCH_CAPABILITIES_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A ULONG value that contains a bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>NdisReserved1</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>NumTotalMacAddresses</b>

<dd>
<p>A ULONG value that contains the total number of media access control (MAC) addresses that the network adapter supports.</p>
<div class="alert"><b>Note</b>  Drivers must set this member to zero for revision 2 and later revisions of this structure.</div>
<div> </div>
</dd>

### -field <b>NumMacAddressesPerPort</b>

<dd>
<p>A ULONG value that contains the number of MAC addresses that are supported for each port.</p>
<div class="alert"><b>Note</b>  Drivers must set this member to zero for revision 2 and later revisions of this structure.</div>
<div> </div>
</dd>

### -field <b>NumVlansPerPort</b>

<dd>
<p>A ULONG value that contains the number of VLANs that are supported for each port.</p>
<div class="alert"><b>Note</b>  Drivers must set this member to zero for revision 2 and later revisions of this structure.</div>
<div> </div>
</dd>

### -field <b>NdisReserved2</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>NdisReserved3</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>NicSwitchCapabilities</b>

<dd>
<p>A ULONG value that contains a bitwise OR of the following flags that specify the capabilities of the NIC switch: </p>
<p></p>
<dl>

### -field <a id="NDIS_NIC_SWITCH_CAPS_VLAN_SUPPORTED"></a><a id="ndis_nic_switch_caps_vlan_supported"></a>NDIS_NIC_SWITCH_CAPS_VLAN_SUPPORTED

<dd>
<p>This flag specifies that the NIC switch supports hardware packet filtering based on the virtual local area network (VLAN) identifier (ID). </p>
<div class="alert"><b>Note</b>  This flag should be set only if the NIC switch supports VLAN ID filtering on individual SR-IOV virtual ports (VPorts).</div>
<div> </div>
</dd>

### -field <a id="NDIS_NIC_SWITCH_CAPS_PER_VPORT_INTERRUPT_MODERATION_SUPPORTED"></a><a id="ndis_nic_switch_caps_per_vport_interrupt_moderation_supported"></a>NDIS_NIC_SWITCH_CAPS_PER_VPORT_INTERRUPT_MODERATION_SUPPORTED

<dd>
<p>This flag specifies that the NIC switch can support interrupt moderation configuration on individual VPorts. </p>
</dd>

### -field <a id="NDIS_NIC_SWITCH_CAPS_ASYMMETRIC_QUEUE_PAIRS_FOR_NONDEFAULT_VPORT_SUPPORTED"></a><a id="ndis_nic_switch_caps_asymmetric_queue_pairs_for_nondefault_vport_supported"></a>NDIS_NIC_SWITCH_CAPS_ASYMMETRIC_QUEUE_PAIRS_FOR_NONDEFAULT_VPORT_SUPPORTED

<dd>
<p>This flag specifies that the NIC switch can configure a different number of queue pairs for each nondefault VPort. This means that each nondefault VPort can be configured asymmetrically to have a different number of queue pairs. </p>
<p>If this flag is not set, all nondefault VPorts must be configured symmetrically to have the same number of queue pairs. </p>
<p>Regardless of whether this flag is set, the NIC switch must support the ability to set the number of queue pairs on the default VPort. These may differ from the number of queue-pairs that are set on the nondefault VPorts.</p>
<div class="alert"><b>Note</b>  A queue pair consists of a transmit queue and receive queue. Queue pairs associated with the default VPort are configured at the time of switch creation through an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451815">OID_NIC_SWITCH_CREATE_SWITCH</a>.
One or more queue pairs are configured on a nondefault VPort through an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>.
</div>
<div> </div>
<p>For more information, see <a href="NULL">Symmetric and Asymmetric Assignment of Queue Pairs</a>.</p>
<p></p>
</dd>

### -field <a id="NDIS_NIC_SWITCH_CAPS_VF_RSS_SUPPORTED"></a><a id="ndis_nic_switch_caps_vf_rss_supported"></a>NDIS_NIC_SWITCH_CAPS_VF_RSS_SUPPORTED

<dd>
<p>This flag specifies that queue pairs from nondefault VPorts that are attached to a PCI Express (PCIe) Virtual Function (VF) can be used for receive side scaling (RSS). The VF miniport driver runs in the guest operating system of a Hyper-V child partition. </p>
<p>If this flag is set, the miniport driver supports RSS on a VF and can use  one or more of the queue pairs from the nondefault VPort for RSS.</p>
<div class="alert"><b>Note</b>  Starting with Windows Server 2012, only one nondefault VPort can be attached to a VF.</div>
<div> </div>
</dd>

### -field <a id="NDIS_NIC_SWITCH_CAPS_SINGLE_VPORT_POOL"></a><a id="ndis_nic_switch_caps_single_vport_pool"></a>NDIS_NIC_SWITCH_CAPS_SINGLE_VPORT_POOL

<dd>
<p>This flag specifies that the nondefault VPorts can be created in a non-reserved manner from the VPort pool on the network adapter. This allows available nondefault VPorts to be created and assigned on an as-needed basis to the PF and allocated VFs. If the network adapter supports the virtual machine queue (VMQ) interface, nondefault VPorts that are assigned to the PF can also be used for VM receive queues.</p>
<div class="alert"><b>Note</b>  The default VPort is always reserved for assignment to the PF.</div>
<div> </div>
<p>If this flag is set, available nondefault VPorts are created and assigned to the PF and allocated VFs. However, this mechanism does not reserve nondefault VPorts for VF creation and assignment. As a result, situations may occur where a VF may not be assigned a VPort if the pool has been exhausted of available VPorts.</p>
<div class="alert"><b>Note</b>  If a VF cannot be assigned a VPort, packet traffic over the VF occurs over the SR-IOV synthetic data path. For more information about this data path, see <a href="NULL">SR-IOV Data Paths</a>.</div>
<div> </div>
<p>If this flag is not set, the creation and assignment of nondefault VPorts is reserved for VF assignment.  Additional nondefault VPorts  can be created and assigned to the PF. </p>
<p>For more information about VMQ, see <a href="NULL">Virtual Machine Queue (VMQ)</a>.</p>
<p>For more information about VPorts, see <a href="NULL">Managing Virtual Ports</a>.
</p>
</dd>
</dl>
</dd>

### -field <b>MaxNumSwitches</b>

<dd>
<p>A ULONG value that specifies the maximum number of switches that can be created on the network adapter's PCI Express (PCIe) Physical Function (PF).</p>
<div class="alert"><b>Note</b>  Starting with Windows Server 2012, Windows only supports the default NIC switch on the network adapter. Therefore, this member must always be set to one. 
</div>
<div> </div>
</dd>

### -field <b>MaxNumVPorts</b>

<dd>
<p>A ULONG value that specifies the maximum number of VPorts that can be created on a network adapter. This includes the default VPort that is always attached to the PF. </p>
<div class="alert"><b>Note</b>  The NIC switch must support at least (<b>MaxNumVFs</b> + 1) VPorts.</div>
<div> </div>
</dd>

### -field <b>NdisReserved4</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>MaxNumVFs</b>

<dd>
<p>A ULONG value that specifies the maximum number of VFs that can be created on the NIC switch. </p>
<div class="alert"><b>Note</b>  Depending on the available hardware resources on the network adapter, the miniport driver can set the <b>MaxNumVFs</b> member to a value that is less than its <b>*NumVFs</b>
keyword. For more information about this keyword, see <a href="NULL">Standardized INF Keywords for SR-IOV</a>.</div>
<div> </div>
</dd>

### -field <b>MaxNumQueuePairs</b>

<dd>
<p>A ULONG value that specifies the maximum number of queue pairs that can be assigned to all VPorts. This includes the default VPort that is attached to the PF.</p>
<div class="alert"><b>Note</b>  This value must be greater than or equal to the value of <b>MaxNumVPorts</b>.</div>
<div> </div>
</dd>

### -field <b>NdisReserved5</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>NdisReserved6</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>NdisReserved7</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>MaxNumQueuePairsPerNonDefaultVPort</b>

<dd>
<p>A ULONG value that specifies the maximum number of queue pairs that can be assigned to a nondefault VPort. </p>
<p>This value is specified in powers of 2, and provides for asymmetric configuration and assignment of queue pairs to VPorts. For more information, see <a href="NULL">Symmetric and Asymmetric Assignment of Queue Pairs</a>.</p>
</dd>

### -field <b>NdisReserved8</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>NdisReserved9</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>NdisReserved10</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>NdisReserved11</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>NdisReserved12</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>MaxNumMacAddresses</b>

<dd>
<p>A ULONG value that specifies the maximum number of unicast MAC address filters that are available on the NIC switch.  </p>
<div class="alert"><b>Note</b>  This value must be greater than or equal to the value of <b>MaxNumVPorts</b>. This enables each VPort (including the default VPort) to be configured to have at least one unicast MAC address filter.</div>
<div> </div>
</dd>

### -field <b>NdisReserved13</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>NdisReserved14</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>NdisReserved15</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>NdisReserved16</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>NdisReserved17</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>MaxNumRssCapableNonDefaultPFVPorts</b>

<dd>
<p>A ULONG value that specifies the maximum number of RSS-capable non-default PFVPorts. </p>
</dd>

### -field <b>NumberOfIndirectionTableEntriesForDefaultVPort</b>

<dd>
<p>A ULONG value that specifies the number of indirection table entries for the default VPort.</p>
</dd>

### -field <b>NumberOfIndirectionTableEntriesPerNonDefaultPFVPort</b>

<dd>
<p>A ULONG value that specifies the number of indirection table entries for each non-default PFVPort.</p>
</dd>

### -field <b>MaxNumQueuePairsForDefaultVPort</b>

<dd>
<p>A ULONG value that specifies the maximum number of queue pairs that can be assigned to the default VPort. </p>
<p>This value is specified in powers of 2, and provides for asymmetric configuration and assignment of queue pairs to VPorts. For more information, see <a href="NULL">Symmetric and Asymmetric Assignment of Queue Pairs</a>.</p>
</dd>
</dl>

## -remarks
<p>
    The <b>NDIS_NIC_SWITCH_CAPABILITIES</b> structure is used in the 
    members of the following structures:</p>

<p>The <b>HardwareNicSwitchCapabilities</b> and 
    <b>CurrentNicSwitchCapabilities</b> members of the 
    <a href="..\ndis\ns-ndis--ndis-miniport-adapter-hardware-assist-attributes.md">
    NDIS_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES</a> structure.</p>

<p>The 
    <b>NicSwitchCapabilities</b> member of the 
    <a href="..\ndis\ns-ndis--ndis-filter-attach-parameters.md">
    NDIS_FILTER_ATTACH_PARAMETERS</a> and 
    <a href="..\ndis\ns-ndis--ndis-bind-parameters.md">NDIS_BIND_PARAMETERS</a> structures. </p>

<p>OID query requests of <a href="netvista.oid_nic_switch_current_capabilities">
    OID_NIC_SWITCH_CURRENT_CAPABILITIES</a> and 
    <a href="netvista.oid_nic_switch_hardware_capabilities">
    OID_NIC_SWITCH_HARDWARE_CAPABILITIES</a> return an <b>NDIS_NIC_SWITCH_CAPABILITIES</b> structure.</p>

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
<dt><b></b></dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-bind-parameters.md">NDIS_BIND_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-filter-attach-parameters.md">NDIS_FILTER_ATTACH_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-adapter-hardware-assist-attributes.md">NDIS_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569760">OID_NIC_SWITCH_CURRENT_CAPABILITIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569761">OID_NIC_SWITCH_HARDWARE_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NIC_SWITCH_CAPABILITIES structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
