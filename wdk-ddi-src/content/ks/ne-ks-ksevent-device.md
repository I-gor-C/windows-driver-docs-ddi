---
UID: NE.ks.KSEVENT_DEVICE
title: KSEVENT_DEVICE
author: windows-driver-content
description: Specifies event notifications that the driver generates to indicate that a device has been lost or preempted.
old-location: stream\ksevent_device.htm
old-project: stream
ms.assetid: 92594bdd-a458-4262-ac4c-013cffb7a725
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSEVENT_DEVICE
req.alt-loc: Ks.h
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
req.iface: 
---

# KSEVENT_DEVICE enumeration



## -description
<p>Specifies event notifications that the driver generates to indicate that a device has been lost or preempted.</p>


## -syntax

````
typedef enum  { 
  KSEVENT_DEVICE_LOST       = 0,
  KSEVENT_DEVICE_PREEMPTED  = 1
} KSEVENT_DEVICE;
````


## -enum-fields
<dl>

### -field <a id="KSEVENT_DEVICE_LOST"></a><a id="ksevent_device_lost"></a><b>KSEVENT_DEVICE_LOST</b>

<dd>
<p>A camera device has been removed from the system. See <a href="https://msdn.microsoft.com/library/windows/hardware/jj156039">KSEVENT_DEVICE_LOST</a>.</p>
</dd>

### -field <a id="KSEVENT_DEVICE_PREEMPTED"></a><a id="ksevent_device_preempted"></a><b>KSEVENT_DEVICE_PREEMPTED</b>

<dd>
<p>A camera device has been preempted by a new Windows app. See <a href="https://msdn.microsoft.com/library/windows/hardware/jj156040">KSEVENT_DEVICE_PREEMPTED</a>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj156039">KSEVENT_DEVICE_LOST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj156040">KSEVENT_DEVICE_PREEMPTED</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSEVENT_DEVICE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
