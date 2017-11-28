---
UID: NF.ndis.NdisMSetVirtualFunctionBusData
title: NdisMSetVirtualFunctionBusData
author: windows-driver-content
description: A miniport driver calls the NdisMSetVirtualFunctionBusData function to write data to the PCI Express (PCIe) configuration space of a Virtual Function (VF) on the network adapter.
old-location: netvista\ndismsetvirtualfunctionbusdata.htm
old-project: netvista
ms.assetid: 74c6789e-22a6-42e9-bc14-8b9f93da668b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMSetVirtualFunctionBusData
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
req.alt-api: NdisMSetVirtualFunctionBusData
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

# NdisMSetVirtualFunctionBusData function



## -description
<p>A miniport driver calls the <b>NdisMSetVirtualFunctionBusData</b> function to write data to the PCI  Express (PCIe) configuration space of a Virtual Function (VF) on the network adapter. </p>


## -syntax

````
ULONG NdisMSetVirtualFunctionBusData(
  _In_ NDIS_HANDLE            NdisMiniportHandle,
  _In_ NDIS_SRIOV_FUNCTION_ID VFId,
  _In_ PVOID                  Buffer,
  _In_ ULONG                  Offset,
  _In_ ULONG                  Length
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

### -param <i>VFId</i> [in]

<dd>
<p>The identifier of the VF to which data is written to its  PCI configuration space.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to a buffer that contains the data to be written to the PCI configuration space.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>The offset, in units of bytes, in the PCI configuration space to which data is written.

</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The length, in units of bytes, of the data to be written.</p>
</dd>
</dl>

## -returns
<p><b>NdisMSetVirtualFunctionBusData</b> returns the number of bytes written to the PCI configuration space. If the write operation fails, <b>NdisMSetVirtualFunctionBusData</b> returns zero.</p>

## -remarks
<p>The PF miniport driver typically calls <b>NdisMSetVirtualFunctionBusData</b> when it handles an OID method request of  <a href="https://msdn.microsoft.com/library/windows/hardware/hh451925">OID_SRIOV_WRITE_VF_CONFIG_SPACE</a>.  
However, the driver can call this function any time after virtualization has been enabled on the network adapter through a call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh451481">NdisMEnableVirtualization</a>.</p>

<p>For more information about backchannel communication within the single root I/O virtualization (SR-IOV) interface, see <a href="NULL">SR-IOV PF/VF Backchannel Communication</a>.</p>

<p>For more information about the SR-IOV interface, see 	<a href="NULL">Overview of Single Root I/O Virtualization (SR-IOV)</a>.</p>

<p>If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV <a href="devinst.driver_packages">driver package</a>, its miniport driver must not call <b>NdisMSetVirtualFunctionBusData</b>. Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call <a href="https://msdn.microsoft.com/library/windows/hardware/hh451552">SetVirtualFunctionData</a>. This function is exposed from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451143">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface that is supported by the underlying PCI bus driver.</p>

<p>The VBD that runs in the Hyper-V parent partition's management operating system can query the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451143">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface by issuing an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> request to its physical device object (PDO) on the PCI bus. This request must be made from IRQL = PASSIVE_LEVEL. In this request, the driver must  set the <i>InterfaceType</i> parameter to GUID_PCI_VIRTUALIZATION_INTERFACE.</p>

<p>The PF miniport driver typically calls <b>NdisMSetVirtualFunctionBusData</b> when it handles an OID method request of  <a href="https://msdn.microsoft.com/library/windows/hardware/hh451925">OID_SRIOV_WRITE_VF_CONFIG_SPACE</a>.  
However, the driver can call this function any time after virtualization has been enabled on the network adapter through a call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh451481">NdisMEnableVirtualization</a>.</p>

<p>For more information about backchannel communication within the single root I/O virtualization (SR-IOV) interface, see <a href="NULL">SR-IOV PF/VF Backchannel Communication</a>.</p>

<p>For more information about the SR-IOV interface, see 	<a href="NULL">Overview of Single Root I/O Virtualization (SR-IOV)</a>.</p>

<p>If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV <a href="devinst.driver_packages">driver package</a>, its miniport driver must not call <b>NdisMSetVirtualFunctionBusData</b>. Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call <a href="https://msdn.microsoft.com/library/windows/hardware/hh451552">SetVirtualFunctionData</a>. This function is exposed from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451143">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface that is supported by the underlying PCI bus driver.</p>

<p>The VBD that runs in the Hyper-V parent partition's management operating system can query the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451143">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface by issuing an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> request to its physical device object (PDO) on the PCI bus. This request must be made from IRQL = PASSIVE_LEVEL. In this request, the driver must  set the <i>InterfaceType</i> parameter to GUID_PCI_VIRTUALIZATION_INTERFACE.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451143">GUID_PCI_VIRTUALIZATION_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451481">NdisMEnableVirtualization</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451814">OID_NIC_SWITCH_ALLOCATE_VF</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451925">OID_SRIOV_WRITE_VF_CONFIG_SPACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451552">SetVirtualFunctionData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMSetVirtualFunctionBusData function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
