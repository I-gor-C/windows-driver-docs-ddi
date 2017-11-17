---
UID: NF.ndis.NdisMReadConfigBlock
title: NdisMReadConfigBlock
author: windows-driver-content
description: A miniport driver for a PCI Express (PCIe) Virtual Function (VF) calls the NdisMReadConfigBlock function to read data from a VF configuration block.
old-location: netvista\ndismreadconfigblock.htm
ms.assetid: a4b5e669-7abb-4c60-b2dc-249103d0b20c
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMReadConfigBlock
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
req.irql: <= APC_LEVEL
ms.keywords: NdisMReadConfigBlock
req.iface: 
---

# NdisMReadConfigBlock function



## -description
<p>A miniport driver for a PCI Express (PCIe) Virtual Function (VF) calls the <b>NdisMReadConfigBlock</b> function to read data from a VF configuration block.  Read operations for a VF configuration block are handled by the miniport driver of the network adapter's PCIe Physical Function (PF).</p>


## -syntax

````
NDIS_STATUS NdisMReadConfigBlock(
  _In_  NDIS_HANDLE NdisMiniportHandle,
  _In_  ULONG       BlockId,
  _Out_ PVOID       Buffer,
  _In_  ULONG       Length
);
````


## -parameters
<dl>

### -param <i>NdisMiniportHandle</i> [in]

<dd>
<p>The network adapter handle that NDIS passed to the 
     <i>MiniportAdapterHandle</i> parameter of 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>.</p>
</dd>

### -param <i>BlockId</i> [in]

<dd>
<p>A ULONG value that specifies the identifier of the VF configuration block to be read. This identifier is proprietary to the independent hardware vendor (IHV) and is used only by the PF and VF miniport drivers.
</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer that will contain the requested configuration data.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The number of bytes to be read from the VF configuration block.</p>
</dd>
</dl>

## -returns
<p><b>NdisMReadConfigBlock</b> can return one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The query operation completed successfully.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>The query operation failed.</p>

<p> </p>

## -remarks
<p>The VF miniport driver  calls <b>NdisMReadConfigBlock</b> to initiate a backchannel read request of VF configuration data by the PF miniport driver. Once notified of this request, the PF driver returns the data from the specified VF configuration block.</p>

<p>A VF configuration block is used for backchannel communication between the PF and VF miniport drivers. The IHV can define one or more VF configuration blocks for the device. Each VF configuration block has an IHV-defined format, length,  and block ID.</p>

<p>For more information about backchannel communication within the single root I/O virtualization (SR-IOV) interface, see <a href="NULL">SR-IOV PF/VF Backchannel Communication</a>.</p>

<p>For more information about the SR-IOV interface, see 	<a href="NULL">Overview of Single Root I/O Virtualization (SR-IOV)</a>.</p>

<p>If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV <a href="devinst.driver_packages">driver package</a>, its miniport driver must not call <b>NdisMReadConfigBlock</b>. Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call <a href="https://msdn.microsoft.com/library/windows/hardware/hh439637">ReadVfConfigBlock</a>. This function is exposed from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451146">GUID_VPCI_INTERFACE_STANDARD</a> interface that is supported by the underlying virtual PCI (VPCI) bus driver.</p>

<p>The VBD that runs in a Hyper-V child partition's guest operating system can query the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451146">GUID_VPCI_INTERFACE_STANDARD</a> interface by issuing an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> request to its physical device object (PDO) on the VPCI bus. This request must be made from IRQL = PASSIVE_LEVEL. In this request, the driver must  set the <i>InterfaceType</i> parameter to GUID_VPCI_INTERFACE_STANDARD.</p>

<p>The VF miniport driver  calls <b>NdisMReadConfigBlock</b> to initiate a backchannel read request of VF configuration data by the PF miniport driver. Once notified of this request, the PF driver returns the data from the specified VF configuration block.</p>

<p>A VF configuration block is used for backchannel communication between the PF and VF miniport drivers. The IHV can define one or more VF configuration blocks for the device. Each VF configuration block has an IHV-defined format, length,  and block ID.</p>

<p>For more information about backchannel communication within the single root I/O virtualization (SR-IOV) interface, see <a href="NULL">SR-IOV PF/VF Backchannel Communication</a>.</p>

<p>For more information about the SR-IOV interface, see 	<a href="NULL">Overview of Single Root I/O Virtualization (SR-IOV)</a>.</p>

<p>If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV <a href="devinst.driver_packages">driver package</a>, its miniport driver must not call <b>NdisMReadConfigBlock</b>. Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call <a href="https://msdn.microsoft.com/library/windows/hardware/hh439637">ReadVfConfigBlock</a>. This function is exposed from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451146">GUID_VPCI_INTERFACE_STANDARD</a> interface that is supported by the underlying virtual PCI (VPCI) bus driver.</p>

<p>The VBD that runs in a Hyper-V child partition's guest operating system can query the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451146">GUID_VPCI_INTERFACE_STANDARD</a> interface by issuing an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> request to its physical device object (PDO) on the VPCI bus. This request must be made from IRQL = PASSIVE_LEVEL. In this request, the driver must  set the <i>InterfaceType</i> parameter to GUID_VPCI_INTERFACE_STANDARD.</p>

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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451146">GUID_VPCI_INTERFACE_STANDARD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439637">ReadVfConfigBlock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMReadConfigBlock function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
