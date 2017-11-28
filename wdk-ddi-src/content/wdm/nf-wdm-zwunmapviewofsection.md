---
UID: NF.wdm.ZwUnmapViewOfSection
title: ZwUnmapViewOfSection
author: windows-driver-content
description: The ZwUnmapViewOfSection routine unmaps a view of a section from the virtual address space of a subject process.
old-location: kernel\zwunmapviewofsection.htm
old-project: kernel
ms.assetid: ebc67162-4e36-4af8-bc3b-764633dcda5d
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ZwUnmapViewOfSection
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwUnmapViewOfSection,NtUnmapViewOfSection
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ZwUnmapViewOfSection function



## -description
<p>The <b>ZwUnmapViewOfSection</b> routine unmaps a <a href="wdkgloss.v#wdkgloss.view#wdkgloss.view"><i>view</i></a> of a section from the virtual address space of a subject process.</p>


## -syntax

````
NTSTATUS ZwUnmapViewOfSection(
  _In_     HANDLE ProcessHandle,
  _In_opt_ PVOID  BaseAddress
);
````


## -parameters
<dl>

### -param <i>ProcessHandle</i> [in]

<dd>
<p>Handle to a process object that was previously passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff566481">ZwMapViewOfSection</a>.</p>
</dd>

### -param <i>BaseAddress</i> [in, optional]

<dd>
<p>Pointer to the base virtual address of the view to unmap. This value can be any virtual address within the view.</p>
</dd>
</dl>

## -returns
<p><b>ZwUnmapViewOfSection</b> returns an NTSTATUS value. Possible return values include:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The routine successfully performed the requested operation.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The caller does not have access rights to the process object or to the base virtual address of the view.</p>

<p> </p>

## -remarks
<p>This routine unmaps the entire view of the section that contains <i>BaseAddress</i> from the virtual address space of the specified process—even if <i>BaseAddress</i> does not point to the beginning of the view.</p>

<p>On return from <b>ZwUnmapViewOfSection</b>, the virtual-address region occupied by the view is no longer reserved and is available to map other views or private pages. If the view was also the last reference to the underlying section, all committed pages in the section are decommitted, and the section is deleted.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p>This routine unmaps the entire view of the section that contains <i>BaseAddress</i> from the virtual address space of the specified process—even if <i>BaseAddress</i> does not point to the beginning of the view.</p>

<p>On return from <b>ZwUnmapViewOfSection</b>, the virtual-address region occupied by the view is no longer reserved and is available to map other views or private pages. If the view was also the last reference to the underlying section, all committed pages in the section are decommitted, and the section is deleted.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566481">ZwMapViewOfSection</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567029">ZwOpenSection</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwUnmapViewOfSection routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
