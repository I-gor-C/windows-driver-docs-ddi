---
UID: NC.ndkpi.NDK_FN_LISTEN
title: NDK_FN_LISTEN
author: windows-driver-content
description: The NdkListen (NDK_FN_LISTEN) function puts an NDK listener object into listening mode.
old-location: netvista\ndk_fn_listen.htm
old-project: netvista
ms.assetid: 1C3DF31C-500E-456A-B121-48F5945D6999
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: NdkListen
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

# NDK_FN_LISTEN callback



## -description
<p>The <i>NdkListen</i> (<i>NDK_FN_LISTEN</i>) function puts an NDK listener object into listening mode.</p>


## -prototype

````
NDK_FN_LISTEN NdkListen;

NTSTATUS NdkListen(
  _In_     NDK_LISTENER                                    *pNdkListener,
           _In_reads_bytes_(AddressLength) const PSOCKADDR pAddress,
  _In_     ULONG                                           AddressLength,
  _In_     NDK_FN_REQUEST_COMPLETION                       RequestCompletion,
  _In_opt_ PVOID                                           RequestContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkListener</i> [in]

<dd>
<p>A pointer to an NDK listener object (<a href="..\ndkpi\ns-ndkpi--ndk-listener.md">NDK_LISTENER</a>).</p>
</dd>

### -param <i>pAddress</i> 

<dd>
<p>A local address to listen on. For AF_INET or AF_INET6 <i>pAddress</i> contains the local IP address and local ND port.

</p>
</dd>

### -param <i>AddressLength</i> [in]

<dd>
<p>The size, in bytes, of local address data at the <i>pAddress</i> parameter.

</p>
</dd>

### -param <i>RequestCompletion</i> [in]

<dd>
<p>A pointer to a request completion callback routine <i>NdkRequestCompletion</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-request-completion.md">NDK_FN_REQUEST_COMPLETION</a>).</p>
</dd>

### -param <i>RequestContext</i> [in, optional]

<dd>
<p>A context value to pass to the <i>Context</i> parameter of the  callback function that is specified in the <i>RequestCompletion</i> parameter.</p>
</dd>
</dl>

## -returns
<p>The 
     <i>NdkListen</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The listen request succeeded.
</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p> The operation is pending and will be completed later. The driver will call the specified <i>RequestCompletion</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-request-completion.md">NDK_FN_REQUEST_COMPLETION</a>) function to complete the pending operation.
 </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The request failed due to insufficient resources. </p><dl>
<dt><b>STATUS_SHARING_VIOLATION</b></dt>
</dl><p>	  The request failed because the specified local address is already in use.</p><dl>
<dt><b>STATUS_INVALID_ADDRESS</b></dt>
</dl><p>	The request failed because the specified local address is not a valid address for the adapter. </p><dl>
<dt><b>STATUS_TOO_MANY_ADDRESSES</b></dt>
</dl><p>The request failed because the consumer specified a local port number of zero, and the Network Direct provider was unable to allocate a port from the ephemeral port space (ports 49152-65535.)</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p><i>NdkListen</i> puts a listener object into listening mode on the specified  local address.</p>

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
<a href="..\ndkpi\nc-ndkpi-ndk-fn-request-completion.md">NDK_FN_REQUEST_COMPLETION</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-listener.md">NDK_LISTENER</a>
</dt>
<dt>
<a href="NULL">NDKPI Object Lifetime Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_LISTEN callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
