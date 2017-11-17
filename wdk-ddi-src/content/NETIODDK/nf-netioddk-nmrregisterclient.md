---
UID: NF.netioddk.NmrRegisterClient
title: NmrRegisterClient
author: windows-driver-content
description: The NmrRegisterClient function registers a client module with the NMR.
old-location: netvista\nmrregisterclient.htm
ms.assetid: 9a8d2bc1-a75a-449d-8cfe-9d1f16a9dbb7
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: netioddk.h
req.include-header: Wsk.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NmrRegisterClient
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
req.irql: PASSIVE_LEVEL
ms.keywords: NmrRegisterClient
req.iface: 
---

# NmrRegisterClient function



## -description
<p>The 
  <b>NmrRegisterClient</b> function registers a client module with the NMR.</p>


## -syntax

````
NTSTATUS NmrRegisterClient(
  _In_  PNPI_CLIENT_CHARACTERISTICS ClientCharacteristics,
  _In_  PVOID                       ClientContext,
  _Out_ PHANDLE                     NmrClientHandle
);
````


## -parameters
<dl>

### -param <i>ClientCharacteristics</i> [in]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/03d73a80-0860-4ec7-8eb1-5954f64b6026">
     NPI_CLIENT_CHARACTERISTICS</a> structure that describes the characteristics of the client module. The
     client module must make sure that this structure remains valid and resident in memory as long as the
     client module is registered with the NMR.</p>
</dd>

### -param <i>ClientContext</i> [in]

<dd>
<p>A pointer to a caller-supplied context for the registration. The client module uses this context
     to keep track of the state of the client registration. The contents of the client module's registration
     context are opaque to the NMR. The NMR passes this pointer to the client module whenever it calls the
     client module's 
     <a href="https://msdn.microsoft.com/8f8abdb1-d018-4404-a80a-74017c324a0f">ClientAttachProvider</a> callback
     function. The client module must make sure that its registration context remains valid and resident in
     memory as long as the client module is registered with the NMR.</p>
</dd>

### -param <i>NmrClientHandle</i> [out]

<dd>
<p>A pointer to a variable that receives a handle used by the NMR to represent the registration of
     the client module. The client module must save this handle and pass it as a parameter to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568774">NmrDeregisterClient</a> function when it
     deregisters from the NMR.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>NmrRegisterClient</b> function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The NMR successfully registered the client module.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The NMR did not have sufficient system resources to register the client module.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A client module calls the 
    <b>NmrRegisterClient</b> function to register as a client of an 
    <a href="netvista.network_programming_interface">NPI</a> so that it can attach to
    provider modules that register as providers of the same 
    NPI.</p>

<p>A client module typically calls the 
    <b>NmrRegisterClient</b> function from its 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function after it has completed
    all other initialization tasks. The call to the 
    <b>NmrRegisterClient</b> function indicates to the NMR that the client module is ready to attach to any
    provider modules that have registered or will register as providers of the same 
    <a href="netvista.network_programming_interface">NPI</a> for which the client module
    has registered as a client.</p>

<p>A client module calls the 
    <b>NmrRegisterClient</b> function to register as a client of an 
    <a href="netvista.network_programming_interface">NPI</a> so that it can attach to
    provider modules that register as providers of the same 
    NPI.</p>

<p>A client module typically calls the 
    <b>NmrRegisterClient</b> function from its 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function after it has completed
    all other initialization tasks. The call to the 
    <b>NmrRegisterClient</b> function indicates to the NMR that the client module is ready to attach to any
    provider modules that have registered or will register as providers of the same 
    <a href="netvista.network_programming_interface">NPI</a> for which the client module
    has registered as a client.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568774">NmrDeregisterClient</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568812">NPI_CLIENT_CHARACTERISTICS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NmrRegisterClient function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
