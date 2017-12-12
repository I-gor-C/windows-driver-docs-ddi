---
UID: NS.VPCI._VPCI_INTERFACE_STANDARD
title: _VPCI_INTERFACE_STANDARD
author: windows-driver-content
description: The VPCI_INTERFACE_STANDARD interface structure enables device drivers to access blocks of configuration data that is specific to a PCI Express (PCIe) virtual function (VF) of devices that support the single root I/O virtualization (SR-IOV) interface.
old-location: kernel\vpci_interface_standard.htm
old-project: kernel
ms.assetid: 8a34f6b6-ed97-4cb1-95d8-2623202d673b
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _VPCI_INTERFACE_STANDARD, VPCI_INTERFACE_STANDARD, *PVPCI_INTERFACE_STANDARD
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: vpci.h
req.include-header: Wdm.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Server 2012 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VPCI_INTERFACE_STANDARD
req.alt-loc: vpci.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# _VPCI_INTERFACE_STANDARD structure



## -description
The <b>VPCI_INTERFACE_STANDARD</b> interface structure enables device drivers to access blocks of configuration data that is specific to a PCI Express (PCIe) virtual function (VF) of devices that support the single root I/O virtualization (SR-IOV) interface. 

This structure describes the <a href="kernel.guid_vpci_interface_standard">GUID_VPCI_INTERFACE_STANDARD</a> interface.



## -syntax

````
typedef struct _VPCI_INTERFACE_STANDARD {
  USHORT                 Size;
  USHORT                 Version;
  PVOID                  Context;
  PINTERFACE_REFERENCE   InterfaceReference;
  PINTERFACE_DEREFERENCE InterfaceDereference;
  PVPCI_READ_BLOCK       WriteVfConfigBlock;
  PVPCI_READ_BLOCK       ReadVfConfigBlock;
  UINT32                 SerialNumber;
} VPCI_INTERFACE_STANDARD, *PVPCI_INTERFACE_STANDARD;
````


## -struct-fields

### -field Size

The size, in bytes, of this structure.


### -field Version

The driver-defined interface version.


### -field Context

A pointer to interface-specific context information.


### -field InterfaceReference

A pointer to an <a href="kernel.interfacereference">InterfaceReference</a> routine that increments the interface's reference count.


### -field InterfaceDereference

A pointer to an <a href="kernel.interfacedereference">InterfaceDereference</a> routine that decrements the interface's reference count.


### -field WriteVfConfigBlock

A pointer to a <a href="..\vpci\nc-vpci-vpci_write_block.md">WriteVfConfigBlock</a> routine that writes a block of configuration data for a PCIe VF.


### -field ReadVfConfigBlock

A pointer to a <a href="..\vpci\nc-vpci-vpci_read_block.md">ReadVfConfigBlock</a> routine that reads a block of configuration data for a PCIe VF.


### -field SerialNumber

A UINT32 value that contains the serial number for the PCIe VF on the device. The virtualization stack generates a unique serial number for each VF that is exposed on the device.


## -remarks
The <a href="kernel.guid_vpci_interface_standard">GUID_VPCI_INTERFACE_STANDARD</a> interface is provided by the virtual PCI (VPCI) bus driver that creates the physical device objects (PDOs) that are layered below the loaded drivers for the VFs. These drivers are loaded in the guest operating system that runs in a Hyper-V child partition.

A driver obtains a pointer to the <b>VPCI_INTERFACE_STANDARD</b> structure by sending an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> IRP to its bus driver with <b>InterfaceType</b> set to GUID_VPCI_INTERFACE_STANDARD.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Server 2012 and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Vpci.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="kernel.guid_vpci_interface_standard">GUID_VPCI_INTERFACE_STANDARD</a>
</dt>
<dt>
<a href="kernel.interfacedereference">InterfaceDereference</a>
</dt>
<dt>
<a href="kernel.interfacereference">InterfaceReference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a>
</dt>
<dt>
<a href="..\vpci\nc-vpci-vpci_read_block.md">ReadVfConfigBlock</a>
</dt>
<dt>
<a href="..\vpci\nc-vpci-vpci_write_block.md">WriteVfConfigBlock</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20VPCI_INTERFACE_STANDARD structure%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

