---
UID: NF.wsk.WskCaptureProviderNPI
title: WskCaptureProviderNPI
author: windows-driver-content
description: The WskCaptureProviderNPI function captures a provider Network Programming Interface (NPI) when it becomes available from the WSK subsystem.
old-location: netvista\wskcaptureprovidernpi.htm
ms.assetid: b5c6667e-33b4-4482-8817-c01d9d314c3a
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WskCaptureProviderNPI
req.alt-loc: Netio.lib,Netio.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Netio.lib
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: WskCaptureProviderNPI
req.iface: 
req.product: Windows 10 or later.
---

# WskCaptureProviderNPI function



## -description
<p>The 
  <b>WskCaptureProviderNPI</b> function captures a provider 
  <a href="netvista.network_programming_interface">Network Programming Interface
  (NPI)</a> when it becomes available from the WSK subsystem.</p>


## -syntax

````
NTSTATUS WskCaptureProviderNPI(
  _In_  PWSK_REGISTRATION WskRegistration,
  _In_  ULONG             WaitTimeout,
  _Out_ PWSK_PROVIDER_NPI WskProviderNpi
);
````


## -parameters
<dl>

### -param <i>WskRegistration</i> [in]

<dd>
<p>A pointer to the memory location initialized by 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571143">WskRegister</a> that identifies a WSK
     application's registration instance. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571178">WSK_REGISTRATION</a>.</p>
</dd>

### -param <i>WaitTimeout</i> [in]

<dd>
<p>The time, in milliseconds, that the 
     <b>WskCaptureProviderNPI</b> function can wait until the WSK provider NPI becomes available. Alternately,
     the following can be specified:
     </p>
<p></p>
<dl>

### -param <a id="WSK_NO_WAIT"></a><a id="wsk_no_wait"></a>WSK_NO_WAIT

<dd>
<p>Return from this function immediately if the provider NPI is not available.</p>
</dd>

### -param <a id="WSK_INFINITE_WAIT"></a><a id="wsk_infinite_wait"></a>WSK_INFINITE_WAIT

<dd>
<p>Wait until the provider NPI is available from the WSK subsystem.</p>
</dd>
</dl>
<p>For more information about how this parameter is used, see 
     <a href="netvista.registering_a_winsock_kernel_application">Registering a Winsock
     Kernel Application</a>.</p>
</dd>

### -param <i>WskProviderNpi</i> [out]

<dd>
<p>A pointer to the NPI returned by the WSK provider. This 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571177">WSK_PROVIDER_NPI</a> structure contains a
     pointer to the WSK provider dispatch table of WSK functions that the WSK application can call.</p>
</dd>
</dl>

## -returns
<p><b>WskCaptureProviderNPI</b> returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The provider NPI capture completed successfully.</p><dl>
<dt><b>STATUS_DEVICE_NOT_READY</b></dt>
</dl><p>The provider NPI was not yet available.</p><dl>
<dt><b>STATUS_NOINTERFACE</b></dt>
</dl><p>The version requested by the WSK client is not supported by the WSK subsystem.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>The provider NPI capture failed.</p>

<p> </p>

## -remarks
<p>For each call to 
    <b>WskCaptureProviderNPI</b> that returns a success code, there must be exactly one corresponding 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571145">WskReleaseProviderNPI</a> call that uses
    the same 
    <i>WskRegistration</i> parameter that was passed to 
    <b>WskCaptureProviderNPI</b>.</p>

<p><b>WskCaptureProviderNPI</b> can be called after a call is made to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571128">WskDeregister</a> only if the 
    <i>WskRegistration</i> block is not freed or overwritten. After 
    <b>WskDeregister</b> is called, any further calls to 
    <b>WskCaptureProviderNPI</b> will fail with status code STATUS_DEVICE_NOT_READY, and, unless the provider
    NPI becomes available concurrently, any existing 
    <b>WskCaptureProviderNPI</b> calls that are blocked in other threads waiting for the WSK provider NPI to
    become available will also return immediately with status code STATUS_DEVICE_NOT_READY.</p>

<p>For more information about attaching a WSK application to the WSK subsystem, see 
    <a href="netvista.registering_a_winsock_kernel_application">Registering a Winsock Kernel
    Application</a>.</p>

<p>Callers of the 
    <b>WskCaptureProviderNPI</b> function must be running at IRQL = PASSIVE_LEVEL if 
    <i>WaitTimeout</i> is not set to WSK_NO_WAIT; otherwise, callers must be running at IRQL &lt;=
    DISPATCH_LEVEL.</p>

<p>For each call to 
    <b>WskCaptureProviderNPI</b> that returns a success code, there must be exactly one corresponding 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571145">WskReleaseProviderNPI</a> call that uses
    the same 
    <i>WskRegistration</i> parameter that was passed to 
    <b>WskCaptureProviderNPI</b>.</p>

<p><b>WskCaptureProviderNPI</b> can be called after a call is made to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571128">WskDeregister</a> only if the 
    <i>WskRegistration</i> block is not freed or overwritten. After 
    <b>WskDeregister</b> is called, any further calls to 
    <b>WskCaptureProviderNPI</b> will fail with status code STATUS_DEVICE_NOT_READY, and, unless the provider
    NPI becomes available concurrently, any existing 
    <b>WskCaptureProviderNPI</b> calls that are blocked in other threads waiting for the WSK provider NPI to
    become available will also return immediately with status code STATUS_DEVICE_NOT_READY.</p>

<p>For more information about attaching a WSK application to the WSK subsystem, see 
    <a href="netvista.registering_a_winsock_kernel_application">Registering a Winsock Kernel
    Application</a>.</p>

<p>Callers of the 
    <b>WskCaptureProviderNPI</b> function must be running at IRQL = PASSIVE_LEVEL if 
    <i>WaitTimeout</i> is not set to WSK_NO_WAIT; otherwise, callers must be running at IRQL &lt;=
    DISPATCH_LEVEL.</p>

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
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wsk.h (include Wsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Netio.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571128">WskDeregister</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571143">WskRegister</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571145">WskReleaseProviderNPI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WskCaptureProviderNPI function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
