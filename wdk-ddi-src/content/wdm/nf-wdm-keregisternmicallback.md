---
UID: NF.wdm.KeRegisterNmiCallback
title: KeRegisterNmiCallback function
author: windows-driver-content
description: The KeRegisterNmiCallback routine registers a routine to be called whenever a nonmaskable interrupt (NMI) occurs.
old-location: kernel\keregisternmicallback.htm
old-project: kernel
ms.assetid: 46e666a6-be4c-40fb-b9e1-00ced9fb4d05
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
req.product: Windows 10 or later.
---

# KeRegisterNmiCallback function



## -description
The <b>KeRegisterNmiCallback</b> routine registers a routine to be called whenever a nonmaskable interrupt (NMI) occurs.



## -syntax

````
PVOID KeRegisterNmiCallback(
  _In_     PNMI_CALLBACK CallbackRoutine,
  _In_opt_ PVOID         Context
);
````


## -parameters

### -param CallbackRoutine [in]

Pointer to a function of the form:

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

### -param Context [in, optional]

Specifies the value to be passed as the <i>Context</i> parameter of <i>XxxNmiCallback</i> when it is called.


## -returns
On success, <b>KeRegisterNmiCallback</b> returns an opaque pointer that the caller passes to <a href="kernel.kederegisternmicallback">KeDeregisterNmiCallback</a> to deregister the callback. The routine returns <b>NULL</b> if it is unable to register the callback.


## -remarks
When a nonmaskable interrupt occurs, the system calls each registered callback in reverse order from the order in which they were registered. For the first callback, the system passes <b>FALSE</b> as the <i>Handled</i> parameter. For each subsequent callback, if any previous callback returned <b>TRUE</b>, the system passes <b>TRUE</b> as the <i>Handled</i> parameter, otherwise it passes <b>FALSE</b>. If any callback returns a value of <b>TRUE</b>, the system considers the interrupt to have been handled. Otherwise, the system calls the HAL's default handler for the interrupt, which normally causes the system to bug check.

The callback routine must be able to be run at IRQL = HIGH_LEVEL. 


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
Available in Windows  Server 2003 and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
&lt;= APC_LEVEL (see Remarks section)

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_irqlkeapclte2">IrqlKeApcLte2</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.kederegisternmicallback">KeDeregisterNmiCallback</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeRegisterNmiCallback routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

