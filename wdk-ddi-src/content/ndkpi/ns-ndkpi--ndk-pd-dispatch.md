---
UID: NS.ndkpi._NDK_PD_DISPATCH
title: NDK_PD_DISPATCH
author: windows-driver-content
description: The NDK_PD_DISPATCH structure specifies dispatch function entry points for the NDK protection domain (PD) object.
old-location: netvista\ndk_pd_dispatch.htm
old-project: netvista
ms.assetid: 3BAD6CF9-8DCD-470F-9C2E-C7C9C0B29ADA
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDK_PD_DISPATCH, NDK_PD_DISPATCH
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
req.alt-api: NDK_PD_DISPATCH
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

# NDK_PD_DISPATCH structure



## -description
<p>The <b>NDK_PD_DISPATCH</b> structure specifies dispatch function entry points for the NDK protection domain (PD) object.</p>


## -syntax

````
typedef struct _NDK_PD_DISPATCH {
  NDK_FN_CLOSE_OBJECT                       NdkClosePd;
  NDK_FN_QUERY_EXTENSION_INTERFACE          NdkQueryExtension;
  NDK_FN_CREATE_MR                          NdkCreateMr;
  NDK_FN_CREATE_MW                          NdkCreateMw;
  NDK_FN_CREATE_SRQ                         NdkCreateSrq;
  NDK_FN_CREATE_QP                          NdkCreateQp;
  NDK_FN_CREATE_QP_WITH_SRQ                 NdkCreateQpWithSrq;
  NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN NdkGetPrivilegedMemoryRegionToken;
} NDK_PD_DISPATCH;
````


## -struct-fields
<dl>

### -field NdkClosePd

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-close-object.md">NDK_FN_CLOSE_OBJECT</a> dispatch function.</p>
</dd>

### -field NdkQueryExtension

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-query-extension-interface.md">NDK_FN_QUERY_EXTENSION_INTERFACE</a> dispatch function.</p>
</dd>

### -field NdkCreateMr

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-create-mr.md">NDK_FN_CREATE_MR</a> dispatch function.</p>
</dd>

### -field NdkCreateMw

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-create-mw.md">NDK_FN_CREATE_MW</a> dispatch function.</p>
</dd>

### -field NdkCreateSrq

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-create-srq.md">NDK_FN_CREATE_SRQ</a> dispatch function.</p>
</dd>

### -field NdkCreateQp

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-create-qp.md">NDK_FN_CREATE_QP</a> dispatch function.</p>
</dd>

### -field NdkCreateQpWithSrq

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-create-qp-with-srq.md">NDK_FN_CREATE_QP_WITH_SRQ</a> dispatch function.</p>
</dd>

### -field NdkGetPrivilegedMemoryRegionToken

<dd>
<p>The entry point for the object's <a href="..\ndkpi\nc-ndkpi-ndk-fn-get-privileged-memory-region-token.md">NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN</a> dispatch function.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDK_PD_DISPATCH</b> structure is used in the <a href="..\ndkpi\ns-ndkpi--ndk-pd.md">NDK_PD</a> structure.</p>

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
<a href="..\ndkpi\ns-ndkpi--ndk-pd.md">NDK_PD</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-close-object.md">NDK_FN_CLOSE_OBJECT</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-mr.md">NDK_FN_CREATE_MR</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-mw.md">NDK_FN_CREATE_MW</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-qp.md">NDK_FN_CREATE_QP</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-qp-with-srq.md">NDK_FN_CREATE_QP_WITH_SRQ</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-srq.md">NDK_FN_CREATE_SRQ</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-get-privileged-memory-region-token.md">NDK_FN_GET_PRIVILEGED_MEMORY_REGION_TOKEN</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-query-extension-interface.md">NDK_FN_QUERY_EXTENSION_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_PD_DISPATCH structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
