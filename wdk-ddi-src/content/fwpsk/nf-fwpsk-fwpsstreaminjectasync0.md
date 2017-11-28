---
UID: NF.fwpsk.FwpsStreamInjectAsync0
title: FwpsStreamInjectAsync0
author: windows-driver-content
description: The FwpsStreamInjectAsync0 function injects TCP data segments into a TCP data stream.Note  FwpsStreamInjectAsync0 is a specific version of FwpsStreamInjectAsync.
old-location: netvista\fwpsstreaminjectasync0.htm
old-project: netvista
ms.assetid: d72c3067-21df-40ee-a898-100fcdc5eaca
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpsStreamInjectAsync0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsStreamInjectAsync0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
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
req.iface: 
---

# FwpsStreamInjectAsync0 function



## -description
<p>The 
  <b>FwpsStreamInjectAsync0</b> function injects TCP data segments into a TCP data stream.</p>


## -syntax

````
NTSTATUS NTAPI FwpsStreamInjectAsync0(
  _In_     HANDLE                injectionHandle,
  _In_opt_ HANDLE                injectionContext,
  _In_     UINT32                flags,
  _In_     UINT64                flowId,
  _In_     UINT32                calloutId,
  _In_     UINT16                layerId,
  _In_     UINT32                streamFlags,
  _Inout_  NET_BUFFER_LIST       *netBufferList,
  _In_     SIZE_T                dataLength,
  _In_     FWPS_INJECT_COMPLETE0 completionFn,
  _In_opt_ HANDLE                completionContext
);
````


## -parameters
<dl>

### -param <i>injectionHandle</i> [in]

<dd>
<p>An injection handle that was previously created by a call to the 
     <a href="..\fwpsk\nf-fwpsk-fwpsinjectionhandlecreate0.md">
     FwpsInjectionHandleCreate0</a> function.</p>
</dd>

### -param <i>injectionContext</i> [in, optional]

<dd>
<p>An optional handle to the injection context.</p>
</dd>

### -param <i>flags</i> [in]

<dd>
<p>Reserved. Callout drivers should set this parameter to zero.</p>
</dd>

### -param <i>flowId</i> [in]

<dd>
<p>A run-time identifier that specifies the data flow into which to inject the data. The run-time
     identifier for a data flow is provided to a callout driver through the FWPS_METADATA_FIELD_FLOW_HANDLE
     metadata value that the filter engine provided to the callout driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function.</p>
</dd>

### -param <i>calloutId</i> [in]

<dd>
<p>The run-time identifier for the callout in the filter engine. This identifier was returned when
     the callout driver called either the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a> or 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a> functions to
     register the callout with the filter engine.</p>
</dd>

### -param <i>layerId</i> [in]

<dd>
<p>The run-time identifier for the filtering layer at which the data stream is being processed. This
     value must be either FWPS_LAYER_STREAM_V4 or FWPS_LAYER_STREAM_V6. The run-time identifier for the layer
     at which the data stream is being processed is provided to a callout in the 
     <b>layerId</b> member of the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552401">FWPS_INCOMING_VALUES0</a> structure that
     the filter engine passed to the callout driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function.</p>
</dd>

### -param <i>streamFlags</i> [in]

<dd>
<p>Flags that specify characteristics of the data stream into which the data is to be injected.
     </p>
<p>When injecting data into an inbound data stream, a callout driver specifies one or more of the
     following flags:</p>
<p></p>
<dl>

### -param <a id="FWPS_STREAM_FLAG_RECEIVE"></a><a id="fwps_stream_flag_receive"></a><b>FWPS_STREAM_FLAG_RECEIVE</b>

<dd>
<p>Specifies that the data is to be injected into the inbound data stream. This flag is required
       when injecting data into an inbound data stream.</p>
</dd>

### -param <a id="FWPS_STREAM_FLAG_RECEIVE_DISCONNECT"></a><a id="fwps_stream_flag_receive_disconnect"></a><b>FWPS_STREAM_FLAG_RECEIVE_DISCONNECT</b>

<dd>
<p>Specifies that the FIN flag is to be set in the TCP header for the data being injected into the
       inbound data stream.</p>
<div class="alert"><b>Note</b>  If this flag is set, the <b>FWPS_STREAM_FLAG_RECEIVE</b> flag must also be set, or else <b>STATUS_FWP_INVALID_PARAMETER</b> will be returned.</div>
<div> </div>
</dd>

### -param <a id="FWPS_STREAM_FLAG_RECEIVE_EXPEDITED"></a><a id="fwps_stream_flag_receive_expedited"></a><b>FWPS_STREAM_FLAG_RECEIVE_EXPEDITED</b>

<dd>
<p>Specifies that the data being injected into the inbound data stream is high-priority,
       out-of-band data.</p>
</dd>

### -param <a id="FWPS_STREAM_FLAG_RECEIVE_PUSH"></a><a id="fwps_stream_flag_receive_push"></a><b>FWPS_STREAM_FLAG_RECEIVE_PUSH</b>

<dd>
<p>Specifies that the inbound data has arrived with the PUSH flag set in the TCP header, which
       indicates that the sender requests immediate data transfer. Unwanted delays in data transfer can occur
       if this flag is not set. This flag is available starting with Windows Vista with SP1.</p>
</dd>
</dl>
<p>When injecting data into an outbound data stream, a callout driver specifies one or more of the
     following flags:</p>
<p></p>
<dl>

### -param <a id="FWPS_STREAM_FLAG_SEND"></a><a id="fwps_stream_flag_send"></a><b>FWPS_STREAM_FLAG_SEND</b>

<dd>
<p>Specifies that the data is to be injected into the outbound data stream. This flag is required
       when injecting data into an outbound data stream.</p>
</dd>

### -param <a id="FWPS_STREAM_FLAG_SEND_EXPEDITED"></a><a id="fwps_stream_flag_send_expedited"></a><b>FWPS_STREAM_FLAG_SEND_EXPEDITED</b>

<dd>
<p>Specifies that the data being injected into the outbound data stream is high-priority,
       out-of-band data.</p>
</dd>

### -param <a id="FWPS_STREAM_FLAG_SEND_NODELAY"></a><a id="fwps_stream_flag_send_nodelay"></a><b>FWPS_STREAM_FLAG_SEND_NODELAY</b>

<dd>
<p>Specifies that the callout driver requests that there is no buffering of the data being injected
       into the outbound data stream.</p>
</dd>

### -param <a id="FWPS_STREAM_FLAG_SEND_DISCONNECT"></a><a id="fwps_stream_flag_send_disconnect"></a><b>FWPS_STREAM_FLAG_SEND_DISCONNECT</b>

<dd>
<p>Specifies that the stream is to be disconnected after the data being injected into the outbound
       data stream has been sent. The network stack will set the FIN flag in the TCP header of the last
       packet that is sent out.</p>
<div class="alert"><b>Note</b>  If this flag is set, the <b>FWPS_STREAM_FLAG_SEND</b> flag must also be set, or else <b>STATUS_FWP_INVALID_PARAMETER</b> will be returned.</div>
<div> </div>
</dd>
</dl>
</dd>

### -param <i>netBufferList</i> [in, out]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that describes
     the data that is being injected into the data stream. A callout driver allocates a <b>NET_BUFFER_LIST</b>
     structure to use for injecting data into a data stream by calling the 
     <a href="..\fwpsk\nf-fwpsk-fwpsallocateclonenetbufferlist0.md">
     FwpsAllocateCloneNetBufferList0</a>, 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551135">FwpsAllocateNetBufferAndNetBufferList0</a>, or 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551149">FwpsCloneStreamData0</a> functions. The
     <b>NET_BUFFER_LIST</b> structure can describe a chain of network buffer lists. If the 
     <i>streamFlags</i> parameter is <b>FWPS_STREAM_FLAG_RECEIVE_DISCONNECT</b> or <b>FWPS_STREAM_FLAG_SEND_DISCONNECT</b>, 
     <i>netBufferList</i> can be <b>NULL</b>.</p>
</dd>

### -param <i>dataLength</i> [in]

<dd>
<p>The number of bytes of data being injected into the data stream.</p>
</dd>

### -param <i>completionFn</i> [in]

<dd>
<p>A pointer to a 
     <a href="..\fwpsk\nc-fwpsk-fwps-inject-complete0.md">completionFn</a> callout function provided by
     the callout driver. The filter engine calls this function after the packet data, described by the 
     <i>netBufferList</i> parameter, has been injected into the network stack. </p>
<p>If the 
     <i>netBufferList</i> parameter describes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> chain, 
     <i>completionFn</i> will be called once for each <b>NET_BUFFER_LIST</b> in the chain.</p>
<p>If the 
     <i>netBufferList</i> parameter is <b>NULL</b>  and the 
     <i>streamFlags</i> parameter has either <b>FWPS_STREAM_FLAG_RECEIVE_DISCONNECT</b> or <b>FWPS_STREAM_FLAG_SEND_DISCONNECT</b> set, the <a href="..\fwpsk\nc-fwpsk-fwps-inject-complete0.md">completionFn</a> function will not be called.</p>
<p>This parameter is required and cannot be <b>NULL</b>. If it is <b>NULL</b>, <b>STATUS_FWP_NULL_POINTER</b> will be returned.</p>
</dd>

### -param <i>completionContext</i> [in, optional]

<dd>
<p>A pointer to a callout driver–provided context that is passed to the callout function pointed to
     by the 
     <i>completionFn</i> parameter. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsStreamInjectAsync0</b> function an NTSTATUS code such as one of the following.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The injection into the data stream was initiated successfully. The filter engine will call the
       completion function that was specified when the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure was allocated
       after the filter engine has completed injecting the data into the data stream.</p><dl>
<dt><b>STATUS_FWP_TCPIP_NOT_READY</b></dt>
</dl><p>The TCP/IP network stack is not ready to accept injection of stream data.</p><dl>
<dt><b>STATUS_FWP_INJECT_HANDLE_CLOSING</b></dt>
</dl><p>The injection handle is being closed.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A callout driver calls the 
    <b>FwpsStreamInjectAsync0</b> function from within a callout's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function to inject new
    or cloned data into the data stream that is currently being processed. A callout driver can call the
    FwpsStreamInjectAsync0 function only if it is processing a data flow at the stream layer.</p>

<p>A callout driver can also call the 
    <b>FwpsStreamInjectAsync0</b> function from outside of a callout's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function to inject data into a data stream that is currently deferred. A data
    stream is deferred when a callout's 
    <i>classifyFn</i> callout function sets the 
    <b>streamAction</b> member of the 
    <a href="netvista.fwps_stream_callout_io_packet0">
    FWPS_STREAM_CALLOUT_IO_PACKET0</a> structure to FWPS_STREAM_ACTION_DEFER.</p>

<p>In addition, a callout driver can call the 
    <b>FwpsStreamInjectAsync0</b> function from outside of a callout's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function to inject data into a data stream after a FIN indication has been
    pended.</p>

<p>Alternately, a callout driver can call the 
    <b>FwpsStreamInjectAsync0</b> function from an arbitrary thread context outside a callout's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function if the callout driver clones and blocks all data indicated for
    out-of-band processing. A callout driver that redirects all indicated data to user mode for processing
    can call the 
    <b>FwpsStreamInjectAsync0</b> function in this way.</p>

<p>A callout can pend a data segment by first cloning it with a call to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551149">FwpsCloneStreamData0</a> function,
    followed by blocking the data segment by setting FWP_ACTION_BLOCK in the 
    <b>actionType</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure.</p>

<p>Injected stream data will not be reindicated to the callout, but it will be made available to stream
    callouts from lower-weight sublayers.</p>

<p>If the return value is not STATUS_SUCCESS, the completion function will not be called. In this case,
    the network buffer list pointed to by 
    <i>metBufferList</i> must be freed by a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551172">FwpsFreeNetBufferList0</a> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551170">FwpsFreeCloneNetBufferList0</a>.</p>

<p>A callout driver calls the 
    <b>FwpsStreamInjectAsync0</b> function from within a callout's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function to inject new
    or cloned data into the data stream that is currently being processed. A callout driver can call the
    FwpsStreamInjectAsync0 function only if it is processing a data flow at the stream layer.</p>

<p>A callout driver can also call the 
    <b>FwpsStreamInjectAsync0</b> function from outside of a callout's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function to inject data into a data stream that is currently deferred. A data
    stream is deferred when a callout's 
    <i>classifyFn</i> callout function sets the 
    <b>streamAction</b> member of the 
    <a href="netvista.fwps_stream_callout_io_packet0">
    FWPS_STREAM_CALLOUT_IO_PACKET0</a> structure to FWPS_STREAM_ACTION_DEFER.</p>

<p>In addition, a callout driver can call the 
    <b>FwpsStreamInjectAsync0</b> function from outside of a callout's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function to inject data into a data stream after a FIN indication has been
    pended.</p>

<p>Alternately, a callout driver can call the 
    <b>FwpsStreamInjectAsync0</b> function from an arbitrary thread context outside a callout's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function if the callout driver clones and blocks all data indicated for
    out-of-band processing. A callout driver that redirects all indicated data to user mode for processing
    can call the 
    <b>FwpsStreamInjectAsync0</b> function in this way.</p>

<p>A callout can pend a data segment by first cloning it with a call to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551149">FwpsCloneStreamData0</a> function,
    followed by blocking the data segment by setting FWP_ACTION_BLOCK in the 
    <b>actionType</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure.</p>

<p>Injected stream data will not be reindicated to the callout, but it will be made available to stream
    callouts from lower-weight sublayers.</p>

<p>If the return value is not STATUS_SUCCESS, the completion function will not be called. In this case,
    the network buffer list pointed to by 
    <i>metBufferList</i> must be freed by a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551172">FwpsFreeNetBufferList0</a> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551170">FwpsFreeCloneNetBufferList0</a>.</p>

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
<a href="..\fwpsk\nc-fwpsk-fwps-inject-complete0.md">completionFn</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsallocateclonenetbufferlist0.md">
   FwpsAllocateCloneNetBufferList0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsallocatenetbufferandnetbufferlist0.md">
   FwpsAllocateNetBufferAndNetBufferList0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551149">FwpsCloneStreamData0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551180">FwpsInjectionHandleCreate0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551181">FwpsInjectionHandleDestroy0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552401">FWPS_INCOMING_VALUES0</a>
</dt>
<dt>
<a href="netvista.fwps_stream_callout_io_packet0">
   FWPS_STREAM_CALLOUT_IO_PACKET0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsStreamInjectAsync0 function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
