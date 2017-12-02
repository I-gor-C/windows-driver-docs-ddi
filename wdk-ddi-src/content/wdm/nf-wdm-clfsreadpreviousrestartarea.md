---
UID: NF.wdm.ClfsReadPreviousRestartArea
title: ClfsReadPreviousRestartArea
author: windows-driver-content
description: The ClfsReadPreviousRestartArea routine reads the previous restart record relative to the current record in a read context.
old-location: kernel\clfsreadpreviousrestartarea.htm
old-project: kernel
ms.assetid: 832da270-e1e1-41bf-a9cf-0b363c0d2d74
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ClfsReadPreviousRestartArea
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
req.alt-api: ClfsReadPreviousRestartArea
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

# ClfsReadPreviousRestartArea function



## -description
<p>The <b>ClfsReadPreviousRestartArea</b> routine reads the previous restart record relative to the current record in a read context.</p>


## -syntax

````
NTSTATUS ClfsReadPreviousRestartArea(
  _In_  PVOID     pvReadContext,
  _Out_ PVOID     *ppvRestartBuffer,
  _Out_ PULONG    pcbRestartBuffer,
  _Out_ PCLFS_LSN plsnRestart
);
````


## -parameters
<dl>

### -param pvReadContext [in]

<dd>
<p>A pointer to a read context obtained by a previous call to <a href="..\wdm\nf-wdm-clfsreadrestartarea.md">ClfsReadRestartArea</a>.</p>
</dd>

### -param ppvRestartBuffer [out]

<dd>
<p>A pointer to a variable that receives a pointer to the data buffer of the restart record that is read.</p>
</dd>

### -param pcbRestartBuffer [out]

<dd>
<p>A pointer to a ULONG-typed variable that receives the size, in bytes, of the buffer pointed to by *<i>ppvRestartBuffer</i>. This is the length of the data buffer of the restart record that is read.</p>
</dd>

### -param plsnRestart [out]

<dd>
<p>A pointer to a <a href="kernel.clfs_lsn">CLFS_LSN</a> structure that receives the previous LSN of the restart record that was read.</p>
</dd>
</dl>

## -returns
<p><b>ClfsReadPreviousRestartArea</b> returns STATUS_SUCCESS if it succeeds; otherwise, it returns one of the error codes defined in Ntstatus.h. If there are no previous restart areas, the return value is STATUS_LOG_START_OF_LOG.</p>

## -remarks
<p>For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>.</p>

<p>For information about reading records from CLFS streams, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560785">Reading Data Records from a CLFS Stream</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff560786">Reading Restart Records from a CLFS Stream</a>.</p>

<p>Read contexts are not thread-safe. Clients are responsible for serializing access to read contexts.</p>

<p>Clients append restart records to a CLFS log by calling <a href="..\wdm\nf-wdm-clfswriterestartarea.md">ClfsWriteRestartArea</a>.       </p>

<p>With the <b>ReadPreviousLogRestartArea</b> routine, clients can implement a form of fuzzy checkpointing. For example, the checkpoint state could consist of the log records delimited by two or more restart records. </p>

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
<a href="kernel.clfs_lsn">CLFS_LSN</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-clfsreadrestartarea.md">ClfsReadRestartArea</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-clfswriterestartarea.md">ClfsWriteRestartArea</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsReadPreviousRestartArea routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
