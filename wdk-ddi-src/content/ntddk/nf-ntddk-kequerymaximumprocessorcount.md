---
UID: NF.ntddk.KeQueryMaximumProcessorCount
title: KeQueryMaximumProcessorCount
author: windows-driver-content
description: The KeQueryMaximumProcessorCount routine returns the maximum number of processors.
old-location: kernel\kequerymaximumprocessorcount.htm
old-project: kernel
ms.assetid: bab2c478-4e46-40d9-a4b6-6f322b18ab0a
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KeQueryMaximumProcessorCount
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeQueryMaximumProcessorCount
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
req.iface: 
---

# KeQueryMaximumProcessorCount function



## -description
<p>The <b>KeQueryMaximumProcessorCount</b> routine returns the maximum number of processors.</p>


## -syntax

````
ULONG KeQueryMaximumProcessorCount(void);
````


## -parameters


## -returns
<p><b>KeQueryMaximumProcessorCount</b> returns the maximum number of processors as a ULONG value.</p>

<p><b>KeQueryMaximumProcessorCount</b> returns the maximum number of processors as a ULONG value.</p>

<p><b>KeQueryMaximumProcessorCount</b> returns the maximum number of processors as a ULONG value.</p>

## -remarks
<p>The value returned by the <b>KeQueryMaximumProcessorCount</b> routine does not change at runtime.</p>

<p>If your code uses an array of buffers, one buffer for each processor, you must decide whether to have a statically sized array based on <b>KeQueryMaximumProcessorCount</b> or a dynamically sized array based on <a href="https://msdn.microsoft.com/library/windows/hardware/ff552985">KeQueryActiveProcessorCount</a>.</p>

<p>To optimize based on the number of processors, you need a resizable structure for Windows Server 2008. In this case, use <b>KeQueryActiveProcessorCount</b>.</p>

<p>If you are not optimizing and if the data structures that result from using maximum processor count are relatively small, a resizable structure is not necessary. In this case, use <b>KeQueryMaximumProcessorCount</b> to determine size for a static array.</p>

<p>Windows 7 and later versions of Windows support processor groups. Drivers that are designed to handle information about processor groups should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a> routine, which specifies a processor group, instead of <b>KeQueryMaximumProcessorCount</b>, which does not. However, the implementation of <b>KeQueryMaximumProcessorCount</b> in Windows 7 and later versions of Windows provides compatibility for drivers that were written for earlier versions of Windows, which do not support processor groups. In this implementation, <b>KeQueryMaximumProcessorCount</b> returns the maximum number of logical processors that can be in group 0.</p>

<p>The value returned by the <b>KeQueryMaximumProcessorCount</b> routine does not change at runtime.</p>

<p>If your code uses an array of buffers, one buffer for each processor, you must decide whether to have a statically sized array based on <b>KeQueryMaximumProcessorCount</b> or a dynamically sized array based on <a href="https://msdn.microsoft.com/library/windows/hardware/ff552985">KeQueryActiveProcessorCount</a>.</p>

<p>To optimize based on the number of processors, you need a resizable structure for Windows Server 2008. In this case, use <b>KeQueryActiveProcessorCount</b>.</p>

<p>If you are not optimizing and if the data structures that result from using maximum processor count are relatively small, a resizable structure is not necessary. In this case, use <b>KeQueryMaximumProcessorCount</b> to determine size for a static array.</p>

<p>Windows 7 and later versions of Windows support processor groups. Drivers that are designed to handle information about processor groups should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a> routine, which specifies a processor group, instead of <b>KeQueryMaximumProcessorCount</b>, which does not. However, the implementation of <b>KeQueryMaximumProcessorCount</b> in Windows 7 and later versions of Windows provides compatibility for drivers that were written for earlier versions of Windows, which do not support processor groups. In this implementation, <b>KeQueryMaximumProcessorCount</b> returns the maximum number of logical processors that can be in group 0.</p>

<p>The value returned by the <b>KeQueryMaximumProcessorCount</b> routine does not change at runtime.</p>

<p>If your code uses an array of buffers, one buffer for each processor, you must decide whether to have a statically sized array based on <b>KeQueryMaximumProcessorCount</b> or a dynamically sized array based on <a href="https://msdn.microsoft.com/library/windows/hardware/ff552985">KeQueryActiveProcessorCount</a>.</p>

<p>To optimize based on the number of processors, you need a resizable structure for Windows Server 2008. In this case, use <b>KeQueryActiveProcessorCount</b>.</p>

<p>If you are not optimizing and if the data structures that result from using maximum processor count are relatively small, a resizable structure is not necessary. In this case, use <b>KeQueryMaximumProcessorCount</b> to determine size for a static array.</p>

<p>Windows 7 and later versions of Windows support processor groups. Drivers that are designed to handle information about processor groups should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a> routine, which specifies a processor group, instead of <b>KeQueryMaximumProcessorCount</b>, which does not. However, the implementation of <b>KeQueryMaximumProcessorCount</b> in Windows 7 and later versions of Windows provides compatibility for drivers that were written for earlier versions of Windows, which do not support processor groups. In this implementation, <b>KeQueryMaximumProcessorCount</b> returns the maximum number of logical processors that can be in group 0.</p>

<p>The value returned by the <b>KeQueryMaximumProcessorCount</b> routine does not change at runtime.</p>

<p>If your code uses an array of buffers, one buffer for each processor, you must decide whether to have a statically sized array based on <b>KeQueryMaximumProcessorCount</b> or a dynamically sized array based on <a href="https://msdn.microsoft.com/library/windows/hardware/ff552985">KeQueryActiveProcessorCount</a>.</p>

<p>To optimize based on the number of processors, you need a resizable structure for Windows Server 2008. In this case, use <b>KeQueryActiveProcessorCount</b>.</p>

<p>If you are not optimizing and if the data structures that result from using maximum processor count are relatively small, a resizable structure is not necessary. In this case, use <b>KeQueryMaximumProcessorCount</b> to determine size for a static array.</p>

<p>Windows 7 and later versions of Windows support processor groups. Drivers that are designed to handle information about processor groups should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a> routine, which specifies a processor group, instead of <b>KeQueryMaximumProcessorCount</b>, which does not. However, the implementation of <b>KeQueryMaximumProcessorCount</b> in Windows 7 and later versions of Windows provides compatibility for drivers that were written for earlier versions of Windows, which do not support processor groups. In this implementation, <b>KeQueryMaximumProcessorCount</b> returns the maximum number of logical processors that can be in group 0.</p>

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
<p>Available in Windows Vista and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552985">KeQueryActiveProcessorCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeQueryMaximumProcessorCount routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
