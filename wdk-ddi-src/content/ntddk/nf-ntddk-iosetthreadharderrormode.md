---
UID: NF.ntddk.IoSetThreadHardErrorMode
title: IoSetThreadHardErrorMode
author: windows-driver-content
description: The IoSetThreadHardErrorMode routine enables or disables hard error reporting for the current thread.
old-location: kernel\iosetthreadharderrormode.htm
old-project: kernel
ms.assetid: bedb6399-8f79-477a-9a90-4a7dec5c5dae
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoSetThreadHardErrorMode
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoSetThreadHardErrorMode
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# IoSetThreadHardErrorMode function



## -description
<p>The <b>IoSetThreadHardErrorMode</b> routine enables or disables hard error reporting for the current thread.</p>


## -syntax

````
BOOLEAN IoSetThreadHardErrorMode(
  _In_ BOOLEAN EnableHardErrors
);
````


## -parameters
<dl>

### -param EnableHardErrors [in]

<dd>
<p>Specifies whether hard error reporting to the user should be enabled or disabled for this thread. A value of <b>TRUE</b> enables hard error reporting. <b>FALSE</b> disables it. </p>
</dd>
</dl>

## -returns
<p><b>IoSetThreadHardErrorMode</b> returns <b>TRUE</b> if hard errors were enabled from this thread before this routine completed execution. Otherwise, this routine returns <b>FALSE</b>. </p>

## -remarks
<p>If hard errors are disabled for a given thread, calls to <b>IoRaiseHardError</b> will not display a message to the user indicating that a serious error has occurred. In addition, the IRP that is passed to <b>IoRaiseHardError </b>is completed without any data being copied into user buffers. Calling <b>IoRaiseInformationalHardError</b> after disabling hard errors causes that routine to always return <b>FALSE</b> for this thread.</p>

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
<p>Available in Microsoft Windows 2000 and later versions of Windows. </p>
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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-ioraiseharderror.md">IoRaiseHardError</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-ioraiseinformationalharderror.md">IoRaiseInformationalHardError</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoSetThreadHardErrorMode routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
