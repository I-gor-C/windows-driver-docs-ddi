---
UID: NN.portcls.IPortClsNotifications
title: IPortClsNotifications
author: windows-driver-content
description: An interface implemented by ports to provide notification helpers to miniports to support audio module communication.
old-location: audio\iportclsnotifications.htm
old-project: audio
ms.assetid: 03F65E4E-C942-4748-8D3E-938A6AC51B2A
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcUnregisterIoTimeout
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10, version 1703 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPortClsNotifications
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# IPortClsNotifications interface



## -description
<p>An interface implemented by ports to provide
 notification helpers to miniports to support audio module communication.</p>
<p>For more information about audio modules, 
 see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/audio/implementing-audio-module-communication">Implementing Audio Module Discovery</a>. 
 </p>
<p>The miniport audio driver will call into their port to create and send the notification.  </p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPortClsNotifications</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPortClsNotifications</b> also has these types of members:</p>

<p>The <b>IPortClsNotifications</b> interface has these methods.</p>

<p>Allocates a buffer of the specified size, in the specified memory pool, for use in sending notifications, to allow for communications between audio modules and UWP apps. </p>

<p>Frees a previously allocated IPortClsNotifications buffer. The buffer is used in sending notifications, to allow for communications between audio modules and UWP apps. </p>

<p>Sends a notification to the listening UWP apps, to allow for communications between audio modules and UWP apps. </p>

<p> </p>

## -members
<p>The <b>IPortClsNotifications</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iportclsnotifications_allocnotification">IPortClsNotifications::AllocNotificationBuffer</a>
</td>
<td align="left" width="63%">
<p>Allocates a buffer of the specified size, in the specified memory pool, for use in sending notifications, to allow for communications between audio modules and UWP apps. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iportclsnotifications_freenotification">IPortClsNotifications::FreeNotificationBuffer</a>
</td>
<td align="left" width="63%">
<p>Frees a previously allocated IPortClsNotifications buffer. The buffer is used in sending notifications, to allow for communications between audio modules and UWP apps. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iportclsnotifications_sendnotification">IPortClsNotifications::SendNotification</a>
</td>
<td align="left" width="63%">
<p>Sends a notification to the listening UWP apps, to allow for communications between audio modules and UWP apps. </p>
</td>
</tr>
</table><p>Allocates a buffer of the specified size, in the specified memory pool, for use in sending notifications, to allow for communications between audio modules and UWP apps. </p>

<p>Frees a previously allocated IPortClsNotifications buffer. The buffer is used in sending notifications, to allow for communications between audio modules and UWP apps. </p>

<p>Sends a notification to the listening UWP apps, to allow for communications between audio modules and UWP apps. </p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 10, version 1703 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>