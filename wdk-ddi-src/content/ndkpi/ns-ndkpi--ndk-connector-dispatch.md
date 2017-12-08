---
UID: NS.ndkpi._NDK_CONNECTOR_DISPATCH
title: NDK_CONNECTOR_DISPATCH
author: windows-driver-content
description: The NDK_CONNECTOR_DISPATCH structure specifies dispatch function entry points for the NDK connector object.
old-location: netvista\ndk_connector_dispatch.htm
old-project: netvista
ms.assetid: BBC24A32-4CB6-47AB-BD1D-298159EC9919
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDK_CONNECTOR_DISPATCH, NDK_CONNECTOR_DISPATCH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDK_CONNECTOR_DISPATCH
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

# NDK_CONNECTOR_DISPATCH structure



## -description
<p>The <b>NDK_CONNECTOR_DISPATCH</b> structure specifies dispatch function entry points for the NDK connector object.</p>


## -syntax

````
typedef struct _NDK_CONNECTOR_DISPATCH {
  NDK_FN_CLOSE_OBJECT                 NdkCloseConnector;
  NDK_FN_QUERY_EXTENSION_INTERFACE    NdkQueryExtension;
  NDK_FN_CONNECT                      NdkConnect;
  NDK_FN_CONNECT_WITH_SHARED_ENDPOINT NdkConnectWithSharedEndpoint;
  NDK_FN_COMPLETE_CONNECT             NdkCompleteConnect;
  NDK_FN_ACCEPT                       NdkAccept;
  NDK_FN_REJECT                       NdkReject;
  NDK_FN_GET_CONNECTION_DATA          NdkGetConnectionData;
  NDK_FN_GET_LOCAL_ADDRESS            NdkGetLocalAddress;
  NDK_FN_GET_PEER_ADDRESS             NdkGetPeerAddress;
  NDK_FN_DISCONNECT                   NdkDisconnect;
} NDK_CONNECTOR_DISPATCH, *PNDK_CONNECTOR_DISPATCH;
````


## -struct-fields
<dl>

### -field NdkCloseConnector

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-close-object.md">NDK_FN_CLOSE_OBJECT</a> dispatch function.</p>
</dd>

### -field NdkQueryExtension

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-query-extension-interface.md">NDK_FN_QUERY_EXTENSION_INTERFACE</a> dispatch function.</p>
</dd>

### -field NdkConnect

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-connect.md">NDK_FN_CONNECT</a> dispatch function.</p>
</dd>

### -field NdkConnectWithSharedEndpoint

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-connect-with-shared-endpoint.md">NDK_FN_CONNECT_WITH_SHARED_ENDPOINT</a> dispatch function.</p>
</dd>

### -field NdkCompleteConnect

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-complete-connect.md">NDK_FN_COMPLETE_CONNECT</a> dispatch function.</p>
</dd>

### -field NdkAccept

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-accept.md">NDK_FN_ACCEPT</a> dispatch function.</p>
</dd>

### -field NdkReject

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-reject.md">NDK_FN_REJECT</a> dispatch function.</p>
</dd>

### -field NdkGetConnectionData

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-get-connection-data.md">NDK_FN_GET_CONNECTION_DATA</a> dispatch function.</p>
</dd>

### -field NdkGetLocalAddress

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-get-local-address.md">NDK_FN_GET_LOCAL_ADDRESS</a> dispatch function.</p>
</dd>

### -field NdkGetPeerAddress

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-get-peer-address.md">NDK_FN_GET_PEER_ADDRESS</a> dispatch function.</p>
</dd>

### -field NdkDisconnect

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-disconnect.md">NDK_FN_DISCONNECT</a> dispatch function.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDK_CONNECTOR_DISPATCH</b> structure is used in the <a href="..\ndkpi\ns-ndkpi--ndk-connector.md">NDK_CONNECTOR</a> structure.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-connector.md">NDK_CONNECTOR</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-accept.md">NDK_FN_ACCEPT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-close-object.md">NDK_FN_CLOSE_OBJECT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-complete-connect.md">NDK_FN_COMPLETE_CONNECT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-connect.md">NDK_FN_CONNECT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-connect-with-shared-endpoint.md">NDK_FN_CONNECT_WITH_SHARED_ENDPOINT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-disconnect.md">NDK_FN_DISCONNECT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-get-connection-data.md">NDK_FN_GET_CONNECTION_DATA</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-get-local-address.md">NDK_FN_GET_LOCAL_ADDRESS</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-get-peer-address.md">NDK_FN_GET_PEER_ADDRESS</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-query-extension-interface.md">NDK_FN_QUERY_EXTENSION_INTERFACE</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-reject.md">NDK_FN_REJECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_CONNECTOR_DISPATCH structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
