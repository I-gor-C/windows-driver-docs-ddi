---
UID: NF.wdm.ExSetResourceOwnerPointer
title: ExSetResourceOwnerPointer
author: windows-driver-content
description: The ExSetResourceOwnerPointer routine sets the owner thread pointer for an executive resource.
old-location: kernel\exsetresourceownerpointer.htm
old-project: kernel
ms.assetid: 985f811e-cf4f-4dbe-8ede-497ba4eceffd
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ExSetResourceOwnerPointer
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
req.alt-api: ExSetResourceOwnerPointer
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ExSetResourceOwnerPointer function



## -description
<p>The <b>ExSetResourceOwnerPointer</b> routine sets the owner thread pointer for an executive resource.</p>


## -syntax

````
VOID ExSetResourceOwnerPointer(
  _Inout_ PERESOURCE Resource,
  _In_    PVOID      OwnerPointer
);
````


## -parameters
<dl>

### -param Resource [in, out]

<dd>
<p>A pointer to an executive resource owned by the current thread.</p>
</dd>

### -param OwnerPointer [in]

<dd>
<p>A pointer to an owner thread pointer of type ERESOURCE_THREAD (for additional requirements, see the following Remarks section).</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>ExSetResourceOwnerPointer</b>, used in conjunction with <b>ExReleaseResourceForThreadLite</b>, provides a means for one thread (acting as an resource manager thread) to acquire and release resources for use by another thread (acting as a resource user thread).</p>

<p>After calling <b>ExSetResourceOwnerPointer</b> for a specific resource, the only other routine that can be called for that resource is <b>ExReleaseResourceForThreadLite</b>.</p>

<p>The resource manager thread acquires ownership of the resource and passes ownership to the user thread by calling <b>ExSetResourceOwnerPointer</b>. The caller must allocate the memory for the ERESOURCE_THREAD value pointed to by <i>OwnerPointer</i> in system memory, and this memory must remain allocated until <b>ExReleaseResourceForThreadLite</b> returns. The caller must also set the two low-order bits of the ERESOURCE_THREAD value pointed to by <i>OwnerPointer</i> to one — this encoding is used internally by the resource services to distinguish between owner and thread addresses.</p>

<p>When the user thread is done with the resource, the resource manager thread releases the user thread's ownership of the resource by calling <b>ExReleaseResourceForThreadLite</b>. The <i>ResourceThreadId</i> input parameter is set to the value of the <i>OwnerPointer</i> parameter used in the previous call to <b>ExSetResourceOwnerPointer</b> that gave the worker thread ownership of the resource.</p>

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
<p>&lt;= DISPATCH_LEVEL</p>
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
<a href="..\wdm\nf-wdm-exreleaseresourceforthreadlite.md">ExReleaseResourceForThreadLite</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExSetResourceOwnerPointer routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
