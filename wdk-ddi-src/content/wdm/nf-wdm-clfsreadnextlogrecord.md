---
UID: NF.wdm.ClfsReadNextLogRecord
title: ClfsReadNextLogRecord function
author: windows-driver-content
description: The ClfsReadNextLogRecord routine reads the next record in a sequence, relative to the current record in a read context.
old-location: kernel\clfsreadnextlogrecord.htm
old-project: kernel
ms.assetid: 4990f3d7-e48c-49ee-9384-4bcad93c9281
ms.author: windowsdriverdev
ms.date: 12/6/2017
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
req.product: Windows 10 or later.
---

# ClfsReadNextLogRecord function



## -description
The <b>ClfsReadNextLogRecord</b> routine reads the next record in a sequence, relative to the current record in a read context.


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

### -param pvReadContext [in, out]

A pointer to a read context that the caller previously obtained by calling <a href="kernel.clfsreadlogrecord">ClfsReadLogRecord</a> or <a href="kernel.clfsreadrestartarea">ClfsReadRestartArea</a>.

### -param ppvBuffer [out]

A pointer to a variable that receives a pointer to a buffer that contains the record data.

### -param pcbBuffer [out]

A pointer to a ULONG-typed variable that receives the size, in bytes, of the buffer pointed to by *<i>ppvBuffer</i>. This is the length of the data buffer of the record read.

### -param peRecordType [in, out]

A pointer to a variable of type CLFS_RECORD_TYPE. The caller must set this parameter to one of the following values.
<table>
<tr>
<th>Value</th>
<th>Record that will be read</th>
</tr>
<tr>
<td>
<b>ClfsDataRecord</b>
</td>
<td>
The next data record.
</td>
</tr>
<tr>
<td>
<b>ClfsRestartRecord</b>
</td>
<td>
The next restart record.
</td>
</tr>
<tr>
<td>
<b>ClfsClientRecord</b>
</td>
<td>
The next record that is either a data record or a restart record.
</td>
</tr>
</table>
 

### -param plsnUser [in, optional]

A pointer to a <a href="kernel.clfs_lsn">CLFS_LSN</a> structure that supplies the LSN of the record to be read. The specified record is read instead of the record that would have been read according to the mode (<b>ClfsContextUndoNext</b>, <b>ClfsContextPrevious</b>, or <b>ClfsContextForward</b>) of the read context (<i>pvReadContext</i>). The LSN supplied in <i>plsnUser</i> must be less than the current LSN of the read context. This parameter can be <b>NULL</b>.

### -param plsnUndoNext [out]

A pointer to a <b>CLFS_LSN</b> structure that receives the undo-next LSN of the record that is read.

### -param plsnPrevious [out]

A pointer to a <b>CLFS_LSN</b> structure that receives the previous LSN of the record that was read.

### -param plsnRecord [out]

A pointer to a <b>CLFS_LSN</b> structure that receives the LSN of the record that was read.

## -returns
<b>ClfsReadNextLogRecord</b> returns STATUS_SUCCESS if it succeeds; otherwise, it returns one of the error codes defined in Ntstatus.h.

## -remarks
For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>. 

For information about reading records from CLFS streams, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560785">Reading Data Records from a CLFS Stream</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff560786">Reading Restart Records from a CLFS Stream</a>.

Read contexts are not thread-safe. Clients are responsible for serializing access to read contexts. 

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Clfs.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>Clfs.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= APC_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.clfs_lsn">CLFS_LSN</a>
</dt>
<dt>
<a href="kernel.clfsreadlogrecord">ClfsReadLogRecord</a>
</dt>
<dt>
<a href="kernel.clfsreadrestartarea">ClfsReadRestartArea</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsReadNextLogRecord routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
