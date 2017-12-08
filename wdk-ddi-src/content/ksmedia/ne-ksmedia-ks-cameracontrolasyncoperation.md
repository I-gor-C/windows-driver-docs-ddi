---
UID: NE.ksmedia.KS_CameraControlAsyncOperation
title: KS_CameraControlAsyncOperation
author: windows-driver-content
description: Defines notifications that the driver uses to start and stop an asynchronous camera operation, including setting the flash, the image pin control properties, the region of interest in the image, or video stabilization.
old-location: stream\ks_cameracontrolasyncoperation.htm
old-project: stream
ms.assetid: 0ca676d9-5047-451a-abbb-2692cc2d69f6
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: KS_CameraControlAsyncOperation
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

# KS_CameraControlAsyncOperation enumeration



## -description
<p>Defines notifications that the driver uses to start and stop an asynchronous camera operation, including setting the flash, the image pin control properties, the region of interest in the image, or video stabilization.</p>


## -syntax

````
typedef enum  { 
  KS_CAMERACONTROL_ASYNC_START  = 0x0001,
  KS_CAMERACONTROL_ASYNC_STOP   = 0x0002,
  KS_CAMERACONTROL_ASYNC_RESET  = 0x0003
} KS_CameraControlAsyncOperation;
````


## -enum-fields
<dl>

### -field KS_CAMERACONTROL_ASYNC_START

<dd>
<p>Initiate an asynchronous camera control operation.</p>
</dd>

### -field KS_CAMERACONTROL_ASYNC_STOP

<dd>
<p>Stop the requested asynchronous camera control operation and maintain current camera control settings, including the lens focus.</p>
</dd>

### -field KS_CAMERACONTROL_ASYNC_RESET

<dd>
<p>Stop the requested asynchronous camera control operation and reset the lens focus to infinity.</p>
</dd>
</dl>

## -remarks
<p>For more information, see <a href="stream.ksproperty_cameracontrol_s_ex">KSPROPERTY_CAMERACONTROL_S_EX</a>.</p>

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
<a href="stream.ksproperty_cameracontrol_s_ex">KSPROPERTY_CAMERACONTROL_S_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_CameraControlAsyncOperation enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
