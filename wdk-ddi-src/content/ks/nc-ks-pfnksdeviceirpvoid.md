---
UID: NC.ks.PFNKSDEVICEIRPVOID
title: PFNKSDEVICEIRPVOID
author: windows-driver-content
description: An AVStream minidriver's AVStrMiniDeviceCancelRemove routine is called when an IRP_MN_CANCEL_REMOVE_DEVICE is dispatched by the device.
old-location: stream\avstrminidevicecancelremove.htm
old-project: stream
ms.assetid: 993d6530-9183-4f23-ba74-5ab8a6f5da7b
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
req.alt-api: AVStrMiniDeviceCancelRemove
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

# PFNKSDEVICEIRPVOID callback



## -description
<p>An AVStream minidriver's <i>AVStrMiniDeviceCancelRemove</i> routine is called when an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550823">IRP_MN_CANCEL_REMOVE_DEVICE</a> is dispatched by the device.</p>


## -prototype

````
PFNKSDEVICEIRPVOID AVStrMiniDeviceCancelRemove;

void AVStrMiniDeviceCancelRemove(
  _In_ PKSDEVICE Device,
  _In_ PIRP      Irp
)
{ ... }
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>Pointer to the <a href="..\ks\ns-ks--ksdevice.md">KSDEVICE</a> that dispatched the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550823">IRP_MN_CANCEL_REMOVE_DEVICE</a>.</p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff550823">IRP_MN_CANCEL_REMOVE_DEVICE</a> issued by <i>Device</i>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The minidriver specifies this routine's address in the <b>CancelRemove</b> member of its <a href="..\ks\ns-ks--ksdevice-dispatch.md">KSDEVICE_DISPATCH</a> structure.</p>

<p>This routine is called when an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550823">IRP_MN_CANCEL_REMOVE_DEVICE</a> is dispatched by the device.</p>

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
<a href="..\ks\ns-ks--ksdevice.md">KSDEVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVStrMiniDeviceCancelRemove routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
