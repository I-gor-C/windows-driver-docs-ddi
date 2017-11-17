---
UID: NF.fwpsk.FwpsPendOperation0
title: FwpsPendOperation0
author: windows-driver-content
description: The FwpsPendOperation0 function is called by a callout to suspend packet processing pending completion of another operation.Note  FwpsPendOperation0 is a specific version of FwpsPendOperation.
old-location: netvista\fwpspendoperation0.htm
ms.assetid: 03423785-83c5-4908-8c06-3be1b226c29e
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsPendOperation0
req.alt-loc: Fwpkclnt.lib,Fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: FwpsPendOperation0
req.iface: 
---

# FwpsPendOperation0 function



## -description
<p>The 
  <b>FwpsPendOperation0</b> function is called by a callout to suspend packet processing pending completion of
  another operation.</p>


## -syntax

````
NTSTATUS NTAPI FwpsPendOperation0(
  _In_  HANDLE completionHandle,
  _Out_ HANDLE *completionContext
);
````


## -parameters
<dl>

### -param <i>completionHandle</i> [in]

<dd>
<p>A completion handle that is required to pend the current filtering operation. This parameter is
     obtained from the 
     <b>completionHandle</b> member of the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552397">FWPS_INCOMING_METADATA_VALUES0</a> structure passed into the callout driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> function.</p>
</dd>

### -param <i>completionContext</i> [out]

<dd>
<p>The handle to the completion context of this pend operation. When the callout is ready to resume
     packet processing, it calls the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551152">FwpsCompleteOperation0</a> function
     with the value of this parameter as the input 
     <i>completionContext</i> parameter.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsPendOperation0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>Packet processing was successfully pended.</p><dl>
<dt><b>STATUS_FWP_CANNOT_PEND</b></dt>
</dl><p>A call was made to 
       <b>FwpsPendOperation0</b> in a reauthorization classify operation. For more information, see Remarks.</p><dl>
<dt><b>STATUS_FWP_NULL_POINTER</b></dt>
</dl><p>One or more of the parameters is invalid.</p><dl>
<dt><b>STATUS_FWP_TCPIP_NOT_READY</b></dt>
</dl><p>The TCP/IP network stack is not ready to allow this operation.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>The callout should retain the 
    <i>completionContext</i> parameter value until it resumes packet processing. When the operation that
    prompted the call to this function has completed, the callout should call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551152">FwpsCompleteOperation0</a> function,
    passing it the 
    <i>completionContext</i> parameter value.</p>

<p>A callout can call this function only to pend a packet that originates from the
    FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_
    <i>Xxx</i>, FWPM_LAYER_ALE_AUTH_LISTEN_
    <i>Xxx</i>, or FWPM_LAYER_ALE_AUTH_CONNECT_
    <i>Xxx</i> <a href="netvista.filtering_layer_identifiers">filtering layers</a>. A callout can
    pend the current processing operation on a packet when the callout must perform processing on one of
    these layers that may take a long interval to complete or that should occur at IRQL = PASSIVE_LEVEL if
    the current IRQL &gt; PASSIVE_LEVEL.</p>

<p>To complete a connection that was previously pended at the FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_
    <i>Xxx</i> layer, the callout driver must reinject the packet that was cloned at that layer as well as
    call the 
    <b>FwpsCompleteOperation0</b> function.</p>

<p>To be able to pend packet processing, the callout driver's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> function should set the 
    <b>actionType</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure to
    FWP_ACTION_BLOCK and the 
    <b>Flags</b> member to FWPS_CLASSIFY_OUT_FLAG_ABSORB.</p>

<p>Pended connections are reauthenticated after the 
    <b>FwpsCompleteOperation0</b> function executes. TCP connections, if allowed, are created by completing
    the handshake operation, but non-TCP connections only create state entries. Any pended packet data
    is flushed from memory when the 
    <b>FwpsPendOperation0</b> function completes, so applications must retransmit those packets after 
    <b>FwpsCompleteOperation0</b> runs. Callouts could buffer such data and reinject the data on their
    behalf.</p>

<p>Only an initial Application Layer Enforcement (ALE) flow authorization can be postponed by calling 
    <b>FwpsPendOperation0</b> and 
    <b>FwpsCompleteOperation0</b>. If an ALE flow is reauthorized, the FWP_CONDITION_FLAG_IS_REAUTHORIZE flag
    is set. A call to 
    <b>FwpsPendOperation0</b> from the FWPM_LAYER_ALE_AUTH_CONNECT_
    <i>Xxx</i> or FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_
    <i>Xxx</i> <a href="netvista.filtering_layer_identifiers">filtering layers</a> will fail if the
    FWP_CONDITION_FLAG_IS_REAUTHORIZE flag is set, and the STATUS_FWP_CANNOT_PEND status code will be
    returned. For more information, see ALE Reauthorization in the Windows SDK.</p>

<p>The callout should retain the 
    <i>completionContext</i> parameter value until it resumes packet processing. When the operation that
    prompted the call to this function has completed, the callout should call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551152">FwpsCompleteOperation0</a> function,
    passing it the 
    <i>completionContext</i> parameter value.</p>

<p>A callout can call this function only to pend a packet that originates from the
    FWPM_LAYER_ALE_RESOURCE_ASSIGNMENT_
    <i>Xxx</i>, FWPM_LAYER_ALE_AUTH_LISTEN_
    <i>Xxx</i>, or FWPM_LAYER_ALE_AUTH_CONNECT_
    <i>Xxx</i> <a href="netvista.filtering_layer_identifiers">filtering layers</a>. A callout can
    pend the current processing operation on a packet when the callout must perform processing on one of
    these layers that may take a long interval to complete or that should occur at IRQL = PASSIVE_LEVEL if
    the current IRQL &gt; PASSIVE_LEVEL.</p>

<p>To complete a connection that was previously pended at the FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_
    <i>Xxx</i> layer, the callout driver must reinject the packet that was cloned at that layer as well as
    call the 
    <b>FwpsCompleteOperation0</b> function.</p>

<p>To be able to pend packet processing, the callout driver's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> function should set the 
    <b>actionType</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure to
    FWP_ACTION_BLOCK and the 
    <b>Flags</b> member to FWPS_CLASSIFY_OUT_FLAG_ABSORB.</p>

<p>Pended connections are reauthenticated after the 
    <b>FwpsCompleteOperation0</b> function executes. TCP connections, if allowed, are created by completing
    the handshake operation, but non-TCP connections only create state entries. Any pended packet data
    is flushed from memory when the 
    <b>FwpsPendOperation0</b> function completes, so applications must retransmit those packets after 
    <b>FwpsCompleteOperation0</b> runs. Callouts could buffer such data and reinject the data on their
    behalf.</p>

<p>Only an initial Application Layer Enforcement (ALE) flow authorization can be postponed by calling 
    <b>FwpsPendOperation0</b> and 
    <b>FwpsCompleteOperation0</b>. If an ALE flow is reauthorized, the FWP_CONDITION_FLAG_IS_REAUTHORIZE flag
    is set. A call to 
    <b>FwpsPendOperation0</b> from the FWPM_LAYER_ALE_AUTH_CONNECT_
    <i>Xxx</i> or FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_
    <i>Xxx</i> <a href="netvista.filtering_layer_identifiers">filtering layers</a> will fail if the
    FWP_CONDITION_FLAG_IS_REAUTHORIZE flag is set, and the STATUS_FWP_CANNOT_PEND status code will be
    returned. For more information, see ALE Reauthorization in the Windows SDK.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fba7eb60-0d19-4bfd-b484-2e615d3e9237">
   FWPS_INCOMING_METADATA_VALUES0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551152">FwpsCompleteOperation0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsPendOperation0 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
