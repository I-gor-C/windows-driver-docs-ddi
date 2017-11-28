---
UID: NE.wdm._IO_CONTAINER_NOTIFICATION_CLASS
title: IO_CONTAINER_NOTIFICATION_CLASS
author: windows-driver-content
description: The IO_CONTAINER_NOTIFICATION_CLASS enumeration contains constants that indicate the classes of events for which a kernel-mode driver can register to receive notifications.
old-location: kernel\io_container_notification_class.htm
old-project: kernel
ms.assetid: cc2ce023-ebb1-4a8e-a06a-e2f11a89d258
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows 7 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IO_CONTAINER_NOTIFICATION_CLASS
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IO_CONTAINER_NOTIFICATION_CLASS enumeration



## -description
<p>The <b>IO_CONTAINER_NOTIFICATION_CLASS</b> enumeration contains constants that indicate the classes of events for which a kernel-mode driver can register to receive notifications.</p>


## -syntax

````
typedef enum _IO_CONTAINER_NOTIFICATION_CLASS { 
  IoSessionStateNotification       = 0,
  IoMaxContainerNotificationClass  = 1
} IO_CONTAINER_NOTIFICATION_CLASS;
````


## -enum-fields
<dl>

### -field <a id="IoSessionStateNotification"></a><a id="iosessionstatenotification"></a><a id="IOSESSIONSTATENOTIFICATION"></a><b>IoSessionStateNotification</b>

<dd>
<p>Session state notifications. The driver uses this enumeration constant to request notifications about changes in the state of user sessions that the driver is interested in.</p>
</dd>

### -field <a id="IoMaxContainerNotificationClass"></a><a id="iomaxcontainernotificationclass"></a><a id="IOMAXCONTAINERNOTIFICATIONCLASS"></a><b>IoMaxContainerNotificationClass</b>

<dd>
<p>Specifies the maximum value in this enumeration type. </p>
</dd>
</dl>

## -remarks
<p>To register for notifications, a driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549501">IoRegisterContainerNotification</a> routine and sets this routine's <i>NotificationClass</i> parameter to an <b>IO_CONTAINER_NOTIFICATION_CLASS</b> constant (other than <b>IoMaxContainerNotificationClass</b>). Currently, <b>IoRegisterContainerNotification</b> supports only <i>NotificationClass</i> = <b>IoSessionStateNotification</b>. </p>

<p>To register for notifications, a driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549501">IoRegisterContainerNotification</a> routine and sets this routine's <i>NotificationClass</i> parameter to an <b>IO_CONTAINER_NOTIFICATION_CLASS</b> constant (other than <b>IoMaxContainerNotificationClass</b>). Currently, <b>IoRegisterContainerNotification</b> supports only <i>NotificationClass</i> = <b>IoSessionStateNotification</b>. </p>

<p>To register for notifications, a driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549501">IoRegisterContainerNotification</a> routine and sets this routine's <i>NotificationClass</i> parameter to an <b>IO_CONTAINER_NOTIFICATION_CLASS</b> constant (other than <b>IoMaxContainerNotificationClass</b>). Currently, <b>IoRegisterContainerNotification</b> supports only <i>NotificationClass</i> = <b>IoSessionStateNotification</b>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 7 and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549501">IoRegisterContainerNotification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IO_CONTAINER_NOTIFICATION_CLASS enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
