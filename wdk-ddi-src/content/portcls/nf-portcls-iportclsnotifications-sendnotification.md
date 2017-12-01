---
UID: NF.portcls.IPortClsNotifications.SendNotification
title: IPortClsNotifications::SendNotification
author: windows-driver-content
description: Sends a notification to the listening UWP apps, to allow for communications between audio modules and UWP apps.
old-location: audio\iportclsnotifications_sendnotification.htm
old-project: audio
ms.assetid: 0683C30D-0AAD-4859-BA30-908FA747CC35
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IPortClsNotifications, SendNotification, IPortClsNotifications::SendNotification
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 10, version 1703 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPortClsNotifications.SendNotification
req.alt-loc: Portcls.lib,Portcls.dll
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
req.iface: IPortClsNotifications
---

# IPortClsNotifications::SendNotification method



## -description
<p>Sends a notification to the listening UWP apps, to allow for communications between audio modules and UWP apps. </p>


## -syntax

````
NTSTATUS  SendNotification(
  [in] Const GUID*   NotificationId,
  [in] Notification PPCNOTIFICATION* 
);
````


## -parameters
<dl>

### -param <i> NotificationId</i> [in]

<dd>
<p>KSNOTIFICATIONID_AudioModule
</p>
</dd>

### -param <i>PPCNOTIFICATION* </i> [in]

<dd>
<p>Pointer to a <a href="..\portcls\ns-portcls--pcnotification-buffer.md">PCNOTIFICATION_BUFFER</a> structure to send to the listening audio module UWP clients. </p>
</dd>
</dl>

## -returns
<p>This function returns void.</p>

## -remarks
<p>Pointer to the PCNOTIFICATION structure to send to Audio Module clients.

The expected format of the payload is a <a href="..\ksmedia\ns-ksmedia--ksaudiomodule-notification.md">KSAUDIOMODULE_NOTIFICATION</a> structure. The miniport driver can optionally send additional information immediately following the <b>KSAUDIOMODULE_NOTIFICATION</b> structure that will be untouched and sent to the Audio Module clients.

</p>

<p>For more information about audio modules, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/audio/implementing-audio-module-communication">Implementing Audio Module Discovery</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-iportclsnotifications.md">IPortClsNotifications</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortClsNotifications::SendNotification method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
