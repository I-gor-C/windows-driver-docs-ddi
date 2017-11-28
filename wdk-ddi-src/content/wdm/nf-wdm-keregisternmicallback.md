---
UID: NF.wdm.KeRegisterNmiCallback
title: KeRegisterNmiCallback
author: windows-driver-content
description: The KeRegisterNmiCallback routine registers a routine to be called whenever a nonmaskable interrupt (NMI) occurs.
old-location: kernel\keregisternmicallback.htm
old-project: kernel
ms.assetid: 46e666a6-be4c-40fb-b9e1-00ced9fb4d05
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KeRegisterNmiCallback
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows  Server 2003 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeRegisterNmiCallback
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlKeApcLte2, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# KeRegisterNmiCallback function



## -description
<p>The <b>KeRegisterNmiCallback</b> routine registers a routine to be called whenever a nonmaskable interrupt (NMI) occurs.</p>


## -syntax

````
PVOID KeRegisterNmiCallback(
  _In_     PNMI_CALLBACK CallbackRoutine,
  _In_opt_ PVOID         Context
);
````


## -parameters
<dl>

### -param <i>CallbackRoutine</i> [in]

<dd>
<p>Pointer to a function of the form:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>BOOLEAN
 XxxNmiCallback(
 IN PVOID Context,
  IN BOOLEAN Handled
 );</pre>
</td>
</tr>
</table></span></div>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>Specifies the value to be passed as the <i>Context</i> parameter of <i>XxxNmiCallback</i> when it is called.</p>
</dd>
</dl>

## -returns
<p>On success, <b>KeRegisterNmiCallback</b> returns an opaque pointer that the caller passes to <a href="https://msdn.microsoft.com/library/windows/hardware/ff552008">KeDeregisterNmiCallback</a> to deregister the callback. The routine returns <b>NULL</b> if it is unable to register the callback.</p>

## -remarks
<p>When a nonmaskable interrupt occurs, the system calls each registered callback in reverse order from the order in which they were registered. For the first callback, the system passes <b>FALSE</b> as the <i>Handled</i> parameter. For each subsequent callback, if any previous callback returned <b>TRUE</b>, the system passes <b>TRUE</b> as the <i>Handled</i> parameter, otherwise it passes <b>FALSE</b>. If any callback returns a value of <b>TRUE</b>, the system considers the interrupt to have been handled. Otherwise, the system calls the HAL's default handler for the interrupt, which normally causes the system to bug check.</p>

<p>The callback routine must be able to be run at IRQL = HIGH_LEVEL. </p>

<p>When a nonmaskable interrupt occurs, the system calls each registered callback in reverse order from the order in which they were registered. For the first callback, the system passes <b>FALSE</b> as the <i>Handled</i> parameter. For each subsequent callback, if any previous callback returned <b>TRUE</b>, the system passes <b>TRUE</b> as the <i>Handled</i> parameter, otherwise it passes <b>FALSE</b>. If any callback returns a value of <b>TRUE</b>, the system considers the interrupt to have been handled. Otherwise, the system calls the HAL's default handler for the interrupt, which normally causes the system to bug check.</p>

<p>The callback routine must be able to be run at IRQL = HIGH_LEVEL. </p>

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
<p>Available in Windows  Server 2003 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<p>&lt;= APC_LEVEL (see Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547806">IrqlKeApcLte2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552008">KeDeregisterNmiCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeRegisterNmiCallback routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
