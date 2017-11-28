---
UID: NS.ndkpi._NDK_CQ_DISPATCH
title: NDK_CQ_DISPATCH
author: windows-driver-content
description: The NDK_CQ_DISPATCH structure specifies dispatch function entry points for the NDK completion queue (CQ) object.
old-location: netvista\ndk_cq_dispatch.htm
old-project: netvista
ms.assetid: 632E4FE8-BA03-4232-80E1-5EB3CC760D14
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDK_CQ_DISPATCH, NDK_CQ_DISPATCH
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
req.alt-api: NDK_CQ_DISPATCH
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

# NDK_CQ_DISPATCH structure



## -description
<p>The <b>NDK_CQ_DISPATCH</b> structure specifies dispatch function entry points for the NDK completion queue (CQ) object.</p>


## -syntax

````
typedef struct _NDK_CQ_DISPATCH {
  NDK_FN_CLOSE_OBJECT                    NdkCloseCq;
  NDK_FN_QUERY_EXTENSION_INTERFACE       NdkQueryExtension;
  NDK_FN_RESIZE_CQ                       NdkResizeCq;
  NDK_FN_ARM_CQ                          NdkArmCq;
  NDK_FN_GET_CQ_RESULTS                  NdkGetCqResults;
  NDK_FN_CONTROL_CQ_INTERRUPT_MODERATION NdkControlCqInterruptModeration;
  NDK_FN_GET_CQ_RESULTS_EX               NdkGetCqResultsEx;
} NDK_CQ_DISPATCH, *PNDK_CQ_DISPATCH;
````


## -struct-fields
<dl>

### -field <b>NdkCloseCq</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439863">NDK_FN_CLOSE_OBJECT</a> dispatch function.</p>
</dd>

### -field <b>NdkQueryExtension</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439905">NDK_FN_QUERY_EXTENSION_INTERFACE</a> dispatch function.</p>
</dd>

### -field <b>NdkResizeCq</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439913">NDK_FN_RESIZE_CQ</a> dispatch function.</p>
</dd>

### -field <b>NdkArmCq</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439858">NDK_FN_ARM_CQ</a> dispatch function.</p>
</dd>

### -field <b>NdkGetCqResults</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439891">NDK_FN_GET_CQ_RESULTS</a> dispatch function.</p>
</dd>

### -field <b>NdkControlCqInterruptModeration</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/jj552973">NDK_FN_CONTROL_CQ_INTERRUPT_MODERATION</a> dispatch function.</p>
</dd>

### -field <b>NdkGetCqResultsEx</b>

<dd>
<p>The entry point for the object's <a href="https://msdn.microsoft.com/library/windows/hardware/dn265506">NDK_FN_GET_CQ_RESULTS_EX</a> dispatch function. </p>
<p><b>Note</b>  This member is supported only in NDKPI 1.2 (Windows Server 2012 R2) and later.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDK_CQ_DISPATCH</b> structure is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439854">NDK_CQ</a> structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439854">NDK_CQ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439858">NDK_FN_ARM_CQ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439863">NDK_FN_CLOSE_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj552973">NDK_FN_CONTROL_CQ_INTERRUPT_MODERATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439891">NDK_FN_GET_CQ_RESULTS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439905">NDK_FN_QUERY_EXTENSION_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439913">NDK_FN_RESIZE_CQ</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_CQ_DISPATCH structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
