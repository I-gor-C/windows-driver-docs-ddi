---
UID: NC.ndkpi.NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS
title: NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS
author: windows-driver-content
description: The NdkGetSharedEndpointLocalAddress (NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS) function returns the local address for an NDK shared endpoint.
old-location: netvista\ndk_fn_get_shared_endpoint_local_address.htm
ms.assetid: C7B6B7DC-359D-44C2-8348-EC1EE5965800
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdkGetSharedEndpointLocalAddress
req.alt-loc: ndkpi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: NDIS_WWAN_VISIBLE_PROVIDERS, NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
req.iface: 
---

# NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS callback



## -description
<p>The <i>NdkGetSharedEndpointLocalAddress</i> (<i>NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS</i>) function returns the local address for an NDK  shared endpoint.</p>


## -prototype

````
NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS NdkGetSharedEndpointLocalAddress;

NTSTATUS NdkGetSharedEndpointLocalAddress(
  _In_ NDK_SHARED_ENDPOINT                                                   *pNdkSharedEndpoint,
       _Out_writes_bytes_to_opt_(*pAddressLength, *pAddressLength) PSOCKADDR pAddress,
       _Inout_ ULONG                                                         *pAddressLength
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkSharedEndpoint</i> [in]

<dd>
<p>A pointer to an NDK shared endpoint object  (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439937">NDK_SHARED_ENDPOINT</a>).</p>
</dd>

### -param <i>pAddress</i> 

<dd>
<p>A local address is returned in this buffer.</p>
</dd>

### -param <i>pAddressLength</i> 

<dd>
<p>The size, in bytes, of the address buffer for input, and the size, in bytes, of the actual address written into the buffer for output.</p>
</dd>
</dl>

## -returns
<p>The 
     <i>NdkGetSharedEndpointLocalAddress</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>A local address was written to the buffer in the <i>pAddress</i> parameter.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer size specified in the <i>*pAddressLength</i> parameter input is too small. <i>*pAddressLength</i> output value is updated with the required buffer size.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p><i>NdkGetSharedEndpointLocalAddress</i> returns the local address for a shared endpoint. <i>NdkGetSharedEndpointLocalAddress</i> retrieves port information for an AF_INET or AF_INET6  shared endpoint. That is, if the NDK consumer specifies zero as the ND port number in a shared endpoint creation request, the NDK provider picks a port. An NDK consumer can determine the port that the provider picked with <i>NdkGetSharedEndpointLocalAddress</i>.</p>

<p><i>NdkGetSharedEndpointLocalAddress</i> returns the local address for a shared endpoint. <i>NdkGetSharedEndpointLocalAddress</i> retrieves port information for an AF_INET or AF_INET6  shared endpoint. That is, if the NDK consumer specifies zero as the ND port number in a shared endpoint creation request, the NDK provider picks a port. An NDK consumer can determine the port that the provider picked with <i>NdkGetSharedEndpointLocalAddress</i>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndkpi.h (include Ndkpi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439937">NDK_SHARED_ENDPOINT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
