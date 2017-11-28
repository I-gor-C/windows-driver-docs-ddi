---
UID: NF.netioddk.NmrClientAttachProvider
title: NmrClientAttachProvider
author: windows-driver-content
description: The NmrClientAttachProvider function attaches a client module to a provider module.
old-location: netvista\nmrclientattachprovider.htm
old-project: netvista
ms.assetid: dca8f82b-f058-4765-890c-973f8462c2f5
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NmrClientAttachProvider
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: netioddk.h
req.include-header: Wsk.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NmrClientAttachProvider
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NmrClientAttachProvider function



## -description
<p>The 
  <b>NmrClientAttachProvider</b> function attaches a client module to a provider module.</p>


## -syntax

````
NTSTATUS NmrClientAttachProvider(
  _In_        HANDLE NmrBindingHandle,
  _In_        PVOID  ClientBindingContext,
  _In_  const VOID   *ClientDispatch,
  _Out_       PVOID  *ProviderBindingContext,
  _Out_ const VOID   **ProviderDispatch
);
````


## -parameters
<dl>

### -param <i>NmrBindingHandle</i> [in]

<dd>
<p>A handle used by the NMR to represent the binding between the client module and the provider
     module. The NMR passes this handle to the client module when it calls the client module's 
     <a href="netvista.clientattachprovider">ClientAttachProvider</a> callback
     function.</p>
</dd>

### -param <i>ClientBindingContext</i> [in]

<dd>
<p>A pointer to a caller-supplied context for the binding between the client module and the provider
     module. The client module uses this context to keep track of the state of the binding. The contents of
     the client module's binding context are opaque to the provider module. The provider module passes this
     pointer to the client module whenever it calls any of the client module's 
     <a href="netvista.network_programming_interface">NPI</a> callback functions that
     require the client module's binding context. The client module must make sure that this context remains
     valid and resident in memory as long as the provider module is attached to the client module.</p>
</dd>

### -param <i>ClientDispatch</i> [in]

<dd>
<p>A pointer to a constant structure that contains the dispatch table of 
     <a href="netvista.network_programming_interface">NPI</a> callback functions for the
     client module. The client module must make sure that this structure remains valid and resident in memory
     as long as the provider module is attached to the client module. The contents of the structure are 
     NPI-specific. If the 
     NPI does not define a client
     dispatch table structure, the client module must set this parameter to <b>NULL</b>.</p>
</dd>

### -param <i>ProviderBindingContext</i> [out]

<dd>
<p>A pointer to a variable that receives a pointer to the provider module's context for the binding
     between the client module and the provider module. The provider module uses this context to keep track
     of the state of the binding. The contents of the provider module's binding context are opaque to the
     client module. The client module passes this pointer to the provider module whenever it calls any of the
     provider module's 
     <a href="netvista.network_programming_interface">NPI</a> functions that require the
     provider module's binding context.</p>
</dd>

### -param <i>ProviderDispatch</i> [out]

<dd>
<p>A pointer to a variable that receives a pointer to a structure that contains the dispatch table of
     
     <a href="netvista.network_programming_interface">NPI</a> functions for the provider
     module. The contents of the structure are 
     NPI-specific.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>NmrClientAttachProvider</b> function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The client module was successfully attached to the provider module.</p><dl>
<dt><b>STATUS_NOINTERFACE</b></dt>
</dl><p>The provider module did not attach to the client module.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A client module calls the 
    <b>NmrClientAttachProvider</b> function from its 
    <a href="netvista.clientattachprovider">ClientAttachProvider</a> callback
    function to attach itself to a provider module.</p>

<p>When a client module calls the 
    <b>NmrClientAttachProvider</b> function, the NMR calls the provider module's 
    <a href="netvista.providerattachclient">ProviderAttachClient</a> callback
    function to complete the attachment process. The 
    <b>NmrClientAttachProvider</b> function returns the status code that is returned by the provider module's 
    <i>ProviderAttachClient</i> callback
    function.</p>

<p>If the 
    <b>NmrClientAttachProvider</b> function does not return STATUS_SUCCESS, the client module should perform
    any necessary cleanup of the data contained within its binding context structure. The client module
    should then free the memory for its binding context structure if it dynamically allocated the memory for
    the structure.</p>

<p>If the 
    <b>NmrClientAttachProvider</b> function returns STATUS_SUCCESS and the client module dynamically allocated
    the memory for its binding context, the client module should free that allocated memory when the NMR
    calls the client module's 
    <a href="netvista.clientcleanupbindingcontext">
    ClientCleanupBindingContext</a> callback function after the client module and provider module are
    detached from each other.</p>

<p>If the 
    <b>NmrClientAttachProvider</b> function returns STATUS_SUCCESS, the client module must save the pointers
    returned in the 
    <i>ProviderBindingContext</i> and 
    <i>ProviderDispatch</i> parameters so that it can call the provider module's 
    <a href="netvista.network_programming_interface">NPI</a> functions.</p>

<p>A client module calls the 
    <b>NmrClientAttachProvider</b> function from its 
    <a href="netvista.clientattachprovider">ClientAttachProvider</a> callback
    function to attach itself to a provider module.</p>

<p>When a client module calls the 
    <b>NmrClientAttachProvider</b> function, the NMR calls the provider module's 
    <a href="netvista.providerattachclient">ProviderAttachClient</a> callback
    function to complete the attachment process. The 
    <b>NmrClientAttachProvider</b> function returns the status code that is returned by the provider module's 
    <i>ProviderAttachClient</i> callback
    function.</p>

<p>If the 
    <b>NmrClientAttachProvider</b> function does not return STATUS_SUCCESS, the client module should perform
    any necessary cleanup of the data contained within its binding context structure. The client module
    should then free the memory for its binding context structure if it dynamically allocated the memory for
    the structure.</p>

<p>If the 
    <b>NmrClientAttachProvider</b> function returns STATUS_SUCCESS and the client module dynamically allocated
    the memory for its binding context, the client module should free that allocated memory when the NMR
    calls the client module's 
    <a href="netvista.clientcleanupbindingcontext">
    ClientCleanupBindingContext</a> callback function after the client module and provider module are
    detached from each other.</p>

<p>If the 
    <b>NmrClientAttachProvider</b> function returns STATUS_SUCCESS, the client module must save the pointers
    returned in the 
    <i>ProviderBindingContext</i> and 
    <i>ProviderDispatch</i> parameters so that it can call the provider module's 
    <a href="netvista.network_programming_interface">NPI</a> functions.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.clientattachprovider">ClientAttachProvider</a>
</dt>
<dt>
<a href="netvista.providerattachclient">ProviderAttachClient</a>
</dt>
<dt>
<a href="netvista.clientcleanupbindingcontext">ClientCleanupBindingContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NmrClientAttachProvider function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
