---
UID: NF.ndis.NdisMGetVirtualFunctionBusData
title: NdisMGetVirtualFunctionBusData
author: windows-driver-content
description: A miniport driver calls the NdisMGetVirtualFunctionBusData function to read data from the PCI Express (PCIe) configuration space of a specified Virtual Function (VF) on the network adapter.
old-location: netvista\ndismgetvirtualfunctionbusdata.htm
old-project: netvista
ms.assetid: 15e2e1f4-6039-4588-a7ba-bd8aa6b78839
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMGetVirtualFunctionBusData
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
req.alt-api: NdisMGetVirtualFunctionBusData
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

# NdisMGetVirtualFunctionBusData function



## -description
<p>A miniport driver calls the <b>NdisMGetVirtualFunctionBusData</b> function to read data from the PCI  Express (PCIe) configuration space of a specified Virtual Function (VF) on the network adapter. </p>


## -syntax

````
ULONG NdisMGetVirtualFunctionBusData(
  _In_  NDIS_HANDLE            NdisMiniportHandle,
  _In_  NDIS_SRIOV_FUNCTION_ID VFId,
  _Out_ PVOID                  Buffer,
  _In_  ULONG                  Offset,
  _In_  ULONG                  Length
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
<p>The identifier of the VF from which the data from the PCI configuration space is returned.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>A pointer to a buffer that receives the data that is read from the VF's PCI configuration space.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>The offset, in units of bytes, in the VF's PCI configuration space from which data is read.

</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The length, in units of bytes, of the data to be read.</p>
<div class="alert"><b>Note</b>  The size of the buffer referenced by <i>Buffer</i> must be at least as large as the value of the <i>Length</i> parameter.</div>
<div> </div>
</dd>
</dl>

## -returns
<p><b>NdisMGetVirtualFunctionBusData</b> returns the number of bytes that are read from the PCI configuration space. If the read operation fails, <b>NdisMGetVirtualFunctionBusData</b> returns zero.</p>

## -remarks
<p>The PF miniport driver typically calls <b>NdisMGetVirtualFunctionBusData</b> when it handles an OID method request of  <a href="https://msdn.microsoft.com/library/windows/hardware/hh451879">OID_SRIOV_READ_VF_CONFIG_SPACE</a>.  
However, the driver can call this function any time after virtualization has been enabled on the network adapter through a call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh451481">NdisMEnableVirtualization</a>.</p>

<p>For more information on how to query the VF's PCI configuration space, see <a href="NULL">Querying the PCI Configuration Space for a Virtual Function</a>.</p>

<p>For more information about the SR-IOV interface, see 	<a href="NULL">Overview of Single Root I/O Virtualization (SR-IOV)</a>.</p>

<p>If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV <a href="devinst.driver_packages">driver package</a>, its miniport driver must not call <b>NdisMGetVirtualFunctionBusData</b>. Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call <a href="https://msdn.microsoft.com/library/windows/hardware/hh451137">GetVirtualFunctionData</a>. This function is exposed from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451143">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface that is supported by the underlying PCI bus driver.</p>

<p>The VBD that runs in the Hyper-V parent partition's management operating system can query the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451143">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface by issuing an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> request to its physical device object (PDO) on the PCI bus. This request must be made from IRQL = PASSIVE_LEVEL. In this request, the driver must  set the <i>InterfaceType</i> parameter to GUID_PCI_VIRTUALIZATION_INTERFACE.</p>

<p>The PF miniport driver typically calls <b>NdisMGetVirtualFunctionBusData</b> when it handles an OID method request of  <a href="https://msdn.microsoft.com/library/windows/hardware/hh451879">OID_SRIOV_READ_VF_CONFIG_SPACE</a>.  
However, the driver can call this function any time after virtualization has been enabled on the network adapter through a call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh451481">NdisMEnableVirtualization</a>.</p>

<p>For more information on how to query the VF's PCI configuration space, see <a href="NULL">Querying the PCI Configuration Space for a Virtual Function</a>.</p>

<p>For more information about the SR-IOV interface, see 	<a href="NULL">Overview of Single Root I/O Virtualization (SR-IOV)</a>.</p>

<p>If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV <a href="devinst.driver_packages">driver package</a>, its miniport driver must not call <b>NdisMGetVirtualFunctionBusData</b>. Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call <a href="https://msdn.microsoft.com/library/windows/hardware/hh451137">GetVirtualFunctionData</a>. This function is exposed from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451143">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface that is supported by the underlying PCI bus driver.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451137">GetVirtualFunctionData</a>
</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451879">OID_SRIOV_READ_VF_CONFIG_SPACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMGetVirtualFunctionBusData function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
