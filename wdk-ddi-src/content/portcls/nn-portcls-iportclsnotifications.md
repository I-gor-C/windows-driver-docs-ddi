---
UID: NN.portcls.IPortClsNotifications
title: IPortClsNotifications
author: windows-driver-content
description: An interface implemented by ports to provide notification helpers to miniports to support audio module communication.
old-location: audio\iportclsnotifications.htm
old-project: audio
ms.assetid: 03F65E4E-C942-4748-8D3E-938A6AC51B2A
ms.author: windowsdriverdev
ms.date: 12/6/2017
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
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
---

# IPortClsNotifications interface



## -description
An interface implemented by ports to provide
 notification helpers to miniports to support audio module communication.

For more information about audio modules, 
 see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/audio/implementing-audio-module-communication">Implementing Audio Module Discovery</a>. 
 

The miniport audio driver will call into their port to create and send the notification.  



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPortClsNotifications</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPortClsNotifications</b> also has these types of members:

The <b>IPortClsNotifications</b> interface has these methods.

Allocates a buffer of the specified size, in the specified memory pool, for use in sending notifications, to allow for communications between audio modules and UWP apps. 

Frees a previously allocated IPortClsNotifications buffer. The buffer is used in sending notifications, to allow for communications between audio modules and UWP apps. 

Sends a notification to the listening UWP apps, to allow for communications between audio modules and UWP apps. 

 


## -members
The <b>IPortClsNotifications</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iportclsnotifications_allocnotification">IPortClsNotifications::AllocNotificationBuffer</a>
</td>
<td align="left" width="63%">
Allocates a buffer of the specified size, in the specified memory pool, for use in sending notifications, to allow for communications between audio modules and UWP apps. 

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iportclsnotifications_freenotification">IPortClsNotifications::FreeNotificationBuffer</a>
</td>
<td align="left" width="63%">
Frees a previously allocated IPortClsNotifications buffer. The buffer is used in sending notifications, to allow for communications between audio modules and UWP apps. 

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iportclsnotifications_sendnotification">IPortClsNotifications::SendNotification</a>
</td>
<td align="left" width="63%">
Sends a notification to the listening UWP apps, to allow for communications between audio modules and UWP apps. 

</td>
</tr>
</table>Allocates a buffer of the specified size, in the specified memory pool, for use in sending notifications, to allow for communications between audio modules and UWP apps. 

Frees a previously allocated IPortClsNotifications buffer. The buffer is used in sending notifications, to allow for communications between audio modules and UWP apps. 

Sends a notification to the listening UWP apps, to allow for communications between audio modules and UWP apps. 

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows 10, version 1703 and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>