---
UID: NF.wdm.ClfsReadNextLogRecord
title: ClfsReadNextLogRecord
author: windows-driver-content
description: The ClfsReadNextLogRecord routine reads the next record in a sequence, relative to the current record in a read context.
old-location: kernel\clfsreadnextlogrecord.htm
old-project: kernel
ms.assetid: 4990f3d7-e48c-49ee-9384-4bcad93c9281
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ClfsReadNextLogRecord
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClfsReadNextLogRecord
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
req.iface: 
req.product: Windows 10 or later.
---

# ClfsReadNextLogRecord function



## -description
<p>The <b>ClfsReadNextLogRecord</b> routine reads the next record in a sequence, relative to the current record in a read context.</p>


## -syntax

````
NTSTATUS ClfsReadNextLogRecord(
  _Inout_  PVOID             pvReadContext,
  _Out_    PVOID             *ppvBuffer,
  _Out_    PULONG            pcbBuffer,
  _Inout_  PCLFS_RECORD_TYPE peRecordType,
  _In_opt_ PCLFS_LSN         plsnUser,
  _Out_    PCLFS_LSN         plsnUndoNext,
  _Out_    PCLFS_LSN         plsnPrevious,
  _Out_    PCLFS_LSN         plsnRecord
);
````


## -parameters
<dl>

### -param <i>pvReadContext</i> [in, out]

<dd>
<p>A pointer to a read context that the caller previously obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff541682">ClfsReadLogRecord</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff541709">ClfsReadRestartArea</a>.</p>
</dd>

### -param <i>ppvBuffer</i> [out]

<dd>
<p>A pointer to a variable that receives a pointer to a buffer that contains the record data.</p>
</dd>

### -param <i>pcbBuffer</i> [out]

<dd>
<p>A pointer to a ULONG-typed variable that receives the size, in bytes, of the buffer pointed to by *<i>ppvBuffer</i>. This is the length of the data buffer of the record read.</p>
</dd>

### -param <i>peRecordType</i> [in, out]

<dd>
<p>A pointer to a variable of type CLFS_RECORD_TYPE. The caller must set this parameter to one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Record that will be read</th>
</tr>
<tr>
<td>
<p><b>ClfsDataRecord</b></p>
</td>
<td>
<p>The next data record.</p>
</td>
</tr>
<tr>
<td>
<p><b>ClfsRestartRecord</b></p>
</td>
<td>
<p>The next restart record.</p>
</td>
</tr>
<tr>
<td>
<p><b>ClfsClientRecord</b></p>
</td>
<td>
<p>The next record that is either a data record or a restart record.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>plsnUser</i> [in, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541824">CLFS_LSN</a> structure that supplies the LSN of the record to be read. The specified record is read instead of the record that would have been read according to the mode (<b>ClfsContextUndoNext</b>, <b>ClfsContextPrevious</b>, or <b>ClfsContextForward</b>) of the read context (<i>pvReadContext</i>). The LSN supplied in <i>plsnUser</i> must be less than the current LSN of the read context. This parameter can be <b>NULL</b>.</p>
</dd>

### -param <i>plsnUndoNext</i> [out]

<dd>
<p>A pointer to a <b>CLFS_LSN</b> structure that receives the undo-next LSN of the record that is read.</p>
</dd>

### -param <i>plsnPrevious</i> [out]

<dd>
<p>A pointer to a <b>CLFS_LSN</b> structure that receives the previous LSN of the record that was read.</p>
</dd>

### -param <i>plsnRecord</i> [out]

<dd>
<p>A pointer to a <b>CLFS_LSN</b> structure that receives the LSN of the record that was read.</p>
</dd>
</dl>

## -returns
<p><b>ClfsReadNextLogRecord</b> returns STATUS_SUCCESS if it succeeds; otherwise, it returns one of the error codes defined in Ntstatus.h.</p>

## -remarks
<p>For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>. </p>

<p>For information about reading records from CLFS streams, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560785">Reading Data Records from a CLFS Stream</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff560786">Reading Restart Records from a CLFS Stream</a>.</p>

<p>Read contexts are not thread-safe. Clients are responsible for serializing access to read contexts. </p>

<p>For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541824">CLFS_LSN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541682">ClfsReadLogRecord</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541709">ClfsReadRestartArea</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsReadNextLogRecord routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
