---
UID: NS.strmini._HW_STREAM_REQUEST_BLOCK
title: HW_STREAM_REQUEST_BLOCK
author: windows-driver-content
description: The stream class driver uses the HW_STREAM_REQUEST_BLOCK structure to pass information to and from the minidriver, using minidriver provided callbacks.
old-location: stream\hw_stream_request_block.htm
old-project: stream
ms.assetid: e2a19bb1-631d-4160-9980-f3cbeb0b085a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: HW_STREAM_REQUEST_BLOCK, HW_STREAM_REQUEST_BLOCK, *PHW_STREAM_REQUEST_BLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HW_STREAM_REQUEST_BLOCK
req.alt-loc: strmini.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# HW_STREAM_REQUEST_BLOCK structure



## -description
<p>The stream class driver uses the HW_STREAM_REQUEST_BLOCK structure to pass information to and from the minidriver, using minidriver provided callbacks.</p>


## -syntax

````
typedef struct _HW_STREAM_REQUEST_BLOCK {
  ULONG                           SizeOfThisPacket;
  SRB_COMMAND                     Command;
  NTSTATUS                        Status;
  PHW_STREAM_OBJECT               StreamObject;
  PVOID                           HwDeviceExtension;
  PVOID                           SRBExtension;
  union {
    PKSSTREAM_HEADER                       DataBufferArray;
    PHW_STREAM_DESCRIPTOR                  StreamBuffer;
    KSSTATE                                StreamState;
    PSTREAM_TIME_REFERENCE                 TimeReference;
    PSTREAM_PROPERTY_DESCRIPTOR            PropertyInfo;
    PKSDATAFORMAT                          OpenFormat;
    struct _PORT_CONFIGURATION_INFORMATION  *ConfigInfo;
    HANDLE                                 MasterClockHandle;
    DEVICE_POWER_STATE                     DeviceState;
    PSTREAM_DATA_INTERSECT_INFO            IntersectInfo;
    PVOID                                  MethodInfo;
    LONG                                   FilterTypeIndex;
    BOOLEAN                                Idle;
  } CommandData;
  ULONG                           NumberOfBuffers;
  ULONG                           TimeoutCounter;
  ULONG                           TimeoutOriginal;
  struct _HW_STREAM_REQUEST_BLOCK  *NextSRB;
  PIRP                            Irp;
  ULONG                           Flags;
  PVOID                           HwInstanceExtension;
  union {
    ULONG NumberOfBytesToTransfer;
    ULONG ActualBytesTransferred;
  };
  PKSSCATTER_GATHER               ScatterGatherBuffer;
  ULONG                           NumberOfPhysicalPages;
  ULONG                           NumberOfScatterGatherElements;
  ULONG                           Reserved[1];
} HW_STREAM_REQUEST_BLOCK, *PHW_STREAM_REQUEST_BLOCK;
````


## -struct-fields
<dl>

### -field SizeOfThisPacket

<dd>
<p>Specifies the size, in bytes, of this structure.</p>
</dd>

### -field Command

<dd>
<p>
      Specifies the operation to be performed by the minidriver's callback. The class driver passes SRB_XXX command codes to minidriver callbacks.</p>
</dd>

### -field Status

<dd>
<p>When the minidriver completes a stream request, it fills this member with the status code of the request. See the documentation for the appropriate <b>StrMini</b><i>Xxx</i><b>Request</b> routine for the status codes minidrivers are expected to use.</p>
</dd>

### -field StreamObject

<dd>
<p>For stream oriented requests, the class driver sets this to point to the <a href="..\strmini\ns-strmini--hw-stream-object~r1.md">HW_STREAM_OBJECT</a> structure that specifies the stream the class driver is making a request on.</p>
</dd>

### -field HwDeviceExtension

<dd>
<p>Pointer to the minidriver's device extension. The minidriver may use this buffer to record private information. The minidriver sets the size of this buffer in the <a href="..\strmini\ns-strmini--hw-initialization-data.md">HW_INITIALIZATION_DATA</a> structure it passes when it registers itself via <a href="stream.streamclassregisterminidriver">StreamClassRegisterMinidriver</a>. The class driver also passes pointers to this buffer in the <b>HwDeviceExtension</b> member of the <a href="..\strmini\ns-strmini--hw-stream-object~r1.md">HW_STREAM_OBJECT</a>, <a href="..\strmini\ns-strmini--hw-time-context.md">HW_TIME_CONTEXT</a>, and <a href="..\strmini\ns-strmini--port-configuration-information~r1.md">PORT_CONFIGURATION_INFORMATION</a> structures it passes to the minidriver.</p>
</dd>

### -field SRBExtension

<dd>
<p>Points to an uninitialized buffer the class driver allocates for the minidriver to use while processing this stream request block. This buffer is deallocated once the minidriver completes its handling of the block (see <a href="..\strmini\nf-strmini-streamclassdevicenotification.md">StreamClassDeviceNotification</a> or <a href="..\strmini\nf-strmini-streamclassstreamnotification.md">StreamClassStreamNotification</a> for details).</p>
</dd>

### -field CommandData

<dd>
<p><b>CommandData</b> is a union of members provided for command-code-specific data.
      
     </p>
<dl>

### -field DataBufferArray

<dd>
<p>Pointer to an array of <a href="stream.ksstream_header">KSSTREAM_HEADER</a> structures. The number of entries in this array is specified in <b>NumberOfBuffers</b>. Each KSSTREAM_HEADER describes one block of data.</p>
<p>This member is used when the command code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff568200">SRB_READ_DATA</a>

or <a href="https://msdn.microsoft.com/library/windows/hardware/ff568220">SRB_WRITE_DATA</a>.</p>
</dd>

### -field StreamBuffer

<dd>
<p>Points to the <a href="..\strmini\ns-strmini--hw-stream-descriptor.md">HW_STREAM_DESCRIPTOR</a> structure the minidriver fills in with a description of the kernel streaming semantics it supports.
</p>
<p>The minidriver specifies the size of this buffer in the <b>StreamDescriptorSize</b> member of its <a href="..\strmini\ns-strmini--port-configuration-information~r1.md">PORT_CONFIGURATION_INFORMATION</a> structure.
</p>
<p>This member is used when the command code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff568173">SRB_GET_STREAM_INFO</a>.</p>
</dd>

### -field StreamState

<dd>
<p>
       The stream state.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff565110">KSPROPERTY_CONNECTION_STATE</a> for details.</p>
<p>This member is used when the command code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff568178">SRB_GET_STREAM_STATE</a>

or <a href="https://msdn.microsoft.com/library/windows/hardware/ff568210">SRB_SET_STREAM_STATE</a>.</p>
</dd>

### -field TimeReference

<dd>
<p>A pointer to a STREAM_TIME_REFERENCE structure.</p>
</dd>

### -field PropertyInfo

<dd>
<p>Points to the <a href="..\strmini\ns-strmini--stream-property-descriptor.md">STREAM_PROPERTY_DESCRIPTOR</a> structure that specifies the parameters for the property get or set operation.</p>
<p>This member is used when the command code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff568170">SRB_GET_DEVICE_PROPERTY</a>,

<a href="https://msdn.microsoft.com/library/windows/hardware/ff568204">SRB_SET_DEVICE_PROPERTY</a>,

<a href="https://msdn.microsoft.com/library/windows/hardware/ff568175">SRB_GET_STREAM_PROPERTY</a>, or

<a href="https://msdn.microsoft.com/library/windows/hardware/ff568207">SRB_SET_STREAM_PROPERTY</a>.</p>
</dd>

### -field OpenFormat

<dd>
<p>Pointer to the <a href="stream.ksdataformat">KSDATAFORMAT</a> structure that specifies the format.</p>
<p>This member is used when the command code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff568191">SRB_OPEN_STREAM</a>

or <a href="https://msdn.microsoft.com/library/windows/hardware/ff568196">SRB_PROPOSE_DATA_FORMAT</a>.</p>
</dd>

### -field ConfigInfo

<dd>
<p>Pointer to the <a href="..\strmini\ns-strmini--port-configuration-information~r1.md">PORT_CONFIGURATION_INFORMATION</a> structure used to initialize the device</p>
<p>This member is used when the command code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff568185">SRB_INITIALIZE_DEVICE</a>.</p>
</dd>

### -field MasterClockHandle

<dd>
<p>Handle for the clock object that now serves as the master clock.</p>
<p>This member is used when the command code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff568190">SRB_OPEN_MASTER_CLOCK</a>

or <a href="https://msdn.microsoft.com/library/windows/hardware/ff568179">SRB_INDICATE_MASTER_CLOCK</a>.</p>
</dd>

### -field DeviceState

<dd>
<p>Specifies the new power state.</p>
<p>This member is used when the command code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff568157">SRB_CHANGE_POWER_STATE</a>.</p>
</dd>

### -field IntersectInfo

<dd>
<p>Pointer to a <a href="..\strmini\ns-strmini--stream-data-intersect-info.md">STREAM_DATA_INTERSECT_INFO</a> structure that describes the parameters of this operation.</p>
<p>This member is used when the command code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff568168">SRB_GET_DATA_INTERSECTION</a>.</p>
</dd>

### -field MethodInfo

<dd>
<p>Pointer to a buffer that the method data will be read from or written to.  </p>
<p>This member is available on Windows XP and later.</p>
</dd>

### -field FilterTypeIndex

<dd>
<p>Filter type index for SRB_OPEN_DEVICE_INSTANCE.  </p>
<p>This member is available on Windows XP and later.</p>
</dd>

### -field Idle

<dd>
<p>This member is set to <b>TRUE</b> if no open handles to the device remain.  This member is set to <b>FALSE</b>  if the device is no longer idle (a handle to the device has been opened).</p>
<p>This member is used when the command code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff568186">SRB_NOTIFY_IDLE_STATE</a>. </p>
<p>  This member is available on Windows XP and later, except for Windows Server 2003.</p>
</dd>
</dl>
</dd>

### -field NumberOfBuffers

<dd>
<p>If Command is either <a href="https://msdn.microsoft.com/library/windows/hardware/ff568200">SRB_READ_DATA</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff568220">SRB_WRITE_DATA</a>, then this specifies the number of entries in the array of <a href="stream.ksstream_header">KSSTREAM_HEADER</a> structures that begins at the address pointed to by <b>CommandData.DataBufferArray</b>. Otherwise this parameter is unused.</p>
</dd>

### -field TimeoutCounter

<dd>
<p>The number of seconds before this request times out. The class driver decrements this once per second. If the class driver decrements <b>TimeoutCounter</b> to zero before the minidriver completes this request, it will call the minidriver's <a href="stream.strminirequesttimeout">StrMiniRequestTimeout</a> routine. If the minidriver sets this to zero, the request does not time out.</p>
</dd>

### -field TimeoutOriginal

<dd>
<p>The class driver sets this to the original value of <b>TimeoutCounter</b> upon the creation of the SRB.</p>
</dd>

### -field NextSRB

<dd>
<p>Points to another stream request block. The minidriver can use this member to queue stream request blocks.</p>
</dd>

### -field Irp

<dd>
<p>Pointer to the IRP for the request. Most minidrivers do not need to use this member.</p>
</dd>

### -field Flags

<dd>
<p>Specifies the type of request. The class driver and the minidriver can use this member to determine which callback the class driver passed this stream request block to.</p>
<table>
<tr>
<th>Value</th>
<th>Callback used</th>
</tr>
<tr>
<td>
<p>None</p>
</td>
<td>
<p>
<a href="stream.strminireceivedevicepacket">StrMiniReceiveDevicePacket</a>
</p>
</td>
</tr>
<tr>
<td>
<p>SRB_HW_FLAGS_STREAM_REQUEST</p>
</td>
<td>
<p>
<a href="stream.strminireceivestreamcontrolpacket">StrMiniReceiveStreamControlPacket</a>
</p>
</td>
</tr>
<tr>
<td>
<p>SRB_HW_FLAGS_DATA_TRANSFER | SRB_HW_FLAGS_STREAM_REQUEST</p>
</td>
<td>
<p>
<a href="stream.strminireceivestreamdatapacket">StrMiniReceiveStreamDataPacket</a>
</p>
</td>
</tr>
</table>
<p> </p>
<p>SRB_HW_FLAGS_STREAM_REQUEST bit is set for stream-specific requests (which are passed to the minidriver's <b>StrMiniReceiveStream</b><i>Xxx</i><b>Packet</b> routines). The SRB_HW_FLAGS_DATA_TRANSFER bit is set for data transfer requests (which are passed to the minidriver's </p>
</dd>

### -field HwInstanceExtension

<dd>
<p>Pointer to the minidriver's instance extension. The minidriver may use this buffer to record private information global to this instance of the minidriver. The minidriver sets the size of this buffer in the <a href="..\strmini\ns-strmini--hw-initialization-data.md">HW_INITIALIZATION_DATA</a> structure it passes when it registers itself via <a href="stream.streamclassregisterminidriver">StreamClassRegisterMinidriver</a>.</p>
</dd>

### -field NumberOfBytesToTransfer

<dd>
<p>For a SRB_READ_DATA or SRB_WRITE_DATA request, the number of bytes to be transferred.</p>
</dd>

### -field ActualBytesTransferred

<dd>
<p>For control requests, the number of bytes actually transferred. </p>
</dd>

### -field ScatterGatherBuffer

<dd>
<p>Points to an array of KSSCATTER_GATHER structures, of the form:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct {
    PHYSICAL_ADDRESS PhysicalAddress;
    ULONG Length;
} KSSCATTER_GATHER, *PKSSCATTER_GATHER;</pre>
</td>
</tr>
</table></span></div>
<p>The array describes a scatter/gather list that can be used by the minidriver to do DMA. The memory does not need to be probed, locked, mapped, or flushed -- the stream class driver performs these for the minidriver.</p>
</dd>

### -field NumberOfPhysicalPages

<dd>
<p>Specifies the size of the array passed in the <b>ScatterGatherBuffer</b> member.</p>
</dd>

### -field NumberOfScatterGatherElements

<dd>
<p>Specifies the number of physical elements pointed to by <b>ScatterGatherBuffer</b>.</p>
</dd>

### -field Reserved[1]

<dd>
<p>Reserved for system use. Do not use.</p>
</dd>
</dl>

## -remarks
<p>The stream class driver passes pointers to HW_STREAM_REQUEST_BLOCK structures to the minidriver's <a href="stream.strminireceivestreamdatapacket">StrMiniReceiveStreamDataPacket</a>, <a href="stream.strminireceivestreamcontrolpacket">StrMiniReceiveStreamControlPacket</a>, and <a href="stream.strminireceivedevicepacket">StrMiniReceiveDevicePacket</a> routines.</p>

<p>The minidriver owns this stream request block until the request times out or it completes the request. The minidriver signals to the class driver that it has completed the request by calling <a href="..\strmini\nf-strmini-streamclassdevicenotification.md">StreamClassDeviceNotification</a>(DeviceRequestComplete, pSrb-&gt;HwDeviceExtension, pSRB) for device-specific requests, or calling <a href="..\strmini\nf-strmini-streamclassstreamnotification.md">StreamClassStreamNotification</a>(StreamRequestComplete, pSrb-&gt;StreamObject, pSrb) for stream-specific requests. (The minidriver can also complete a request by calling <a href="..\strmini\nf-strmini-streamclasscompleterequestandmarkqueueready.md">StreamClassCompleteRequestAndMarkQueueReady</a>(pSrb). See that routine for details.)</p>

<p>If the class driver times out the request, it will call the minidriver's <a href="stream.strminirequesttimeout">StrMiniRequestTimeout</a> routine, which has the responsibility of terminating processing of the request. If the minidriver queues a request for later processing, it should set the <b>TimeoutCounter</b> member to zero, which will prevent the class driver from timing out the request. Once the minidriver is ready to resume processing the request, it should reset the <b>TimeoutCounter</b> member to the value of <b>TimeoutOriginal</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
</table>