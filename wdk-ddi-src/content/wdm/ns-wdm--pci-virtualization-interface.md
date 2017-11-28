---
UID: NS.wdm._PCI_VIRTUALIZATION_INTERFACE
title: PCI_VIRTUALIZATION_INTERFACE
author: windows-driver-content
description: The PCI_VIRTUALIZATION_INTERFACE structure enables drivers to manage and configure the PCI Express (PCIe) configuration space for a virtual function (VF).
old-location: kernel\pci_virtualization_interface.htm
old-project: kernel
ms.assetid: eb55d42b-2c89-4b6d-a75c-6f79d6a14f57
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PCI_VIRTUALIZATION_INTERFACE, PCI_VIRTUALIZATION_INTERFACE, *PPCI_VIRTUALIZATION_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Server 2012 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCI_VIRTUALIZATION_INTERFACE
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# PCI_VIRTUALIZATION_INTERFACE structure



## -description
<p>The <b>PCI_VIRTUALIZATION_INTERFACE</b> structure enables drivers to manage and configure the PCI Express (PCIe) configuration space for a virtual function (VF). VFs are exposed on the PCI bus by devices that support the  single root I/O virtualization (SR-IOV) interface.  </p>
<p>This structure describes the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451143">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface.</p>


## -syntax

````
typedef struct _PCI_VIRTUALIZATION_INTERFACE {
  USHORT                            Size;
  USHORT                            Version;
  PVOID                             Context;
  PINTERFACE_REFERENCE              InterfaceReference;
  PINTERFACE_DEREFERENCE            InterfaceDereference;
  PSET_VIRTUAL_DEVICE_DATA          SetVirtualFunctionData;
  PGET_VIRTUAL_DEVICE_DATA          GetVirtualFunctionData;
  PGET_VIRTUAL_DEVICE_LOCATION      GetLocation;
  PGET_VIRTUAL_DEVICE_RESOURCES     GetResources;
  PENABLE_VIRTUALIZATION            EnableVirtualization;
  PGET_VIRTUAL_FUNCTION_PROBED_BARS GetVirtualFunctionProbedBars;
} PCI_VIRTUALIZATION_INTERFACE, *PPCI_VIRTUALIZATION_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>The driver-defined interface version.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>A pointer to interface-specific context information.</p>
</dd>

### -field <b>InterfaceReference</b>

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff547833">InterfaceReference</a> routine that increments the interface's reference count.</p>
</dd>

### -field <b>InterfaceDereference</b>

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff547829">InterfaceDereference</a> routine that decrements the interface's reference count.</p>
</dd>

### -field <b>SetVirtualFunctionData</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh451552">SetVirtualFunctionData</a> routine that writes data to the PCIe configuration space of an SR-IOV device's VF.</p>
</dd>

### -field <b>GetVirtualFunctionData</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh451137">GetVirtualFunctionData</a> routine that reads data from the PCIe configuration space of an SR-IOV device's VF.</p>
</dd>

### -field <b>GetLocation</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh451128">GetLocation</a> routine that provides information about the current device location of a VF  in the PCIe hierarchy. This information is necessary for a virtualization system that is using an I/O memory management unit (IOMMU) to route traffic to or from the device.</p>
</dd>

### -field <b>GetResources</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh451131">GetResources</a> routine that provides information about the resources that are available for virtualization on an SR-IOV device.</p>
</dd>

### -field <b>EnableVirtualization</b>

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/hh451005">EnableVirtualization</a> routine that enables or disables virtualization on an SR-IOV device.</p>
</dd>

### -field <b>GetVirtualFunctionProbedBars</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh451140">GetVirtualFunctionProbedBars</a> routine that allows a non-privileged Hyper-V virtual machine (VM) to determine what would be read from the PCIe Base Address Registers (BARs) of a VF after a query by the PCI bus driver. The PCI driver performs this query to determine the memory or I/O address space that the device requires.</p>
</dd>
</dl>

## -remarks
<p>For devices that support the SR-IOV interface, drivers occasionally have to access and manage  the PCIe configuration space of the device's VFs.  Drivers call routines from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451143">GUID_PCI_VIRTUALIZATION_INTERFACE</a> interface to access the PCIe configuration space of the VFs on the device.</p>

<p>The <b>PCI_VIRTUALIZATION_INTERFACE</b> structure is an extension of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a> structure.</p>

<p>A driver obtains a pointer to the <b>PCI_VIRTUALIZATION_INTERFACE</b> structure by sending an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> I/O request packet (IRP) to its bus driver with <i>InterfaceType</i> set to GUID_PCI_VIRTUALIZATION_INTERFACE.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Server 2012 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546561">GUID_BUS_INTERFACE_STANDARD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451143">GUID_PCI_VIRTUALIZATION_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547829">InterfaceDereference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547833">InterfaceReference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PCI_VIRTUALIZATION_INTERFACE structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
