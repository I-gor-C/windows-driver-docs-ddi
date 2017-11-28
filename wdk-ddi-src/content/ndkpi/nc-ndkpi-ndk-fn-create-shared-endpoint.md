---
UID: NC.ndkpi.NDK_FN_CREATE_SHARED_ENDPOINT
title: NDK_FN_CREATE_SHARED_ENDPOINT
author: windows-driver-content
description: The NdkCreateSharedEndpoint (NDK_FN_CREATE_SHARED_ENDPOINT) function creates an NDK shared endpoint.
old-location: netvista\ndk_fn_create_shared_endpoint.htm
old-project: netvista
ms.assetid: FE65B384-387E-4E04-8CF4-9C218F83A0C8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_WWAN_VISIBLE_PROVIDERS, NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdkCreateSharedEndpoint
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
req.iface: 
---

# NDK_FN_CREATE_SHARED_ENDPOINT callback



## -description
<p>The <i>NdkCreateSharedEndpoint</i> (<i>NDK_FN_CREATE_SHARED_ENDPOINT</i>) function creates an NDK shared endpoint.</p>


## -prototype

````
NDK_FN_CREATE_SHARED_ENDPOINT NdkCreateSharedEndpoint;

NTSTATUS NdkCreateSharedEndpoint(
  _In_     NDK_ADAPTER                                     *pNdkAdapter,
           _In_reads_bytes_(AddressLength) const PSOCKADDR pAddress,
  _In_     ULONG                                           AddressLength,
  _In_     NDK_FN_CREATE_COMPLETION                        CreateCompletion,
  _In_opt_ PVOID                                           RequestContext,
           _Outptr_ NDK_SHARED_ENDPOINT                    **ppNdkSharedEndpoint
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkAdapter</i> [in]

<dd>
<p>A pointer to an NDK adapter object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a>).</p>
</dd>

### -param <i>pAddress</i> 

<dd>
<p>A local address to use for initiating outgoing connections. For AF_INET or AF_INET6 <i>pAddress</i> contains the local IP address and local ND port.

</p>
</dd>

### -param <i>AddressLength</i> [in]

<dd>
<p>The size, in bytes, of local address data at the <i>pAddress</i> parameter.

</p>
</dd>

### -param <i>CreateCompletion</i> [in]

<dd>
<p>A pointer to an <i>NdkCreateCompletion</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439871">NDK_FN_CREATE_COMPLETION</a>) function that completes the creation of an NDK object.</p>
</dd>

### -param <i>RequestContext</i> [in, optional]

<dd>
<p>A context value that the NDK provider passes back to the <i>NdkCreateCompletion</i> function that is specified in the <i>CreateCompletion</i> parameter.</p>
</dd>

### -param <i>ppNdkSharedEndpoint</i> 

<dd>
<p>A pointer to a created shared endpoint object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439937">NDK_SHARED_ENDPOINT</a>) is returned in this location if the request succeeds without returning STATUS_PENDING. If the request returns STATUS_PENDING then this parameter is ignored and the created object is returned with the callback that is specified in the  <i>CreateCompletion</i> parameter.</p>
</dd>
</dl>

## -returns
<p>The 
     <i>NdkCreateSharedEndpoint</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The shared endpoint object was  created successfully and returned with the <i>*ppNdkSharedEndpoint</i> parameter.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p> The operation is pending and will be completed later. The provider will call the function specified in the <i>CreateCompletion</i> parameter (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439871">NDK_FN_CREATE_COMPLETION</a>) to complete the pending operation.
 </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The request failed due to insufficient resources. </p><dl>
<dt><b>STATUS_SHARING_VIOLATION</b></dt>
</dl><p>	  The request failed because the specified local address is already in use.</p><dl>
<dt><b>STATUS_TOO_MANY_ADDRESSES</b></dt>
</dl><p>The request failed because the consumer specified a local port number of zero, and the Network Direct provider was unable to allocate a port from the ephemeral port space (ports 49152-65535.)</p><dl>
<dt><b>STATUS_INVALID_ADDRESS</b></dt>
</dl><p>	The request failed because the specified local address is not a valid address for the adapter. </p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p>The <i>NdkCreateSharedEndpoint</i> function creates an NDK shared endpoint to use as the local address for multiple outgoing connections that are destined to different remote addresses. This is analogous to having multiple incoming connections to the same local address that are represented by a listener object.</p>

<p> If the function returns STATUS_SUCCESS, the created object is returned in the <i>ppNdkSharedEndpoint</i> parameter. If <i>NdkCreateSharedEndpoint</i> returns STATUS_PENDING, the created object is returned by the <i>NdkCreateCompletion</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439871">NDK_FN_CREATE_COMPLETION</a>) function that is specified in the <i>CreateCompletion</i> parameter.</p>

<p>The <i>NdkCreateSharedEndpoint</i> function creates an NDK shared endpoint to use as the local address for multiple outgoing connections that are destined to different remote addresses. This is analogous to having multiple incoming connections to the same local address that are represented by a listener object.</p>

<p> If the function returns STATUS_SUCCESS, the created object is returned in the <i>ppNdkSharedEndpoint</i> parameter. If <i>NdkCreateSharedEndpoint</i> returns STATUS_PENDING, the created object is returned by the <i>NdkCreateCompletion</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439871">NDK_FN_CREATE_COMPLETION</a>) function that is specified in the <i>CreateCompletion</i> parameter.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439850">NDK_ADAPTER_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439871">NDK_FN_CREATE_COMPLETION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439937">NDK_SHARED_ENDPOINT</a>
</dt>
<dt>
<a href="NULL">NDKPI Object Lifetime Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_CREATE_SHARED_ENDPOINT callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
