---
UID: NF.ndis.NdisMEnableVirtualization
title: NdisMEnableVirtualization
author: windows-driver-content
description: A miniport driver calls the NdisMEnableVirtualization function during the creation or deletion of a NIC switch on the network adapter.
old-location: netvista\ndismenablevirtualization.htm
old-project: netvista
ms.assetid: 5a82dfe6-8844-4b18-8f54-7bf143fcd2ff
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisMEnableVirtualization
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMEnableVirtualization
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisMEnableVirtualization function



## -description
<p>A miniport driver calls the <b>NdisMEnableVirtualization</b> function during the creation or deletion of a NIC switch on the network adapter. By calling this function, the driver configures the single root I/O virtualization (SR-IOV) Extended Capability structure in the PCI Express (PCIe) configuration space for the network adapter's Physical Function (PF).</p>


## -syntax

````
NDIS_STATUS NdisMEnableVirtualization(
  _In_ NDIS_HANDLE NdisMiniportHandle,
  _In_ USHORT      NumVFs,
  _In_ BOOLEAN     EnableVFMigration,
  _In_ BOOLEAN     EnableMigrationInterrupt,
  _In_ BOOLEAN     EnableVirtualization
);
````


## -parameters
<dl>

### -param <i>NdisMiniportHandle</i> [in]

<dd>
<p>The network adapter handle that NDIS passed to the 
     <i>MiniportAdapterHandle</i> parameter of 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>.</p>
</dd>

### -param <i>NumVFs</i> [in]

<dd>
<p>A USHORT value that contains the number of  Virtual Functions (VFs) that are to be enabled for the network adapter.  <b>NdisMEnableVirtualization</b> sets the <b>NumVFs</b> member of the SR-IOV Extended Capability structure to the value of the <i>NumVFs</i> parameter. </p>
<div class="alert"><b>Note</b>  If the <i>EnableVirtualization</i> parameter is FALSE, <i>NumVFs</i> must be set to zero.</div>
<div> </div>
</dd>

### -param <i>EnableVFMigration</i> [in]

<dd>
<p> This parameter is reserved for NDIS and must be set to FALSE.</p>
</dd>

### -param <i>EnableMigrationInterrupt</i> [in]

<dd>
<p> This parameter is reserved for NDIS and must be set to FALSE.</p>
</dd>

### -param <i>EnableVirtualization</i> [in]

<dd>
<p>A BOOLEAN value that specifies whether  virtualization should be enabled in the PCI configuration space of the network adapter.  If <i>EnableVirtualization</i> is TRUE, <b>NdisMEnableVirtualization</b> sets the <b>VF Enable</b> bit  of the SR-IOV Control member. <b>NdisMEnableVirtualization</b> clears this bit if <i>EnableVirtualization</i> is FALSE.</p>
</dd>
</dl>

## -returns
<p><b>NdisMEnableVirtualization</b> can return one of the following status values.</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The virtualization operation completed successfully.</p><dl>
<dt><b>NDIS_STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The adapter or system does not support SR-IOV.</p><dl>
<dt><b>NDIS_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>EnableVirtualization</i> parameter is set to FALSE and the <i>NumVFs</i> parameter is set to a nonzero value.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>The virtualization operation failed.</p>

<p> </p>

## -remarks
<p>PF miniport drivers call <b>NdisMEnableVirtualization</b> to configure the SR-IOV Extended Capability fields in the PCI configuration space. This call is used to enable or disable virtualization in the configuration space, and also to specify the number of VFs that should be exposed to the PCIe  fabric  by the network adapter.</p>

<p>When the PF miniport driver handles an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451815">OID_NIC_SWITCH_CREATE_SWITCH</a>, the driver calls <b>NdisMEnableVirtualization</b> to enable virtualization on the network adapter for the NIC switch. The driver does this by calling <b>NdisMEnableVirtualization</b> with the following parameter settings.</p>

<p></p>

<p><a id="NumVFs"></a><a id="numvfs"></a><a id="NUMVFS"></a><i>NumVFs</i></p>

<p>Set to the number of VFs to be enabled for the NIC switch.</p>

<p><a id="EnableVirtualization"></a><a id="enablevirtualization"></a><a id="ENABLEVIRTUALIZATION"></a><i>EnableVirtualization</i></p>

<p>Set to TRUE.</p>

<p>When the PF miniport driver handles an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451817">OID_NIC_SWITCH_DELETE_SWITCH</a>, the driver calls <b>NdisMEnableVirtualization</b> to disable virtualization on the network adapter. The driver does this by calling <b>NdisMEnableVirtualization</b> with the following parameter settings:</p>

<p>Set to zero.</p>

<p>Set to FALSE.</p>

<p>For more information on how to create a NIC switch, see <a href="NULL">Creating a NIC Switch</a>.</p>

<p>For more information about the SR-IOV interface, see 	<a href="NULL">Overview of Single Root I/O Virtualization (SR-IOV)</a>.</p>

<p>If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV <a href="devinst.driver_packages">driver package</a>, its miniport driver must not call <b>NdisMEnableVirtualization</b>. Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call <a href="..\wdm\nc-wdm-enable-virtualization.md">EnableVirtualization</a>. This function is provided by the <a href="kernel.guid_pci_virtualization_interface">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface that is supported by the underlying PCI bus driver. </p>

<p>The VBD that runs in the Hyper-V parent partition's management operating system can query the <a href="kernel.guid_pci_virtualization_interface">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface by issuing an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> request to its physical device object (PDO) on the PCI bus. This request must be made from IRQL = PASSIVE_LEVEL. In this request, the driver must  set the <i>InterfaceType</i> parameter to GUID_PCI_VIRTUALIZATION_INTERFACE.</p>

## -requirements
<table>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="..\wdm\nc-wdm-enable-virtualization.md">EnableVirtualization</a>
</dt>
<dt>
<a href="kernel.guid_pci_virtualization_interface">GUID_PCI_VIRTUALIZATION_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451815">OID_NIC_SWITCH_CREATE_SWITCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451817">OID_NIC_SWITCH_DELETE_SWITCH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMEnableVirtualization function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
