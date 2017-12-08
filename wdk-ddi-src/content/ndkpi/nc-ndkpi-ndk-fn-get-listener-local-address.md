---
UID: NC.ndkpi.NDK_FN_GET_LISTENER_LOCAL_ADDRESS
title: NDK_FN_GET_LISTENER_LOCAL_ADDRESS
author: windows-driver-content
description: The NdkGetListenerLocalAddress (NDK_FN_GET_LISTENER_LOCAL_ADDRESS) function returns the local address for an NDK listener.
old-location: netvista\ndk_fn_get_listener_local_address.htm
old-project: netvista
ms.assetid: 7BF5322F-5283-445D-AC3F-19382CB28E2B
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: NdkGetListenerLocalAddress
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

# NDK_FN_GET_LISTENER_LOCAL_ADDRESS callback



## -description
<p>The <i>NdkGetListenerLocalAddress</i> (<i>NDK_FN_GET_LISTENER_LOCAL_ADDRESS</i>) function returns the local address for an NDK  listener.</p>


## -prototype

````
NDK_FN_GET_LISTENER_LOCAL_ADDRESS NdkGetListenerLocalAddress;

NTSTATUS NdkGetListenerLocalAddress(
  _In_ NDK_LISTENER                                                          *pNdkListener,
       _Out_writes_bytes_to_opt_(*pAddressLength, *pAddressLength) PSOCKADDR pAddress,
       _Inout_ ULONG                                                         *pAddressLength
)
{ ... }
````


## -parameters
<dl>

### -param pNdkListener [in]

<dd>
<p>A pointer to an NDK listener object (<a href="..\ndkpi\ns-ndkpi--ndk-listener.md">NDK_LISTENER</a>).</p>
</dd>

### -param pAddress 

<dd>
<p>A local address for a listener is returned in this buffer.</p>
</dd>

### -param pAddressLength 

<dd>
<p>The size, in bytes, of the address buffer for input, and the size, in bytes, of the actual address written into the buffer for output.</p>
</dd>
</dl>

## -returns
<p>The 
     <i>NdkGetListenerLocalAddress</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>A local address was written to the buffer in the <i>pAddress</i> parameter.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer size specified in the <i>*pAddressLength</i> parameter input is too small. <i>*pAddressLength</i> output value is updated with the required buffer size.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p><i>NdkGetListenerLocalAddress</i> returns the local address for a listener. The local address is useful for retrieving port information for an AF_INET or AF_INET6 listener. For example, if the NDK consumer specifies zero as the ND port number in a listen request and the NDK provider specifies a port, the NDK consumer can use <i>NdkGetListenerLocalAddress</i> to  determine which port the provider specified.</p>

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
<a href="..\ndkpi\ns-ndkpi--ndk-listener.md">NDK_LISTENER</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-listen.md">NDK_FN_LISTEN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_GET_LISTENER_LOCAL_ADDRESS callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
