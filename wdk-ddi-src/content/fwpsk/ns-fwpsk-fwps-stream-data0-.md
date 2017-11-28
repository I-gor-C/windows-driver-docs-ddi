---
UID: NS.fwpsk.FWPS_STREAM_DATA0_
title: FWPS_STREAM_DATA0_
author: windows-driver-content
description: The FWPS_STREAM_DATA0 structure describes a portion of a data stream.Note  FWPS_STREAM_DATA0 is a specific version of FWPS_STREAM_DATA.
old-location: netvista\fwps_stream_data0.htm
old-project: netvista
ms.assetid: 7e9daf20-12d6-42dc-99fb-9e9efe5a9900
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FWPS_STREAM_DATA0_, FWPS_STREAM_DATA0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FWPS_STREAM_DATA0
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

# FWPS_STREAM_DATA0_ structure



## -description
<p>The <b>FWPS_STREAM_DATA0</b> structure describes a portion of a data stream.</p>


## -syntax

````
typedef struct FWPS_STREAM_DATA0_ {
  UINT32                   flags;
  FWPS_STREAM_DATA_OFFSET0 dataOffset;
  SIZE_T                   dataLength;
  NET_BUFFER_LIST          *netBufferListChain;
} FWPS_STREAM_DATA0;
````


## -struct-fields
<dl>

### -field <b>flags</b>

<dd>
<p>A variable containing flags that specify the characteristics of the data stream.
     </p>
<p>For inbound data streams, this can be one or more of the following flags:</p>
<p></p>
<dl>

### -field <a id="FWPS_STREAM_FLAG_RECEIVE"></a><a id="fwps_stream_flag_receive"></a>FWPS_STREAM_FLAG_RECEIVE

<dd>
<p>Specifies that the stream is an inbound data stream. This flag is always set for inbound data
       streams.</p>
</dd>

### -field <a id="FWPS_STREAM_FLAG_RECEIVE_EXPEDITED"></a><a id="fwps_stream_flag_receive_expedited"></a>FWPS_STREAM_FLAG_RECEIVE_EXPEDITED

<dd>
<p>Specifies that the inbound data stream contains high-priority out-of-band data.</p>
</dd>

### -field <a id="FWPS_STREAM_FLAG_RECEIVE_DISCONNECT"></a><a id="fwps_stream_flag_receive_disconnect"></a>FWPS_STREAM_FLAG_RECEIVE_DISCONNECT

<dd>
<p>Specifies that the inbound data has arrived with the FIN flag set in the TCP header. This
       indicates that the sender has disconnected the stream.</p>
</dd>

### -field <a id="FWPS_STREAM_FLAG_RECEIVE_ABORT"></a><a id="fwps_stream_flag_receive_abort"></a>FWPS_STREAM_FLAG_RECEIVE_ABORT

<dd>
<p>Specifies that the inbound data has arrived with the RST flag set in the TCP header. This
       indicates that the sender has reset the stream.
       </p>
<div class="alert"><b>Note</b>  This flag is not implemented in Windows Vista.</div>
<div> </div>
</dd>
</dl>
<p>For outbound data streams, this can be one or more of the following flags:</p>
<p></p>
<dl>

### -field <a id="FWPS_STREAM_FLAG_SEND"></a><a id="fwps_stream_flag_send"></a>FWPS_STREAM_FLAG_SEND

<dd>
<p>Specifies that the stream is an outbound data stream. This flag is always set for outbound data
       streams.</p>
</dd>

### -field <a id="FWPS_STREAM_FLAG_SEND_EXPEDITED"></a><a id="fwps_stream_flag_send_expedited"></a>FWPS_STREAM_FLAG_SEND_EXPEDITED

<dd>
<p>Specifies that the outbound data stream contains high-priority out-of-band data.</p>
</dd>

### -field <a id="FWPS_STREAM_FLAG_SEND_NODELAY"></a><a id="fwps_stream_flag_send_nodelay"></a>FWPS_STREAM_FLAG_SEND_NODELAY

<dd>
<p>Specifies that the sending client requests that the outbound data stream is not to be buffered.
       If this flag is set, a callout driver should not hold onto the stream buffer any longer than
       necessary.</p>
</dd>

### -field <a id="FWPS_STREAM_FLAG_SEND_DISCONNECT"></a><a id="fwps_stream_flag_send_disconnect"></a>FWPS_STREAM_FLAG_SEND_DISCONNECT

<dd>
<p>Specifies that the stream is to be disconnected after the data in the outbound data stream has
       been sent. The network stack will set the FIN flag in the TCP header of the last packet that is sent
       out.</p>
</dd>

### -field <a id="FWPS_STREAM_FLAG_SEND_ABORT"></a><a id="fwps_stream_flag_send_abort"></a>FWPS_STREAM_FLAG_SEND_ABORT

<dd>
<p>Specifies that the stream is to be reset after the data in the outbound data stream has been
       sent. The network stack will set the RST flag in the TCP header of the last packet that is sent out.
       Callout drivers must not call the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff551213">FwpsStreamInjectAsync0</a> function
       to inject data into the stream if this flag is set.
       </p>
<div class="alert"><b>Note</b>  This flag is not implemented in Windows Vista.</div>
<div> </div>
</dd>
</dl>
</dd>

### -field <b>dataOffset</b>

<dd>
<p>An 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552420">FWPS_STREAM_DATA_OFFSET0</a> structure
     that specifies the offset into the data stream where the portion of the data stream begins.</p>
</dd>

### -field <b>dataLength</b>

<dd>
<p>The number of bytes in the portion of the data stream.</p>
</dd>

### -field <b>netBufferListChain</b>

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that describes
     the portion of the data stream.</p>
</dd>
</dl>

## -remarks
<p>The filter engine uses the FWPS_STREAM_DATA0 structure to describe the portion of a data stream that a
    callout's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function can process. The 
    <b>dataStream</b> member of the 
    <a href="netvista.fwps_stream_callout_io_packet0">
    FWPS_STREAM_CALLOUT_IO_PACKET0</a> structure points to an FWPS_STREAM_DATA0 structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a>
</dt>
<dt>
<a href="netvista.fwps_stream_callout_io_packet0">
   FWPS_STREAM_CALLOUT_IO_PACKET0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552420">FWPS_STREAM_DATA_OFFSET0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551213">FwpsStreamInjectAsync0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_STREAM_DATA0 structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
