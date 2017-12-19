---
UID: NF.storport.StorPortNotification
title: StorPortNotification function
author: windows-driver-content
description: The miniport driver uses the StorPortNotification routine to notify the Storport driver of certain events and conditions.
old-location: storage\storportnotification.htm
old-project: storage
ms.assetid: 3f361f50-3ca2-4fb6-828c-27928b50cf55
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: StorPortNotification
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortNotification
req.alt-loc: Storport.lib,Storport.dll
req.ddi-compliance: StorPortNotification2, StorPortStatusPending, StorPortTimer
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# StorPortNotification function



## -description
The miniport driver uses the <b>StorPortNotification</b> routine to notify the Storport driver of certain events and conditions.

The <b>StorPortNotification</b> routine takes a variable number of parameters depending on the notification type specified.



## -syntax

````
VOID StorPortNotification(
   IN SCSI_NOTIFICATION_TYPE NotificationType,
   IN PVOID                  HwDeviceExtension,
   ...                       arguments
);
````


## -parameters

### -param NotificationType 

Specifies the notification type, which can be one of the following values.

<table>
<tr>
<th>Notification type</th>
<th>Description</th>
</tr>
<tr>
<td>

<a href="storage.storportnotification__notificationtype___bufferoverrundetected_">BufferOverrunDetected</a>


</td>
<td>
This notification type has no arguments and gives the miniport driver an opportunity to bugcheck the system if it detects a corruption.

</td>
</tr>
<tr>
<td>

<a href="storage.storportnotification__notificationtype___buschangedetected_">BusChangeDetected</a>


</td>
<td>
Indicates that a target device might have been added or removed from a dynamic bus.

</td>
</tr>
<tr>
<td>

<a href="storage.iotargetrequestservicetime">IoTargetRequestServiceTime</a>


</td>
<td>
Indicates to Storport the amount of time that was required to process a specified request.

</td>
</tr>
<tr>
<td>

<a href="storage.storportnotification__notificationtype___linkdown_">LinkDown</a>


</td>
<td>
Indicates that the link is down and will probably be down for some time. StorPort will pause the adapter in response to this notification.

</td>
</tr>
<tr>
<td>

<a href="storage.storportnotification__notificationtype___linkup_">LinkUp</a>


</td>
<td>
Indicates that the link has been restored. StorPort restarts the adapter so that it can resume operation in response to this notification. Miniport drivers should not send this notification unless the link is down.

</td>
</tr>
<tr>
<td>

<a href="storage.storportnotification__notificationtype___querytickcount_">QueryTickCount</a>


</td>
<td>
This notification type returns a LARGE_INTEGER that holds the value from <a href="kernel.kequerytickcount">KeQueryTickCount</a>.

</td>
</tr>
<tr>
<td>

<a href="storage.storportnotification__notificationtype___requestcomplete_">RequestComplete</a>


</td>
<td>
Indicates that the given SRB has finished. After this notification is sent, the port driver owns the request.

</td>
</tr>
<tr>
<td>

<a href="storage.storportnotification__notificationtype___requesttimercall_">RequestTimerCall</a>


</td>
<td>
Indicates that the miniport driver requires the port driver to call the miniport driver's <a href="storage.hwstortimer">HwStorTimer</a> routine in the requested number of microseconds.

</td>
</tr>
<tr>
<td>

<a href="storage.storportnotification__notificationtype___resetdetected_">ResetDetected</a>


</td>
<td>
Indicates that the HBA has detected a reset on the bus. After this notification is sent, the miniport driver is still responsible for completing any active requests. The port driver will manage all required bus-reset delays.

</td>
</tr>
<tr>
<td>

<a href="storage.storportnotification__notificationtype___wmievent__pathid____0xff_">WMIEvent</a>


</td>
<td>
Indicates that the miniport driver has detected an event for which one or more WMI data consumers are registered.

</td>
</tr>
<tr>
<td>

<a href="storage.storportnotification__notificationtype___wmireregister__pathid____0xff">WMIReregister</a>


</td>
<td>
Indicates that the miniport driver has changed the data items or the number of instances of a given data block that was previously registered by calling <a href="kernel.iowmiregistrationcontrol">IoWMIRegistrationControl</a>.

</td>
</tr>
</table>
 


### -param HwDeviceExtension 

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls <a href="storage.storportinitialize">StorPortInitialize</a>. The port driver frees this memory when it removes the device.


### -param arguments 

Specifies the arguments corresponding to the notification type.


## -returns
None.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.storport_storportnotification2">StorPortNotification2</a>, <a href="devtest.storport_storportstatuspending">StorPortStatusPending</a>, <a href="devtest.storport_storporttimer">StorPortTimer</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.storportinitialize">StorPortInitialize</a>
</dt>
<dt>
<a href="storage.storportnotification__notificationtype___bufferoverrundetected_">StorPortNotification for BufferOverrunDetected</a>
</dt>
<dt>
<a href="storage.storportnotification__notificationtype___buschangedetected_">StorPortNotification for BusChangeDetected</a>
</dt>
<dt>
<a href="storage.storportnotification__notificationtype___linkdown_">StorPortNotification for LinkDown</a>
</dt>
<dt>
<a href="storage.storportnotification__notificationtype___linkup_">StorPortNotification for LinkUp</a>
</dt>
<dt>
<a href="storage.storportnotification__notificationtype___querytickcount_">StorPortNotification for QueryTickCount</a>
</dt>
<dt>
<a href="storage.storportnotification__notificationtype___requestcomplete_">StorPortNotification for RequestComplete</a>
</dt>
<dt>
<a href="storage.storportnotification__notificationtype___requesttimercall_">StorPortNotification for RequestTimerCall</a>
</dt>
<dt>
<a href="storage.storportnotification__notificationtype___resetdetected_">StorPortNotification for ResetDetected</a>
</dt>
<dt>
<a href="storage.storportnotification__notificationtype___wmievent__pathid____0xff_">StorPortNotification for WMIEvent</a>
</dt>
<dt>
<a href="storage.storportnotification__notificationtype___wmireregister__pathid____0xff">StorPortNotification for WMIReregister</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortNotification routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

