---
UID: NF.ntifs.FsRtlLogCcFlushError
title: FsRtlLogCcFlushError
author: windows-driver-content
description: The FsRtlLogCcFlushError routine logs a lost delayed-write error and displays a dialog box to the user.
old-location: ifsk\fsrtllogccflusherror.htm
old-project: ifsk
ms.assetid: e516758d-d1fe-4977-93bb-f427972fdd3c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlLogCcFlushError
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlLogCcFlushError
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
req.irql: <= APC_LEVEL
req.iface: 
---

# FsRtlLogCcFlushError function



## -description
<p>The <b>FsRtlLogCcFlushError</b> routine logs a lost delayed-write error and displays a dialog box to the user.</p>


## -syntax

````
NTSTATUS FsRtlLogCcFlushError(
  _In_ PUNICODE_STRING          FileName,
  _In_ PDEVICE_OBJECT           DeviceObject,
  _In_ PSECTION_OBJECT_POINTERS SectionObjectPointer,
  _In_ NTSTATUS                 FlushError,
  _In_ ULONG                    Flags
);
````


## -parameters
<dl>

### -param FileName [in]

<dd>
<p>The name of the file that could not be flushed.</p>
</dd>

### -param DeviceObject [in]

<dd>
<p>A pointer to the device object that this log entry should be filed against.</p>
</dd>

### -param SectionObjectPointer [in]

<dd>
<p>A pointer to the section object for the file on which the flush failed.</p>
</dd>

### -param FlushError [in]

<dd>
<p>The error returned by the call to <a href="..\ntifs\nf-ntifs-ccflushcache.md">CcFlushCache</a>.</p>
</dd>

### -param Flags [in]

<dd>
<p>A value of 0 or a bitwise combination of one or more of the following flags:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FSRTL_CC_FLUSH_ERROR_FLAG_NO_HARD_ERROR</p>
</td>
<td>
<p>Suppresses presentation of an informational dialog box to the user.</p>
</td>
</tr>
<tr>
<td>
<p>FSRTL_CC_FLUSH_ERROR_FLAG_NO_LOG_ENTRY</p>
</td>
<td>
<p>Suppresses generation of a system error log entry.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>The <b>FsRtlLogCcFlushError</b> routine returns STATUS_SUCCESS on success or another NTSTATUS value, such as STATUS_INSUFFICIENT_RESOURCES.</p>

## -remarks
<p>Unless the call includes appropriate <i>Flags</i>, the <b>FsRtlLogCcFlushError</b> routine uses <a href="..\ntddk\nf-ntddk-ioraiseinformationalharderror.md">IoRaiseInformationalHardError</a> to display a dialog box to the user, including the specific error and <i>FileName</i>, and uses <a href="..\wdm\nf-wdm-iowriteerrorlogentry.md">IoWriteErrorLogEntry</a> logs the error. </p>

<p>If the entire <i>FileName</i> cannot fit within the log buffer, the routine inserts an ellipsis into the file name.</p>

<p>If the cache still has pages that have been modified, the error is not fatal. The routine returns to the caller without logging an error or displaying the dialog box. </p>

<p>If the error is fatal, the routine increments the lost delayed write counter in the processor control block (<a href="wdkgloss.p#wdkgloss.prcb#wdkgloss.prcb"><i>PRCB</i></a>). This counter can be used in troubleshooting lost delayed write errors.</p>

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
<p>Available in Windows Vista and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-ccflushcache.md">CcFlushCache</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-ioraiseinformationalharderror.md">IoRaiseInformationalHardError</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iowriteerrorlogentry.md">IoWriteErrorLogEntry</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlLogCcFlushError routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
