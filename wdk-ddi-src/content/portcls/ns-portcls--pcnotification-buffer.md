---
UID: NS.portcls._PCNOTIFICATION_BUFFER
title: PCNOTIFICATION_BUFFER
author: windows-driver-content
description: The notification buffer used by IPortClsNotifications.
old-location: audio\pcnotification_buffer.htm
old-project: audio
ms.assetid: EEE091E4-29D1-4C6F-B543-C54736660CCA
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PCNOTIFICATION_BUFFER, PCNOTIFICATION_BUFFER, *PPCNOTIFICATION_BUFFER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCNOTIFICATION_BUFFER
req.alt-loc: Portcls.h
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

# PCNOTIFICATION_BUFFER structure



## -description
<p>The notification buffer used by <a href="audio.iportclsnotifications">IPortClsNotifications</a>.</p>


## -syntax

````
typedef struct _PCNOTIFICATION_BUFFER {
  UCHAR NotificationBuffer[1];
} PCNOTIFICATION_BUFFER, *PPCNOTIFICATION_BUFFER;
````


## -struct-fields
<dl>

### -field <b>NotificationBuffer</b>

<dd>
<p>The notification buffer used by <a href="audio.iportclsnotifications">IPortClsNotifications</a>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 10, version 1703</p>
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

## -see-also
<dl>
<dt>
<a href="audio.iportclsnotifications">IPortClsNotifications</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PCNOTIFICATION_BUFFER structure%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
