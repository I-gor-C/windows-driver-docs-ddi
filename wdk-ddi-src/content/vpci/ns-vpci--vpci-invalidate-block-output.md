---
UID: NS.vpci._VPCI_INVALIDATE_BLOCK_OUTPUT
title: VPCI_INVALIDATE_BLOCK_OUTPUT
author: windows-driver-content
description: The VPCI_INVALIDATE_BLOCK_OUTPUT structure is used in an IOCTL_VPCI_INVALIDATE_BLOCK IOCTL request.
old-location: kernel\vpci_invalidate_block_output.htm
old-project: kernel
ms.assetid: 6971C724-CE5E-44BC-8D3A-FAD248771E6F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VPCI_INVALIDATE_BLOCK_OUTPUT, VPCI_INVALIDATE_BLOCK_OUTPUT, *PVPCI_INVALIDATE_BLOCK_OUTPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: vpci.h
req.include-header: Vpci.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VPCI_INVALIDATE_BLOCK_OUTPUT
req.alt-loc: Vpci.h
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
req.iface: 
req.product: Windows 10 or later.
---

# VPCI_INVALIDATE_BLOCK_OUTPUT structure



## -description
<p>The <b>VPCI_INVALIDATE_BLOCK_OUTPUT</b> structure is used in an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439301">IOCTL_VPCI_INVALIDATE_BLOCK</a> IOCTL request.

The driver for a PCI Express (PCIe) virtual function (VF) issues the <b>IOCTL_VPCI_INVALIDATE_BLOCK</b> IOCTL request in order be notified of changes to data in one or more VF configuration blocks. When the IOCTL request is completed, the <b>VPCI_INVALIDATE_BLOCK_OUTPUT</b> structure specifies which VF configuration blocks have been changed.</p>


## -syntax

````
typedef struct _VPCI_INVALIDATE_BLOCK_OUTPUT {
  UINT64 BlockMask;
} VPCI_INVALIDATE_BLOCK_OUTPUT, *PVPCI_INVALIDATE_BLOCK_OUTPUT;
````


## -struct-fields
<dl>

### -field BlockMask

<dd>
<p>A <b>UINT64</b> value that specifies a bitmask for the first 64 VF configuration blocks. Each bit in the bitmask corresponds to a VF configuration block. If a bit is set to one, the data associated with the corresponding VF configuration block has changed.</p>
</dd>
</dl>

## -remarks
<p>A VF configuration block is used for backchannel communication between the drivers of the PCIe PF and a VF on a device that supports the SR-IOV interface. Data from a VF configuration block can be exchanged between the following drivers:</p>

<p>The VF driver, which runs in the guest operating system. This operating system runs within a Hyper-V child partition.</p>

<p>The PF driver, which runs in the management operating system.

This operating system runs within the Hyper-V parent partition.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Vpci.h (include Vpci.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439301">IOCTL_VPCI_INVALIDATE_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20VPCI_INVALIDATE_BLOCK_OUTPUT structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
