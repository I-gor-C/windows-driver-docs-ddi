---
UID: NF.srb.ScsiPortGetVirtualAddress
title: ScsiPortGetVirtualAddress
author: windows-driver-content
description: The ScsiPortGetVirtualAddress routine returns a virtual address associated with a physical address if the physical address was obtained by a call to ScsiPortGetPhysicalAddress.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
old-location: storage\scsiportgetvirtualaddress.htm
old-project: storage
ms.assetid: 8e9a247a-f906-4f0e-8249-b67a042aada5
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ScsiPortGetVirtualAddress
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: srb.h
req.include-header: Miniport.h, Scsi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ScsiPortGetVirtualAddress
req.alt-loc: Scsiport.lib,Scsiport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Scsiport.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# ScsiPortGetVirtualAddress function



## -description
<p>The <b>ScsiPortGetVirtualAddress</b> routine returns a virtual address associated with a physical address if the physical address was obtained by a call to <b>ScsiPortGetPhysicalAddress</b>.</p>


## -syntax

````
PVOID ScsiPortGetVirtualAddress(
  _In_ PVOID                 HwDeviceExtension,
  _In_ SCSI_PHYSICAL_ADDRESS PhysicalAddress
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the HBA's mapped access ranges. This area is available to the miniport driver in the <b>DeviceExtension-&gt;HwDeviceExtension</b> member of the HBA's device object immediately after the miniport driver calls <a href="..\srb\nf-srb-scsiportinitialize.md">ScsiPortInitialize</a>. The port driver frees this memory when it removes the device. </p>
</dd>

### -param <i>PhysicalAddress</i> [in]

<dd>
<p>Specifies the physical address to be mapped. This value must have been returned by <b>ScsiPortGetPhysicalAddress</b> and must be from an uncached device extension or SRB extension.</p>
</dd>
</dl>

## -returns
<p><b>ScsiPortGetVirtualAddress</b> returns a mapped pointer for the given input address. If the <i>PhysicalAddress</i> value is invalid, it returns <b>NULL</b>.</p>

## -remarks
<p><b>ScsiPortGetVirtualAddress</b> uses <b>SCSI_PHYSICAL_ADDRESS</b> to represent physical addresses.</p>

<p>The <b>SCSI_PHYSICAL_ADDRESS</b> type is an operating system-independent data type that SCSI miniport drivers use to represent either a physical addresses or a bus-relative address. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Srb.h (include Miniport.h or Scsi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Scsiport.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\srb\nf-srb-scsiportgetuncachedextension.md">ScsiPortGetUncachedExtension</a>
</dt>
<dt>
<a href="..\srb\nf-srb-scsiportgetphysicaladdress.md">ScsiPortGetPhysicalAddress</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ScsiPortGetVirtualAddress routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
