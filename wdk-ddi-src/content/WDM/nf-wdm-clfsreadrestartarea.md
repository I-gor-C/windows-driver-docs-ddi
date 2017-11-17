---
UID: NF.wdm.ClfsReadRestartArea
title: ClfsReadRestartArea
author: windows-driver-content
description: The ClfsReadRestartArea routine reads the restart record that was most recently written to a specified CLFS stream.
old-location: kernel\clfsreadrestartarea.htm
ms.assetid: d391a7ed-220e-412a-8e32-22b206c7a062
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClfsReadRestartArea
req.alt-loc: Clfs.sys,Ext-MS-Win-fs-clfs-l1-1-0.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Clfs.lib
req.dll: Clfs.sys
req.irql: <= APC_LEVEL
ms.keywords: ClfsReadRestartArea
req.iface: 
req.product: Windows 10 or later.
---

# ClfsReadRestartArea function



## -description
<p>The <b>ClfsReadRestartArea</b> routine reads the restart record that was most recently written to a specified CLFS stream.</p>


## -syntax

````
NTSTATUS ClfsReadRestartArea(
  _Inout_ PVOID     pvMarshalContext,
  _Out_   PVOID     *ppvRestartBuffer,
  _Out_   PULONG    pcbRestartBuffer,
  _Out_   PCLFS_LSN plsn,
  _Out_   PVOID     *ppvReadContext
);
````


## -parameters
<dl>

### -param <i>pvMarshalContext</i> [in, out]

<dd>
<p>A pointer to an opaque context that represents a marshalling area associated with a CLFS stream. The caller previously obtained this pointer by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff541520">ClfsCreateMarshallingArea</a>.</p>
</dd>

### -param <i>ppvRestartBuffer</i> [out]

<dd>
<p>A pointer to a variable that receives a pointer to the data buffer of the restart record.</p>
</dd>

### -param <i>pcbRestartBuffer</i> [out]

<dd>
<p>A pointer to a ULONG-typed variable that receives the size, in bytes, of the data buffer pointed to by <i>pcbRestartBuffer</i>. This is the length of the data buffer of the restart record.</p>
</dd>

### -param <i>plsn</i> [out]

<dd>
<p>A pointer to a CLFS_LSN structure that receives the LSN of the restart record that was read.</p>
</dd>

### -param <i>ppvReadContext</i> [out]

<dd>
<p>A pointer to a variable that receives a pointer to an opaque read context. The caller can pass this context to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541699">ClfsReadPreviousRestartArea</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff541690">ClfsReadNextLogRecord</a>. When the caller has finished using the read context, it must free the context by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff541767">ClfsTerminateReadLog</a>.</p>
</dd>
</dl>

## -returns
<p><b>ClfsReadRestartArea</b> returns STATUS_SUCCESS if it succeeds; otherwise, it returns one of the error codes defined in Ntstatus.h.</p>

## -remarks
<p>For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>.</p>

<p>For information about reading records from CLFS streams, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560785">Reading Data Records from a CLFS Stream</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff560786">Reading Restart Records from a CLFS Stream</a>.</p>

<p>Read contexts are not thread-safe. Clients are responsible for serializing access to read contexts. </p>

<p>For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>.</p>

<p>For information about reading records from CLFS streams, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560785">Reading Data Records from a CLFS Stream</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff560786">Reading Restart Records from a CLFS Stream</a>.</p>

<p>Read contexts are not thread-safe. Clients are responsible for serializing access to read contexts. </p>

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
<p>Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Clfs.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Clfs.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541520">ClfsCreateMarshallingArea</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541690">ClfsReadNextLogRecord</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541699">ClfsReadPreviousRestartArea</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541767">ClfsTerminateReadLog</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsReadRestartArea routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
