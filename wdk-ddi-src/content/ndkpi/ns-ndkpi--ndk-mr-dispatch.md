---
UID: NS.ndkpi._NDK_MR_DISPATCH
title: NDK_MR_DISPATCH
author: windows-driver-content
description: The NDK_MR_DISPATCH structure specifies dispatch function entry points for the NDK memory region (MR) object.
old-location: netvista\ndk_mr_dispatch.htm
old-project: netvista
ms.assetid: C0EC5488-B08D-40A6-9E90-48E59B45B116
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDK_MR_DISPATCH, NDK_MR_DISPATCH
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
req.alt-api: NDK_MR_DISPATCH
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

# NDK_MR_DISPATCH structure



## -description
<p>The <b>NDK_MR_DISPATCH</b> structure specifies dispatch function entry points for the NDK memory region (MR) object.</p>


## -syntax

````
typedef struct _NDK_MR_DISPATCH {
  NDK_FN_CLOSE_OBJECT                NdkCloseMr;
  NDK_FN_QUERY_EXTENSION_INTERFACE   NdkQueryExtension;
  NDK_FN_REGISTER_MR                 NdkRegisterMr;
  NDK_FN_DEREGISTER_MR               NdkDeregisterMr;
  NDK_FN_INITIALIZE_FAST_REGISTER_MR NdkInitializeFastRegisterMr;
  NDK_FN_GET_REMOTE_TOKEN_FROM_MR    NdkGetRemoteTokenFromMr;
  NDK_FN_GET_LOCAL_TOKEN_FROM_MR     NdkGetLocalTokenFromMr;
} NDK_MR_DISPATCH, *PNDK_MR_DISPATCH;
````


## -struct-fields
<dl>

### -field <b>NdkCloseMr</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439863">NDK_FN_CLOSE_OBJECT</a> dispatch function.</p>
</dd>

### -field <b>NdkQueryExtension</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439905">NDK_FN_QUERY_EXTENSION_INTERFACE</a> dispatch function.</p>
</dd>

### -field <b>NdkRegisterMr</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439908">NDK_FN_REGISTER_MR</a> dispatch function.</p>
</dd>

### -field <b>NdkDeregisterMr</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439884">NDK_FN_DEREGISTER_MR</a> dispatch function.</p>
</dd>

### -field <b>NdkInitializeFastRegisterMr</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439900">NDK_FN_INITIALIZE_FAST_REGISTER_MR</a> dispatch function.</p>
</dd>

### -field <b>NdkGetRemoteTokenFromMr</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439897">NDK_FN_GET_REMOTE_TOKEN_FROM_MR</a> dispatch function.</p>
</dd>

### -field <b>NdkGetLocalTokenFromMr</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439894">NDK_FN_GET_LOCAL_TOKEN_FROM_MR</a> dispatch function.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDK_MR_DISPATCH</b> structure is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439922">NDK_MR</a> structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439922">NDK_MR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439863">NDK_FN_CLOSE_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439884">NDK_FN_DEREGISTER_MR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439897">NDK_FN_GET_REMOTE_TOKEN_FROM_MR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439894">NDK_FN_GET_LOCAL_TOKEN_FROM_MR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439900">NDK_FN_INITIALIZE_FAST_REGISTER_MR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439905">NDK_FN_QUERY_EXTENSION_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439908">NDK_FN_REGISTER_MR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_MR_DISPATCH structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
