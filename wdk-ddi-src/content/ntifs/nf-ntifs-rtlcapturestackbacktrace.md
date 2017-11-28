---
UID: NF.ntifs.RtlCaptureStackBackTrace
title: RtlCaptureStackBackTrace
author: windows-driver-content
description: The RtlCaptureStackBackTrace routine captures a stack back trace by walking up the stack and recording the information for each frame.
old-location: ifsk\rtlcapturestackbacktrace.htm
old-project: ifsk
ms.assetid: e4ad1eac-1788-4dfe-9444-f40e0de156c4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlCaptureStackBackTrace
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in starting with Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlCaptureStackBackTrace
req.alt-loc: NtDll.dll,NtosKrnl.exe,API-MS-Win-Core-RTLSupport-l1-1-0.dll,API-MS-Win-Core-RTLSupport-l1-2-0.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib; 
OneCoreUAP.lib on Windows 10
req.dll: NtDll.dll (user mode); 
NtosKrnl.exe (kernel mode)
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# RtlCaptureStackBackTrace function



## -description
<p>The <b>RtlCaptureStackBackTrace</b> routine captures a stack back trace by walking up the stack and recording the information for each frame.</p>


## -syntax

````
USHORT RtlCaptureStackBackTrace(
  _In_      ULONG  FramesToSkip,
  _In_      ULONG  FramesToCapture,
  _Out_     PVOID  *BackTrace,
  _Out_opt_ PULONG BackTraceHash
);
````


## -parameters
<dl>

### -param <i>FramesToSkip</i> [in]

<dd>
<p>The number of frames to skip from the start of the back trace.</p>
</dd>

### -param <i>FramesToCapture</i> [in]

<dd>
<p>The number of frames to be captured. </p>
</dd>

### -param <i>BackTrace</i> [out]

<dd>
<p>An array of pointers captured from the current stack trace.</p>
</dd>

### -param <i>BackTraceHash</i> [out, optional]

<dd>
<p>An optional value that can be used to organize hash tables. If this parameter is <b>NULL</b>, no hash value is computed.</p>
<p>This value is calculated based on the values of the pointers returned in the <i>BackTrace</i> array. Two identical stack traces will generate identical hash values.</p>
</dd>
</dl>

## -returns
<p>The number of captured frames.</p>

## -remarks


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
<p>Available in starting with Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or FltKernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib; </dt>
<dt>OneCoreUAP.lib on Windows 10</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtDll.dll (user mode); </dt>
<dt>NtosKrnl.exe (kernel mode)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>