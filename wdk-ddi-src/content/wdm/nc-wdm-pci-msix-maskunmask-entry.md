---
UID: NC.wdm.PCI_MSIX_MASKUNMASK_ENTRY
title: PCI_MSIX_MASKUNMASK_ENTRY
author: windows-driver-content
description: The MaskTableEntry routine masks an interrupt in the MSI-X hardware interrupt table.
old-location: kernel\masktableentry.htm
old-project: kernel
ms.assetid: ADD9AA38-594D-413A-BE8B-BCC6B62EAA8E
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista with Service Pack 1 (SP1), Windows Server 2008, and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MaskTableEntry
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
req.irql: <= DIRQL
req.iface: 
req.product: Windows 10 or later.
---

# PCI_MSIX_MASKUNMASK_ENTRY callback



## -description
<p>The <i>MaskTableEntry</i> routine masks an interrupt in the MSI-X hardware interrupt table.</p>


## -prototype

````
PCI_MSIX_MASKUNMASK_ENTRY MaskTableEntry;

NTSTATUS MaskTableEntry(
  _In_ PVOID Context,
  _In_ ULONG TableEntry
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to interface-specific context information. The caller passes the value that is passed as the <b>Context</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558787">PCI_MSIX_TABLE_CONFIG_INTERFACE</a> structure for the interface.</p>
</dd>

### -param <i>TableEntry</i> [in]

<dd>
<p>The index of the table entry in the MSI-X hardware interrupt table.</p>
</dd>
</dl>

## -returns
<p>The <i>MaskTableEntry</i> routine might return one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>TableEntry</i> parameter is invalid.</p>

<p> </p>

## -remarks
<p>If a table entry is masked, the device does not generate any interrupts that correspond to that table entry.</p>

<p>You can unmask the table entry by calling <a href="https://msdn.microsoft.com/library/windows/hardware/gg604859">UnmaskTableEntry</a>.</p>

<p>If a table entry is masked, the device does not generate any interrupts that correspond to that table entry.</p>

<p>You can unmask the table entry by calling <a href="https://msdn.microsoft.com/library/windows/hardware/gg604859">UnmaskTableEntry</a>.</p>

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
<p>Available in Windows Vista with Service Pack 1 (SP1), Windows Server 2008, and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DIRQL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/gg604859">UnmaskTableEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558787">PCI_MSIX_TABLE_CONFIG_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PCI_MSIX_MASKUNMASK_ENTRY routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
