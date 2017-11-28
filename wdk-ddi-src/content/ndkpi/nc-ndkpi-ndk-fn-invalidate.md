---
UID: NC.ndkpi.NDK_FN_INVALIDATE
title: NDK_FN_INVALIDATE
author: windows-driver-content
description: The NdkInvalidate (NDK_FN_INVALIDATE) function Invalidates a fast-register NDK memory region (MR) or memory window (MW).
old-location: netvista\ndk_fn_invalidate.htm
old-project: netvista
ms.assetid: 79A39FEE-173F-4106-9759-97CF6BE5DA65
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
req.alt-api: NdkInvalidate
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

# NDK_FN_INVALIDATE callback



## -description
<p>The <i>NdkInvalidate</i> (<i>NDK_FN_INVALIDATE</i>) function Invalidates a fast-register NDK memory region (MR) or memory window (MW).</p>


## -prototype

````
NDK_FN_INVALIDATE NdkInvalidate;

NTSTATUS NdkInvalidate(
  _In_     NDK_QP            *pNdkQp,
  _In_opt_ PVOID             RequestContext,
  _In_     NDK_OBJECT_HEADER *pNdkMrOrMw,
  _In_     ULONG             Flags
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkQp</i> [in]

<dd>
<p>A pointer to an NDK queue pair (QP) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439933">NDK_QP</a>).</p>
</dd>

### -param <i>RequestContext</i> [in, optional]

<dd>
<p>A context value to return in the <b>RequestContext</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439935">NDK_RESULT</a> structure for this request.</p>
</dd>

### -param <i>pNdkMrOrMw</i> [in]

<dd>
<p>A pointer to either an memory region (MR) object  (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439922">NDK_MR</a>) or an memory (MW) object  (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439926">NDK_MW</a>) that is specified in an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439928">NDK_OBJECT_HEADER</a> structure. If an MR object is specified, the MR object must have been registered with the <i>NdkFastRegister</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439887">NDK_FN_FAST_REGISTER</a>) function.  The NDK  consumer must never specify an  MR object that was registered with the  <i>NdkRegister</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-register-mr.md">NDK_FN_REGISTER</a>) function in the <i>pNdkMrOrMw</i>  parameter. Access to MR objects registered with the  <i>NdkRegister</i> (<i>NDK_FN_REGISTER</i>)) function can be removed with the NdkDeregisterMr (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439884">NDK_FN_DEREGISTER_MR</a>) function.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A bitwise OR of flags which specifies the operations that are allowed. The following flags are supported:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDK_OP_FLAG_SILENT_SUCCESS"></a><a id="ndk_op_flag_silent_success"></a><dl>

### -param <b>NDK_OP_FLAG_SILENT_SUCCESS</b>


### -param 0x00000001

</dl>
</td>
<td width="60%">
<p>Indicates the successful completion of this request does not generate a completion event in the outbound completion queue. However, requests that fail do generate an event in the completion queue.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDK_OP_FLAG_READ_FENCE"></a><a id="ndk_op_flag_read_fence"></a><dl>

### -param <b>NDK_OP_FLAG_READ_FENCE</b>


### -param 0x00000002

</dl>
</td>
<td width="60%">
<p>Indicates that all prior read requests must be complete before the hardware begins processing this request.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDK_OP_FLAG_DEFER"></a><a id="ndk_op_flag_defer"></a><dl>

### -param <b>NDK_OP_FLAG_DEFER</b>


### -param 0x00000200

</dl>
</td>
<td width="60%">
<p>Indicates to the NDK provider that it may defer indicating the request to hardware for processing. For more information about this flag, see <a href="NULL">NDKPI Deferred Processing Scheme</a>.</p>
<p><b>Note</b>  This flag is supported only in NDKPI 1.2 (Windows Server 2012 R2) and later.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>The  
     <i>NdkInvalidate</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The request was posted successfully. A completion entry will be queued to the CQ when the work request is completed.</p><dl>
<dt><b>STATUS_CONNECTION_INVALID</b></dt>
</dl><p>The QP is not connected. </p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p><i>NdkInvalidate</i> invalidates an NDK fast-register MR or MW.</p>

<p><i>NdkInvalidate</i> invalidates an NDK fast-register MR or MW.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439887">NDK_FN_FAST_REGISTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439884">NDK_FN_DEREGISTER_MR</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-register-mr.md">NDK_FN_REGISTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439922">NDK_MR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439926">NDK_MW</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439928">NDK_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439933">NDK_QP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439935">NDK_RESULT</a>
</dt>
<dt>
<a href="NULL">NDKPI Completion Handling Requirements</a>
</dt>
<dt>
<a href="NULL">NDKPI Deferred Processing Scheme</a>
</dt>
<dt>
<a href="NULL">NDKPI Work Request Posting Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_INVALIDATE callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
