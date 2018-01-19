---
UID : NC:ndkpi.NDK_FN_GET_CONNECTION_DATA
title : NDK_FN_GET_CONNECTION_DATA
author : windows-driver-content
description : The NdkGetConnectionData (NDK_FN_GET_CONNECTION_DATA) function gets read limit values and the private data sent by the peer.
old-location : netvista\ndk_fn_get_connection_data.htm
old-project : netvista
ms.assetid : A6099DCB-7F10-4BDB-B463-422C2B7A2B3F
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NDIS_WWAN_VISIBLE_PROVIDERS, NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : ndkpi.h
req.include-header : Ndkpi.h
req.target-type : Windows
req.target-min-winverclnt : None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NdkGetConnectionData
req.alt-loc : ndkpi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <=DISPATCH_LEVEL
req.typenames : NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
---


# NDK_FN_GET_CONNECTION_DATA callback function
The <i>NdkGetConnectionData</i>  (<i>NDK_FN_GET_CONNECTION_DATA</i>) function gets read limit values and the private data sent by the peer.

## Syntax

```
NDK_FN_GET_CONNECTION_DATA NdkFnGetConnectionData;

NTSTATUS NdkFnGetConnectionData(
  NDK_CONNECTOR *pNdkConnector,
  ULONG *pInboundReadLimit,
  ULONG *pOutboundReadLimit,
  PVOID pPrivateData,
  ULONG *pPrivateDataLength
)
{...}
```

## Parameters

`*pNdkConnector`



`*pInboundReadLimit`



`*pOutboundReadLimit`



`pPrivateData`

A pointer to private data that is returned.

`*pPrivateDataLength`




## Return Value

The <i>NdkGetConnectionData</i> function returns one of the following NTSTATUS codes.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The operation completed successfully.
<dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl>The value in the <i>*pPrivateDataLength</i> parameter specified a buffer size that was too small to hold the connection private data. <i>*pPrivateDataLength</i> is updated with the required size.
<dl>
<dt><b>Other status codes</b></dt>
</dl>An error occurred.

## Remarks

The <i>NdkGetConnectionData</i>   function gets the private data sent by the peer with connect, accept, or reject requests and the effective inbound and outbound read limit values. These values are derived from the local and remote peers' requested values and the provider's maximum limits.

To access the private data and the effective inbound read limit (IRD) and outbound read limit (ORD) values from the active side, an NDK consumer can call <i>NdkGetConnectionData</i> for a connector object that was  passed to the <a href="..\ndkpi\nc-ndkpi-ndk_fn_connect_event_callback.md">NDK_FN_CONNECT_EVENT_CALLBACK</a> function.   

To access the private data and effective IRD and ORD values from the passive side, the consumer can call <i>NdkGetConnectionData</i> for a connector object for which <a href="..\ndkpi\nc-ndkpi-ndk_fn_connect.md">NDK_FN_CONNECT</a> or  <a href="..\ndkpi\nc-ndkpi-ndk_fn_connect_with_shared_endpoint.md">NDK_FN_CONNECT_WITH_SHARED_ENDPOINT</a> completed successfully An NDK consumer will not call this function after it calls the <a href="..\ndkpi\nc-ndkpi-ndk_fn_accept.md">NDK_FN_ACCEPT</a> function on the passive side or the <a href="..\ndkpi\nc-ndkpi-ndk_fn_complete_connect.md">NDK_FN_COMPLETE_CONNECT</a> function  on the active side.


If  the <i>pPrivateData</i> parameter  is NULL and <i>*pPrivateDataLength</i> is zero, an NDK provider must return STATUS_SUCCESS and store the required private data buffer size (<i>RDS</i>) in <i>*pPrivateDataLength</i>. 

If <i>pPrivateData</i> is NULL and <i>*pPrivateDataLength</i> is greater than zero, this is an invalid request. A consumer must never do this.


If <i>pPrivateData</i> is not NULL, the provider must copy the private data to the buffer at  <i>pPrivateData</i> up to the smaller of <i>*pPrivateDataLength</i> or <i>RDS</i> in  bytes. 

If <i>*pPrivateDataLength</i> is greater than or equal to <i>RDS</i>, the provider must return STATUS_SUCCESS. Otherwise, the provider must return STATUS_BUFFER_TOO_SMALL. In both cases, the provider must store the <i>RDS</i> in <i>*pPrivateDataLength</i> before returning.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndkpi.h (include Ndkpi.h) |
| **Library** |  |
| **IRQL** | <=DISPATCH_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_connector.md">NDK_CONNECTOR</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi-_ndk_connector_dispatch.md">NDK_CONNECTOR_DISPATCH</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_GET_CONNECTION_DATA callback function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>