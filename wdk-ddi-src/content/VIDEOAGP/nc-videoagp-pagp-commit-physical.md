---
UID: NC.videoagp.PAGP_COMMIT_PHYSICAL
title: PAGP_COMMIT_PHYSICAL
author: windows-driver-content
description: The AgpCommitPhysical function maps system (physical) memory to the specified range of AGP-decodable physical addresses.
old-location: display\agpcommitphysical.htm
ms.assetid: 3c3a6936-7435-4a42-99e6-2c048613af23
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: videoagp.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AgpCommitPhysical
req.alt-loc: videoagp.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: VPOSVERSIONINFO, VPOSVERSIONINFO, *PVPOSVERSIONINFO
req.iface: 
req.product: Windows 10 or later.
---

# PAGP_COMMIT_PHYSICAL callback



## -description
<p>The <b>AgpCommitPhysical</b> function maps system (physical) memory to the specified range of AGP-decodable physical addresses.</p>


## -prototype

````
PAGP_COMMIT_PHYSICAL AgpCommitPhysical;

BOOLEAN APIENTRY AgpCommitPhysical(
  _In_ PVOID HwDeviceExtension,
  _In_ PVOID PhysicalReserveContext,
  _In_ ULONG Pages,
  _In_ ULONG Offset
)
{ ... }
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the device extension of the miniport driver.</p>
</dd>

### -param <i>PhysicalReserveContext</i> [in]

<dd>
<p>Identifies a reserved physical address range. The context handle is obtained from <a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a>.</p>
</dd>

### -param <i>Pages</i> [in]

<dd>
<p>Specifies the number of pages of system memory to commit.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the page offset at which to commit the pages. The offset is applied to the reserved physical address range associated with <b>PhysicalReserveContext</b>.</p>
</dd>
</dl>

## -returns
<p><b>AgpCommitPhysical</b> returns <b>TRUE</b> if the mapping was successful, and <b>FALSE</b> otherwise.</p>

## -remarks
<p>A video miniport driver must first reserve physical addresses by calling <a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a> before it calls this function.</p>

<p>Do not call <b>AgpCommitPhysical</b> to commit addresses that have already been committed. If the range of pages that is specified by <b>PhysicalReserveContext</b>, <b>Pages</b>, and <b>Offset</b> includes any pages that were previously committed, <b>AgpCommitPhysical</b> might fail.</p>

<p>Video miniport drivers that run on Microsoft Windows 2000 should always reserve and commit a physical range whose size is a multiple of 64 kilobytes. Reserving or committing a physical range that is not a multiple of 64 kilobytes can result in <a href="https://msdn.microsoft.com/966dfc6c-6830-4872-b411-2801e3a4b753">AgpReserveVirtual</a> or <a href="https://msdn.microsoft.com/8a3e7fcd-d838-47ad-a42b-7eb070f81418">AgpCommitVirtual</a> returning an invalid virtual address.</p>

<p>On Windows XP and later, <b>AgpCommitPhysical</b> automatically expands the committed range so that it is a multiple of 64 kilobytes.</p>

<p>When a video miniport driver calls <b>AgpCommitPhysical</b>, a portion of the physical address range identified by <b>PhysicalReserveContext</b> is mapped to locked pages of physical memory. The mapped portion begins <b>Offset</b> pages into the range identified by <b>PhysicalReserveContext</b>. The video miniport driver can access committed physical memory as if it were contiguous.</p>

<p>A video miniport driver must first reserve physical addresses by calling <a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a> before it calls this function.</p>

<p>Do not call <b>AgpCommitPhysical</b> to commit addresses that have already been committed. If the range of pages that is specified by <b>PhysicalReserveContext</b>, <b>Pages</b>, and <b>Offset</b> includes any pages that were previously committed, <b>AgpCommitPhysical</b> might fail.</p>

<p>Video miniport drivers that run on Microsoft Windows 2000 should always reserve and commit a physical range whose size is a multiple of 64 kilobytes. Reserving or committing a physical range that is not a multiple of 64 kilobytes can result in <a href="https://msdn.microsoft.com/966dfc6c-6830-4872-b411-2801e3a4b753">AgpReserveVirtual</a> or <a href="https://msdn.microsoft.com/8a3e7fcd-d838-47ad-a42b-7eb070f81418">AgpCommitVirtual</a> returning an invalid virtual address.</p>

<p>On Windows XP and later, <b>AgpCommitPhysical</b> automatically expands the committed range so that it is a multiple of 64 kilobytes.</p>

<p>When a video miniport driver calls <b>AgpCommitPhysical</b>, a portion of the physical address range identified by <b>PhysicalReserveContext</b> is mapped to locked pages of physical memory. The mapped portion begins <b>Offset</b> pages into the range identified by <b>PhysicalReserveContext</b>. The video miniport driver can access committed physical memory as if it were contiguous.</p>

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
<p>Available in Windows 2000 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Videoagp.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/8a3e7fcd-d838-47ad-a42b-7eb070f81418">AgpCommitVirtual</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/966dfc6c-6830-4872-b411-2801e3a4b753">AgpReserveVirtual</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PAGP_COMMIT_PHYSICAL callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
