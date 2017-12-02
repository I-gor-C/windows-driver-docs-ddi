---
UID: NF.ndis.NdisMInvalidateConfigBlock
title: NdisMInvalidateConfigBlock
author: windows-driver-content
description: A miniport driver calls the NdisMInvalidateConfigBlock function to notify NDIS that the data for one or more Virtual Function (VF) configuration blocks has been changed.
old-location: netvista\ndisminvalidateconfigblock.htm
old-project: netvista
ms.assetid: 26D07A41-C431-41F1-9F5E-880B48CC2F0B
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NdisMInvalidateConfigBlock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMInvalidateConfigBlock
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisMInvalidateConfigBlock function



## -description
<p>A miniport driver calls the <b>NdisMInvalidateConfigBlock</b> function to notify NDIS that the data for one or more Virtual Function (VF) configuration blocks has been changed.</p>


## -syntax

````
VOID NdisMInvalidateConfigBlock(
  _In_ NDIS_HANDLE            NdisMiniportHandle,
  _In_ NDIS_SRIOV_FUNCTION_ID VFId,
  _In_ ULONGLONG              BlockMask
);
````


## -parameters
<dl>

### -param NdisMiniportHandle [in]

<dd>
<p>The network adapter handle that NDIS passed to the 
     <i>MiniportAdapterHandle</i> parameter of 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>.</p>
</dd>

### -param VFId [in]

<dd>
<p>The identifier of the VF for which the device location is returned.</p>
</dd>

### -param BlockMask [in]

<dd>
<p>A ULONGLONG value that specifies a bitmask for the first 64 VF configuration blocks. Each bit in the bitmask corresponds to a VF configuration block. If the bit is set to one, the data associated with the corresponding VF configuration block has changed.
</p>
</dd>
</dl>

## -returns
<p>
     None.</p>

## -remarks
<p>A VF configuration block is used for backchannel communication between the PF and VF miniport drivers. The IHV can define one or more VF configuration blocks for the device. Each VF configuration block has an IHV-defined format, length,  and block ID.</p>

<p>VF configuration data is exchanged between the following drivers:</p>

<p>The VF driver, which runs in the guest operating system. This operating system runs within a Hyper-V child partition.

</p>

<p>The PF driver, which runs in the management operating system.

This operating system runs within the Hyper-V parent partition.</p>

<p>In order to handle notifications of invalid VF configuration data, NDIS and the miniport drivers perform the following steps:</p>

<p>In the guest operating system, NDIS issues an I/O control request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh439301">IOCTL_VPCI_INVALIDATE_BLOCK</a> request. When this IOCTL is completed, NDIS is notified that VF configuration data has changed.</p>

<p>In the management operating system, the following steps occur:<ol>
<li>The PF miniport driver calls the <b>NdisMInvalidateConfigBlock</b> function to notify NDIS that VF configuration data has changed and is no longer valid. </li>
<li>
<p>NDIS signals the virtualization stack, which runs in the management operating system, about the change to VF configuration block data. The virtualization stack caches the <i>BlockMask</i> parameter data. </p>
<div class="alert"><b>Note</b>  Each time that the PF miniport driver calls <b>NdisMInvalidateConfigBlock</b>, the virtualization  stack ORs the <i>BlockMask</i> parameter data with the current value in its cache.</div>
<div> </div>
</li>
<li>
<p>The virtualization stack notifies the virtual PCI (VPCI) driver, which  runs in the guest operating system, about the invalidation of VF configuration data.  The virtualization stack sends the cached <i>BlockMask</i> parameter data to the VPCI driver.</p>
</li>
</ol>
</p>

<p>NDIS signals the virtualization stack, which runs in the management operating system, about the change to VF configuration block data. The virtualization stack caches the <i>BlockMask</i> parameter data. </p>

<p>The virtualization stack notifies the virtual PCI (VPCI) driver, which  runs in the guest operating system, about the invalidation of VF configuration data.  The virtualization stack sends the cached <i>BlockMask</i> parameter data to the VPCI driver.</p>

<p>In the guest operating system, the following steps occur:<ol>
<li>
<p>The VPCI driver saves the cached <i>BlockMask</i> parameter data in the <b>BlockMask</b> member of the <a href="..\vpci\ns-vpci--vpci-invalidate-block-output.md">VPCI_INVALIDATE_BLOCK_OUTPUT</a> structure that is associated with the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439301">IOCTL_VPCI_INVALIDATE_BLOCK</a> request.</p>
</li>
<li>
<p>The VPCI driver successfully completes  the  <a href="https://msdn.microsoft.com/library/windows/hardware/hh439301">IOCTL_VPCI_INVALIDATE_BLOCK</a> request. When this happens, NDIS issues an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451903">OID_SRIOV_VF_INVALIDATE_CONFIG_BLOCK</a>  to the VF miniport driver. An <a href="..\ntddndis\ns-ntddndis--ndis-sriov-vf-invalidate-config-block-info.md">NDIS_SRIOV_VF_INVALIDATE_CONFIG_BLOCK_INFO</a> request is passed along in the OID request. This structure contains the cached <i>BlockMask</i> parameter data.</p>
<p>NDIS also issues another <a href="https://msdn.microsoft.com/library/windows/hardware/hh439301">IOCTL_VPCI_INVALIDATE_BLOCK</a> request to handle successive notifications of changes to VF configuration data.</p>
</li>
<li>
<p>When the VF driver handles the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451903">OID_SRIOV_VF_INVALIDATE_CONFIG_BLOCK</a> request, it reads data from the specified VF configuration blocks.</p>
</li>
</ol>
</p>

<p>The VPCI driver saves the cached <i>BlockMask</i> parameter data in the <b>BlockMask</b> member of the <a href="..\vpci\ns-vpci--vpci-invalidate-block-output.md">VPCI_INVALIDATE_BLOCK_OUTPUT</a> structure that is associated with the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439301">IOCTL_VPCI_INVALIDATE_BLOCK</a> request.</p>

<p>The VPCI driver successfully completes  the  <a href="https://msdn.microsoft.com/library/windows/hardware/hh439301">IOCTL_VPCI_INVALIDATE_BLOCK</a> request. When this happens, NDIS issues an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451903">OID_SRIOV_VF_INVALIDATE_CONFIG_BLOCK</a>  to the VF miniport driver. An <a href="..\ntddndis\ns-ntddndis--ndis-sriov-vf-invalidate-config-block-info.md">NDIS_SRIOV_VF_INVALIDATE_CONFIG_BLOCK_INFO</a> request is passed along in the OID request. This structure contains the cached <i>BlockMask</i> parameter data.</p>

<p>NDIS also issues another <a href="https://msdn.microsoft.com/library/windows/hardware/hh439301">IOCTL_VPCI_INVALIDATE_BLOCK</a> request to handle successive notifications of changes to VF configuration data.</p>

<p>When the VF driver handles the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451903">OID_SRIOV_VF_INVALIDATE_CONFIG_BLOCK</a> request, it reads data from the specified VF configuration blocks.</p>

<p>For more information about backchannel communication within the single root I/O virtualization (SR-IOV) interface, see <a href="netvista.sr_iov_pf_vf_backchannel_communication">SR-IOV PF/VF Backchannel Communication</a>.</p>

<p>For more information about the SR-IOV interface, see 	<a href="netvista.overview_of_single_root_i_o_virtualization__sr-iov_">Overview of Single Root I/O Virtualization (SR-IOV)</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439301">IOCTL_VPCI_INVALIDATE_BLOCK</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-sriov-vf-invalidate-config-block-info.md">NDIS_SRIOV_VF_INVALIDATE_CONFIG_BLOCK_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451879">OID_SRIOV_READ_VF_CONFIG_SPACE</a>
</dt>
<dt>
<a href="..\vpci\ns-vpci--vpci-invalidate-block-output.md">VPCI_INVALIDATE_BLOCK_OUTPUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMInvalidateConfigBlock function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
