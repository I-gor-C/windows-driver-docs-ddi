---
UID: NF.ksproxy.IKsPin.KsDecrementPendingIoCount
title: IKsPin::KsDecrementPendingIoCount
author: windows-driver-content
description: The KsDecrementPendingIoCount method decrements the number of input/output (I/O) operations that are in progress on a pin.
old-location: stream\ikspin_ksdecrementpendingiocount.htm
old-project: stream
ms.assetid: 92e0355c-b89f-46c2-b406-e3c73fc37000
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IKsPin, KsDecrementPendingIoCount, IKsPin::KsDecrementPendingIoCount
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
req.alt-api: IKsPin.KsDecrementPendingIoCount
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

# IKsPin::KsDecrementPendingIoCount method



## -description
<p>The <b>KsDecrementPendingIoCount</b> method decrements the number of input/output (I/O) operations that are in progress on a pin.</p>


## -syntax

````
LONG KsDecrementPendingIoCount();
````


## -parameters


## -returns
<p>Returns an integer from 0 to <i>n</i>, the value that represents the new number of I/O operations that are in progress.</p>

<p>Returns an integer from 0 to <i>n</i>, the value that represents the new number of I/O operations that are in progress.</p>

<p>Returns an integer from 0 to <i>n</i>, the value that represents the new number of I/O operations that are in progress.</p>

## -remarks
<p>The <b>KsDecrementPendingIoCount</b> method is typically called from within an interface handler as described in the following sequence:</p>

<p>The proxy creates an instance of an interface handler (<a href="..\ksproxy\nn-ksproxy-iksinterfacehandler.md">IKsInterfaceHandler</a>) to handle a particular media type. </p>

<p>A client calls the <a href="stream.iksinterfacehandler_kssetpin">IKsInterfaceHandler::KsSetPin</a> method to inform that interface handler about the pin with which to communicate when passing data. </p>

<p>The client calls the <a href="stream.iksinterfacehandler_ksprocessmediasamples">IKsInterfaceHandler::KsProcessMediaSamples</a> method to move samples from or to the assigned pin. <b>KsProcessMediaSamples</b> performs I/O operations and for each I/O operation, calls <a href="stream.ikspin_ksincrementpendingiocount">IKsPin::KsIncrementPendingIoCount</a> to increment the I/O count.</p>

<p>The client calls the <a href="stream.iksinterfacehandler_kscompleteio">IKsInterfaceHandler::KsCompleteIo</a> method to complete an I/O operation. <b>KsCompleteIo</b> calls <b>KsDecrementPendingIoCount</b> to decrement the I/O count.</p>

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
<a href="..\ksproxy\nn-ksproxy-iksinterfacehandler.md">IKsInterfaceHandler</a>
</dt>
<dt>
<a href="stream.iksinterfacehandler_kscompleteio">IKsInterfaceHandler::KsCompleteIo</a>
</dt>
<dt>
<a href="stream.iksinterfacehandler_ksprocessmediasamples">IKsInterfaceHandler::KsProcessMediaSamples</a>
</dt>
<dt>
<a href="stream.iksinterfacehandler_kssetpin">IKsInterfaceHandler::KsSetPin</a>
</dt>
<dt>
<a href="stream.ikspin_ksincrementpendingiocount">IKsPin::KsIncrementPendingIoCount</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsPin::KsDecrementPendingIoCount method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
