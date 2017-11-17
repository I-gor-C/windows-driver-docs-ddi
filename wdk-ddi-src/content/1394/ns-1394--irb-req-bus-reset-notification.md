---
UID: NS.1394._IRB_REQ_BUS_RESET_NOTIFICATION
title: IRB_REQ_BUS_RESET_NOTIFICATION
author: windows-driver-content
description: This structure contains the fields necessary for the 1394 bus driver to carry out a bus reset notification request.
old-location: ieee\irb_req_bus_reset_notification.htm
ms.assetid: 3EF9BB26-81B2-4ED7-A934-AF3E73B650A0
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 1394.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRB_REQ_BUS_RESET_NOTIFICATION
req.alt-loc: 1394.h
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
ms.keywords: IRB_REQ_BUS_RESET_NOTIFICATION, IRB_REQ_BUS_RESET_NOTIFICATION
---

# IRB_REQ_BUS_RESET_NOTIFICATION structure



## -description
<p>This structure contains the fields necessary for the 1394 bus driver to carry out a bus reset notification request. </p>
<p>This is the suggested method for a client driver on top of the 1394 bus driver to get notified about 1394 bus resets. The client registers by using this IRB in its START_DEVICE routine, and de-registers using the same IRB, but with different flags, in its REMOVE routine. </p>
<p>This notification is only issued if after the bus reset, the target device is still present on the bus. This way the caller does not have to verify that the target device is on the bus.</p>


## -syntax

````
typedef struct _IRB_REQ_BUS_RESET_NOTIFICATION {
  ULONG                       fulFlags;
  PBUS_BUS_RESET_NOTIFICATION ResetRoutine;
  PVOID                       ResetContext;
} IRB_REQ_BUS_RESET_NOTIFICATION;
````


## -struct-fields
<dl>

### -field <b>fulFlags</b>

<dd>
<p>Specifies whether a callback should be registered or deactivated. Use REGISTER_NOTIFICATION_ROUTINE to register <b>ResetRoutine</b> as the callback. Use DEREGISTER_NOTIFICATION_ROUTINE to deactivate any previously registered callback.</p>
<div class="alert"><b>Note</b>  In Windows 7 and later, set the EXTENDED_NOTIFICATION_ROUTINE flag  to register for extended bus reset notifications supported by the new IEEE 1394 bus driver. This notification returns information about the current generation of the bus, such as the generation count and node ids, to 1394 client drivers in the context of the bus reset notification.</div>
<div> </div>
</dd>

### -field <b>ResetRoutine</b>

<dd>
<p>Points to the notification routine for bus resets. The notification routine parameters follow this prototype:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>void BusResetNotificationRoutine(IN PVOID Context);
 </pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>ResetContext</b>

<dd>
<p>Specifies the argument to be passed to the notification routine.</p>
<p>When the EXTENDED_NOTIFICATION_ROUTINE flag is specified, <b>ResetContext</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/gg266399">BUS_RESET_DATA</a> structure. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1394.h</dt>
</dl>
</td>
</tr>
</table>