---
UID: NC.ndkpi.NDK_FN_COMPLETE_CONNECT
title: NDK_FN_COMPLETE_CONNECT
author: windows-driver-content
description: The NdkCompleteConnect (NDK_FN_COMPLETE_CONNECT) function completes an asynchronous connection request.
old-location: netvista\ndk_fn_complete_connect.htm
old-project: netvista
ms.assetid: 85AD83CE-C00F-4D5A-BCDE-22D1B83201A8
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
req.alt-api: NdkCompleteConnect
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

# NDK_FN_COMPLETE_CONNECT callback



## -description
<p>The <i>NdkCompleteConnect</i> (<i>NDK_FN_COMPLETE_CONNECT</i>) function completes an asynchronous connection request.</p>


## -prototype

````
NDK_FN_COMPLETE_CONNECT NdkCompleteConnect;

NTSTATUS NdkCompleteConnect(
  _In_     NDK_CONNECTOR                    *pNdkConnector,
  _In_opt_ NDK_FN_DISCONNECT_EVENT_CALLBACK DisconnectEvent,
  _In_opt_ PVOID                            DisconnectEventContext,
  _In_     NDK_FN_REQUEST_COMPLETION        RequestCompletion,
  _In_opt_ PVOID                            RequestContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkConnector</i> [in]

<dd>
<p>A pointer to an NDK connector object (<a href="..\ndkpi\ns-ndkpi--ndk-connector.md">NDK_CONNECTOR</a>).
</p>
</dd>

### -param <i>DisconnectEvent</i> [in, optional]

<dd>
<p>An optional disconnect notification callback <i>NdkDisconnectEventCallback</i>  function(<a href="..\ndkpi\nc-ndkpi-ndk-fn-disconnect-event-callback.md">NDK_FN_DISCONNECT_EVENT_CALLBACK</a>) that the provider calls when the peer disconnects.</p>
</dd>

### -param <i>DisconnectEventContext</i> [in, optional]

<dd>
<p>A context value to pass back to the <i>NdkDisconnectEventCallback</i> function that is specified in the  <i>DisconnectEvent</i> parameter.</p>
</dd>

### -param <i>RequestCompletion</i> [in]

<dd>
<p>A pointer to a request completion callback <i>NdkRequestCompletion</i>  function (<a href="..\ndkpi\nc-ndkpi-ndk-fn-request-completion.md">NDK_FN_REQUEST_COMPLETION</a>).</p>
</dd>

### -param <i>RequestContext</i> [in, optional]

<dd>
<p>A context value that  the provider passes back to the <i>NdkRequestCompletion</i> function that is specified in the <i>RequestCompletion</i> parameter.</p>
</dd>
</dl>

## -returns
<p>The 
     <i>NDK_FN_COMPLETE_CONNECT</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The request was completed successfully.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The request is pending. The provider will call the <i>NdkRequestCompletion</i> function that is specified in the <i>RequestCompletion</i> parameter  to complete the request asynchronously.</p><dl>
<dt><b>STATUS_CONNECTION_INVALID</b></dt>
</dl><p>The request failed because the queue pair is not connecting. </p><dl>
<dt><b>STATUS_CONNECTION_ABORTED</b></dt>
</dl><p>The accepting peer abandoned the pending connection establishment.</p><dl>
<dt><b>STATUS_IO_TIMEOUT</b></dt>
</dl><p>The request failed because the connection establishment timed out. This is not an indication of a catastrophic or permanent failure, but it ends connection establishment for this connector.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p>The <i>NdkCompleteConnect</i> function completes a connection request that was  initiated by a previous call to the <i>NdkConnect</i>  (<a href="..\ndkpi\nc-ndkpi-ndk-fn-connect.md">NDK_FN_CONNECT</a>) function. The NDK consumer calls <i>NdkCompleteConnect</i> after the peer accepts the connection request.</p>

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
<a href="..\ndkpi\ns-ndkpi--ndk-connector.md">NDK_CONNECTOR</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-connector-dispatch.md">NDK_CONNECTOR_DISPATCH</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-connect.md">NDK_FN_CONNECT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-disconnect-event-callback.md">NDK_FN_DISCONNECT_EVENT_CALLBACK</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-request-completion.md">NDK_FN_REQUEST_COMPLETION</a>
</dt>
<dt>
<a href="NULL">NDKPI Object Lifetime Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_COMPLETE_CONNECT callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
