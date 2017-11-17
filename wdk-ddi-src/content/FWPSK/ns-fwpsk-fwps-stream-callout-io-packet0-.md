---
UID: NS.fwpsk.FWPS_STREAM_CALLOUT_IO_PACKET0_
title: FWPS_STREAM_CALLOUT_IO_PACKET0_
author: windows-driver-content
description: The FWPS_STREAM_CALLOUT_IO_PACKET0 structure describes the data passed by the filter engine to a callout's classifyFn callout function when filtering a data stream.Note  FWPS_STREAM_CALLOUT_IO_PACKET0 is a specific version of FWPS_STREAM_CALLOUT_IO_PACKET. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information.
old-location: netvista\fwps_stream_callout_io_packet0.htm
ms.assetid: 2c0539f0-116e-4344-9584-db7416d258e0
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FWPS_STREAM_CALLOUT_IO_PACKET0
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
ms.keywords: FWPS_STREAM_CALLOUT_IO_PACKET0_, FWPS_STREAM_CALLOUT_IO_PACKET0
req.iface: 
---

# FWPS_STREAM_CALLOUT_IO_PACKET0_ structure



## -description
<p>The <b>FWPS_STREAM_CALLOUT_IO_PACKET0</b> structure describes the data passed by the filter engine to a
  callout's 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function when filtering a
  data stream.</p>


## -syntax

````
typedef struct FWPS_STREAM_CALLOUT_IO_PACKET0_ {
  FWPS_STREAM_DATA0       *streamData;
  SIZE_T                  missedBytes;
  UINT32                  countBytesRequired;
  SIZE_T                  countBytesEnforced;
  FWPS_STREAM_ACTION_TYPE streamAction;
} FWPS_STREAM_CALLOUT_IO_PACKET0;
````


## -struct-fields
<dl>

### -field <b>streamData</b>

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552419">FWPS_STREAM_DATA0</a> structure that
     describes the portion of the data stream available to the callout driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function for processing.</p>
</dd>

### -field <b>missedBytes</b>

<dd>
<p>The number of bytes in the data stream that are missing since the last time the callout driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function was called. This
     member is nonzero if a higher weight filter in the filter engine prevented the callout driver's 
     classifyFn callout function from processing a
     portion of the data stream.</p>
</dd>

### -field <b>countBytesRequired</b>

<dd>
<p>A value set by a callout's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function. This value
     specifies how many additional bytes of stream data are required by the callout function if it sets the 
     <b>streamAction</b> member to <b>FWPS_STREAM_ACTION_NEED_MORE_DATA</b>. The filter engine waits until it
     receives at least this many additional bytes of stream data before calling the callout driver's 
     classifyFn callout function again.
     </p>
<p>If a callout's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function sets the 
     <b>streamAction</b> member to a value other than <b>FWPS_STREAM_ACTION_NEED_MORE_DATA</b>, then it should set
     this member to zero.</p>
</dd>

### -field <b>countBytesEnforced</b>

<dd>
<p>A value set by a callout's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function. This value
     specifies the number of leading bytes of data in the portion of the data stream being processed to which
     the action specified by the 
     <b>streamAction</b> member or by the action returned by the callout function applies. Any remaining data
     in the stream buffer will be passed to the callout driver again the next time the filter engine calls
     the callout driver's 
     classifyFn callout function.</p>
</dd>

### -field <b>streamAction</b>

<dd>
<p>An <b>FWPS_STREAM_ACTION_TYPE</b> value set by a callout's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function that specifies
     the action to be applied to the data stream. This action is independent of the action returned by the
     callout function. A callout's 
     classifyFn callout function sets this member
     to one of the following:
     </p>
<p></p>
<dl>

### -field <a id="FWPS_STREAM_ACTION_NONE"></a><a id="fwps_stream_action_none"></a>FWPS_STREAM_ACTION_NONE

<dd>
<p>No stream-specific action is required.</p>
</dd>

### -field <a id="FWPS_STREAM_ACTION_ALLOW_CONNECTION"></a><a id="fwps_stream_action_allow_connection"></a>FWPS_STREAM_ACTION_ALLOW_CONNECTION

<dd>
<p>Indicates that all future data segments belonging to a flow are permitted. In this case, WFP stops classifying any data segments to the callout and attempts to offload the flow to the hardware such that no more inspection overhead is incurred.</p>
</dd>

### -field <a id="FWPS_STREAM_ACTION_NEED_MORE_DATA"></a><a id="fwps_stream_action_need_more_data"></a>FWPS_STREAM_ACTION_NEED_MORE_DATA

<dd>
<p>More stream data is required by the callout function.</p>
</dd>

### -field <a id="FWPS_STREAM_ACTION_DROP_CONNECTION"></a><a id="fwps_stream_action_drop_connection"></a>FWPS_STREAM_ACTION_DROP_CONNECTION

<dd>
<p>The stream connection should be dropped. A callout's 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function should only set
       the 
       <b>streamAction</b> member to this value if the 
       <b>action.type</b> member of the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff552387">FWPS_FILTER0</a> structure that the filter
       engine passed to the callout driver's 
       classifyFn callout function contains the value <b>FWP_ACTION_CALLOUT_UNKNOWN</b>. If a callout's 
       classifyFn callout function sets the 
       <b>streamAction</b> member to this value when the 
       <b>action.type</b> member of the <b>FWPS_FILTER0</b> structure contains the value
       <b>FWP_ACTION_CALLOUT_INSPECTION</b>, the connection will not be dropped.</p>
</dd>

### -field <a id="FWPS_STREAM_ACTION_DEFER"></a><a id="fwps_stream_action_defer"></a>FWPS_STREAM_ACTION_DEFER

<dd>
<p>Processing of the stream data will be deferred until the callout driver calls the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff551210">FwpsStreamContinue0</a> function. This
       action can only be set for an inbound data stream.
       </p>
<p>Deferring an inbound data stream will cause the network stack to stop acknowledging data received
       from the sender. This will lead to a reduction in the size of the sliding TCP window. A callout driver
       can use this behavior to implement flow control to slow down the incoming data rate.</p>
</dd>
</dl>
<p>The <b>FWPS_STREAM_ACTION_TYPE_MAX</b> value is a maximum value for testing purposes.</p>
<p>If a callout's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function sets this member
     to a value other than <b>FWPS_STREAM_ACTION_NONE</b>, then the action returned by the callout function is
     ignored by the filter engine.</p>
</dd>
</dl>

## -remarks
<p>The filter engine passes a pointer to an <b>FWPS_STREAM_CALLOUT_IO_PACKET0</b> structure to a callout's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function as the 
    <i>layerData</i> parameter when filtering a data stream.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552419">FWPS_STREAM_DATA0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551210">FwpsStreamContinue0</a>
</dt>
<dt>
<a href="NULL">Types of Callouts</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_STREAM_CALLOUT_IO_PACKET0 structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
