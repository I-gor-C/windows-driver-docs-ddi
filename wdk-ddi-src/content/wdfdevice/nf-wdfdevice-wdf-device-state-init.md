---
UID: NF.wdfdevice.WDF_DEVICE_STATE_INIT
title: WDF_DEVICE_STATE_INIT
author: windows-driver-content
description: The WDF_DEVICE_STATE_INIT function initializes a driver's WDF_DEVICE_STATE structure.
old-location: wdf\wdf_device_state_init.htm
old-project: wdf
ms.assetid: f8c040aa-bfa0-4b74-ad0a-8796f1cfc4b8
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_DEVICE_STATE_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_DEVICE_STATE_INIT
req.alt-loc: wdfdevice.h
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

# WDF_DEVICE_STATE_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_DEVICE_STATE_INIT</b> function initializes a driver's <a href="..\wdfdevice\ns-wdfdevice--wdf-device-state.md">WDF_DEVICE_STATE</a> structure.</p>


## -syntax

````
VOID WDF_DEVICE_STATE_INIT(
  _Out_ PWDF_DEVICE_STATE PnpDeviceState
);
````


## -parameters
<dl>

### -param PnpDeviceState [out]

<dd>
<p>A pointer to a driver-allocated <a href="..\wdfdevice\ns-wdfdevice--wdf-device-state.md">WDF_DEVICE_STATE</a> structure.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_DEVICE_STATE_INIT</b> function initializes all of the <a href="..\wdfdevice\ns-wdfdevice--wdf-device-state.md">WDF_DEVICE_STATE</a> structure's <a href="..\wudfddi_types\ne-wudfddi-types--wdf-tri-state.md">WDF_TRI_STATE</a>-typed members to <b>WdfUseDefault</b>.</p>

<p>For a code example that uses <b>WDF_DEVICE_STATE_INIT</b>, see <a href="..\wdfdevice\nf-wdfdevice-wdfdevicesetdevicestate.md">WdfDeviceSetDeviceState</a>.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\ns-wdfdevice--wdf-device-state.md">WDF_DEVICE_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DEVICE_STATE_INIT function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
