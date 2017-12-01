---
UID: NC.ndkpi.NDK_FN_SEND
title: NDK_FN_SEND
author: windows-driver-content
description: The NdkSend (NDK_FN_SEND) function posts a send request on an NDK queue pair (QP).
old-location: netvista\ndk_fn_send.htm
old-project: netvista
ms.assetid: 6EDF95F1-AE00-4931-9B18-E316D56D57AF
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
req.alt-api: NdkSend
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

# NDK_FN_SEND callback



## -description
<p>The <i>NdkSend</i> (<i>NDK_FN_SEND</i>) function posts a send request on an NDK queue pair (QP).</p>


## -prototype

````
NDK_FN_SEND NdkSend;

NTSTATUS NdkSend(
  _In_     NDK_QP                         *pNdkQp,
  _In_opt_ PVOID                          RequestContext,
           _In_reads_(nSge) CONST NDK_SGE *pSgl,
  _In_     ULONG                          nSge,
  _In_     ULONG                          Flags
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
<p>A context value to be returned in the <b>RequestContext</b> member of the <a href="..\ndkpi\ns-ndkpi--ndk-result.md">NDK_RESULT</a> structure for this request.
</p>
</dd>

### -param <i>pSgl</i> 

<dd>
<p>An array of SGE structures (<a href="..\ndkpi\ns-ndkpi--ndk-sge.md">NDK_SGE</a>)  that represent the buffers holding the data to send.</p>
</dd>

### -param <i>nSge</i> [in]

<dd>
<p>The number of SGE structures in the array  that is specified in the <i>pSgl</i>
parameter.</p>
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
<td width="40%"><a id="NDK_OP_FLAG_SEND_AND_SOLICIT_EVENT"></a><a id="ndk_op_flag_send_and_solicit_event"></a><dl>

### -param <b>NDK_OP_FLAG_SEND_AND_SOLICIT_EVENT</b>


### -param 0x00000004

</dl>
</td>
<td width="60%">
<p>Indicates that the completion queue for the peer generates a notification. For more information about <b>NDK_OP_FLAG_SEND_AND_SOLICIT_EVENT</b>, see the Remarks section.</p>
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
</dl>

## -returns
<p>The 
     <i>NdkSend</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The send request was posted successfully. A completion entry will be queued to the completion queue (CQ) when the work request is completed.
</p><dl>
<dt><b>STATUS_CONNECTION_INVALID</b></dt>
</dl><p>The queue pair (QP) is not connected.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p><i>NdkSend</i> posts a send request on a queue pair (QP).</p>

<p>You can use the <b>NDK_OP_FLAG_SEND_AND_SOLICIT_EVENT</b> flag if you issue multiple, related send requests. Set this flag on the last request in the group of related send requests.</p>

<p>An NDK consumer can use this flag when issuing multiple, related send requests. The NDK consumer sets this flag only on the last, related send request. The peer will receive all the send requests as normal. However, when the peer receives the last send request (the request with the <b>NDK_OP_FLAG_SEND_AND_SOLICIT_EVENT</b> flag set), the completion queue for the peer generates a notification. The notification is generated after the receive request completes. This flag has no meaning to the receiver (peer) unless the receiver has previously called the <i>NdkArmCq</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-arm-cq.md">NDK_FN_ARM_CQ</a>) function with the notification type set to <b>NDK_CQ_NOTIFY_SOLICITED</b>. </p>

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
<a href="..\ndkpi\ns-ndkpi--ndk-qp.md">NDK_QP</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-result.md">NDK_RESULT</a>
</dt>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-sge.md">NDK_SGE</a>
</dt>
<dt>
<a href="..\ndkpi\nc-ndkpi-ndk-fn-arm-cq.md">NDK_FN_ARM_CQ</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_SEND callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
