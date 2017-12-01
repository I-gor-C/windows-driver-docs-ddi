---
UID: NN.ksproxy.IKsPin~r1
title: IKsPin
author: windows-driver-content
description: The IKsPin interface provides methods that control and retrieve information about a pin.
old-location: stream\ikspin.htm
old-project: stream
ms.assetid: 4717300c-bc98-4e1f-83c3-cbd368b45140
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsSynchronousDeviceControl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: ksproxy.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsPin,IKsPin.KsReceiveAllocator,IKsPin.KsRenegotiateAllocator,IKsPin.KsQualityNotify
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
req.iface: 
---

# IKsPin interface



## -description
<p>The <b>IKsPin</b> interface provides methods that control and retrieve information about a pin.</p>
<p>The IID for this interface is IID_IKsPin.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsPin</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsPin</b> also has these types of members:</p>

<p>The <b>IKsPin</b> interface has these methods.</p>

<p>For proxy use and not recommended for application use. Creates a pin handle and stores it in the KS pin object. </p>

<p>Decrements the number of I/O operations that are in progress on a pin.</p>

<p>Delivers a media sample from an output pin to an input pin. </p>

<p>Retrieves the current communication direction, interface, and medium of a pin. </p>

<p>Increments the number of I/O operations that are in progress on a pin.</p>

<p>Informs a pin that a stream segment completed. Used by interface handlers.</p>

<p>For proxy use and not recommended for application use. Returns a pointer to a <b>IMemAllocator</b> interface for a pin's assigned allocator.</p>

<p>For proxy use and not recommended for application use.</p>

<p>For proxy use and not recommended for application use. Receives quality-management reports from the kernel-mode equivalent of a DirectShow pin.</p>

<p>Retrieves interfaces that a pin supports.</p>

<p>Retrieves mediums that a pin supports.</p>

<p>For proxy use and not recommended for application use. Provides an allocator for an output pin. </p>

<p>Obsolete. Do not use.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsPin</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsPin</b> also has these types of members:</p>

<p>The <b>IKsPin</b> interface has these methods.</p>

<p>For proxy use and not recommended for application use. Creates a pin handle and stores it in the KS pin object. </p>

<p>Decrements the number of I/O operations that are in progress on a pin.</p>

<p>Delivers a media sample from an output pin to an input pin. </p>

<p>Retrieves the current communication direction, interface, and medium of a pin. </p>

<p>Increments the number of I/O operations that are in progress on a pin.</p>

<p>Informs a pin that a stream segment completed. Used by interface handlers.</p>

<p>For proxy use and not recommended for application use. Returns a pointer to a <b>IMemAllocator</b> interface for a pin's assigned allocator.</p>

<p>For proxy use and not recommended for application use.</p>

<p>For proxy use and not recommended for application use. Receives quality-management reports from the kernel-mode equivalent of a DirectShow pin.</p>

<p>Retrieves interfaces that a pin supports.</p>

<p>Retrieves mediums that a pin supports.</p>

<p>For proxy use and not recommended for application use. Provides an allocator for an output pin. </p>

<p>Obsolete. Do not use.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsPin</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsPin</b> also has these types of members:</p>

<p>The <b>IKsPin</b> interface has these methods.</p>

<p>For proxy use and not recommended for application use. Creates a pin handle and stores it in the KS pin object. </p>

<p>Decrements the number of I/O operations that are in progress on a pin.</p>

<p>Delivers a media sample from an output pin to an input pin. </p>

<p>Retrieves the current communication direction, interface, and medium of a pin. </p>

<p>Increments the number of I/O operations that are in progress on a pin.</p>

<p>Informs a pin that a stream segment completed. Used by interface handlers.</p>

<p>For proxy use and not recommended for application use. Returns a pointer to a <b>IMemAllocator</b> interface for a pin's assigned allocator.</p>

<p>For proxy use and not recommended for application use.</p>

<p>For proxy use and not recommended for application use. Receives quality-management reports from the kernel-mode equivalent of a DirectShow pin.</p>

<p>Retrieves interfaces that a pin supports.</p>

<p>Retrieves mediums that a pin supports.</p>

<p>For proxy use and not recommended for application use. Provides an allocator for an output pin. </p>

<p>Obsolete. Do not use.</p>

<p> </p>

## -members
<p>The <b>IKsPin</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.ikspin_kscreatesinkpinhandle">KsCreateSinkPinHandle</a>
</td>
<td align="left" width="63%">
<p>For proxy use and not recommended for application use. Creates a pin handle and stores it in the KS pin object. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.ikspin_ksdecrementpendingiocount">KsDecrementPendingIoCount</a>
</td>
<td align="left" width="63%">
<p>Decrements the number of I/O operations that are in progress on a pin.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.ikspin_ksdeliver">KsDeliver</a>
</td>
<td align="left" width="63%">
<p>Delivers a media sample from an output pin to an input pin. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.ikspin_ksgetcurrentcommunication">KsGetCurrentCommunication</a>
</td>
<td align="left" width="63%">
<p>Retrieves the current communication direction, interface, and medium of a pin. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.ikspin_ksincrementpendingiocount">KsIncrementPendingIoCount</a>
</td>
<td align="left" width="63%">
<p>Increments the number of I/O operations that are in progress on a pin.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.ikspin_ksmediasamplescompleted">KsMediaSamplesCompleted</a>
</td>
<td align="left" width="63%">
<p>Informs a pin that a stream segment completed. Used by interface handlers.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.ikspin_kspeekallocator">KsPeekAllocator</a>
</td>
<td align="left" width="63%">
<p>For proxy use and not recommended for application use. Returns a pointer to a <b>IMemAllocator</b> interface for a pin's assigned allocator.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.ikspin_kspropagateacquire">KsPropagateAcquire</a>
</td>
<td align="left" width="63%">
<p>For proxy use and not recommended for application use.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>KsQualityNotify</b></td>
<td align="left" width="63%">
<p>For proxy use and not recommended for application use. Receives quality-management reports from the kernel-mode equivalent of a DirectShow pin.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.ikspin_ksqueryinterfaces">KsQueryInterfaces</a>
</td>
<td align="left" width="63%">
<p>Retrieves interfaces that a pin supports.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.ikspin_ksquerymediums">KsQueryMediums</a>
</td>
<td align="left" width="63%">
<p>Retrieves mediums that a pin supports.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>KsReceiveAllocator</b></td>
<td align="left" width="63%">
<p>For proxy use and not recommended for application use. Provides an allocator for an output pin. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>KsRenegotiateAllocator</b></td>
<td align="left" width="63%">
<p>Obsolete. Do not use.</p>
</td>
</tr>
</table><p>For proxy use and not recommended for application use. Creates a pin handle and stores it in the KS pin object. </p>

<p>Decrements the number of I/O operations that are in progress on a pin.</p>

<p>Delivers a media sample from an output pin to an input pin. </p>

<p>Retrieves the current communication direction, interface, and medium of a pin. </p>

<p>Increments the number of I/O operations that are in progress on a pin.</p>

<p>Informs a pin that a stream segment completed. Used by interface handlers.</p>

<p>For proxy use and not recommended for application use. Returns a pointer to a <b>IMemAllocator</b> interface for a pin's assigned allocator.</p>

<p>For proxy use and not recommended for application use.</p>

<p>For proxy use and not recommended for application use. Receives quality-management reports from the kernel-mode equivalent of a DirectShow pin.</p>

<p>Retrieves interfaces that a pin supports.</p>

<p>Retrieves mediums that a pin supports.</p>

<p>For proxy use and not recommended for application use. Provides an allocator for an output pin. </p>

<p>Obsolete. Do not use.</p>

<p> </p>

## -remarks
<p>An interface handler (<a href="..\ksproxy\nn-ksproxy-iksinterfacehandler.md">IKsInterfaceHandler</a>) uses many of the <b>IKsPin</b> methods to route media samples of a particular media type. 
    
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ksproxy\nn-ksproxy-iksinterfacehandler.md">IKsInterfaceHandler</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsPin interface%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
