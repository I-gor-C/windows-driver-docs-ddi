---
UID: NF.fltkernel.FltGetRequestorSessionId
title: FltGetRequestorSessionId
author: windows-driver-content
description: The FltGetRequestorSessionId routine returns the session ID of the process that originally requested the specified I/O operation.
old-location: ifsk\fltgetrequestorsessionid.htm
old-project: ifsk
ms.assetid: 6a0eb588-fe64-4f36-8648-8e006e16704e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltGetRequestorSessionId
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 7 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltGetRequestorSessionId
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
req.iface: 
---

# FltGetRequestorSessionId function



## -description
<p>The <b>FltGetRequestorSessionId</b> routine returns the session ID of the process that originally requested the specified I/O operation.</p>


## -syntax

````
NTSTATUS FltGetRequestorSessionId(
  _In_  PFLT_CALLBACK_DATA CallbackData,
  _Out_ PULONG             SessionId
);
````


## -parameters
<dl>

### -param <i>CallbackData</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a> structure specifying the I/O operation.</p>
</dd>

### -param <i>SessionId</i> [out]

<dd>
<p>A pointer to the session ID for the requesting operation.</p>
</dd>
</dl>

## -returns
<p>The <b>FltGetRequestorSessionId</b> routine returns STATUS_SUCCESS on success or STATUS_UNSUCCESSFUL on failure.</p>

## -remarks
<p>If a process has no session ID, the SessionId parameter refers to -1 and the <b>FltGetRequestorSessionId</b> routine returns STATUS_SUCCESS.</p>

<p>If the <b>FltGetRequestorSessionId</b> routine returns STATUS_UNSUCCESSFUL, <i>SessionId</i> is not valid.</p>

<p>If a process has no session ID, the SessionId parameter refers to -1 and the <b>FltGetRequestorSessionId</b> routine returns STATUS_SUCCESS.</p>

<p>If the <b>FltGetRequestorSessionId</b> routine returns STATUS_UNSUCCESSFUL, <i>SessionId</i> is not valid.</p>

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
<p>Available in Microsoft Windows 7 and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>FltKernel.h (include FltKernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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