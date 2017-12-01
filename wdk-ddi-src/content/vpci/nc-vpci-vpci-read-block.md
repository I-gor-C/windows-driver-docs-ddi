---
UID: NC.vpci.VPCI_READ_BLOCK
title: VPCI_READ_BLOCK
author: windows-driver-content
description: The ReadVfConfigBlock routine reads a block of configuration data for a PCI Express (PCIe) virtual function (VF). This routine is called by the driver of a PCIe VF on a device that supports the single root I/O virtualization (SR-IOV) interface.
old-location: kernel\readvfconfigblock.htm
old-project: kernel
ms.assetid: 8960F064-C1F8-4964-AFFE-FC77D886D043
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VMB_CHANNEL_STATE_CHANGE_CALLBACKS, VMB_CHANNEL_STATE_CHANGE_CALLBACKS, *PVMB_CHANNEL_STATE_CHANGE_CALLBACKS
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
req.iface: 
req.product: Windows 10 or later.
---

# VPCI_READ_BLOCK callback



## -description
<p> The <i>ReadVfConfigBlock</i> routine reads a block of configuration data for a PCI Express (PCIe) virtual function (VF). This routine is called by the  driver of a PCIe VF on a device that supports the single root I/O virtualization (SR-IOV) interface. </p>


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
<dl>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to interface-specific context information. The caller passes the value that is passed as the <b>Context</b> member of the <a href="..\vpci\ns-vpci--vpci-interface-standard.md">VPCI_INTERFACE_STANDARD</a> structure for the interface.</p>
</dd>

### -param <i>BlockId</i> [in]

<dd>
<p>The identifier of the VF configuration block to be read. This identifier is proprietary to the independent hardware vendor (IHV) and is used only by the drivers for the PCIe physical function (PF) and VF on the device.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer that will contain the configuration data to be read. For more information, see Remarks.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The number of bytes to be read from the VF configuration block.

</p>
<div class="alert"><b>Note</b>  The value of this parameter must not exceed <b>VPCI_MAX_READ_WRITE_BLOCK_SIZE</b>.</div>
<div> </div>
</dd>
</dl>

## -returns
<p>The <i>ReadVfConfigBlock</i> routine returns <b>STATUS_SUCCESS</b> if the operation succeeds. Otherwise, the routine returns an appropriate NTSTATUS value.
</p>

## -remarks
<p>When the <i>ReadVfConfigBlock</i> routine is called, the driver of the PF is notified to return data from a specified VF configuration block.</p>

<p>A VF configuration block is used for backchannel communication between the drivers of the PF and a VF on a device that supports the SR-IOV interface. The IHV can define one or more VF configuration blocks for the device. Each VF configuration block has an IHV-defined format, length,  and block ID.</p>

<p>VF configuration data can be exchanged between the following drivers in a protected manner:<ul>
<li>
<p>The VF driver, which runs in the guest operating system. This operating system runs within a Hyper-V child partition.

</p>
</li>
<li>
<p>The PF driver, which runs in the management operating system.

This operating system runs within the Hyper-V parent partition.</p>
</li>
</ul>
</p>

<p>The VF driver, which runs in the guest operating system. This operating system runs within a Hyper-V child partition.

</p>

<p>The PF driver, which runs in the management operating system.

This operating system runs within the Hyper-V parent partition.</p>

<p>Data from each VF configuration block is  used only by the drivers of the PF and VF.

</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows Server 2012 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Vpci.h (include Wdm.h or Pcivirt.h)</dt>
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
<a href="..\vpci\ni-vpci-ioctl-vpci-read-block.md">IOCTL_VPCI_READ_BLOCK</a>
</dt>
<dt>
<a href="..\vpci\ns-vpci--vpci-interface-standard.md">VPCI_INTERFACE_STANDARD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20VPCI_READ_BLOCK routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
