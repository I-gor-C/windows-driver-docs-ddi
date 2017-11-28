---
UID: NS.1394._BUS_RESET_DATA
title: BUS_RESET_DATA
author: windows-driver-content
description: The BUS_RESET_DATA structure specifies the context for the extended bus reset notification routine.
old-location: ieee\bus_reset_data.htm
old-project: IEEE
ms.assetid: 82A01880-AC8D-4285-A780-EE195F186B71
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: BUS_RESET_DATA, BUS_RESET_DATA, *PBUS_RESET_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 1394.h
req.include-header: 1394.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BUS_RESET_DATA
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
---

# BUS_RESET_DATA structure



## -description
<p>The <b>BUS_RESET_DATA</b> structure specifies the context for the extended bus reset notification routine. </p>


## -syntax

````
typedef struct _BUS_RESET_DATA {
  PVOID        ResetContext;
  ULONG        GenerationCount;
  NODE_ADDRESS DeviceNodeId;
  NODE_ADDRESS LocalNodeId;
  UCHAR        SpeedToNode;
} BUS_RESET_DATA, *PBUS_RESET_DATA;
````


## -struct-fields
<dl>

### -field <b>ResetContext</b>

<dd>
<p>Pointer to a client driver-defined context when a bus reset occurs. The argument that is specified in the <b>u.BusResetNotification.ResetContext</b> parameter when the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537638">REQUEST_BUS_RESET_NOTIFICATION</a> request is sent.</p>
</dd>

### -field <b>GenerationCount</b>

<dd>
<p>The current generation of the 1394 bus.</p>
</dd>

### -field <b>DeviceNodeId</b>

<dd>
<p>The 1394 address for the device.</p>
</dd>

### -field <b>LocalNodeId</b>

<dd>
<p>The 1394 address for the local host.</p>
</dd>

### -field <b>SpeedToNode</b>

<dd>
<p>The negotiated speed to the device. The possible values are as follows:</p>
<table>
<tr>
<th>Flag</th>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>SPEED_FLAGS_800</td>
<td>0x08</td>
<td>    800 Mb/s</td>
</tr>
<tr>
<td>SPEED_FLAGS_1600</td>
<td>0x10</td>
<td>160 Mb/s</td>
</tr>
<tr>
<td>SPEED_FLAGS_3200</td>
<td>0x20</td>
<td>3200 Mb/s</td>
</tr>
</table>
<p> </p>
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
<p>Available in Windows 7 and later versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1394.h (include 1394.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="NULL">Device Driver Interface (DDI) Changes in Windows 7</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20BUS_RESET_DATA structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
