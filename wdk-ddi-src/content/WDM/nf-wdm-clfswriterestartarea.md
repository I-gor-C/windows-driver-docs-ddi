---
UID: NF.wdm.ClfsWriteRestartArea
title: ClfsWriteRestartArea
author: windows-driver-content
description: The ClfsWriteRestartArea routine atomically appends a new restart record to a CLFS stream, flushes the restart record to stable storage, and optionally updates the base LSN of the stream.
old-location: kernel\clfswriterestartarea.htm
ms.assetid: e97006e1-5a18-4478-9cac-30eb70142fa7
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
req.alt-api: ClfsWriteRestartArea
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
ms.keywords: ClfsWriteRestartArea
req.iface: 
req.product: Windows 10 or later.
---

# ClfsWriteRestartArea function



## -description
<p>The <b>ClfsWriteRestartArea</b> routine atomically appends a new restart record to a CLFS stream, flushes the restart record to stable storage, and optionally updates the base LSN of the stream.</p>


## -syntax

````
NTSTATUS ClfsWriteRestartArea(
  _Inout_   PVOID     pvMarshalContext,
  _In_      PVOID     pvRestartBuffer,
  _In_      ULONG     cbRestartBuffer,
  _In_opt_  PCLFS_LSN plsnBase,
  _In_      ULONG     fFlags,
  _Out_opt_ PULONG    pcbWritten,
  _Out_opt_ PCLFS_LSN plsnNext
);
````


## -parameters
<dl>

### -param <i>pvMarshalContext</i> [in, out]

<dd>
<p>A pointer to an opaque context that represents a marshalling area associated with a CLFS stream. The caller previously obtained this pointer by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff541520">ClfsCreateMarshallingArea</a>.</p>
</dd>

### -param <i>pvRestartBuffer</i> [in]

<dd>
<p>A pointer to a buffer that contains the data for the restart record.</p>
</dd>

### -param <i>cbRestartBuffer</i> [in]

<dd>
<p>The size, in bytes, of the buffer pointed to by <i>pvRestartBuffer</i>. This is the size of the restart data.</p>
</dd>

### -param <i>plsnBase</i> [in, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541824">CLFS_LSN</a> structure that specifies a new base LSN for the stream. If this parameter is <b>NULL</b>, the base LSN is not changed.</p>
</dd>

### -param <i>fFlags</i> [in]

<dd>
<p>This parameter must be one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>The restart record is placed in newly allocated space in an I/O block. The number of reserved records in the marshalling area is not changed.</p>
</td>
</tr>
<tr>
<td>
<p>CLFS_FLAG_USE_RESERVATION</p>
</td>
<td>
<p>The restart record is placed in previously reserved space in an I/O block. The number of reserved records in the marshalling area is reduced by one.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pcbWritten</i> [out, optional]

<dd>
<p>A pointer to a ULONG-typed variable that receives the number of bytes actually forced to stable storage. This parameter can be <b>NULL</b>.</p>
</dd>

### -param <i>plsnNext</i> [out, optional]

<dd>
<p>A pointer to a <b>CLFS_LSN</b> structure that receives the LSN of the newly written restart record.</p>
</dd>
</dl>

## -returns
<p><b>ClfsWriteRestartArea</b> returns STATUS_SUCCESS if it succeeds; otherwise, it returns one of the error codes defined in Ntstatus.h.</p>

## -remarks
<p>Typically ClfsWriteRestartArea is called as the last act of a client checkpoint.</p>

<p>ClfsWriteRestartArea is a relatively expensive operation because it causes a flush of all records currently in the marshalling area along with a flush of stream and log metadata.</p>

<p>At any one time, only one marshalling area should be used to write data to a stream. Having two marshalling areas writing into the stream might result in stream corruption.</p>

<p>If you just want to set the base LSN of a stream, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff540773">ClfsAdvanceLogBase</a>, which does not necessarily flush any data to stable storage.</p>

<p>For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>. </p>

<p>Typically ClfsWriteRestartArea is called as the last act of a client checkpoint.</p>

<p>ClfsWriteRestartArea is a relatively expensive operation because it causes a flush of all records currently in the marshalling area along with a flush of stream and log metadata.</p>

<p>At any one time, only one marshalling area should be used to write data to a stream. Having two marshalling areas writing into the stream might result in stream corruption.</p>

<p>If you just want to set the base LSN of a stream, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff540773">ClfsAdvanceLogBase</a>, which does not necessarily flush any data to stable storage.</p>

<p>For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541824">CLFS_LSN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540773">ClfsAdvanceLogBase</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541520">ClfsCreateMarshallingArea</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541709">ClfsReadRestartArea</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541699">ClfsReadPreviousRestartArea</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsWriteRestartArea routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
