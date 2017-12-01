---
UID: NF.ntddk.RtlRunOnceBeginInitialize
title: RtlRunOnceBeginInitialize
author: windows-driver-content
description: The RtlRunOnceBeginInitialize routine begins a one-time initialization.
old-location: kernel\rtlrunoncebegininitialize.htm
old-project: kernel
ms.assetid: ed96b2ec-95ea-47a6-a3b0-f4d018e0c8e2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlRunOnceBeginInitialize
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
req.alt-api: RtlRunOnceBeginInitialize
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

# RtlRunOnceBeginInitialize function



## -description
<p>The <b>RtlRunOnceBeginInitialize</b> routine begins a one-time initialization.</p>


## -syntax

````
NTSTATUS RtlRunOnceBeginInitialize(
  _Inout_ PRTL_RUN_ONCE RunOnce,
  _In_    ULONG         Flags,
  _Out_   PVOID         *Context
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
<p>Perform initialization asynchronously. The driver can perform multiple completion attempts in parallel. If this flag is used, subsequent calls to this routine will fail unless this flag is also specified.</p>
</dd>

### -param <a id="RTL_RUN_ONCE_CHECK_ONLY"></a><a id="rtl_run_once_check_only"></a>RTL_RUN_ONCE_CHECK_ONLY

<dd>
<p>Do not begin initialization, but check to determine if initialization has already occurred. If <b>RtlRunOnceBeginInitialize</b> returns STATUS_SUCCESS, the initialization succeeded, and *<i>Context</i> contains the initialized data. </p>
</dd>
</dl>
</dd>

### -param <i>Context</i> [out]

<dd>
<p>Specifies a pointer to a PVOID variable that receives the initialized data. The value of *<i>Context</i> is valid only when the routine returns STATUS_SUCCESS.</p>
</dd>
</dl>

## -returns
<p><b>RtlRunOnceBeginInitialize</b> returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The one-time initialization has already completed. The initialized data is stored in the memory location that <i>Context</i> points to.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The caller has successfully begun one-time initialization. The caller now performs the driver-specific initialization steps and then calls <a href="..\ntddk\nf-ntddk-rtlrunoncecomplete.md">RtlRunOnceComplete</a> to complete the initialization. </p>

<p> </p>

## -remarks
<p>Drivers can alternatively perform one-time initialization by calling <a href="..\ntddk\nf-ntddk-rtlrunonceexecuteonce.md">RtlRunOnceExecuteOnce</a> and supplying a <a href="kernel.runonceinitialization">RunOnceInitialization</a> routine.</p>

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
<a href="..\ntddk\nf-ntddk-rtlrunoncecomplete.md">RtlRunOnceComplete</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlRunOnceBeginInitialize routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
