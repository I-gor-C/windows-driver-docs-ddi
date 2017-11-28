---
UID: NC.fwpsk.FWPS_NET_BUFFER_LIST_NOTIFY_FN1
title: FWPS_NET_BUFFER_LIST_NOTIFY_FN1
author: windows-driver-content
description: The filter engine calls the FWPS_NET_BUFFER_LIST_NOTIFY_FN1 callout function to notify the callout driver about events that are associated with packets tagged by the callout.Note   FWPS_NET_BUFFER_LIST_NOTIFY_FN1 is the specific version of FWPS_NET_BUFFER_LIST_NOTIFY_FN used in Windows 8 and later. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. For Windows 7, FWPS_NET_BUFFER_LIST_NOTIFY_FN0 is available.
old-location: netvista\fwps_net_buffer_list_notify_fn1.htm
old-project: netvista
ms.assetid: fe9ab4b2-5692-4b6e-a7fc-11e9ac8280bc
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpmEngineOpen0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsNetBufferListNotifyFN1
req.alt-loc: fwpsk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# FWPS_NET_BUFFER_LIST_NOTIFY_FN1 callback



## -description
<p>The filter engine calls the <i>
  FWPS_NET_BUFFER_LIST_NOTIFY_FN1</i> callout function to notify the callout driver about events that are
  associated with packets tagged by the callout.<div class="alert"><b>Note</b>  <i>
  FWPS_NET_BUFFER_LIST_NOTIFY_FN1</i> is the specific version of <i>FWPS_NET_BUFFER_LIST_NOTIFY_FN</i> used in Windows 8 and later. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information. For Windows 7, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552406">FWPS_NET_BUFFER_LIST_NOTIFY_FN0</a> is available.</div>
<div> </div>
</p>


## -prototype

````
FWPS_NET_BUFFER_LIST_NOTIFY_FN1 FwpsNetBufferListNotifyFN1;

NTSTATUS NTAPI FwpsNetBufferListNotifyFN1(
  _In_        FWPS_NET_BUFFER_LIST_EVENT_TYPE0                                                        eventType,
  _Inout_      _When_(eventType == FWPS_NET_BUFFER_LIST_CONTEXT_REMOVED, _Maybenull_) NET_BUFFER_LIST *netBufferList,
  _Inout_opt_ NET_BUFFER_LIST                                                                         *newNetBufferList,
  _In_        UINT16                                                                                  layerId,
  _In_        UINT64                                                                                  context,
  _In_        UINT64                                                                                  contextTag
)
{ ... }
````


## -parameters
<dl>

### -param <i>eventType</i> [in]

<dd>
<p>A value that indicates the type of notification that the filter engine is sending to the callout.
     This parameter will be set to one of the values of the 
     <a href="netvista.fwps_net_buffer_list_event_type0">
     FWPS_NET_BUFFER_LIST_EVENT_TYPE0</a> enumeration.</p>
</dd>

### -param <i>netBufferList</i> [in, out]

<dd>
<p>A pointer to the buffer list that contains packets that were previously tagged as interesting by
     the callout driver.</p>
</dd>

### -param <i>newNetBufferList</i> [in, out, optional]

<dd>
<p>A pointer to an updated buffer list that contains packets that are interesting to the callout
     driver. The use of this parameter differs depending on the type of event. For events where a change is
     made to the indicated packet, the changed version is passed as this parameter.</p>
</dd>

### -param <i>layerId</i> [in]

<dd>
<p>The layer from which the notification function was called.</p>
</dd>

### -param <i>context</i> [in]

<dd>
<p>The context used to tag the packets of interest. This value is the value assigned to the packet by
     the callout driver and is used to identify the packet.</p>
</dd>

### -param <i>contextTag</i> [in]

<dd>
<p>The context tag used to associate the packets of interest with the context of the callout
     driver.</p>
</dd>
</dl>

## -returns
<p>A callout's 
  <i>
  FWPS_NET_BUFFER_LIST_NOTIFY_FN1</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The callout driver accepts the notification from the filter engine.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>This function is associated with a callout driver by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh439674">FwpsNetBufferListAssociateContext1</a>. A callout driver can use a single notification function to
    handle messages for multiple associated buffer lists by using the context and context tag to
    differentiate between instances.</p>

<p>This function is identical to <a href="https://msdn.microsoft.com/library/windows/hardware/ff552406">FWPS_NET_BUFFER_LIST_NOTIFY_FN0</a>, except that the return type is <b>NTSTATUS</b> instead of <b>VOID</b>.</p>

<p>This function is associated with a callout driver by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh439674">FwpsNetBufferListAssociateContext1</a>. A callout driver can use a single notification function to
    handle messages for multiple associated buffer lists by using the context and context tag to
    differentiate between instances.</p>

<p>This function is identical to <a href="https://msdn.microsoft.com/library/windows/hardware/ff552406">FWPS_NET_BUFFER_LIST_NOTIFY_FN0</a>, except that the return type is <b>NTSTATUS</b> instead of <b>VOID</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.fwps_net_buffer_list_event_type0">
     FWPS_NET_BUFFER_LIST_EVENT_TYPE0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552406">FWPS_NET_BUFFER_LIST_NOTIFY_FN0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439674">FwpsNetBufferListAssociateContext1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543875">Callout Driver Callout Functions</a>
</dt>
<dt>
<a href="NULL">Using Packet Tagging</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_NET_BUFFER_LIST_NOTIFY_FN1 callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
