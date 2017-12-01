---
UID: NF.rxprocs.RxLogEventWithBufferDirect
title: RxLogEventWithBufferDirect
author: windows-driver-content
description: RxLogEventWithBufferDirect allocates an I/O error log structure, fills it in with information, and writes the entry to the I/O error log.
old-location: ifsk\rxlogeventwithbufferdirect.htm
old-project: ifsk
ms.assetid: 09a7d452-efa1-4846-8077-1f6ce60515e7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxLogEventWithBufferDirect
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxprocs.h
req.include-header: Rxprocs.h, Rxstruc.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxLogEventWithBufferDirect
req.alt-loc: rxprocs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# RxLogEventWithBufferDirect function



## -description
<p><b>RxLogEventWithBufferDirect</b> allocates an I/O error log structure, fills it in with information, and writes the entry to the I/O error log.</p>


## -syntax

````
VOID RxLogEventWithBufferDirect(
  _In_ PVOID           DeviceObject,
  _In_ PUNICODE_STRING OriginatorId,
  _In_ ULONG           EventId,
  _In_ NTSTATUS        Status,
  _In_ PVOID           DataBuffer,
  _In_ USHORT          DataBufferLength,
  _In_ ULONG           LineNumber
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>A pointer to the RDBSS device object.</p>
</dd>

### -param <i>OriginatorId</i> [in]

<dd>
<p>The string indicating the caller generating the error.</p>
</dd>

### -param <i>EventId</i> [in]

<dd>
<p>The value indicating the I/O error log code which is different than an NTSTATUS value returned by a routine. The legal I/O error log code values are defined in the <i>ntiolog.h</i> header file included with the Microsoft Windows SDK and Visual Studio. </p>
</dd>

### -param <i>Status</i> [in]

<dd>
<p>The value indicating the status code of a routine indicating a failure.</p>
</dd>

### -param <i>DataBuffer</i> [in]

<dd>
<p>A pointer to a data buffer to be added to the I/O error log structure.</p>
</dd>

### -param <i>DataBufferLength</i> [in]

<dd>
<p>The length of the data buffer to be added to the I/O error log structure.</p>
</dd>

### -param <i>LineNumber</i> [in]

<dd>
<p>The line number in the source code file where this failure occurred.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>RxLogEventDirect</b> internally calls the <b>RxLogEventWithAnnotation</b> routine to create and write the log entry passing the <i>Status</i> and <i>LineNumber</i> parameters as the <i>Annotations</i> parameter to <b>RxLogEventWithAnnotation</b>. </p>

<p>The I/O error log entry size is limited to a length of 255 characters. So if the combined length of the <i>EventId</i>, <i>DataBuffer</i>, and <i>Annotations</i> parameters plus the size of the fixed part of the I/O error log entry exceeds 255, then no I/O error log entry will be created.</p>

<p>The <b>RxLogEventWithAnnotation</b> routine needs to allocate memory in order to create the I/O error log entry . Consequently, <b>RxLogEventWithBufferDirect</b> can silently fail if the memory allocation fails. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Rxprocs.h (include Rxprocs.h or Rxstruc.h)</dt>
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
<a href="..\rxprocs\nf-rxprocs-rxlogeventdirect.md">RxLogEventDirect</a>
</dt>
<dt>
<a href="..\rxprocs\nf-rxprocs-rxlogeventwithannotation.md">RxLogEventWithAnnotation</a>
</dt>
<dt>
<a href="..\rxlog\nf-rxlog--rxlog.md">_RxLog</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxLogEventWithBufferDirect function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
