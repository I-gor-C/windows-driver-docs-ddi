---
UID: NC.ks.PFNKSDEVICESETPOWER
title: PFNKSDEVICESETPOWER
author: windows-driver-content
description: AVStream calls a minidriver's AVStrMiniDeviceSetPower routine when it receives an IRP_MN_SET_POWER.
old-location: stream\avstrminidevicesetpower.htm
old-project: stream
ms.assetid: 40d5eb14-b7bd-42b6-a3f5-fe9e8c5c806e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AVStrMiniDeviceSetPower
req.alt-loc: ks.h
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

# PFNKSDEVICESETPOWER callback



## -description
<p>AVStream calls a minidriver's <i>AVStrMiniDeviceSetPower</i> routine when it receives an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a>.</p>


## -prototype

````
PFNKSDEVICESETPOWER AVStrMiniDeviceSetPower;

void AVStrMiniDeviceSetPower(
  _In_ PKSDEVICE          Device,
  _In_ PIRP               Irp,
  _In_ DEVICE_POWER_STATE To,
  _In_ DEVICE_POWER_STATE From
)
{ ... }
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>Pointer to the <a href="..\ks\ns-ks--ksdevice.md">KSDEVICE</a> structure that received the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a>.</p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a> issued by <i>Device</i>.</p>
</dd>

### -param <i>To</i> [in]

<dd>
<p>The target device power state.</p>
</dd>

### -param <i>From</i> [in]

<dd>
<p>The current device power state.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If a driver has registered its device for idle detection, the power manager sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a> to change the power state of an idle device.</p>

<p>The minidriver specifies this routine's address in the <b>SetPower</b> member of its <a href="..\ks\ns-ks--ksdevice-dispatch.md">KSDEVICE_DISPATCH</a> structure.</p>

<p>This routine is optional.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
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
<a href="..\ks\ns-ks--ksdevice-dispatch.md">KSDEVICE_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVStrMiniDeviceSetPower routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
