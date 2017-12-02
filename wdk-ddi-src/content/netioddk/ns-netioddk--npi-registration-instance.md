---
UID: NS.netioddk._NPI_REGISTRATION_INSTANCE
title: NPI_REGISTRATION_INSTANCE
author: windows-driver-content
description: The NPI_REGISTRATION_INSTANCE structure defines the data related to the registration of a network module with the NMR.
old-location: netvista\npi_registration_instance.htm
old-project: netvista
ms.assetid: a368f9d9-a7e0-4b35-ba14-b0919f74029d
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NPI_REGISTRATION_INSTANCE,
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
req.alt-api: NPI_REGISTRATION_INSTANCE
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

# NPI_REGISTRATION_INSTANCE structure



## -description
<p>The NPI_REGISTRATION_INSTANCE structure defines the data related to the registration of a network
  module with the NMR.</p>


## -syntax

````
typedef struct _NPI_REGISTRATION_INSTANCE {
  USHORT        Version;
  USHORT        Size;
  PNPIID        NpiId;
  PNPI_MODULEID ModuleId;
  ULONG         Number;
  const VOID    *NpiSpecificCharacteristics;
} NPI_REGISTRATION_INSTANCE, *PNPI_REGISTRATION_INSTANCE;
````


## -struct-fields
<dl>

### -field Version

<dd>
<p>The version of the NMR with which the network module is registering. A network module should set
     this member to zero.</p>
</dd>

### -field Size

<dd>
<p>The size, in bytes, of the NPI_REGISTRATION_INSTANCE structure.</p>
</dd>

### -field NpiId

<dd>
<p>A pointer to the 
     <a href="netvista.network_programming_interface">NPI</a> identifier for the specific 
     NPI to which the network module
     is registering as either a client or a provider. The NPIID data type is defined as:
     </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef GUID NPIID;
typedef CONST NPIID *PNPIID;</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field ModuleId

<dd>
<p>A pointer to an 
     <a href="netvista.npi_moduleid">NPI_MODULEID</a> structure that uniquely
     identifies the network module.</p>
</dd>

### -field Number

<dd>
<p>The implementation number of the 
     <a href="netvista.network_programming_interface">NPI</a> for which the network module
     is registering as either a client or a provider. A network module can support multiple implementations
     of the same 
     NPI by registering as either a
     client or a provider of each implementation of the 
     NPI. If there is only one
     implementation of an 
     NPI, this member is set to
     zero.</p>
</dd>

### -field NpiSpecificCharacteristics

<dd>
<p>A pointer to a structure that specifies characteristics that are unique to the network module. The
     contents of the structure are 
     <a href="netvista.network_programming_interface">NPI</a>-specific. A network module
     should set this member to <b>NULL</b> if it is registering as a client of an NPI that does not define a client
     characteristics structure or if it is registering as a provider of an NPI that does not define a
     provider characteristics structure.</p>
</dd>
</dl>

## -remarks
<p>An NPI_REGISTRATION_INSTANCE structure is a member of the 
    <a href="..\netioddk\ns-netioddk--npi-client-characteristics.md">NPI_CLIENT_CHARACTERISTICS</a> and 
    <a href="..\netioddk\ns-netioddk--npi-provider-characteristics.md">
    NPI_PROVIDER_CHARACTERISTICS</a> structures. These structures are used for registering network modules
    with the NMR.</p>

<p>When the NMR calls a cleint module's 
    <a href="netvista.clientattachprovider">ClientAttachProvider</a> callback
    function, it passes a pointer to the NPI_REGISTRATION_INSTANCE structure for the provider module to which
    the client module can attach itself. Likewise, when the NMR calls a provider module's 
    <a href="netvista.providerattachclient">ProviderAttachClient</a> callback
    function, it passes a pointer to the NPI_REGISTRATION_INSTANCE structure for the client module to which
    the provider module can attach itself.</p>

<p>A network module must make sure that the memory for the NPIID pointed to by the 
    <b>NpiId</b> member, the memory for the 
    <a href="netvista.npi_moduleid">NPI_MODULEID</a> structure pointed to by the 
    <b>ModuleId</b> member, and the memory for the 
    <a href="netvista.network_programming_interface">NPI</a>-specific characteristics
    structure pointed to by the 
    <b>NpiSpecificCharacteristics</b> member remain valid and resident in memory as long as the network module
    is registered with the NMR.</p>

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
<a href="netvista.clientattachprovider">ClientAttachProvider</a>
</dt>
<dt>
<a href="netvista.providerattachclient">ProviderAttachClient</a>
</dt>
<dt>
<a href="..\netioddk\ns-netioddk--npi-client-characteristics.md">NPI_CLIENT_CHARACTERISTICS</a>
</dt>
<dt>
<a href="netvista.npi_moduleid">NPI_MODULEID</a>
</dt>
<dt>
<a href="..\netioddk\ns-netioddk--npi-provider-characteristics.md">NPI_PROVIDER_CHARACTERISTICS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NPI_REGISTRATION_INSTANCE structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
