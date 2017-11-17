---
UID: NS.ndkpi._NDK_LISTENER_DISPATCH
title: NDK_LISTENER_DISPATCH
author: windows-driver-content
description: The NDK_LISTENER_DISPATCH structure specifies dispatch function entry points for the NDK listener object.
old-location: netvista\ndk_listener_dispatch.htm
ms.assetid: CF44B920-428A-4CD0-94BF-15F80189D9C3
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDK_LISTENER_DISPATCH
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
ms.keywords: NDK_LISTENER_DISPATCH, NDK_LISTENER_DISPATCH
req.iface: 
---

# NDK_LISTENER_DISPATCH structure



## -description
<p>The <b>NDK_LISTENER_DISPATCH</b> structure specifies dispatch function entry points for the NDK listener object.</p>


## -syntax

````
typedef struct _NDK_LISTENER_DISPATCH {
  NDK_FN_CLOSE_OBJECT               NdkCloseListener;
  NDK_FN_QUERY_EXTENSION_INTERFACE  NdkQueryExtension;
  NDK_FN_LISTEN                     NdkListen;
  NDK_FN_GET_LISTENER_LOCAL_ADDRESS NdkGetLocalAddress;
  NDK_FN_CONTROL_CONNECT_EVENTS     NdkControlConnectEvents;
} NDK_LISTENER_DISPATCH, *PNDK_LISTENER_DISPATCH;
````


## -struct-fields
<dl>

### -field <b>NdkCloseListener</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439863">NDK_FN_CLOSE_OBJECT</a> dispatch function.</p>
</dd>

### -field <b>NdkQueryExtension</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439905">NDK_FN_QUERY_EXTENSION_INTERFACE</a> dispatch function.</p>
</dd>

### -field <b>NdkListen</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439902">NDK_FN_LISTEN</a> dispatch function.</p>
</dd>

### -field <b>NdkGetLocalAddress</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439892">NDK_FN_GET_LISTENER_LOCAL_ADDRESS</a> dispatch function.</p>
</dd>

### -field <b>NdkControlConnectEvents</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439869">NDK_FN_CONTROL_CONNECT_EVENTS</a> dispatch function.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDK_LISTENER_DISPATCH</b> structure is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439918">NDK_LISTENER</a> structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439918">NDK_LISTENER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439863">NDK_FN_CLOSE_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439869">NDK_FN_CONTROL_CONNECT_EVENTS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439892">NDK_FN_GET_LISTENER_LOCAL_ADDRESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439902">NDK_FN_LISTEN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439905">NDK_FN_QUERY_EXTENSION_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_LISTENER_DISPATCH structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
