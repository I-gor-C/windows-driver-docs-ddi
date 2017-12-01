---
UID: NF.ntddk.RtlRunOnceComplete
title: RtlRunOnceComplete
author: windows-driver-content
description: The RtlRunOnceComplete routine completes the one-time initialization began by RtlRunOnceBeginInitialize.
old-location: kernel\rtlrunoncecomplete.htm
old-project: kernel
ms.assetid: 1cdc4fde-2370-4e58-9e67-dec731cdb935
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlRunOnceComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlRunOnceComplete
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

# RtlRunOnceComplete function



## -description
<p>The <b>RtlRunOnceComplete</b> routine completes the one-time initialization began by <a href="..\ntddk\nf-ntddk-rtlrunoncebegininitialize.md">RtlRunOnceBeginInitialize</a>.</p>


## -syntax

````
NTSTATUS RtlRunOnceComplete(
  _Inout_  PRTL_RUN_ONCE RunOnce,
  _In_     ULONG         Flags,
  _In_opt_ PVOID         Context
);
````


## -parameters
<dl>

### -param <i>RunOnce</i> [in, out]

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563626">RTL_RUN_ONCE</a> one-time initialization structure.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Drivers can optionally specify one or more of the following flags:</p>
<p></p>
<dl>

### -param <a id="RTL_RUN_ONCE_ASYNC"></a><a id="rtl_run_once_async"></a>RTL_RUN_ONCE_ASYNC

<dd>
<p>Operate in asynchronous mode. This mode enables multiple completion attempts to execute in parallel. If this flag is used, subsequent calls to the <b>RtlRunOnceComplete</b> routine will fail unless this flag is also specified.</p>
</dd>

### -param <a id="RTL_RUN_ONCE_INIT_FAILED"></a><a id="rtl_run_once_init_failed"></a>RTL_RUN_ONCE_INIT_FAILED

<dd>
<p>The initialization attempt failed. </p>
</dd>
</dl>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>Specifies the initialized data. </p>
</dd>
</dl>

## -returns
<p><b>RtlRunOnceComplete</b> returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The operation could not be completed. If the caller specified RTL_RUN_ONCE_ASYNC in the <i>Flags</i> parameter, this value can indicate that another thread completed the initialization.</p>

<p> </p>

## -remarks
<p>If <b>RtlRunOnceComplete</b> returns STATUS_SUCCESS, any subsequent call to <a href="..\ntddk\nf-ntddk-rtlrunoncebegininitialize.md">RtlRunOnceBeginInitialize</a> for the same <a href="https://msdn.microsoft.com/library/windows/hardware/ff563626">RTL_RUN_ONCE</a> structure supplies <i>Context</i> as the initialized data.</p>

<p>If the caller specified RTL_RUN_ONCE_ASYNC in the <i>Flags</i> parameter and <b>RtlRunOnceComplete</b> returns any value other than STATUS_SUCCESS, the caller must clean up any initialization that it attempted. </p>

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
<p>Available in Windows Vista and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563626">RTL_RUN_ONCE</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlrunoncebegininitialize.md">RtlRunOnceBeginInitialize</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlrunonceexecuteonce.md">RtlRunOnceExecuteOnce</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlrunonceinitialize.md">RtlRunOnceInitialize</a>
</dt>
<dt>
<a href="kernel.runonceinitialization">RunOnceInitialization</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlRunOnceComplete routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
