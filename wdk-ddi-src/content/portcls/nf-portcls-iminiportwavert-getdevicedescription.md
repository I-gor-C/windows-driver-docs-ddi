---
UID: NF.portcls.IMiniportWaveRT.GetDeviceDescription
title: IMiniportWaveRT::GetDeviceDescription
author: windows-driver-content
description: The GetDeviceDescription method returns a pointer to a DEVICE_DESCRIPTION structure describing the device.
old-location: audio\iminiportwavert_getdevicedescription.htm
old-project: audio
ms.assetid: c6c0da06-c304-4d2d-907c-ccbb141c385b
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IMiniportWaveRT, GetDeviceDescription, IMiniportWaveRT::GetDeviceDescription
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportWaveRT.GetDeviceDescription
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Passive level
req.iface: IMiniportWaveRT
---

# IMiniportWaveRT::GetDeviceDescription method



## -description
<p>The <code>GetDeviceDescription</code> method returns a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543107">DEVICE_DESCRIPTION</a> structure describing the device.</p>


## -syntax

````
NTSTATUS GetDeviceDescription(
  [out] PDEVICE_DESCRIPTION DeviceDescription
);
````


## -parameters
<dl>

### -param <i>DeviceDescription</i> [out]

<dd>
<p>Pointer to a DEVICE_DESCRIPTION structure to be filled in by the miniport. The caller specifies a valid, non-NULL pointer value for this parameter.</p>
</dd>
</dl>

## -returns
<p><code>GetDeviceDescription</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error status code.</p>

## -remarks
<p>The <i>DeviceDescription</i> parameter contains a pointer to a DEVICE_DESCRIPTION structure that the miniport fills in to describe the device</p>

<p>The <i>DeviceDescription</i> parameter contains a pointer to a DEVICE_DESCRIPTION structure that the miniport fills in to describe the device</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Passive level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536737">IMiniportWaveRT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536920">IPortWaveRT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543107">DEVICE_DESCRIPTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportWaveRT::GetDeviceDescription method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
