---
UID: NC.ndkpi.NDK_FN_SRQ_RECEIVE
title: NDK_FN_SRQ_RECEIVE
author: windows-driver-content
description: The NdkSrqReceive (NDK_FN_SRQ_RECEIVE) function posts a receive request on an NDK shared receive queue (SRQ).
old-location: netvista\ndk_fn_srq_receive.htm
old-project: netvista
ms.assetid: 1D615DEA-5599-4A3D-AEE7-BDBFE9D40C47
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: NdkSrqReceive
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

# NDK_FN_SRQ_RECEIVE callback



## -description
<p>The <i>NdkSrqReceive</i> (<i>NDK_FN_SRQ_RECEIVE</i>) function posts a receive request on an NDK shared receive queue (SRQ).</p>


## -prototype

````
NDK_FN_SRQ_RECEIVE NdkSrqReceive;

NTSTATUS NdkSrqReceive(
  _In_     NDK_SRQ                        *pNdkSrq,
  _In_opt_ PVOID                          RequestContext,
           _In_reads_(nSge) const NDK_SGE *pSgl,
  _In_     ULONG                          nSge
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkSrq</i> [in]

<dd>
<p>A pointer to an NDK shared receive queue (SRQ) object
(<a href="https://msdn.microsoft.com/library/windows/hardware/hh439939">NDK_SRQ</a>).</p>
</dd>

### -param <i>RequestContext</i> [in, optional]

<dd>
<p>A context value to be returned in the <b>RequestContext</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439935">NDK_RESULT</a> structure for this request.
</p>
</dd>

### -param <i>pSgl</i> 

<dd>
<p>An array of SGE structures (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439936">NDK_SGE</a>) that represent the buffers to receive incoming data.
</p>
</dd>

### -param <i>nSge</i> [in]

<dd>
<p>The number of SGE structures in the array  that is specified in the <i>pSgl</i>
parameter.</p>
</dd>
</dl>

## -returns
<p>The 
     <i>NdkSrqReceive</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The receive request was posted successfully. A completion entry will be queued to the completion queue (CQ) when the request is completed.
</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p><i>NdkSrqReceive</i> posts a receive request to a shared receive queue (SRQ).</p>

<p><i>NdkSrqReceive</i> posts a receive request to a shared receive queue (SRQ).</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439935">NDK_RESULT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439936">NDK_SGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439939">NDK_SRQ</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_SRQ_RECEIVE callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
