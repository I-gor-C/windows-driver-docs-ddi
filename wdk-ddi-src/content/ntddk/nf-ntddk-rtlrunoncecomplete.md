---
UID: NF.ntddk.RtlRunOnceComplete
title: RtlRunOnceComplete function
author: windows-driver-content
description: The RtlRunOnceComplete routine completes the one-time initialization began by RtlRunOnceBeginInitialize.
old-location: kernel\rtlrunoncecomplete.htm
old-project: kernel
ms.assetid: 1cdc4fde-2370-4e58-9e67-dec731cdb935
ms.author: windowsdriverdev
ms.date: 12/6/2017
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
---

# RtlRunOnceComplete function



## -description
The <b>RtlRunOnceComplete</b> routine completes the one-time initialization began by <a href="kernel.rtlrunoncebegininitialize">RtlRunOnceBeginInitialize</a>.


## -syntax

````
NTSTATUS RtlRunOnceComplete(
  _Inout_  PRTL_RUN_ONCE RunOnce,
  _In_     ULONG         Flags,
  _In_opt_ PVOID         Context
);
````


## -parameters

### -param RunOnce [in, out]

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563626">RTL_RUN_ONCE</a> one-time initialization structure.

### -param Flags [in]

Drivers can optionally specify one or more of the following flags:


### -param RTL_RUN_ONCE_ASYNC

Operate in asynchronous mode. This mode enables multiple completion attempts to execute in parallel. If this flag is used, subsequent calls to the <b>RtlRunOnceComplete</b> routine will fail unless this flag is also specified.

### -param RTL_RUN_ONCE_INIT_FAILED

The initialization attempt failed. 
</dd>
</dl>

### -param Context [in, optional]

Specifies the initialized data. 

## -returns
<b>RtlRunOnceComplete</b> returns one of the following NTSTATUS values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The operation completed successfully.
<dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl>The operation could not be completed. If the caller specified RTL_RUN_ONCE_ASYNC in the <i>Flags</i> parameter, this value can indicate that another thread completed the initialization.

 

## -remarks
If <b>RtlRunOnceComplete</b> returns STATUS_SUCCESS, any subsequent call to <a href="kernel.rtlrunoncebegininitialize">RtlRunOnceBeginInitialize</a> for the same <a href="https://msdn.microsoft.com/library/windows/hardware/ff563626">RTL_RUN_ONCE</a> structure supplies <i>Context</i> as the initialized data.

If the caller specified RTL_RUN_ONCE_ASYNC in the <i>Flags</i> parameter and <b>RtlRunOnceComplete</b> returns any value other than STATUS_SUCCESS, the caller must clean up any initialization that it attempted. 

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows Vista and later versions of Windows.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563626">RTL_RUN_ONCE</a>
</dt>
<dt>
<a href="kernel.rtlrunoncebegininitialize">RtlRunOnceBeginInitialize</a>
</dt>
<dt>
<a href="kernel.rtlrunonceexecuteonce">RtlRunOnceExecuteOnce</a>
</dt>
<dt>
<a href="kernel.rtlrunonceinitialize">RtlRunOnceInitialize</a>
</dt>
<dt>
<a href="kernel.runonceinitialization">RunOnceInitialization</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlRunOnceComplete routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
