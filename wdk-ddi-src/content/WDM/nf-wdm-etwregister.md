---
UID: NF.wdm.EtwRegister
title: EtwRegister
author: windows-driver-content
description: The EtwRegister function registers the event provider and must be called before a provider can start tracing.
old-location: devtest\etwregister.htm
ms.assetid: 89a37edb-0f58-45c2-9045-b31eec5a4281
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: devtest
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EtwRegister
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
ms.keywords: EtwRegister
req.iface: 
req.product: Windows 10 or later.
---

# EtwRegister function



## -description
<p>The <b>EtwRegister</b> function registers the event provider and must be called before a provider can start tracing. The <b>EtwRegister</b> function is the kernel mode counterpart to the user-mode <b>EventRegister</b> function. The function can also provide a pointer to an optional callback function that can be used to provide additional event filtering capabilities. </p>


## -syntax

````
NTSTATUS EtwRegister(
  _In_     LPCGUID            ProviderId,
  _In_opt_ PETWENABLECALLBACK EnableCallback,
  _In_opt_ PVOID              CallbackContext,
  _Out_    PREGHANDLE         RegHandle
);
````


## -parameters
<dl>

### -param <i>ProviderId</i> [in]

<dd>
<p>A pointer to the event provider GUID. </p>
</dd>

### -param <i>EnableCallback</i> [in, optional]

<dd>
<p>A pointer to an optional callback function. The callback function provides additional event filtering capabilities. The callback function is user-defined.</p>
</dd>

### -param <i>CallbackContext</i> [in, optional]

<dd>
<p>The function passes back the optional callback context when a callback is made. You can specify the optional context when you register a provider.  The <i>CallbackContext</i> parameter supports the scenarios in which one callback is shared by multiple providers, as in a C++ class. The <i>CallbackContext</i> provides a way to distinguish the target provider instances for the enable callback. </p>
</dd>

### -param <i>RegHandle</i> [out]

<dd>
<p>A pointer to a variable that receives the provider registration handle if the function call is successful. </p>
</dd>
</dl>

## -returns
<p>The <b>EtwRegister</b> function returns a status code from the following list:</p><dl>
<dt><b>STATUS_SUCCESS  </b></dt>
</dl><p>Indicates that event provider was successfully registered with ETW.   </p><dl>
<dt><b>STATUS_INVALID_PARAMETER  </b></dt>
</dl><p>Indicates that the parameter  was not valid. </p><dl>
<dt><b>STATUS_Xxx </b></dt>
</dl><p>Indicates that the request failed for the reason specified by the NTSTATUS value. See Ntstatus.h for detailed information about the actual status return code.</p>

<p> </p>

## -remarks
<p>Before a kernel-mode driver can trace events, the driver must register as an event provider using the <b>EtwRegister</b> function. When a kernel mode driver calls <b>EtwRegister</b>, the function returns a registration handle. This registration handle can be used to test whether a keyword or level is enabled for a specific provider and to call event tracing and logging functions. After tracing is complete, a driver must call the <b>EtwUnregister</b> function to unregister the provider. For every call to <b>EtwRegister</b> there must be a corresponding call to <b>EtwUnregister</b>. Failure to unregister the event provider can cause errors when the process is unloaded because the callback functions associated with the process are no longer valid. No tracing calls should be made that fall outside of the code bounded by the <b>EtwRegister</b> and <b>EtwUnregister</b> functions. For the best performance, you can call the <b>EtwRegister</b> function in your <b>DriverEntry</b> routine and the <b>EtwUnregister</b> function in your <b>DriverUnload</b> routine.</p>

<p>Callers of <b>EtwRegister</b> must be running at IRQL = PASSIVE_LEVEL in the context of a system thread.</p>

<p>Before a kernel-mode driver can trace events, the driver must register as an event provider using the <b>EtwRegister</b> function. When a kernel mode driver calls <b>EtwRegister</b>, the function returns a registration handle. This registration handle can be used to test whether a keyword or level is enabled for a specific provider and to call event tracing and logging functions. After tracing is complete, a driver must call the <b>EtwUnregister</b> function to unregister the provider. For every call to <b>EtwRegister</b> there must be a corresponding call to <b>EtwUnregister</b>. Failure to unregister the event provider can cause errors when the process is unloaded because the callback functions associated with the process are no longer valid. No tracing calls should be made that fall outside of the code bounded by the <b>EtwRegister</b> and <b>EtwUnregister</b> functions. For the best performance, you can call the <b>EtwRegister</b> function in your <b>DriverEntry</b> routine and the <b>EtwUnregister</b> function in your <b>DriverUnload</b> routine.</p>

<p>Callers of <b>EtwRegister</b> must be running at IRQL = PASSIVE_LEVEL in the context of a system thread.</p>

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
<dt>Wdm.h (include Wdm.h or Ntddk.h)</dt>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545613">EtwUnregister</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [devtest\devtest]:%20EtwRegister function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
