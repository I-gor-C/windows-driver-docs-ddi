---
UID: NF.ntifs.CcSetLogHandleForFile
title: CcSetLogHandleForFile
author: windows-driver-content
description: The CcSetLogHandleForFile routine sets a log handle for a file.
old-location: ifsk\ccsetloghandleforfile.htm
old-project: ifsk
ms.assetid: 7bb56650-a75e-4b49-bfb3-83848ede29c0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: CcSetLogHandleForFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available on Microsoft Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CcSetLogHandleForFile
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
req.irql: Any level
req.iface: 
---

# CcSetLogHandleForFile function



## -description
<p>The <b>CcSetLogHandleForFile</b> routine sets a log handle for a file. </p>


## -syntax

````
VOID CcSetLogHandleForFile(
  _In_ PFILE_OBJECT  FileObject,
  _In_ PVOID         LogHandle,
  _In_ PFLUSH_TO_LSN FlushToLsnRoutine
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>Pointer to the file object for the file for which the log handle is to be stored. </p>
</dd>

### -param <i>LogHandle</i> [in]

<dd>
<p>Pointer to the log handle that is to be stored. </p>
</dd>

### -param <i>FlushToLsnRoutine</i> [in]

<dd>
<p>Pointer to a log file flush callback routine to call before flushing buffers for this file. This routine is called to ensure that a log file is flushed to the most recent logical sequence number (LSN) for any buffer control block (BCB) being flushed. This routine is declared as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef
VOID (*PFLUSH_TO_LSN) (
            IN PVOID LogHandle,
            IN LARGE_INTEGER Lsn
            );</pre>
</td>
</tr>
</table></span></div>
<dl class="indent">

### -param <a id="LogHandle"></a><a id="loghandle"></a><a id="LOGHANDLE"></a><p><a id="LogHandle"></a><a id="loghandle"></a><a id="LOGHANDLE"></a><b><i>LogHandle</i></b></p>


<dd>
<p>Pointer to an opaque structure that is used to identify this client. </p>
</dd>

### -param <a id="Lsn"></a><a id="lsn"></a><a id="LSN"></a><p><a id="Lsn"></a><a id="lsn"></a><a id="LSN"></a><b><i>Lsn</i></b></p>


<dd>
<p>This is the LSN that must be on the disk on return from this callback routine. </p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>CcSetLogHandleForFile</b> sets a log handle for a file, for use in subsequent calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539088">CcGetDirtyPages</a>. </p>

<p><b>CcSetLogHandleForFile</b> sets a log handle for a file, for use in subsequent calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539088">CcGetDirtyPages</a>. </p>

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
<p>Available on Microsoft Windows XP and later. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539088">CcGetDirtyPages</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539211">CcSetDirtyPinnedData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcSetLogHandleForFile routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
