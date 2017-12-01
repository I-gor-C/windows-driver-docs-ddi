---
UID: NF.ndis.NdisIfRegisterProvider
title: NdisIfRegisterProvider
author: windows-driver-content
description: The NdisIfRegisterProvider function registers an NDIS network interface provider.
old-location: netvista\ndisifregisterprovider.htm
old-project: netvista
ms.assetid: 1624426b-9e67-4aa2-83d8-f1e6fa484858
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisIfRegisterProvider
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisIfRegisterProvider
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Interfaces_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisIfRegisterProvider function



## -description
<p>The 
  <b>NdisIfRegisterProvider</b> function registers an NDIS network interface provider.</p>


## -syntax

````
NDIS_STATUS NdisIfRegisterProvider(
  _In_  PNDIS_IF_PROVIDER_CHARACTERISTICS ProviderCharacteristics,
  _In_  NDIS_HANDLE                       IfProviderContext,
  _Out_ PNDIS_HANDLE                      pNdisProviderHandle
);
````


## -parameters
<dl>

### -param <i>ProviderCharacteristics</i> [in]

<dd>
<p>A pointer to a caller-provided 
     <a href="..\ndis\ns-ndis--ndis-if-provider-characteristics.md">
     NDIS_IF_PROVIDER_CHARACTERISTICS</a> structure. This structure defines the characteristics of the
     provider, including the entry points for its provider callback functions.</p>
</dd>

### -param <i>IfProviderContext</i> [in]

<dd>
<p>A handle to a caller-provided context area for this network interface provider. Set this parameter
     to <b>NULL</b> if there is no context area.</p>
</dd>

### -param <i>pNdisProviderHandle</i> [out]

<dd>
<p>A pointer to a caller-provided handle variable. If the registration operation succeeds, NDIS
     writes a handle to this variable that identifies the network interface provider. The interface provider
     should retain this handle for use in subsequent calls that require an interface provider handle.</p>
</dd>
</dl>

## -returns
<p><b>NdisIfRegisterProvider</b> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>The operation failed because of insufficient resources.</p><dl>
<dt><b>NDIS_STATUS_INVALID_PARAMETER</b></dt>
</dl><p><b>NdisIfRegisterProvider</b> failed to register the provider because the 
       <a href="..\ndis\ns-ndis--ndis-if-provider-characteristics.md">
       NDIS_IF_PROVIDER_CHARACTERISTICS</a> structure at the 
       <i>ProviderCharacteristics</i> parameter contained invalid member data.</p><dl>
<dt><b>NDIS_STATUS_NOT_SUPPORTED</b></dt>
</dl><p><b>NdisIfRegisterProvider</b> failed to register the provider because the 
       <b>Header</b> member in NDIS_IF_PROVIDER_CHARACTERISTICS specifies a structure version that is not
       supported.</p>

<p> </p>

## -remarks
<p>NDIS drivers call the 
    <b>NdisIfRegisterProvider</b> function once during initialization to register as an NDIS interface
    provider. For example, the driver can call 
    <b>NdisIfRegisterProvider</b> from its 
    <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine. An interface provider is a
    software component that manages network interfaces to support the MIB (
    <a href="netvista.overview_of_ndis_network_interfaces">RFC 2863</a>).</p>

<p>To handle interface provider OID requests, interface providers provide entry points for callback
    functions in the 
    <a href="..\ndis\ns-ndis--ndis-if-provider-characteristics.md">
    NDIS_IF_PROVIDER_CHARACTERISTICS</a> structure at the 
    <i>ProviderCharacteristics</i> parameter of 
    <b>NdisIfRegisterProvider</b>.</p>

<p>NDIS interface providers call the 
    <a href="..\ndis\nf-ndis-ndisifregisterinterface.md">NdisIfRegisterInterface</a> function
    to register a network interface. A provider can register multiple interfaces.</p>

<p>If 
    <b>NdisIfRegisterProvider</b> succeeds, it returns a handle at the location that the 
    <i>pNdisProviderHandle</i> parameter points to. The interface provider should retain this handle for use
    in subsequent calls that require an interface provider handle. For example, a driver must call 
    <a href="..\ndis\nf-ndis-ndisifderegisterprovider.md">NdisIfDeregisterProvider</a> before
    the driver unloads.</p>

<p>A component that is no longer an interface provider can call the 
    <b>NdisIfDeregisterProvider</b> function at any time to release the interface provider resources that NDIS
    allocated when the driver called 
    <b>NdisIfRegisterProvider</b>.</p>

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
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="devtest.ndis_irql_interfaces_function">Irql_Interfaces_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-if-provider-characteristics.md">
   NDIS_IF_PROVIDER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisifderegisterprovider.md">NdisIfDeregisterProvider</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisifregisterinterface.md">NdisIfRegisterInterface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisIfRegisterProvider function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
