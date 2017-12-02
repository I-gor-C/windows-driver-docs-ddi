---
UID: NF.netioddk.NmrDeregisterProvider
title: NmrDeregisterProvider
author: windows-driver-content
description: The NmrDeregisterProvider function deregisters a provider module from the NMR.
old-location: netvista\nmrderegisterprovider.htm
old-project: netvista
ms.assetid: 889f872a-f4fe-4d7a-b9b6-7fb7335831a5
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NmrDeregisterProvider
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
req.alt-api: NmrDeregisterProvider
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NmrDeregisterProvider function



## -description
<p>The 
  <b>NmrDeregisterProvider</b> function deregisters a provider module from the NMR.</p>


## -syntax

````
NTSTATUS NmrDeregisterProvider(
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
     <b>NmrDeregisterProvider</b> function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The NMR initiated the deregistration of the provider module. The provider module must call the 
       <a href="..\netioddk\nf-netioddk-nmrwaitforproviderderegistercomplete.md">
       NmrWaitForProviderDeregisterComplete</a> function to wait until the deregistration is complete
       before the provider module can be unloaded.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>When a provider module calls the 
    <b>NmrDeregisterProvider</b> function, the NMR calls the provider module's 
    <a href="netvista.providerdetachclient">ProviderDetachClient</a> callback
    function and the client module's 
    <a href="netvista.clientdetachprovider">ClientDetachProvider</a> callback
    function for each of the bindings between the provider module and a client module. The deregistration of
    the provider module from the NMR is complete after the provider module has successfully detached from all
    the client modules to which it is attached and all of those client modules have successfully detached
    from the provider module.</p>

<p>A provider module typically calls the 
    <b>NmrDeregisterProvider</b> function from its 
    <a href="kernel.unload">Unload</a> function to detach itself from all of the
    client modules to which it is attached before the provider module is unloaded from the system. After
    calling the 
    <b>NmrDeregisterProvider</b> function a provider module must call the 
    <a href="..\netioddk\nf-netioddk-nmrwaitforproviderderegistercomplete.md">
    NmrWaitForProviderDeregisterComplete</a> function to wait for the deregistration to complete before the
    provider module can be unloaded. A provider module must not return from a call to its 
    <i>Unload</i> function until after deregistration is
    complete.</p>

<p>
<div class="alert"><b>Note</b>  If a provider module uses the Windows Driver Framework, it will typically call the
     
     <b>NmrDeregisterProvider</b> function from its 
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\netioddk\nf-netioddk-nmrregisterprovider.md">NmrRegisterProvider</a>
</dt>
<dt>
<a href="..\netioddk\nf-netioddk-nmrwaitforproviderderegistercomplete.md">
   NmrWaitForProviderDeregisterComplete</a>
</dt>
<dt>
<a href="netvista.providerdetachclient">ProviderDetachClient</a>
</dt>
<dt>
<a href="netvista.clientdetachprovider">ClientDetachProvider</a>
</dt>
<dt>
<a href="kernel.unload">Unload</a>
</dt>
<dt>
<a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-unload.md">EvtDriverUnload</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NmrDeregisterProvider function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
