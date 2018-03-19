---
UID: NC:ndkpi.NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS
title: NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS
author: windows-driver-content
description: The NdkGetSharedEndpointLocalAddress (NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS) function returns the local address for an NDK shared endpoint.
old-location: netvista\ndk_fn_get_shared_endpoint_local_address.htm
old-project: netvista
ms.assetid: C7B6B7DC-359D-44C2-8348-EC1EE5965800
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS, NdkGetSharedEndpointLocalAddress, NdkGetSharedEndpointLocalAddress callback function [Network Drivers Starting with Windows Vista], ndkpi/NdkGetSharedEndpointLocalAddress, netvista.ndk_fn_get_shared_endpoint_local_address
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: "<=DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	ndkpi.h
api_name:
-	NdkGetSharedEndpointLocalAddress
product: Windows
targetos: Windows
req.typenames: NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
---


# NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS callback function
The <i>NdkGetSharedEndpointLocalAddress</i> (<i>NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS</i>) function returns the local address for an NDK  shared endpoint.

## Syntax

```
NDK_FN_GET_SHARED_ENDPOINT_LOCAL_ADDRESS NdkFnGetSharedEndpointLocalAddress;

NTSTATUS NdkFnGetSharedEndpointLocalAddress(
  NDK_SHARED_ENDPOINT *pNdkSharedEndpoint,
  PSOCKADDR pAddress,
  ULONG *pAddressLength
)
{...}
```

## Parameters

`*pNdkSharedEndpoint`

A pointer to an NDK shared endpoint object  (<a href="..\ndkpi\ns-ndkpi-_ndk_shared_endpoint.md">NDK_SHARED_ENDPOINT</a>).

`pAddress`

A local address is returned in this buffer.

`*pAddressLength`

The size, in bytes, of the address buffer for input, and the size, in bytes, of the actual address written into the buffer for output.


## Return Value

The 
     <i>NdkGetSharedEndpointLocalAddress</i> function returns one of the following NTSTATUS codes.

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
A local address was written to the buffer in the <i>pAddress</i> parameter.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl>
</td>
<td width="60%">
The buffer size specified in the <i>*pAddressLength</i> parameter input is too small. <i>*pAddressLength</i> output value is updated with the required buffer size.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>Other status codes</b></dt>
</dl>
</td>
<td width="60%">
An error occurred. 

</td>
</tr>
</table>

## Remarks

<i>NdkGetSharedEndpointLocalAddress</i> returns the local address for a shared endpoint. <i>NdkGetSharedEndpointLocalAddress</i> retrieves port information for an AF_INET or AF_INET6  shared endpoint. That is, if the NDK consumer specifies zero as the ND port number in a shared endpoint creation request, the NDK provider picks a port. An NDK consumer can determine the port that the provider picked with <i>NdkGetSharedEndpointLocalAddress</i>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | None supported,Supported in NDIS 6.30 and later. Windows Server 2012 |
| **Target Platform** | Windows |
| **Header** | ndkpi.h (include Ndkpi.h) |
| **IRQL** | "<=DISPATCH_LEVEL" |

## See Also

<a href="..\ndkpi\ns-ndkpi-_ndk_shared_endpoint.md">NDK_SHARED_ENDPOINT</a>