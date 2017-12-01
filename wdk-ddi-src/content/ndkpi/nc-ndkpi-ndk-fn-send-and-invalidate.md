---
UID: NC.ndkpi.NDK_FN_SEND_AND_INVALIDATE
title: NDK_FN_SEND_AND_INVALIDATE
author: windows-driver-content
description: The NdkSendAndInvalidate (NDK_FN_SEND_AND_INVALIDATE) function posts a send request on an NDK queue pair (QP) and supplies a token to be invalidated at the remote peer upon receive completion.
old-location: netvista\ndk_fn_send_and_invalidate.htm
old-project: netvista
ms.assetid: 7E344DFA-159A-4084-905A-0A0F9F102051
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: NDK_FN_SEND_AND_INVALIDATE
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

# NDK_FN_SEND_AND_INVALIDATE callback



## -description
<p>The <i>NdkSendAndInvalidate</i> (<i>NDK_FN_SEND_AND_INVALIDATE</i>) function posts a send request on an NDK queue pair (QP) and supplies a token to be invalidated at the remote peer upon receive completion.</p>


## -prototype

````
NDK_FN_SEND_AND_INVALIDATE NDK_FN_SEND_AND_INVALIDATE;

NTSTATUS NDK_FN_SEND_AND_INVALIDATE(
  _In_     NDK_QP                         *pNdkQp,
  _In_opt_ PVOID                          RequestContext,
           _In_reads_(nSge) CONST NDK_SGE *pSgl,
  _In_     ULONG                          nSge,
  _In_     ULONG                          Flags,
  _In_     UINT32                         RemoteToken
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkQp</i> [in]

<dd>
<p>A pointer to an NDK queue pair (QP) object
(<a href="..\ndkpi\ns-ndkpi--ndk-qp.md">NDK_QP</a>).</p>
</dd>

### -param <i>RequestContext</i> [in, optional]

<dd>
<p>A context value to be returned in the <b>RequestContext</b> member of the <a href="..\ndkpi\ns-ndkpi--ndk-result-ex.md">NDK_RESULT_EX</a> structure for this request.
</p>
</dd>

### -param <i>pSgl</i> 

<dd>
<p>An array of SGE (<a href="..\ndkpi\ns-ndkpi--ndk-sge.md">NDK_SGE</a>)  structures that represent the buffers holding the data to send.</p>
</dd>

### -param <i>nSge</i> [in]

<dd>
<p>The number of SGE structures in the array  that is specified in the <i>pSgl</i>
parameter.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A bitwise OR of flags that specify the operations that are allowed. The following flags are supported:</p>
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
<p>If this request succeeds, it does not generate a completion event in the outbound completion queue. However, if it fails, it does generate a completion event in the outbound completion queue.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDK_OP_FLAG_READ_FENCE"></a><a id="ndk_op_flag_read_fence"></a><dl>

### -param <b>NDK_OP_FLAG_READ_FENCE</b>


### -param 0x00000002

</dl>
</td>
<td width="60%">
<p>All prior read requests must be complete before the hardware begins processing this request.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDK_OP_FLAG_SEND_AND_SOLICIT_EVENT"></a><a id="ndk_op_flag_send_and_solicit_event"></a><dl>

### -param <b>NDK_OP_FLAG_SEND_AND_SOLICIT_EVENT</b>


### -param 0x00000004

</dl>
</td>
<td width="60%">
<p>The completion queue for the peer generates a notification. For more information about <b>NDK_OP_FLAG_SEND_AND_SOLICIT_EVENT</b>, see the Remarks section.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDK_OP_FLAG_INLINE"></a><a id="ndk_op_flag_inline"></a><dl>

### -param <b>NDK_OP_FLAG_INLINE</b>


### -param 0x00000040

</dl>
</td>
<td width="60%">
<p>Indicates that the memory referenced by the SGEs should be transferred inline.  Also, the <b>MemoryRegionToken</b> value in the <a href="..\ndkpi\ns-ndkpi--ndk-sge.md">NDK_SGE</a> entries might be invalid. Inline requests do not need to limit the number of entries in the SGE list to the <b>MaxInitiatorRequestSge</b>  value that is specified when the queue pair was created. The amount of memory transferred inline must be within the inline data limits of the queue pair.</p>
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

### -param <i>RemoteToken</i> [in]

<dd>
<p>The remote token to be invalidated at the peer upon receive completion. The NDK provider at the receiving peer must abort the connection, as specified by lower layer transport rules, if an invalid token was specified by the sending peer.</p>
</dd>
</dl>

## -returns
<p>The 
     <i>NdkSendAndInvalidate</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The request was posted successfully. A completion entry will be queued to the completion queue (CQ) when the work request is completed.
</p><dl>
<dt><b>STATUS_CONNECTION_INVALID</b></dt>
</dl><p>The queue pair (QP) is not connected.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p>You can use the <b>NDK_OP_FLAG_SEND_AND_SOLICIT_EVENT</b> flag if you issue multiple, related send requests. Set this flag on the last request in the group.</p>

<p>An NDK consumer can use this flag when issuing multiple, related send requests. The NDK consumer sets this flag only on the last, related send request. The peer will receive all the send requests as normal. However, when the peer receives the last send request (the request with the <b>NDK_OP_FLAG_SEND_AND_SOLICIT_EVENT</b> flag set), the completion queue for the peer generates a notification. The notification is generated after the receive request completes. This flag has no meaning to the receiver (peer) unless the receiver has previously called the <i>NdkArmCq</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-arm-cq.md">NDK_FN_ARM_CQ</a>) function with the notification type set to <b>NDK_CQ_NOTIFY_SOLICITED</b>. </p>

<p>The NDK consumer should ensure that the <i>NdkSendAndInvalidate</i> function is not called if the receiving peer does not support remote invalidation. The consumer must either negotiate this capability using an out-of-band mechanism or not use this function. If the consumer violates this requirement, the provider's behavior is undefined.</p>

<p>Any <a href="..\ndkpi\ns-ndkpi--ndk-result-ex.md">NDK_RESULT_EX</a> structure that is added to a completion queue as a result of a call to this function must specify <b>NdkOperationTypeSend</b> for the <b>Type</b> member. Note that you do not need to specify a value for the <b>TypeSpecificCompletionOutput</b> member of the <b>NDK_RESULT_EX</b> structure.</p>

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
<a href="..\ndkpi\nc-ndkpi-ndk-fn-arm-cq.md">NDK_FN_ARM_CQ</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-result-ex.md">NDK_RESULT_EX</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-qp.md">NDK_QP</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-sge.md">NDK_SGE</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_SEND_AND_INVALIDATE callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
