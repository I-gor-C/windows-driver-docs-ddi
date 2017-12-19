---
UID: NC.vpci.VPCI_READ_BLOCK
title: VPCI_READ_BLOCK
author: windows-driver-content
description: The ReadVfConfigBlock routine reads a block of configuration data for a PCI Express (PCIe) virtual function (VF). This routine is called by the driver of a PCIe VF on a device that supports the single root I/O virtualization (SR-IOV) interface.
old-location: kernel\readvfconfigblock.htm
old-project: kernel
ms.assetid: 8960F064-C1F8-4964-AFFE-FC77D886D043
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _VMB_CHANNEL_STATE_CHANGE_CALLBACKS, PVMB_CHANNEL_STATE_CHANGE_CALLBACKS, VMB_CHANNEL_STATE_CHANGE_CALLBACKS, *PVMB_CHANNEL_STATE_CHANGE_CALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: vpci.h
req.include-header: Wdm.h, Pcivirt.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in Windows Server 2012 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ReadVfConfigBlock
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
req.irql: <= APC_LEVEL
req.product: Windows 10 or later.
---

# VPCI_READ_BLOCK callback



## -description
 The <i>ReadVfConfigBlock</i> routine reads a block of configuration data for a PCI Express (PCIe) virtual function (VF). This routine is called by the  driver of a PCIe VF on a device that supports the single root I/O virtualization (SR-IOV) interface. 



## -prototype

````
VPCI_READ_BLOCK ReadVfConfigBlock;

NTSTATUS ReadVfConfigBlock(
  _In_  PVOID Context,
  _In_  ULONG BlockId,
  _Out_ PVOID Buffer,
  _In_  ULONG Length
)
{ ... }
````


## -parameters

### -param Context [in]

A pointer to interface-specific context information. The caller passes the value that is passed as the <b>Context</b> member of the <a href="kernel.vpci_interface_standard">VPCI_INTERFACE_STANDARD</a> structure for the interface.


### -param BlockId [in]

The identifier of the VF configuration block to be read. This identifier is proprietary to the independent hardware vendor (IHV) and is used only by the drivers for the PCIe physical function (PF) and VF on the device.


### -param Buffer [out]

A pointer to a caller-allocated buffer that will contain the configuration data to be read. For more information, see Remarks.


### -param Length [in]

The number of bytes to be read from the VF configuration block.



<div class="alert"><b>Note</b>  The value of this parameter must not exceed <b>VPCI_MAX_READ_WRITE_BLOCK_SIZE</b>.</div>
<div> </div>

## -returns
The <i>ReadVfConfigBlock</i> routine returns <b>STATUS_SUCCESS</b> if the operation succeeds. Otherwise, the routine returns an appropriate NTSTATUS value.



## -remarks
When the <i>ReadVfConfigBlock</i> routine is called, the driver of the PF is notified to return data from a specified VF configuration block.

A VF configuration block is used for backchannel communication between the drivers of the PF and a VF on a device that supports the SR-IOV interface. The IHV can define one or more VF configuration blocks for the device. Each VF configuration block has an IHV-defined format, length,  and block ID.

VF configuration data can be exchanged between the following drivers in a protected manner:<ul>
<li>
The VF driver, which runs in the guest operating system. This operating system runs within a Hyper-V child partition.



</li>
<li>
The PF driver, which runs in the management operating system.

This operating system runs within the Hyper-V parent partition.

</li>
</ul>


The VF driver, which runs in the guest operating system. This operating system runs within a Hyper-V child partition.



The PF driver, which runs in the management operating system.

This operating system runs within the Hyper-V parent partition.

Data from each VF configuration block is  used only by the drivers of the PF and VF.




## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported in Windows Server 2012 and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Vpci.h (include Wdm.h or Pcivirt.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="..\vpci\ni-vpci-ioctl_vpci_read_block.md">IOCTL_VPCI_READ_BLOCK</a>
</dt>
<dt>
<a href="kernel.vpci_interface_standard">VPCI_INTERFACE_STANDARD</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20VPCI_READ_BLOCK routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

