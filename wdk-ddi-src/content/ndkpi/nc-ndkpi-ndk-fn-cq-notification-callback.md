---
UID: NC.ndkpi.NDK_FN_CQ_NOTIFICATION_CALLBACK
title: NDK_FN_CQ_NOTIFICATION_CALLBACK
author: windows-driver-content
description: The NdkCqNotificationCallback (NDK_FN_CQ_NOTIFICATION_CALLBACK) function is called by the NDK provider to notify the consumer about a completion queue (CQ) event.
old-location: netvista\ndk_fn_cq_notification_callback.htm
old-project: netvista
ms.assetid: 88035020-9585-41EC-9C63-29DDED779C39
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: NdkCqNotificationCallback
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

# NDK_FN_CQ_NOTIFICATION_CALLBACK callback



## -description
<p>The <i>NdkCqNotificationCallback</i> (<i>NDK_FN_CQ_NOTIFICATION_CALLBACK</i>) function is called by the NDK provider to notify the consumer about  a completion queue (CQ) event.</p>


## -prototype

````
NDK_FN_CQ_NOTIFICATION_CALLBACK NdkCqNotificationCallback;

VOID NdkCqNotificationCallback(
  _In_opt_ PVOID    CqNotificationContext,
  _In_     NTSTATUS CqStatus
)
{ ... }
````


## -parameters
<dl>

### -param CqNotificationContext [in, optional]

<dd>
<p>A context area that was specified in the <i>CqNotificationContext</i> parameter of the <i>NdkCreateCq</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-cq.md">NDK_FN_CREATE_CQ</a>) function when the completion queue (CQ)  object was created.</p>
</dd>

### -param CqStatus [in]

<dd>
<p>Indicates the CQ error status. The following status codes are defined:</p>
<p></p>
<table>
<tr>
<th>Term</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<p><a id="STATUS_SUCCESS"></a><a id="status_success"></a>STATUS_SUCCESS</p>
</td>
<td width="60%">
<p>Indicates the CQ is operating normally.</p>
</td>
</tr>
<tr>
<td width="40%">
<p><a id="STATUS_BUFFER_OVERFLOW"></a><a id="status_buffer_overflow"></a>STATUS_BUFFER_OVERFLOW</p>
</td>
<td width="60%">
<p>Indicates more completions than that maximum that the CQ can hold were attempted to be queued on the CQ and the CQ is  unusable. All of the associated queue pairs (QPs) are also unusable. No future completions will be reported. A STATUS_BUFFER_OVERFLOW error usually indicates a programming error.</p>
</td>
</tr>
<tr>
<td width="40%">
<p><a id="STATUS_INTERNAL_ERROR"></a><a id="status_internal_error"></a>STATUS_INTERNAL_ERROR</p>
</td>
<td width="60%">
<p>Indicates a  fatal error occurred on the CQ and the CQ is  unusable. All of the associated queue pairs (QPs) are also unusable.  No future completions will be reported. A STATUS_INTERNAL_ERROR error usually indicates a hardware error.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>An NDK provider calls <i>NdkCqNotificationCallback</i> to notify the consumer about  a completion queue (CQ) event.</p>

<p>The NDK consumer specified the <i>NdkCqNotificationCallback</i> function  in the <i>CqNotificationContext</i> parameter of the <i>NdkCreateCq</i> (<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-cq.md">NDK_FN_CREATE_CQ</a>) function when the completion queue (CQ) object was created.</p>

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
<a href="..\ndkpi\nc-ndkpi-ndk-fn-create-cq.md">NDK_FN_CREATE_CQ</a>
</dt>
<dt>
<a href="netvista.ndkpi_completion_handling_requirements">NDKPI Completion Handling Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_CQ_NOTIFICATION_CALLBACK callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
