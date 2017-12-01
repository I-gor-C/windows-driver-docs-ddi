---
UID: NF.ksproxy.IKsPin.KsPeekAllocator
title: IKsPin::KsPeekAllocator
author: windows-driver-content
description: The KsPeekAllocator method returns a pointer to an IMemAllocator interface for a pin's assigned allocator.
old-location: stream\ikspin_kspeekallocator.htm
old-project: stream
ms.assetid: fd833d0b-2f81-4002-8280-38e17e528af6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IKsPin, KsPeekAllocator, IKsPin::KsPeekAllocator
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
req.alt-api: IKsPin.KsPeekAllocator
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
req.iface: IKsPin
---

# IKsPin::KsPeekAllocator method



## -description
<p>The <b>KsPeekAllocator</b> method returns a pointer to an <b>IMemAllocator</b> interface for a pin's assigned allocator.</p>


## -syntax

````
IMemAllocator* KsPeekAllocator(
  [in] KSPEEKOPERATION Operation
);
````


## -parameters
<dl>

### -param <i>Operation</i> [in]

<dd>
<p>A value that specifies the type of operation. This value can be one of the following values from the KSPEEKOPERATION enumerated type.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p><b>KsPeekOperation_PeekOnly</b></p>
</td>
<td>
<p><b>IKsPin::KsPeekAllocator </b>does not increment the reference count for the allocator. </p>
</td>
</tr>
<tr>
<td>
<p><b>KsPeekOperation_AddRef</b></p>
</td>
<td>
<p><b>IKsPin::KsPeekAllocator</b> increments the reference count for the allocator (calls AddRef). </p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>Returns a pointer to an <b>IMemAllocator</b> interface if successful; otherwise, returns <b>NULL</b>. </p>

## -remarks
<p>For more information about <b>IMemAllocator</b>, see the Microsoft Windows SDK documentation.</p>

<p>This method is for proxy use and is not recommended for application use.</p>

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
<a href="..\ksproxy\nn-ksproxy-ikspin~r1.md">IKsPin</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsPin::KsPeekAllocator method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
