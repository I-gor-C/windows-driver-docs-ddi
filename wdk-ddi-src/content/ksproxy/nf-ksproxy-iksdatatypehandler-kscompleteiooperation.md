---
UID: NF.ksproxy.IKsDataTypeHandler.KsCompleteIoOperation
title: IKsDataTypeHandler::KsCompleteIoOperation
author: windows-driver-content
description: The KsCompleteIoOperation method cleans up the extended header and completes the input and output (I/O) operation.
old-location: stream\iksdatatypehandler_kscompleteiooperation.htm
old-project: stream
ms.assetid: 46a58007-16bf-422b-8408-30a7b65dbee6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IKsDataTypeHandler, KsCompleteIoOperation, IKsDataTypeHandler::KsCompleteIoOperation
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
req.alt-api: IKsDataTypeHandler.KsCompleteIoOperation
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
req.iface: IKsDataTypeHandler
---

# IKsDataTypeHandler::KsCompleteIoOperation method



## -description
<p>The <b>KsCompleteIoOperation</b> method cleans up the extended header and completes the input and output (I/O) operation. </p>


## -syntax

````
HRESULT KsCompleteIoOperation(
  [in, out] IMediaSample  *Sample,
  [in, out] PVOID         StreamHeader,
  [in]      KSIOOPERATION IoOperation,
  [in]      BOOL          Cancelled
);
````


## -parameters
<dl>

### -param <i>Sample</i> [in, out]

<dd>
<p>Pointer to the <b>IMediaSample</b> interface for the associated media sample.</p>
</dd>

### -param <i>StreamHeader</i> [in, out]

<dd>
<p>Pointer to a buffer that contains the extended header information.</p>
</dd>

### -param <i>IoOperation</i> [in]

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

### -param <i>Cancelled</i> [in]

<dd>
<p>Boolean value that is <b>TRUE</b> if the I/O operation was canceled and <b>FALSE</b> otherwise.</p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code. If the stream's major type is KSDATAFORMAT_TYPE_AUDIO, a <b>KsCompleteIoOperation</b> call is inapplicable, so <b>KsCompleteIoOperation</b> automatically returns NOERROR.</p>

## -remarks
<p>The client only calls <b>KsCompleteIoOperation</b> if the data type handler indicated to the client the existence of extended header information in a call to the <a href="stream.iksdatatypehandler_ksqueryextendedsize">IKsDataTypeHandler::KsQueryExtendedSize</a> method.</p>

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
<a href="stream.iksdatatypehandler_ksqueryextendedsize">IKsDataTypeHandler::KsQueryExtendedSize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsDataTypeHandler::KsCompleteIoOperation method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
