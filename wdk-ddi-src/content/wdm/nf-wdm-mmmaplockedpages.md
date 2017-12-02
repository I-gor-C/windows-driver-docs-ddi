---
UID: NF.wdm.MmMapLockedPages
title: MmMapLockedPages
author: windows-driver-content
description: The MmMapLockedPages routine is obsolete for Windows 2000 and later versions of Windows, and for Windows Me.
old-location: kernel\mmmaplockedpages.htm
old-project: kernel
ms.assetid: f27b7622-614b-4c9e-8253-51f4638e5eb0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: MmMapLockedPages
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Obsolete for Windows 2000 and later versions of Windows, and for Windows Me. This routine is supported only for WDM drivers that must run on Windows 98. Otherwise, use MmMapLockedPagesSpecifyCache.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmMapLockedPages
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# MmMapLockedPages function



## -description
<p>The <b>MmMapLockedPages</b> routine is <u>obsolete</u> for Windows 2000 and later versions of Windows, and for Windows Me. It is supported only for WDM drivers that must run on Windows 98. Otherwise, use <a href="..\wdm\nf-wdm-mmmaplockedpagesspecifycache.md">MmMapLockedPagesSpecifyCache</a>.</p>
<p>The <b>MmMapLockedPages</b> routine maps the physical pages that are described by a given MDL.</p>


## -syntax

````
PVOID MmMapLockedPages(
  _In_ PMDL            MemoryDescriptorList,
  _In_ KPROCESSOR_MODE AccessMode
);
````


## -parameters
<dl>

### -param MemoryDescriptorList [in]

<dd>
<p>Pointer to an MDL that was updated by <a href="..\wdm\nf-wdm-mmprobeandlockpages.md">MmProbeAndLockPages</a>.</p>
</dd>

### -param AccessMode [in]

<dd>
<p>Specifies the access mode in which to map the MDL, either <b>KernelMode</b> or <b>UserMode</b>. Almost all drivers should use <b>KernelMode</b>.</p>
</dd>
</dl>

## -returns
<p><b>MmMapLockedPages</b> returns the starting address of the mapped pages. (For NT-based operating systems prior to Windows NT 4.0 Service Pack 4 (SP4), <b>MmMapLockedPages</b> returns the beginning address of the first page of the mapped pages.)</p>

## -remarks
<p>Use <a href="..\wdm\nf-wdm-mmunmaplockedpages.md">MmUnmapLockedPages</a> to unmap the physical pages that were mapped by <b>MmMapLockedPages</b>.</p>

<p>If <i>AccessMode</i> is KernelMode and <b>MmMapLockedPages</b> cannot map the specified pages, the system issues a bug check. (For this reason, drivers should use <a href="..\wdm\nf-wdm-mmmaplockedpagesspecifycache.md">MmMapLockedPagesSpecifyCache</a> when available; that routine returns <b>NULL</b> on failure, rather than causing a bug check.) If <i>AccessMode</i> is <b>UserMode</b> and the specified pages cannot be mapped, the routine raises an exception. Callers that specify <b>UserMode</b> must wrap the call to <b>MmMapLockedPages</b> in a <b>try/except</b> block. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546823">Handling Exceptions</a>.</p>

<p>Callers of <b>MmMapLockedPages</b> must be running at IRQL &lt;= DISPATCH_LEVEL if <i>AccessMode</i> is <b>KernelMode</b>. Otherwise, the caller must be running at IRQL &lt;= APC_LEVEL.</p>

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
<p>Obsolete for Windows 2000 and later versions of Windows, and for Windows Me. This routine is supported only for WDM drivers that must run on Windows 98. Otherwise, use <a href="..\wdm\nf-wdm-mmmaplockedpagesspecifycache.md">MmMapLockedPagesSpecifyCache</a>. </p>
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
<p>See Remarks section.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-mmgetsystemaddressformdl.md">MmGetSystemAddressForMdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554559">MmGetSystemAddressForMdlSafe</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-mmmaplockedpagesspecifycache.md">MmMapLockedPagesSpecifyCache</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-mmprobeandlockpages.md">MmProbeAndLockPages</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-mmunmaplockedpages.md">MmUnmapLockedPages</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmMapLockedPages routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
