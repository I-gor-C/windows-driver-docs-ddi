---
UID: NF.ksproxy.IKsDataTypeHandler.KsQueryExtendedSize
title: IKsDataTypeHandler::KsQueryExtendedSize
author: windows-driver-content
description: The KsQueryExtendedSize method retrieves extended header information required for input and output (I/O) operations.
old-location: stream\iksdatatypehandler_ksqueryextendedsize.htm
ms.assetid: 14d03e6f-d02c-4b39-8f21-b339c65fb036
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsDataTypeHandler.KsQueryExtendedSize
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
ms.keywords: IKsDataTypeHandler, KsQueryExtendedSize, IKsDataTypeHandler::KsQueryExtendedSize
req.iface: IKsDataTypeHandler
---

# IKsDataTypeHandler::KsQueryExtendedSize method



## -description
<p>The <b>KsQueryExtendedSize</b> method retrieves extended header information required for input and output (I/O) operations. </p>


## -syntax

````
HRESULT KsQueryExtendedSize(
  [out] ULONG *ExtendedSize
);
````


## -parameters
<dl>

### -param <i>ExtendedSize</i> [out]

<dd>
<p>Pointer to a variable that receives the extended header size in bytes.</p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>If <b>KsQueryExtendedSize</b> returns zero at <i>ExtendedSize</i>, clients should not call the <a href="https://msdn.microsoft.com/16411d58-5fff-430f-b96d-78eed1dbb01c">KsPrepareIoOperation</a> and <a href="https://msdn.microsoft.com/46a58007-16bf-422b-8408-30a7b65dbee6">KsCompleteIoOperation</a> methods of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559807">IKsDataTypeHandler</a> interface because I/O preparation and completion operations are not required. For all other values that <b>KsQueryExtendedSize</b> returns at <i>ExtendedSize</i>, clients should allocate memory space for the extended stream header per the returned value and call <b>KsPrepareIoOperation</b> and <b>KsCompleteIoOperation</b> to prepare and complete the I/O operation associated with the header.</p>

<p>If <b>KsQueryExtendedSize</b> returns zero at <i>ExtendedSize</i>, clients should not call the <a href="https://msdn.microsoft.com/16411d58-5fff-430f-b96d-78eed1dbb01c">KsPrepareIoOperation</a> and <a href="https://msdn.microsoft.com/46a58007-16bf-422b-8408-30a7b65dbee6">KsCompleteIoOperation</a> methods of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559807">IKsDataTypeHandler</a> interface because I/O preparation and completion operations are not required. For all other values that <b>KsQueryExtendedSize</b> returns at <i>ExtendedSize</i>, clients should allocate memory space for the extended stream header per the returned value and call <b>KsPrepareIoOperation</b> and <b>KsCompleteIoOperation</b> to prepare and complete the I/O operation associated with the header.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559811">IKsDataTypeHandler::KsCompleteIoOperation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559831">IKsDataTypeHandler::KsPrepareIoOperation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsDataTypeHandler::KsQueryExtendedSize method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
