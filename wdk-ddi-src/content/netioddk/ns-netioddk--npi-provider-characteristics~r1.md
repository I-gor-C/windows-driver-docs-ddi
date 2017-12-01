---
UID: NS.netioddk._NPI_PROVIDER_CHARACTERISTICS~r1
title: NPI_PROVIDER_CHARACTERISTICS
author: windows-driver-content
description: The NPI_PROVIDER_CHARACTERISTICS structure defines the characteristics of a provider module.
old-location: netvista\npi_provider_characteristics.htm
old-project: netvista
ms.assetid: a83220e8-496c-4b83-b774-88ab1f017e8d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NPI_PROVIDER_CHARACTERISTICS, NPI_PROVIDER_CHARACTERISTICS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: netioddk.h
req.include-header: Wsk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NPI_PROVIDER_CHARACTERISTICS
req.alt-loc: netioddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: < DISPATCH_LEVEL
req.iface: 
---

# NPI_PROVIDER_CHARACTERISTICS structure



## -description
<p>The NPI_PROVIDER_CHARACTERISTICS structure defines the characteristics of a provider module.</p>


## -syntax

````
typedef struct _NPI_PROVIDER_CHARACTERISTICS {
  USHORT                                   Version;
  USHORT                                   Length;
  PNPI_PROVIDER_ATTACH_CLIENT_FN           ProviderAttachClient;
  PNPI_PROVIDER_DETACH_CLIENT_FN           ProviderDetachClient;
  PNPI_PROVIDER_CLEANUP_BINDING_CONTEXT_FN ProviderCleanupBindingContext;
  NPI_REGISTRATION_INSTANCE                ProviderRegistrationInstance;
} NPI_PROVIDER_CHARACTERISTICS, *PNPI_PROVIDER_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of the NMR with which the provider is registering. A provider module should set this
     member to zero.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>The size, in bytes, of the NPI_PROVIDER_CHARACTERISTICS structure.</p>
</dd>

### -field <b>ProviderAttachClient</b>

<dd>
<p>A pointer to the provider module's 
     <a href="netvista.providerattachclient">ProviderAttachClient</a> callback
     function.</p>
</dd>

### -field <b>ProviderDetachClient</b>

<dd>
<p>A pointer to the provider module's 
     <a href="netvista.providerdetachclient">ProviderDetachClient</a> callback
     function.</p>
</dd>

### -field <b>ProviderCleanupBindingContext</b>

<dd>
<p>A pointer to the provider module's 
     <a href="netvista.providercleanupbindingcontext">
     ProviderCleanupBindingContext</a> callback function. If the provider module does not dynamically
     allocate the memory for its binding context and no other cleanup of its binding context is required,
     then the provider module does not need to implement a 
     <i>
     ProviderCleanupBindingContext</i> callback function. If the provider module does not implement a 
     <i>
     ProviderCleanupBindingContext</i> callback function, then this member must be set to <b>NULL</b>.</p>
</dd>

### -field <b>ProviderRegistrationInstance</b>

<dd>
<p>An 
     <a href="..\netioddk\ns-netioddk--npi-registration-instance.md">
     NPI_REGISTRATION_INSTANCE</a> structure that specifies the identity of the provider module and the 
     <a href="netvista.network_programming_interface">NPI</a> for which it is
     registering.</p>
</dd>
</dl>

## -remarks
<p>A provider module passes a pointer to an NPI_PROVIDER_CHARACTERISTICS structure to the 
    <a href="..\netioddk\nf-netioddk-nmrregisterprovider.md">NmrRegisterProvider</a> function when it
    registers itself with the NMR.</p>

<p>A provider module must make sure that this structure remains valid and resident in memory as long as
    the provider module is registered with the NMR.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\netioddk\nf-netioddk-nmrregisterprovider.md">NmrRegisterProvider</a>
</dt>
<dt>
<a href="netvista.providerattachclient">ProviderAttachClient</a>
</dt>
<dt>
<a href="netvista.providerdetachclient">ProviderDetachClient</a>
</dt>
<dt>
<a href="netvista.providercleanupbindingcontext">
   ProviderCleanupBindingContext</a>
</dt>
<dt>
<a href="..\netioddk\ns-netioddk--npi-registration-instance.md">NPI_REGISTRATION_INSTANCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NPI_PROVIDER_CHARACTERISTICS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
