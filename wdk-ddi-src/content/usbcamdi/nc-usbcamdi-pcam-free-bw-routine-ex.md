---
UID: NC.usbcamdi.PCAM_FREE_BW_ROUTINE_EX
title: PCAM_FREE_BW_ROUTINE_EX
author: windows-driver-content
description: A camera minidriver's CamFreeBandwidthEx callback function selects an alternate setting within the USB video streaming interface that uses no bandwidth.
old-location: stream\camfreebandwidthex.htm
old-project: stream
ms.assetid: ef6aa2bf-8b45-4048-ac21-b069e28b556f
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: USBC_FUNCTION_DESCRIPTOR, USBC_FUNCTION_DESCRIPTOR, *PUSBC_FUNCTION_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: usbcamdi.h
req.include-header: Usbcamdi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CamFreeBandwidthEx
req.alt-loc: usbcamdi.h
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
req.product: Windows 10 or later.
---

# PCAM_FREE_BW_ROUTINE_EX callback



## -description
<p>A camera minidriver's <b>CamFreeBandwidthEx</b> callback function selects an alternate setting within the USB video streaming interface that uses no bandwidth.</p>


## -prototype

````
PCAM_FREE_BW_ROUTINE_EX CamFreeBandwidthEx;

NTSTATUS CamFreeBandwidthEx(
   PDEVICE_OBJECT BusDeviceObject,
   PVOID          DeviceContext,
   ULONG          StreamNumber
)
{ ... }
````


## -parameters
<dl>

### -param <i>BusDeviceObject</i> 

<dd>
<p>Pointer to the camera minidriver's device object created by the USB hub.</p>
</dd>

### -param <i>DeviceContext</i> 

<dd>
<p>Pointer to the camera minidriver's device context.</p>
</dd>

### -param <i>StreamNumber</i> 

<dd>
<p>Indicates stream number.</p>
</dd>
</dl>

## -returns
<p><b>CamFreeBandwidthEx</b> returns STATUS_SUCCESS or an appropriate error code.</p>

## -remarks
<p>USBCAMD calls the camera minidriver's <b>CamFreeBandwidthEx</b> callback function after the isochronous video stream has stopped.</p>

<p>Typically, this function calls the <b>USBCAMD_SelectAlternateInterface</b> service to select the correct alternate interface and prepare for streaming video.</p>

<p>The original USBCAMD does not call <b>CamFreeBandwidthEx</b>.</p>

<p>This function is required.</p>

<p>USBCAMD calls the camera minidriver's <b>CamFreeBandwidthEx</b> callback function after the isochronous video stream has stopped.</p>

<p>Typically, this function calls the <b>USBCAMD_SelectAlternateInterface</b> service to select the correct alternate interface and prepare for streaming video.</p>

<p>The original USBCAMD does not call <b>CamFreeBandwidthEx</b>.</p>

<p>This function is required.</p>

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
<dt>Usbcamdi.h (include Usbcamdi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568590">USBCAMD_DEVICE_DATA2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568625">USBCAMD_SelectAlternateInterface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20CamFreeBandwidthEx routine%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
