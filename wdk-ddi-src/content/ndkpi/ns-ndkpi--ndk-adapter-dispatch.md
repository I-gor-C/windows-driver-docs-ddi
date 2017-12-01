---
UID: NS.ndkpi._NDK_ADAPTER_DISPATCH
title: NDK_ADAPTER_DISPATCH
author: windows-driver-content
description: The NDK_ADAPTER_DISPATCH structure specifies dispatch function entry points for the NDK adapter object.
old-location: netvista\ndk_adapter_dispatch.htm
old-project: netvista
ms.assetid: 61C425CB-4900-4EB2-8D33-FF235BC03929
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDK_ADAPTER_DISPATCH, NDK_ADAPTER_DISPATCH
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
req.alt-api: NDK_ADAPTER_DISPATCH
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

# NDK_ADAPTER_DISPATCH structure



## -description
<p>The <b>NDK_ADAPTER_DISPATCH</b> structure specifies dispatch function entry points for the NDK adapter object.</p>


## -syntax

````
typedef struct _NDK_ADAPTER_DISPATCH {
  NDK_FN_QUERY_EXTENSION_INTERFACE NdkQueryExtension;
  NDK_FN_QUERY_ADAPTER_INFO        NdkQueryAdapterInfo;
  NDK_FN_CREATE_CQ                 NdkCreateCq;
  NDK_FN_CREATE_PD                 NdkCreatePd;
  NDK_FN_CREATE_SHARED_ENDPOINT    NdkCreateSharedEndpoint;
  NDK_FN_CREATE_CONNECTOR          NdkCreateConnector;
  NDK_FN_CREATE_LISTENER           NdkCreateListener;
  NDK_FN_BUILD_LAM                 NdkBuildLAM;
  NDK_FN_RELEASE_LAM               NdkReleaseLAM;
} NDK_ADAPTER_DISPATCH, *PNDK_ADAPTER_DISPATCH;
````


## -struct-fields
<dl>

### -field <b>NdkQueryExtension</b>

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-query-extension-interface.md">NDK_FN_QUERY_EXTENSION_INTERFACE</a> dispatch function.</p>
</dd>

### -field <b>NdkQueryAdapterInfo</b>

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-query-adapter-info.md">NDK_FN_QUERY_ADAPTER_INFO</a> dispatch function.</p>
</dd>

### -field <b>NdkCreateCq</b>

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-create-cq.md">NDK_FN_CREATE_CQ</a> dispatch function.</p>
</dd>

### -field <b>NdkCreatePd</b>

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-create-pd.md">NDK_FN_CREATE_PD</a> dispatch function.</p>
</dd>

### -field <b>NdkCreateSharedEndpoint</b>

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-create-shared-endpoint.md">NDK_FN_CREATE_SHARED_ENDPOINT</a> dispatch function.</p>
</dd>

### -field <b>NdkCreateConnector</b>

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-create-connector.md">NDK_FN_CREATE_CONNECTOR</a> dispatch function.</p>
</dd>

### -field <b>NdkCreateListener</b>

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-create-listener.md">NDK_FN_CREATE_LISTENER</a> dispatch function.</p>
</dd>

### -field <b>NdkBuildLAM</b>

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-build-lam.md">NDK_FN_BUILD_LAM</a> dispatch function.</p>
</dd>

### -field <b>NdkReleaseLAM</b>

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-release-lam.md">NDK_FN_RELEASE_LAM</a> dispatch function.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDK_ADAPTER_DISPATCH</b> structure is used in the <a href="..\ndkpi\ns-ndkpi--ndk-adapter.md">NDK_ADAPTER</a> structure.</p>

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
<a href="..\ndkpi\ns-ndkpi--ndk-adapter.md">NDK_ADAPTER</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-build-lam.md">NDK_FN_BUILD_LAM</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-connector.md">NDK_FN_CREATE_CONNECTOR</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-cq.md">NDK_FN_CREATE_CQ</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-listener.md">NDK_FN_CREATE_LISTENER</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-pd.md">NDK_FN_CREATE_PD</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-shared-endpoint.md">NDK_FN_CREATE_SHARED_ENDPOINT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-query-adapter-info.md">NDK_FN_QUERY_ADAPTER_INFO</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-query-extension-interface.md">NDK_FN_QUERY_EXTENSION_INTERFACE</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-release-lam.md">NDK_FN_RELEASE_LAM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_ADAPTER_DISPATCH structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
