---
UID: NF.wdm.ClfsFlushToLsn
title: ClfsFlushToLsn
author: windows-driver-content
description: The ClfsFlushToLsn routine forces, to stable storage, all records that have an LSN less than or equal to a specified LSN.
old-location: kernel\clfsflushtolsn.htm
ms.assetid: fb7d97d2-8c02-44c8-8cf5-e9c3b3b718bb
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
req.alt-api: ClfsFlushToLsn
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
ms.keywords: ClfsFlushToLsn
req.iface: 
req.product: Windows 10 or later.
---

# ClfsFlushToLsn function



## -description
<p>The <b>ClfsFlushToLsn</b> routine forces, to stable storage, all records that have an LSN less than or equal to a specified LSN.</p>


## -syntax

````
NTSTATUS ClfsFlushToLsn(
  _In_      PVOID     pvMarshalContext,
  _In_      PCLFS_LSN plsnFlush,
  _Out_opt_ PCLFS_LSN plsnLastFlushed
);
````


## -parameters
<dl>

### -param <i>pvMarshalContext</i> [in]

<dd>
<p>A pointer to an opaque context associated with a marshalling area. The caller previously obtained this pointer by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff541520">ClfsCreateMarshallingArea</a>.</p>
</dd>

### -param <i>plsnFlush</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541824">CLFS_LSN</a> structure. All records that have an LSN less than or equal to <i>plsnFlush</i> are guaranteed to be forced to stable storage. If <i>plsnFlush</i> is equal to CLFS_LSN_NULL, then all records in the marshalling area are forced to stable storage.</p>
</dd>

### -param <i>plsnLastFlushed</i> [out, optional]

<dd>
<p>A pointer to a <b>CLFS_LSN</b> structure that receives the LSN of the oldest record that was not flushed. This is the LSN of the record immediately following the last record flushed. </p>
<div class="alert"><b>Note</b>    On successful return, <i>plsnLastFlushed</i> is greater than the value supplied in <i>plsnFlush</i>. However, <i>plsnLastFlushed</i> does not necessarily point to a record in the stream. For example, if all records in the stream were flushed, <i>plsnLastFlushed</i> is the LSN that will be assigned to the next record written to the stream.</div>
<div> </div>
</dd>
</dl>

## -returns
<p><b>ClfsFlushToLsn</b> returns STATUS_SUCCESS if it succeeds; otherwise, it returns one of the error codes defined in Ntstatus.h.</p>

## -remarks
<p>For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541544">ClfsFlushBuffers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsFlushToLsn routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
