---
UID: NF.wdm.KeRegisterBoundCallback
title: KeRegisterBoundCallback
author: windows-driver-content
description: The KeRegisterBoundCallback routine registers a routine to be called whenever a user-mode bound exception occurs.
old-location: kernel\keregisterboundcallback.htm
old-project: kernel
ms.assetid: 0985589E-074A-45C8-9F8A-384DC42EC884
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KeRegisterBoundCallback
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeRegisterBoundCallback
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
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# KeRegisterBoundCallback function



## -description
<p>The <b>KeRegisterBoundCallback</b> routine registers a routine to be called whenever a user-mode bound exception occurs.</p>


## -syntax

````
PVOID KeRegisterBoundCallback(
  _In_ PBOUND_CALLBACK CallbackRoutine
);
````


## -parameters
<dl>

### -param <i>CallbackRoutine</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn957853">BoundCallback</a> function.</p>
</dd>
</dl>

## -returns
<p>On success, <b>KeRegisterBoundCallback</b> returns an opaque pointer that the caller passes to <a href="https://msdn.microsoft.com/library/windows/hardware/dn957855">KeDeregisterBoundCallback</a> to deregister the callback. The routine returns <b>NULL</b> if it is unable to register the callback.</p>

## -remarks
<p>The <b>KeRegisterBoundCallback</b> routine provides the opportunity for a kernel-mode driver to intercept and handle user-mode bound exceptions. When a bounds exception for a user-mode thread occurs, the system calls the registered  <a href="https://msdn.microsoft.com/library/windows/hardware/dn957853">BoundCallback</a> function to manage the bounds trap. The return value of the <i>BoundCallback</i> function indicates the action that the system should then perform, such as propagating the bounds exception or terminating the user-mode process. </p>

<p>The <b>KeRegisterBoundCallback</b> routine provides the opportunity for a kernel-mode driver to intercept and handle user-mode bound exceptions. When a bounds exception for a user-mode thread occurs, the system calls the registered  <a href="https://msdn.microsoft.com/library/windows/hardware/dn957853">BoundCallback</a> function to manage the bounds trap. The return value of the <i>BoundCallback</i> function indicates the action that the system should then perform, such as propagating the bounds exception or terminating the user-mode process. </p>

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
<p>Available starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn957855">KeDeregisterBoundCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeRegisterBoundCallback routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
