---
UID: NC.ndkpi.NDK_FN_CREATE_MR
title: NDK_FN_CREATE_MR
author: windows-driver-content
description: The NdkCreateMr (NDK_FN_CREATE_MR) function creates an NDK memory region (MR) object.
old-location: netvista\ndk_fn_create_mr.htm
old-project: netvista
ms.assetid: AD0F1FA1-0CE5-40BE-86B8-537C9C8C0B8F
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
req.alt-api: NdkCreateMr
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

# NDK_FN_CREATE_MR callback



## -description
<p>The <i>NdkCreateMr</i> (<i>NDK_FN_CREATE_MR</i>) function creates an NDK memory region (MR) object.</p>


## -prototype

````
NDK_FN_CREATE_MR NdkCreateMr;

NTSTATUS NdkCreateMr(
  _In_     NDK_PD                   *pNdkPd,
  _In_     BOOLEAN                  FastRegister,
  _In_     NDK_FN_CREATE_COMPLETION CreateCompletion,
  _In_opt_ PVOID                    RequestContext,
           _Outptr_ NDK_MR          **ppNdkMr
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkPd</i> [in]

<dd>
<p>A pointer to an NDK protection domain (PD) object (<a href="..\ndkpi\ns-ndkpi--ndk-pd.md">NDK_PD</a>).</p>
</dd>

### -param <i>FastRegister</i> [in]

<dd>
<p>If TRUE, MR is for fast-register only. Otherwise, MR is for normal register only.</p>
</dd>

### -param <i>CreateCompletion</i> [in]

<dd>
<p>A pointer to an <i>NdkCreateCompletion</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-completion.md">NDK_FN_CREATE_COMPLETION</a>) function that completes the creation of an NDK object.</p>
</dd>

### -param <i>RequestContext</i> [in, optional]

<dd>
<p>A context value that the NDK provider passes back to the <i>NdkCreateCompletion</i> function that is specified in the <i>CreateCompletion</i> parameter.</p>
</dd>

### -param <i>ppNdkMr</i> 

<dd>
<p>A pointer to the created MR object (<a href="..\ndkpi\ns-ndkpi--ndk-mr.md">NDK_MR</a>) is returned in this location if request succeeds without returning <b>STATUS_PENDING</b>. If <i>NdkCreateMr</i> returns <b>STATUS_PENDING</b>, this parameter is ignored and the created object is returned  with the callback that is specified in the  <i>CreateCompletion</i> parameter.</p>
</dd>
</dl>

## -returns
<p>The 
     <i>NdkCreateMr</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The MR object was created successfully and returned with the <i>*ppNdkMr</i> parameter.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p> The operation is pending and will be completed later. The provider will call the function specified in the <i>CreateCompletion</i> parameter(<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-completion.md">NDK_FN_CREATE_COMPLETION</a>) to complete the pending operation.
 </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The request failed due to insufficient resources. </p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p>The <i>NdkCreateMr</i> function creates an NDK memory region (MR) object that can be used for memory registration and fast registration requests. If the function returns <b>STATUS_SUCCESS</b>, the created object is returned in the <i>ppNdkMr</i> parameter. If <i>NdkCreateMr</i> returns <b>STATUS_PENDING</b>, the created object is returned by the <i>NdkCreateCompletion</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-completion.md">NDK_FN_CREATE_COMPLETION</a>) function that is specified in the <i>CreateCompletion</i> parameter.</p>

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
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-completion.md">NDK_FN_CREATE_COMPLETION</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-mr.md">NDK_MR</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-pd.md">NDK_PD</a>
</dt>
<dt>
<a href="NULL">NDKPI Object Lifetime Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_CREATE_MR callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
