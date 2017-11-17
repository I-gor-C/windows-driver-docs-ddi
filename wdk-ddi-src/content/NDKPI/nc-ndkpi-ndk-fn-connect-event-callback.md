---
UID: NC.ndkpi.NDK_FN_CONNECT_EVENT_CALLBACK
title: NDK_FN_CONNECT_EVENT_CALLBACK
author: windows-driver-content
description: The NdkConnectEventCallback (NDK_FN_CONNECT_EVENT_CALLBACK) function is called by an NDK provider to notify a consumer about an incoming connection request.
old-location: netvista\ndk_fn_connect_event_callback.htm
ms.assetid: D7009707-7139-4572-A620-C8ACFA6B5665
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
req.alt-api: NdkConnectEventCallback
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

# NDK_FN_CONNECT_EVENT_CALLBACK callback



## -description
<p>The <i>NdkConnectEventCallback</i> (<i>NDK_FN_CONNECT_EVENT_CALLBACK</i>) function is called by an NDK provider to notify a consumer about an incoming connection request.
</p>


## -prototype

````
NDK_FN_CONNECT_EVENT_CALLBACK NdkConnectEventCallback;

VOID NdkConnectEventCallback(
  _In_opt_ PVOID         ConnectEventContext,
  _In_     NDK_CONNECTOR *pNdkConnector
)
{ ... }
````


## -parameters
<dl>

### -param <i>ConnectEventContext</i> [in, optional]

<dd>
<p>A context area that was specified in the <i>ConnectEventContext</i> parameter of the <i>NdkCreateListener</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439874">NDK_FN_CREATE_LISTENER</a>) function when the listener object was created.</p>
</dd>

### -param <i>pNdkConnector</i> [in]

<dd>
<p>A pointer to an NDK connector object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439852">NDK_CONNECTOR</a>) that represents a new incoming connection request.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The NDK consumer specified the <i>NdkConnectEventCallback</i> function  in the <i>ConnectEventContext</i> parameter of the <i>NdkCreateListener</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439874">NDK_FN_CREATE_LISTENER</a>) function when the listener object was created.</p>

<p>The NDK consumer specified the <i>NdkConnectEventCallback</i> function  in the <i>ConnectEventContext</i> parameter of the <i>NdkCreateListener</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439874">NDK_FN_CREATE_LISTENER</a>) function when the listener object was created.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439852">NDK_CONNECTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439874">NDK_FN_CREATE_LISTENER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_CONNECT_EVENT_CALLBACK callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
