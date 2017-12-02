---
UID: NC.ndkpi.NDK_FN_GET_CQ_RESULTS_EX
title: NDK_FN_GET_CQ_RESULTS_EX
author: windows-driver-content
description: The NdkGetCqResultsEx (NDK_FN_GET_CQ_RESULTS_EX) function removes completions from an NDK completion queue (CQ) object.
old-location: netvista\ndk_fn_get_cq_results_ex.htm
old-project: netvista
ms.assetid: DC2782AB-BDFA-45C2-BC2E-ED4B946597D4
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_WWAN_VISIBLE_PROVIDERS, NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.40 and later.
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDK_FN_GET_CQ_RESULTS_EX
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

# NDK_FN_GET_CQ_RESULTS_EX callback



## -description
<p>The <i>NdkGetCqResultsEx</i> (<i>NDK_FN_GET_CQ_RESULTS_EX</i>) function removes completions from an NDK completion queue (CQ) object. This function is identical to the <i>NdkGetCqResults</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-get-cq-results.md">NDK_FN_GET_CQ_RESULTS</a>) function, except that it retrieves an array of <a href="..\ndkpi\ns-ndkpi--ndk-result-ex.md">NDK_RESULT_EX</a> structures instead of an array of <a href="..\ndkpi\ns-ndkpi--ndk-result.md">NDK_RESULT</a> structures.</p>


## -prototype

````
NDK_FN_GET_CQ_RESULTS_EX NDK_FN_GET_CQ_RESULTS_EX;

ULONG NDK_FN_GET_CQ_RESULTS_EX(
  _In_ NDK_CQ                                          *pNdkCq,
       _Out_writes_to_(nResults, return) NDK_RESULT_EX Results[],
  _In_ ULONG                                           nResults
)
{ ... }
````


## -parameters
<dl>

### -param pNdkCq [in]

<dd>
<p>A pointer to an NDK completion queue (CQ) object  (<a href="..\ndkpi\ns-ndkpi--ndk-cq.md">NDK_CQ</a>).</p>
</dd>

### -param Results 

<dd>
<p>An array of <a href="..\ndkpi\ns-ndkpi--ndk-result-ex.md">NDK_RESULT_EX</a> structures that will be filled with completion results that were removed from the CQ.</p>
</dd>

### -param nResults [in]

<dd>
<p>The size, in elements, of the <i>Results</i> array. That is, the maximum number of completions to remove from the CQ.</p>
</dd>
</dl>

## -returns
<p>The <i>NDK_FN_GET_CQ_RESULTS_EX</i> function returns the number of completions that were removed from the CQ. </p>

<p>Zero means there were no completions in the CQ.</p>

## -remarks


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
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.40 and later.</p>
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
<a href="..\ndkpi\ns-ndkpi--ndk-cq.md">NDK_CQ</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-result.md">NDK_RESULT</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-result-ex.md">NDK_RESULT_EX</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-get-cq-results.md">NDK_FN_GET_CQ_RESULTS</a>
</dt>
<dt>
<a href="netvista.ndkpi_completion_handling_requirements">NDKPI Completion Handling Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_GET_CQ_RESULTS_EX callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
