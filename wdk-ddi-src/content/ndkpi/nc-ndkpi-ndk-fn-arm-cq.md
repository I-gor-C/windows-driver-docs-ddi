---
UID: NC.ndkpi.NDK_FN_ARM_CQ
title: NDK_FN_ARM_CQ
author: windows-driver-content
description: The NdkArmCq (NDK_FN_ARM_CQ) function arms an NDK completion queue (CQ) notification.
old-location: netvista\ndk_fn_arm_cq.htm
old-project: netvista
ms.assetid: 8204EC7B-8F90-4F34-BFFB-9F1574AF69BC
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
req.alt-api: NdkArmCq
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

# NDK_FN_ARM_CQ callback



## -description
<p>The <i>NdkArmCq</i> (<i>NDK_FN_ARM_CQ</i>) function arms an NDK completion queue (CQ) notification. </p>


## -prototype

````
NDK_FN_ARM_CQ NdkArmCq;

VOID NdkArmCq(
  _In_ NDK_CQ *pNdkCq,
  _In_ ULONG  Type
)
{ ... }
````


## -parameters
<dl>

### -param <i>pNdkCq</i> [in]

<dd>
<p>A pointer to an NDK completion queue object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439854">NDK_CQ</a>).
</p>
</dd>

### -param <i>Type</i> [in]

<dd>
<p>The type of notification to arm. The following notification types are defined:</p>
<p></p>
<table>
<tr>
<th>Term</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<p><a id="NDK_CQ_NOTIFY_ERRORS"></a><a id="ndk_cq_notify_errors"></a>NDK_CQ_NOTIFY_ERRORS</p>
</td>
<td width="60%">
<p>Notify if there are any completion queue errors such as a completion queue overrun or catastrophic failure.</p>
</td>
</tr>
<tr>
<td width="40%">
<p><a id="NDK_CQ_NOTIFY_ANY"></a><a id="ndk_cq_notify_any"></a>NDK_CQ_NOTIFY_ANY</p>
</td>
<td width="60%">
<p>Notify of the next successful completion in the completion queue.</p>
</td>
</tr>
<tr>
<td width="40%">
<p><a id="NDK_CQ_NOTIFY_SOLICITED"></a><a id="ndk_cq_notify_solicited"></a>NDK_CQ_NOTIFY_SOLICITED</p>
</td>
<td width="60%">
<p>Notify when the completion queue receives a send request that includes the ND_OP_FLAG_SEND_AND_SOLICIT_EVENT flag.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>After the NDK consumer arms a completion queue (CQ) notification, the provider calls the <i>NdkCqNotificationCallback</i> callback function (the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439870">NDK_FN_CQ_NOTIFICATION_CALLBACK</a> routine that the consumer  specified when the CQ was created with the <i>NdkCreateCq</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439873">NDK_FN_CREATE_CQ</a>) function) when the specified type of notification is due.</p>

<p>If the CQ is closed while a call to <i>NdkCqNotificationCallback</i> is in-progress, the close request will remain pending until <i>NdkCqNotificationCallback</i> returns control  to the provider. After the close request is completed, the provider will not call  <i>NdkCqNotificationCallback</i>.</p>

<p>After the NDK consumer arms a completion queue (CQ) notification, the provider calls the <i>NdkCqNotificationCallback</i> callback function (the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439870">NDK_FN_CQ_NOTIFICATION_CALLBACK</a> routine that the consumer  specified when the CQ was created with the <i>NdkCreateCq</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439873">NDK_FN_CREATE_CQ</a>) function) when the specified type of notification is due.</p>

<p>If the CQ is closed while a call to <i>NdkCqNotificationCallback</i> is in-progress, the close request will remain pending until <i>NdkCqNotificationCallback</i> returns control  to the provider. After the close request is completed, the provider will not call  <i>NdkCqNotificationCallback</i>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439854">NDK_CQ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439855">NDK_CQ_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439870">NDK_FN_CQ_NOTIFICATION_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439873">NDK_FN_CREATE_CQ</a>
</dt>
<dt>
<a href="NULL">NDKPI Completion Handling Requirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_FN_ARM_CQ callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
