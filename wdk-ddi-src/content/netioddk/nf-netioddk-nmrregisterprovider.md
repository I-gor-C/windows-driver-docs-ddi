---
UID: NF.netioddk.NmrRegisterProvider
title: NmrRegisterProvider
author: windows-driver-content
description: The NmrRegisterProvider function registers a provider module with the NMR.
old-location: netvista\nmrregisterprovider.htm
old-project: netvista
ms.assetid: aac9382c-5177-4216-bf3d-7970b18662eb
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NmrRegisterProvider
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
req.alt-api: NmrRegisterProvider
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
req.iface: 
---

# NmrRegisterProvider function



## -description
<p>The 
  <b>NmrRegisterProvider</b> function registers a provider module with the NMR.</p>


## -syntax

````
NTSTATUS NmrRegisterProvider(
  _In_  PNPI_PROVIDER_CHARACTERISTICS ProviderCharacteristics,
  _In_  PVOID                         ProviderContext,
  _Out_ PHANDLE                       NmrProviderHandle
);
````


## -parameters
<dl>

### -param <i>ProviderCharacteristics</i> [in]

<dd>
<p>A pointer to an 
     <a href="..\netioddk\ns-netioddk--npi-provider-characteristics.md">
     NPI_PROVIDER_CHARACTERISTICS</a> structure that describes the characteristics of the provider module.
     The provider module must make sure that this structure remains valid and resident in memory as long as
     the provider module is registered with the NMR.</p>
</dd>

### -param <i>ProviderContext</i> [in]

<dd>
<p>A pointer to a caller-supplied context for the registration. The provider module uses this context
     to keep track of the state of the provider registration. The contents of the provider module's
     registration context are opaque to the NMR. The NMR passes this pointer to the provider module whenever
     it calls the provider module's 
     <a href="netvista.providerattachclient">ProviderAttachClient</a> callback
     function. The provider module must make sure that this context remains valid and resident in memory as
     long as the provider module is registered with the NMR.</p>
</dd>

### -param <i>NmrProviderHandle</i> [out]

<dd>
<p>A pointer to a variable that receives a handle used by the NMR to represent the registration of
     the provider module. The provider module must save this handle and pass it as a parameter to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568778">NmrDeregisterProvider</a> function when
     it deregisters from the NMR.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>NmrRegisterProvider</b> function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The NMR successfully registered the provider module.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The NMR did not have sufficient system resources to register the provider module.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A provider module calls the 
    <b>NmrRegisterProvider</b> function to register as a provider of an 
    <a href="netvista.network_programming_interface">NPI</a> so that it can attach to
    client modules that register as clients of the same 
    NPI.</p>

<p>A provider module typically calls the 
    <b>NmrRegisterProvider</b> function from its 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function after it has completed
    all other initialization tasks. The call to the 
    <b>NmrRegisterProvider</b> function indicates to the NMR that the provider module is ready to attach to
    any client modules that have registered or will register as clients of the same 
    <a href="netvista.network_programming_interface">NPI</a> for which the provider module
    has registered as a provider.</p>

<p>A provider module calls the 
    <b>NmrRegisterProvider</b> function to register as a provider of an 
    <a href="netvista.network_programming_interface">NPI</a> so that it can attach to
    client modules that register as clients of the same 
    NPI.</p>

<p>A provider module typically calls the 
    <b>NmrRegisterProvider</b> function from its 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function after it has completed
    all other initialization tasks. The call to the 
    <b>NmrRegisterProvider</b> function indicates to the NMR that the provider module is ready to attach to
    any client modules that have registered or will register as clients of the same 
    <a href="netvista.network_programming_interface">NPI</a> for which the provider module
    has registered as a provider.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568778">NmrDeregisterProvider</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568814">NPI_PROVIDER_CHARACTERISTICS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NmrRegisterProvider function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
