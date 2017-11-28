---
UID: NE.ksmedia.KSEVENT_CAMERACONTROL
title: KSEVENT_CAMERACONTROL
author: windows-driver-content
description: Specifies camera control event notifications that the driver generates to indicate that an operation has been completed or canceled.
old-location: stream\ksevent_cameracontrol.htm
old-project: stream
ms.assetid: 10d08e58-cd1f-4585-a93b-fabeb4fcf27c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSEVENT_CAMERACONTROL
req.alt-loc: Ksmedia.h
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

# KSEVENT_CAMERACONTROL enumeration



## -description
<p>Specifies camera control event notifications that the driver generates to indicate that an operation has been completed or canceled.</p>


## -syntax

````
typedef enum  { 
  KSEVENT_CAMERACONTROL_FOCUS  = 0,
  KSEVENT_CAMERACONTROL_ZOOM   = 1
} KSEVENT_CAMERACONTROL;
````


## -enum-fields
<dl>

### -field <a id="KSEVENT_CAMERACONTROL_FOCUS"></a><a id="ksevent_cameracontrol_focus"></a><b>KSEVENT_CAMERACONTROL_FOCUS</b>

<dd>
<p>A camera focus operation has completed or has been canceled. See <a href="https://msdn.microsoft.com/library/windows/hardware/jj156037">KSEVENT_CAMERACONTROL_FOCUS</a>.</p>
</dd>

### -field <a id="KSEVENT_CAMERACONTROL_ZOOM"></a><a id="ksevent_cameracontrol_zoom"></a><b>KSEVENT_CAMERACONTROL_ZOOM</b>

<dd>
<p>A camera zoom operation has completed or has been canceled. See <a href="https://msdn.microsoft.com/library/windows/hardware/jj156038">KSEVENT_CAMERACONTROL_ZOOM</a>.</p>
</dd>
</dl>

## -remarks
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/jj151593">KSPROPERTY_CAMERACONTROL_S_EX</a>.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/jj151593">KSPROPERTY_CAMERACONTROL_S_EX</a>.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/jj151593">KSPROPERTY_CAMERACONTROL_S_EX</a>.</p>

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
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj156037">KSEVENT_CAMERACONTROL_FOCUS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj156038">KSEVENT_CAMERACONTROL_ZOOM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj151593">KSPROPERTY_CAMERACONTROL_S_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSEVENT_CAMERACONTROL enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
