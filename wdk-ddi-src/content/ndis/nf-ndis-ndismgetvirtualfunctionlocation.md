---
UID: NF.ndis.NdisMGetVirtualFunctionLocation
title: NdisMGetVirtualFunctionLocation function
author: windows-driver-content
description: A miniport driver calls the NdisMGetVirtualFunctionLocation function to query the device location of a PCI Express (PCIe) Virtual Function (VF) on a PCI bus. The driver uses the device location to construct the PCIe Requestor ID (RID) for the VF.
old-location: netvista\ndismgetvirtualfunctionlocation.htm
old-project: netvista
ms.assetid: 772A7763-67C0-4218-8C5F-23972475D2C9
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NdisMGetVirtualFunctionLocation
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
req.alt-api: NdisMGetVirtualFunctionLocation
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
---

# NdisMGetVirtualFunctionLocation function



## -description
A miniport driver calls the <b>NdisMGetVirtualFunctionLocation</b> function to query the device location of a PCI Express (PCIe) Virtual Function (VF) on a  PCI bus. The driver uses the device location to construct the PCIe Requestor ID (RID) for the VF.


## -syntax

````
VOID NdisMGetVirtualFunctionLocation(
  _In_  NDIS_HANDLE            NdisMiniportHandle,
  _In_  NDIS_SRIOV_FUNCTION_ID VFId,
  _Out_ PUSHORT                SegmentNumber,
  _Out_ PUCHAR                 BusNumber,
  _Out_ PUCHAR                 FunctionNumber
);
````


## -parameters

### -param NdisMiniportHandle [in]

The network adapter handle that NDIS passed to the 
     <i>MiniportAdapterHandle</i> parameter of 
     <a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>.

### -param VFId [in]

The identifier of the VF for which the device location is returned.

### -param SegmentNumber [out]

A pointer to a caller-supplied variable in which this function returns a USHORT value for the current PCI segment number. This value specifies the group of PCI buses on which the device is attached.

### -param BusNumber [out]

A pointer to a caller-supplied variable in which this function returns a UCHAR value. This value specifies the current PCI bus number on which the device is attached.

### -param FunctionNumber [out]

A pointer to a caller-supplied variable in which this function returns a UCHAR value. This value specifies the function number of a logical device on the device.

## -returns

     None.

## -remarks
 When  it handles a method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451814">OID_NIC_SWITCH_ALLOCATE_VF</a>, the PF miniport driver must return the RID for the VF that the driver has successfully allocated on the network adapter. The driver generates the RID in the following way:<ol>
<li>
The driver first calls the  <b>NdisMGetVirtualFunctionLocation</b> function to obtain the bus-related location information for the VF.
</li>
<li>
The driver then calls the  <a href="https://msdn.microsoft.com/library/windows/hardware/hh451557">NDIS_MAKE_RID</a> macro with the bus-related location information to generate the RID.
</li>
</ol>


The driver first calls the  <b>NdisMGetVirtualFunctionLocation</b> function to obtain the bus-related location information for the VF.

The driver then calls the  <a href="https://msdn.microsoft.com/library/windows/hardware/hh451557">NDIS_MAKE_RID</a> macro with the bus-related location information to generate the RID.

For more information on how to allocate VF resources, see <a href="netvista.virtual_function_initialization_sequence">Virtual Function Initialization Sequence</a>.

For more information about the SR-IOV interface, see 	<a href="netvista.overview_of_single_root_i_o_virtualization__sr-iov_">Overview of Single Root I/O Virtualization (SR-IOV)</a>.

If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV <a href="devinst.driver_packages">driver package</a>, its miniport driver must not call <b>NdisMGetVirtualFunctionLocation</b>. Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call <a href="..\wdm\nc-wdm-get_virtual_device_location.md">GetLocation</a>. This function is exposed from the <a href="kernel.guid_pci_virtualization_interface">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface supported by the underlying PCI bus driver.

The VBD that runs in the Hyper-V parent partition's management operating system can query the <a href="kernel.guid_pci_virtualization_interface">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface by issuing an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> request to its physical device object (PDO) on the PCI bus. This request must be made from IRQL = PASSIVE_LEVEL. In this request, the driver must  set the <i>InterfaceType</i> parameter to GUID_PCI_VIRTUALIZATION_INTERFACE.

## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
None supported
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012
</td>
</tr>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Supported in NDIS 6.30 and later.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="..\wdm\nc-wdm-get_virtual_device_location.md">GetLocation</a>
</dt>
<dt>
<a href="kernel.guid_pci_virtualization_interface">GUID_PCI_VIRTUALIZATION_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451557">NDIS_MAKE_RID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451814">OID_NIC_SWITCH_ALLOCATE_VF</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMGetVirtualFunctionLocation function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
