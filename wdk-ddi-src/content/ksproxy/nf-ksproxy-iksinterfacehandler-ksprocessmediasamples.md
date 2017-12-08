---
UID: NF.ksproxy.IKsInterfaceHandler.KsProcessMediaSamples
title: IKsInterfaceHandler::KsProcessMediaSamples
author: windows-driver-content
description: The KsProcessMediaSamples method processes media samples.
old-location: stream\iksinterfacehandler_ksprocessmediasamples.htm
old-project: stream
ms.assetid: 3f0982d8-4ac3-40f6-8587-624c26d25510
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IKsInterfaceHandler, KsProcessMediaSamples, IKsInterfaceHandler::KsProcessMediaSamples
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsInterfaceHandler.KsProcessMediaSamples
req.alt-loc: ksproxy.h
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
req.iface: IKsInterfaceHandler
---

# IKsInterfaceHandler::KsProcessMediaSamples method



## -description
<p>The <b>KsProcessMediaSamples</b> method processes media samples.</p>


## -syntax

````
HRESULT KsProcessMediaSamples(
  [in]      IKsDataTypeHandler *KsDataTypeHandler,
  [in]      IMediaSample       **SampleList,
  [in, out] PLONG              SampleCount,
  [in]      KSIOOPERATION      IoOperation,
  [out]     PKSSTREAM_SEGMENT  *StreamSegment
);
````


## -parameters
<dl>

### -param KsDataTypeHandler [in]

<dd>
<p>Pointer to the <a href="..\ksproxy\nn-ksproxy-iksdatatypehandler.md">IKsDataTypeHandler</a> interface for the data type handler that handles the type of media listed at <i>SampleList</i>. This data type handler has specific information about the media type being streamed.</p>
</dd>

### -param SampleList [in]

<dd>
<p>Pointer to a buffer that contains an array of pointers to the <b>IMediaSample</b> interfaces for the list of media samples to process. </p>
</dd>

### -param SampleCount [in, out]

<dd>
<p>Pointer to a variable that initially contains the number of samples in the list at <i>SampleList</i> and, on return, receives the actual number of samples processed.</p>
</dd>

### -param IoOperation [in]

<dd>
<p>Value that specifies the type of I/O operation. This value can be one of the following values from the KSIOOPERATION enumerated type:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p><b>KsIoOperation_Write</b></p>
</td>
<td>
<p>Write data to stream.</p>
</td>
</tr>
<tr>
<td>
<p><b>KsIoOperation_Read</b></p>
</td>
<td>
<p>Read data from stream.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param StreamSegment [out]

<dd>
<p>Pointer to a buffer that receives a pointer to a <a href="..\ksproxy\ns-ksproxy--ksstream-segment.md">KSSTREAM_SEGMENT</a> structure that contains header information for a stream segment that is sent to the kernel-mode pin. </p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>The <b>KsProcessMediaSamples</b> method moves samples from or to a previously assigned filter pin. A stream header is initialized to represent each media sample in the stream segment. The input and output (I/O) are then performed, the count of wait items is incremented, and the proxy I/O thread waits for completion.</p>

<p>The <b>KsProcessMediaSamples</b> method calls the <a href="stream.iksdatatypehandler_ksqueryextendedsize">KsQueryExtendedSize</a> method of the received <a href="..\ksproxy\nn-ksproxy-iksdatatypehandler.md">IKsDataTypeHandler</a> interface to retrieve the size of the extended header. If an extended header size is not specified, <b>KsProcessMediaSamples</b> discards the pointer to the <b>IKsDataTypeHandler</b> interface. If an extended header size is specified, <b>KsProcessMediaSamples</b> holds the pointer to the <b>IKsDataTypeHandler</b> interface until processing of the media samples is complete. The <b>KsProcessMediaSamples</b> method then allocates the stream headers with the appropriate header sizes. For each media sample, <b>KsProcessMediaSamples</b> initializes the header, copies data pointers, sets time stamps, and so on. Each sample is then added to the sample list. If it is a write operation, the sample is held by incrementing the reference count. </p>

<p>For more information about <b>IMediaSample</b>, see the Microsoft Windows SDK documentation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.h (include Ksproxy.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ksproxy\nn-ksproxy-iksdatatypehandler.md">IKsDataTypeHandler</a>
</dt>
<dt>
<a href="stream.iksdatatypehandler_ksqueryextendedsize">IKsDataTypeHandler::KsQueryExtendedSize</a>
</dt>
<dt>
<a href="..\ksproxy\ns-ksproxy--ksstream-segment.md">KSSTREAM_SEGMENT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsInterfaceHandler::KsProcessMediaSamples method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
