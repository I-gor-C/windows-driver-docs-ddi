---
UID: NF.wdm.ObRegisterCallbacks
title: ObRegisterCallbacks
author: windows-driver-content
description: The ObRegisterCallbacks routine registers a list of callback routines for thread, process, and desktop handle operations.
old-location: kernel\obregistercallbacks.htm
old-project: kernel
ms.assetid: 93593979-fe5f-48de-9c98-92acd43ec750
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ObRegisterCallbacks
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista with Service Pack 1 (SP1) and Windows Server 2008.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ObRegisterCallbacks
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
req.product: Windows 10 or later.
---

# ObRegisterCallbacks function



## -description
<p>The <b>ObRegisterCallbacks</b> routine registers a list of callback routines for thread, process, and desktop handle operations.</p>


## -syntax

````
NTSTATUS ObRegisterCallbacks(
  _In_  POB_CALLBACK_REGISTRATION CallBackRegistration,
  _Out_ PVOID                     *RegistrationHandle
);
````


## -parameters
<dl>

### -param <i>CallBackRegistration</i> [in]

<dd>
<p>A pointer to an <a href="..\wdm\ns-wdm--ob-callback-registration.md">OB_CALLBACK_REGISTRATION</a> structure that specifies the list of callback routines and other registration information.</p>
</dd>

### -param <i>RegistrationHandle</i> [out]

<dd>
<p>A pointer to a variable that receives a value that identifies the set of registered callback routines. The caller passes this value to the <a href="..\wdm\nf-wdm-obunregistercallbacks.md">ObUnRegisterCallbacks</a> routine to unregister the set of callbacks. </p>
</dd>
</dl>

## -returns
<p><b>ObRegisterCallbacks</b> returns an NTSTATUS value. This routine might return one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The specified callback routines are registered with the system.</p><dl>
<dt><b>STATUS_FLT_INSTANCE_ALTITUDE_COLLISION</b></dt>
</dl><p>The calling driver or another driver has already registered callback routines for the altitude that <i>CallBackRegistration</i>-&gt;<b>Altitude</b> specifies. For more information about this altitude, see the description of the <b>Altitude</b> member in <a href="..\wdm\ns-wdm--ob-callback-registration.md">OB_CALLBACK_REGISTRATION</a>.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One or more of the parameters that were specified in the registration was invalid. <b>ObRegisterCallbacks</b> might return this error, for example, if an invalid value for <i>CallBackRegistration</i>-&gt;<b>Version</b> is specified or if registration is attempted for object types that do not support callback routines.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The callback routines do not reside in a signed kernel binary image.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>An attempt to allocate memory failed.</p>

<p> </p>

## -remarks
<p>A driver must unregister all callback routines before it unloads. You can unregister the callback routine by calling the <b>ObUnRegisterCallbacks</b> routine.</p>

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
<p>Available starting with Windows Vista with Service Pack 1 (SP1) and Windows Server 2008.</p>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--ob-callback-registration.md">OB_CALLBACK_REGISTRATION</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-obunregistercallbacks.md">ObUnRegisterCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ObRegisterCallbacks routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
