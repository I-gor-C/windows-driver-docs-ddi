---
UID: NN.ksproxy.IKsClockPropertySet
title: IKsClockPropertySet
author: windows-driver-content
description: The IKsClockPropertySet interface provides methods that let the proxy accurately reflect time.
old-location: stream\iksclockpropertyset.htm
old-project: stream
ms.assetid: bf50d4b1-782f-4d15-b6ef-23fa13da68ff
ms.author: windowsdriverdev
ms.date: 12/6/2017
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
req.alt-api: IKsClockPropertySet
req.alt-loc: Ksproxy.lib,Ksproxy.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ksproxy.lib
req.dll: 
req.irql: 
---

# IKsClockPropertySet interface



## -description
The <b>IKsClockPropertySet</b> interface provides methods that let the proxy accurately reflect time.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsClockPropertySet</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsClockPropertySet</b> also has these types of members:

The <b>IKsClockPropertySet</b> interface has these methods.

Retrieves the physical time and the correlated system time from the underlying clock.

Retrieves the presentation time and the correlated system time from the underlying clock.

Retrieves the current physical time from the underlying clock. 

Retrieves the clock resolution from the underlying clock.

Retrieves the streaming state of a pin from the underlying clock.

Retrieves the current presentation time from the underlying clock.

Sets the physical time with the correlated system time on the underlying clock.

Sets the correlated system time with the presentation time on the underlying clock.

Sets the current physical time on the underlying clock.

Sets the current presentation time on the underlying clock.

 

The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsClockPropertySet</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsClockPropertySet</b> also has these types of members:

The <b>IKsClockPropertySet</b> interface has these methods.

Retrieves the physical time and the correlated system time from the underlying clock.

Retrieves the presentation time and the correlated system time from the underlying clock.

Retrieves the current physical time from the underlying clock. 

Retrieves the clock resolution from the underlying clock.

Retrieves the streaming state of a pin from the underlying clock.

Retrieves the current presentation time from the underlying clock.

Sets the physical time with the correlated system time on the underlying clock.

Sets the correlated system time with the presentation time on the underlying clock.

Sets the current physical time on the underlying clock.

Sets the current presentation time on the underlying clock.

 

The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsClockPropertySet</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsClockPropertySet</b> also has these types of members:

The <b>IKsClockPropertySet</b> interface has these methods.

Retrieves the physical time and the correlated system time from the underlying clock.

Retrieves the presentation time and the correlated system time from the underlying clock.

Retrieves the current physical time from the underlying clock. 

Retrieves the clock resolution from the underlying clock.

Retrieves the streaming state of a pin from the underlying clock.

Retrieves the current presentation time from the underlying clock.

Sets the physical time with the correlated system time on the underlying clock.

Sets the correlated system time with the presentation time on the underlying clock.

Sets the current physical time on the underlying clock.

Sets the current presentation time on the underlying clock.

 

## -members
The <b>IKsClockPropertySet</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.iksclockpropertyset_ksgetcorrelatedphysicaltime">KsGetCorrelatedPhysicalTime</a>
</td>
<td align="left" width="63%">
Retrieves the physical time and the correlated system time from the underlying clock.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.iksclockpropertyset_ksgetcorrelatedtime">KsGetCorrelatedTime</a>
</td>
<td align="left" width="63%">
Retrieves the presentation time and the correlated system time from the underlying clock.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.iksclockpropertyset_ksgetphysicaltime">KsGetPhysicalTime</a>
</td>
<td align="left" width="63%">
Retrieves the current physical time from the underlying clock. 
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.iksclockpropertyset_ksgetresolution">KsGetResolution</a>
</td>
<td align="left" width="63%">
Retrieves the clock resolution from the underlying clock.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.iksclockpropertyset_ksgetstate">KsGetState</a>
</td>
<td align="left" width="63%">
Retrieves the streaming state of a pin from the underlying clock.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.iksclockpropertyset_ksgettime">KsGetTime</a>
</td>
<td align="left" width="63%">
Retrieves the current presentation time from the underlying clock.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.iksclockpropertyset_kssetcorrelatedphysicaltime">KsSetCorrelatedPhysicalTime</a>
</td>
<td align="left" width="63%">
Sets the physical time with the correlated system time on the underlying clock.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.iksclockpropertyset_kssetcorrelatedtime">KsSetCorrelatedTime</a>
</td>
<td align="left" width="63%">
Sets the correlated system time with the presentation time on the underlying clock.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.iksclockpropertyset_kssetphysicaltime">KsSetPhysicalTime</a>
</td>
<td align="left" width="63%">
Sets the current physical time on the underlying clock.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.iksclockpropertyset_kssettime">KsSetTime</a>
</td>
<td align="left" width="63%">
Sets the current presentation time on the underlying clock.
</td>
</tr>
</table>Retrieves the physical time and the correlated system time from the underlying clock.

Retrieves the presentation time and the correlated system time from the underlying clock.

Retrieves the current physical time from the underlying clock. 

Retrieves the clock resolution from the underlying clock.

Retrieves the streaming state of a pin from the underlying clock.

Retrieves the current presentation time from the underlying clock.

Sets the physical time with the correlated system time on the underlying clock.

Sets the correlated system time with the presentation time on the underlying clock.

Sets the current physical time on the underlying clock.

Sets the current presentation time on the underlying clock.

 

## -remarks
The IID for this interface is IID_IKsClockPropertySet.

## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ksproxy.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ksproxy.lib</dt>
</dl>
</td>
</tr>
</table>