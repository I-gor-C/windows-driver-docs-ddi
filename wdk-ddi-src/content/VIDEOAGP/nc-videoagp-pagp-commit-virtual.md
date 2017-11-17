---
UID: NC.videoagp.PAGP_COMMIT_VIRTUAL
title: PAGP_COMMIT_VIRTUAL
author: windows-driver-content
description: The AgpCommitVirtual function maps reserved virtual memory to an associated range of AGP-decodable physical addresses.
old-location: display\agpcommitvirtual.htm
ms.assetid: 8a3e7fcd-d838-47ad-a42b-7eb070f81418
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
req.alt-api: AgpCommitVirtual
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

# PAGP_COMMIT_VIRTUAL callback



## -description
<p>The <b>AgpCommitVirtual</b> function maps reserved virtual memory to an associated range of AGP-decodable physical addresses.</p>


## -prototype

````
PAGP_COMMIT_VIRTUAL AgpCommitVirtual;

PVOID APIENTRY AgpCommitVirtual(
  _In_ PVOID HwDeviceExtension,
  _In_ PVOID VirtualReserveContext,
  _In_ ULONG Pages,
  _In_ ULONG Offset
)
{ ... }
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the device extension of the miniport driver'.</p>
</dd>

### -param <i>VirtualReserveContext</i> [in]

<dd>
<p>Identifies a reserved virtual address range. The context handle was obtained from <a href="https://msdn.microsoft.com/966dfc6c-6830-4872-b411-2801e3a4b753">AgpReserveVirtual</a>.</p>
</dd>

### -param <i>Pages</i> [in]

<dd>
<p>Specifies the number of pages of virtual memory to map.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the page offset at which to commit the pages. The offset is applied to the reserved virtual address range that is identified by <b>VirtualReserveContext</b>.</p>
</dd>
</dl>

## -returns
<p><b>AgpCommitVirtual</b> returns the virtual address for the base of the committed pages if the mapping succeeded; otherwise returns <b>NULL</b>.</p>

## -remarks
<p>Before calling <b>AgpCommitVirtual</b> to commit a range of virtual pages, you must do the following:</p>

<p>Call <a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a> to reserve a range of physical addresses for the GPU to use.</p>

<p>Call <a href="https://msdn.microsoft.com/3c3a6936-7435-4a42-99e6-2c048613af23">AgpCommitPhysical</a> to map a portion (or all) of the reserved physical addresses to locked pages in system memory.</p>

<p>Call <a href="https://msdn.microsoft.com/966dfc6c-6830-4872-b411-2801e3a4b753">AgpReserveVirtual</a> to reserve a range of virtual addresses that is associated with the range of physical addresses reserved by <a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a>.</p>

<p>After these items are completed, you can call <b>AgpCommitVirtual</b> to map a portion of the reserved virtual pages to pages that have already been mapped and locked by <a href="https://msdn.microsoft.com/3c3a6936-7435-4a42-99e6-2c048613af23">AgpCommitPhysical</a>. You must not attempt to map a page of virtual addresses if the corresponding page of physical addresses has not already been mapped.</p>

<p>Video miniport drivers that run on Microsoft Windows 2000 should always commit a virtual range whose size is a multiple of 64 kilobytes. If you call <b>AgpCommitVirtual</b> to commit a virtual range that is not a multiple of 64 kilobytes, it can return an invalid virtual address.</p>

<p>On Windows XP and later, <b>AgpCommitVirtual</b> automatically expands the committed range so that it is a multiple of 64 kilobytes.</p>

<p>When a miniport driver calls <b>AgpCommitVirtual</b>, a portion of the virtual address range identified by <b>VirtualReserveContext</b> is mapped to physical addresses. The mapped portion begins <i>Offset</i> pages into the virtual address range that is identified by <b>VirtualReserveContext</b>.</p>

<p>Before calling <b>AgpCommitVirtual</b> to commit a range of virtual pages, you must do the following:</p>

<p>Call <a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a> to reserve a range of physical addresses for the GPU to use.</p>

<p>Call <a href="https://msdn.microsoft.com/3c3a6936-7435-4a42-99e6-2c048613af23">AgpCommitPhysical</a> to map a portion (or all) of the reserved physical addresses to locked pages in system memory.</p>

<p>Call <a href="https://msdn.microsoft.com/966dfc6c-6830-4872-b411-2801e3a4b753">AgpReserveVirtual</a> to reserve a range of virtual addresses that is associated with the range of physical addresses reserved by <a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a>.</p>

<p>After these items are completed, you can call <b>AgpCommitVirtual</b> to map a portion of the reserved virtual pages to pages that have already been mapped and locked by <a href="https://msdn.microsoft.com/3c3a6936-7435-4a42-99e6-2c048613af23">AgpCommitPhysical</a>. You must not attempt to map a page of virtual addresses if the corresponding page of physical addresses has not already been mapped.</p>

<p>Video miniport drivers that run on Microsoft Windows 2000 should always commit a virtual range whose size is a multiple of 64 kilobytes. If you call <b>AgpCommitVirtual</b> to commit a virtual range that is not a multiple of 64 kilobytes, it can return an invalid virtual address.</p>

<p>On Windows XP and later, <b>AgpCommitVirtual</b> automatically expands the committed range so that it is a multiple of 64 kilobytes.</p>

<p>When a miniport driver calls <b>AgpCommitVirtual</b>, a portion of the virtual address range identified by <b>VirtualReserveContext</b> is mapped to physical addresses. The mapped portion begins <i>Offset</i> pages into the virtual address range that is identified by <b>VirtualReserveContext</b>.</p>

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
<a href="https://msdn.microsoft.com/a6f689ab-8cf1-4207-af2b-30957500c190">AgpFreeVirtual</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PAGP_COMMIT_VIRTUAL callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
