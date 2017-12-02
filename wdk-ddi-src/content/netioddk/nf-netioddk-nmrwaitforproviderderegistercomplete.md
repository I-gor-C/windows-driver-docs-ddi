---
UID: NF.netioddk.NmrWaitForProviderDeregisterComplete
title: NmrWaitForProviderDeregisterComplete
author: windows-driver-content
description: The NmrWaitForProviderDeregisterComplete function waits for the deregistration of a provider module to complete.
old-location: netvista\nmrwaitforproviderderegistercomplete.htm
old-project: netvista
ms.assetid: ec6e75e8-f24a-4d76-b6e1-af35b5402f91
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NmrWaitForProviderDeregisterComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: netioddk.h
req.include-header: Wsk.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NmrWaitForProviderDeregisterComplete
req.alt-loc: netio.lib,netio.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Netio.lib
req.dll: 
req.irql: < DISPATCH_LEVEL
req.iface: 
---

# NmrWaitForProviderDeregisterComplete function



## -description
<p>The 
  <b>NmrWaitForProviderDeregisterComplete</b> function waits for the deregistration of a provider module to
  complete.</p>


## -syntax

````
NTSTATUS NmrWaitForProviderDeregisterComplete(
  _In_ HANDLE NmrProviderHandle
);
````


## -parameters
<dl>

### -param NmrProviderHandle [in]

<dd>
<p>A handle used by the NMR to represent the registration of the provider module. The NMR returns
     this handle to the provider module when the provider module calls the 
     <a href="..\netioddk\nf-netioddk-nmrregisterprovider.md">NmrRegisterProvider</a> function.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>NmrWaitForProviderDeregisterComplete</b> function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The NMR completed deregistering the provider module.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The provider module called the 
       <b>NmrWaitForProviderDeregisterComplete</b> function before calling the 
       <a href="..\netioddk\nf-netioddk-nmrderegisterprovider.md">NmrDeregisterProvider</a> function,
       or the handle specified in the NmrClientHandle parameter is not a valid provider handle.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A provider module calls the 
    <b>NmrWaitForProviderDeregisterComplete</b> function to wait for the deregistration of the provider module
    to complete. A provider module calls the 
    <b>NmrWaitForProviderDeregisterComplete</b> function only after calling the 
    <a href="..\netioddk\nf-netioddk-nmrderegisterprovider.md">NmrDeregisterProvider</a> function.</p>

<p>A provider module typically calls the 
    <b>NmrWaitForProviderDeregisterComplete</b> function from its 
    <a href="kernel.unload">Unload</a> function to wait until it is completely
    deregistered from the NMR before the provider module is unloaded from the system. A provider module must
    not return from a call to its 
    <i>Unload</i> function until after deregistration is
    complete.</p>

<p>
<div class="alert"><b>Note</b>  If a provider module uses the Windows Driver Framework, it will typically call the
     
     <b>NmrWaitForProviderDeregisterComplete</b> function from its 
     <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-unload.md">EvtDriverUnload</a> event callback function. In
     this situation, the provider module must not return from a call to its 
     <i>EvtDriverUnload</i> function until after
     deregistration is complete.</div>
<div> </div>
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<dt>Netioddk.h (include Wsk.h)</dt>
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
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\netioddk\nf-netioddk-nmrderegisterprovider.md">NmrDeregisterProvider</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NmrWaitForProviderDeregisterComplete function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
