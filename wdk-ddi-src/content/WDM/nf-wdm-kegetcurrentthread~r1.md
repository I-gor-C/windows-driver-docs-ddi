---
UID: NF.wdm.KeGetCurrentThread~r1
title: KeGetCurrentThread
author: windows-driver-content
description: The KeGetCurrentThread routine identifies the current thread.
old-location: kernel\kegetcurrentthread.htm
ms.assetid: 0fbc9f6d-698b-4fa5-86c4-3f6ef0cc50fb
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeGetCurrentThread
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
ms.keywords: KeGetCurrentThread
req.iface: 
req.product: Windows 10 or later.
---

# KeGetCurrentThread function



## -description
<p>The <b>KeGetCurrentThread</b> routine identifies the current thread. </p>


## -syntax

````
PKTHREAD KeGetCurrentThread(void);
````


## -parameters


## -returns
<p><b>KeGetCurrentThread</b> returns a pointer to an opaque thread object. </p>

<p><b>KeGetCurrentThread</b> returns a pointer to an opaque thread object. </p>

<p><b>KeGetCurrentThread</b> returns a pointer to an opaque thread object. </p>

## -remarks
<p>This routine is identical to <a href="https://msdn.microsoft.com/library/windows/hardware/ff559936">PsGetCurrentThread</a>.</p>

<p>A caller of <b>KeGetCurrentThread</b> can use the returned pointer as an input parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff553062">KeQueryPriorityThread</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff553246">KeSetBasePriorityThread</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff553265">KeSetPriorityThread</a>. However, the memory containing the thread object is opaque; that is, it is reserved for exclusive use by the operating system.</p>

<p>This routine is identical to <a href="https://msdn.microsoft.com/library/windows/hardware/ff559936">PsGetCurrentThread</a>.</p>

<p>A caller of <b>KeGetCurrentThread</b> can use the returned pointer as an input parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff553062">KeQueryPriorityThread</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff553246">KeSetBasePriorityThread</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff553265">KeSetPriorityThread</a>. However, the memory containing the thread object is opaque; that is, it is reserved for exclusive use by the operating system.</p>

<p>This routine is identical to <a href="https://msdn.microsoft.com/library/windows/hardware/ff559936">PsGetCurrentThread</a>.</p>

<p>A caller of <b>KeGetCurrentThread</b> can use the returned pointer as an input parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff553062">KeQueryPriorityThread</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff553246">KeSetBasePriorityThread</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff553265">KeSetPriorityThread</a>. However, the memory containing the thread object is opaque; that is, it is reserved for exclusive use by the operating system.</p>

<p>This routine is identical to <a href="https://msdn.microsoft.com/library/windows/hardware/ff559936">PsGetCurrentThread</a>.</p>

<p>A caller of <b>KeGetCurrentThread</b> can use the returned pointer as an input parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff553062">KeQueryPriorityThread</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff553246">KeSetBasePriorityThread</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff553265">KeSetPriorityThread</a>. However, the memory containing the thread object is opaque; that is, it is reserved for exclusive use by the operating system.</p>

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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553062">KeQueryPriorityThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553246">KeSetBasePriorityThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553265">KeSetPriorityThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559936">PsGetCurrentThread</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeGetCurrentThread routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
