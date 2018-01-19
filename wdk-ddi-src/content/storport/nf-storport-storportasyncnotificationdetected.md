---
UID : NF:storport.StorPortAsyncNotificationDetected
title : StorPortAsyncNotificationDetected function
author : windows-driver-content
description : A storage miniport driver calls StorPortAsyncNotificationDetected to notify the Storport driver of a storage device status change event.
old-location : storage\storportasyncnotificationdetected.htm
old-project : storage
ms.assetid : 558F652C-6D1A-4BAF-9C2C-3F4FE24651D2
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : StorPortAsyncNotificationDetected
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : storport.h
req.include-header : Storport.h
req.target-type : Universal
req.target-min-winverclnt : Available starting with Windows 8.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : StorPortAsyncNotificationDetected
req.alt-loc : storport.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : Any
req.typenames : STOR_SPINLOCK
req.product : Windows 10 or later.
---


# StorPortAsyncNotificationDetected function
A storage miniport driver calls <b>StorPortAsyncNotificationDetected</b> to  notify the Storport driver of a storage device status change event.

The notification is queued as a work item for deferred processing at DISPATCH_LEVEL or lower IRQL.

## Syntax

````
ULONG StorPortAsyncNotificationDetected(
  _In_ PVOID         HwDeviceExtension,
       PSTOR_ADDRESS Address,
       ULONGLONG     Flags
);
````

## Parameters

`HwDeviceExtension`

A pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls <a href="..\storport\nf-storport-storportinitialize.md">StorPortInitialize</a>. The port driver frees this memory when it removes the device.

`Address`

The address of the storage device with a status change event.

`Flags`

The status notifications to indicate to Storport.


The Flags parameter contains a bitwise OR combination of status notifications. All status values can be set with the single <b>RAID_ASYNC_NOTIFY_SUPPORTED_FLAGS</b> value.



<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>


## Return Value

A status value indicating the result of the notification. This can be one of these values:
<dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl>The state change notification is scheduled for processing.
<dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl>The address type invalid.

-or-

<i>HwDeviceExtension</i> is <b>NULL</b>.

-or-

<i>Flags</i> contains an undefined value.
<dl>
<dt><b>STOR_STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl>The storage device unit cannot be found at <i>address</i>.

-or-

The storage device does not support asynchronous notifications.
<dl>
<dt><b>STOR_STATUS_BUSY</b></dt>
</dl>A prior notification is in process and this one cannot be scheduled.

## Remarks

A miniport can detect status events in its <a href="..\storport\nc-storport-hw_interrupt.md">HwStorInterrupt</a> routine and call <b>StorPortAsyncNotificationDetected</b> to queue and process the status change notification later at a lower IRQL. 

When processed by Storport, the status event notification is forwarded to the storage class driver to initiate any necessary system response actions.

If the <i>Flags</i> parameter is 0, Storport will indicate all status values in its notification to the storage class driver.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | storport.h (include Storport.h) |
| **Library** |  |
| **IRQL** | Any |
| **DDI compliance rules** |  |