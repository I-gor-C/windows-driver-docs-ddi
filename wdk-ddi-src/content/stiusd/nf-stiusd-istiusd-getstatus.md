---
UID: NF.stiusd.IStiUSD.GetStatus
title: IStiUSD::GetStatus
author: windows-driver-content
description: A still image minidriver's IStiUSD::GetStatus method returns the status of a still image device.
old-location: image\istiusd_getstatus.htm
ms.assetid: 24133d1d-eac4-4740-9635-1205f7a2c4d4
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: stiusd.h
req.include-header: Stiusd.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IStiUSD.GetStatus
req.alt-loc: stiusd.h
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
ms.keywords: IStiUSD, GetStatus, IStiUSD::GetStatus
req.iface: IStiUSD
req.product: Windows 10 or later.
---

# IStiUSD::GetStatus method



## -description
<p>A still image minidriver's <b>IStiUSD::GetStatus</b> method returns the status of a still image device.</p>


## -syntax

````
HRESULT GetStatus(
   PSTI_DEVICE_STATUS pDevStatus
);
````


## -parameters
<dl>

### -param <i>pDevStatus</i> 

<dd>
<p>Caller-supplied pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548369">STI_DEVICE_STATUS</a> structure.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method should return S_OK. Otherwise, it should return one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The caller supplies values for the <b>dwSize</b> and <b>StatusMask</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548369">STI_DEVICE_STATUS</a> structure, and the minidriver must supply values for the rest of the structure members.</p>

<p>If the driver has previously set the STI_GENCAP_POLLING_NEEDED flag in the device's <a href="https://msdn.microsoft.com/library/windows/hardware/ff548380">STI_DEV_CAPS</a> structure, the minidriver's <b>IStiUSD::GetStatus</b> method is the means by which the event monitor determines if a <a href="NULL">Still Image Device Events</a> has occurred. The event monitor will call the method, specifying STI_DEVSTATUS_EVENT_STATE in the supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff548369">STI_DEVICE_STATUS</a> structure. The driver must poll the device and set STI_EVENTHANDLING_PENDING if an event has occurred.</p>

<p>If the caller specifies STI_DEVSTATUS_ONLINE_STATE in the supplied STI_DEVICE_STATUS structure, the minidriver should set the appropriate flag in the structure's <b>dwOnlineState</b> member.</p>

<p>The caller supplies values for the <b>dwSize</b> and <b>StatusMask</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548369">STI_DEVICE_STATUS</a> structure, and the minidriver must supply values for the rest of the structure members.</p>

<p>If the driver has previously set the STI_GENCAP_POLLING_NEEDED flag in the device's <a href="https://msdn.microsoft.com/library/windows/hardware/ff548380">STI_DEV_CAPS</a> structure, the minidriver's <b>IStiUSD::GetStatus</b> method is the means by which the event monitor determines if a <a href="NULL">Still Image Device Events</a> has occurred. The event monitor will call the method, specifying STI_DEVSTATUS_EVENT_STATE in the supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff548369">STI_DEVICE_STATUS</a> structure. The driver must poll the device and set STI_EVENTHANDLING_PENDING if an event has occurred.</p>

<p>If the caller specifies STI_DEVSTATUS_ONLINE_STATE in the supplied STI_DEVICE_STATUS structure, the minidriver should set the appropriate flag in the structure's <b>dwOnlineState</b> member.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Stiusd.h (include Stiusd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543752">IStiDevice::GetStatus</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IStiUSD::GetStatus method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
