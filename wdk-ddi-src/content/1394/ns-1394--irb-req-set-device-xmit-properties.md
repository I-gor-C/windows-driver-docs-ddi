---
UID: NS.1394._IRB_REQ_SET_DEVICE_XMIT_PROPERTIES
title: IRB_REQ_SET_DEVICE_XMIT_PROPERTIES
author: windows-driver-content
description: This structure contains the fields necessary to carry out a SetDeviceXmitProperties request.
old-location: ieee\irb_req_set_device_xmit_properties.htm
ms.assetid: 1E99F892-CD7C-411D-8832-08F988B9F2D7
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
req.alt-api: IRB_REQ_SET_DEVICE_XMIT_PROPERTIES
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
ms.keywords: IRB_REQ_SET_DEVICE_XMIT_PROPERTIES, IRB_REQ_SET_DEVICE_XMIT_PROPERTIES
---

# IRB_REQ_SET_DEVICE_XMIT_PROPERTIES structure



## -description
<p>This structure contains the fields necessary to carry out a SetDeviceXmitProperties request.</p>


## -syntax

````
typedef struct _IRB_REQ_SET_DEVICE_XMIT_PROPERTIES {
  ULONG fulSpeed;
  ULONG fulPriority;
} IRB_REQ_SET_DEVICE_XMIT_PROPERTIES;
````


## -struct-fields
<dl>

### -field <b>fulSpeed</b>

<dd>
<p>Specifies the maximum speed for transactions to the device. The possible speed values are SPEED_FLAGS_xxx, where xxx is the (approximate) transfer rate in megabits per second. Existing hardware supports transfer rates of 100, 200, and 400 Mb/sec.</p>
<table>
<tr>
<th>Transfer Rate</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>SPEED_FLAGS_100</p>
</td>
<td>
<p>100 Mb/s</p>
</td>
</tr>
<tr>
<td>
<p>SPEED_FLAGS_200</p>
</td>
<td>
<p>200 Mb/s</p>
</td>
</tr>
<tr>
<td>
<p>SPEED_FLAGS_400</p>
</td>
<td>
<p>400 Mb/s</p>
</td>
</tr>
</table>
<p> </p>
<p>Reserved.</p>
<div class="alert"><b>Note</b>  In Windows 7 and later versions of Windows, you can specify new values higher speed and  greater sized payloads. For more information, see <a href="buses.device_driver_interface__ddi__changes_in_windows_7#speed#speed">New Flags for Speed and Payload Size</a> and <a href="buses.device_driver_interface__ddi__changes_in_windows_7#ioctl#ioctl">IEEE 1394 IOCTL Changes</a> in Device Driver Interface (DDI) Changes in Windows 7.</div>
<div> </div>
</dd>

### -field <b>fulPriority</b>

<dd>
<p>Specifies the priority.</p>
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