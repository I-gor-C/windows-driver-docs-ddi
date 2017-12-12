---
UID: NF.wdfdevice.WDF_DEVICE_STATE_INIT
title: WDF_DEVICE_STATE_INIT function
author: windows-driver-content
description: The WDF_DEVICE_STATE_INIT function initializes a driver's WDF_DEVICE_STATE structure.
old-location: wdf\wdf_device_state_init.htm
old-project: wdf
ms.assetid: f8c040aa-bfa0-4b74-ad0a-8796f1cfc4b8
ms.author: windowsdriverdev
ms.date: 12/7/2017
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
req.product: Windows 10 or later.
---

# WDF_DEVICE_STATE_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_DEVICE_STATE_INIT</b> function initializes a driver's <a href="wdf.wdf_device_state">WDF_DEVICE_STATE</a> structure.



## -syntax

````
VOID WDF_DEVICE_STATE_INIT(
  _Out_ PWDF_DEVICE_STATE PnpDeviceState
);
````


## -parameters

### -param PnpDeviceState [out]

A pointer to a driver-allocated <a href="wdf.wdf_device_state">WDF_DEVICE_STATE</a> structure.


## -returns
None


## -remarks
The <b>WDF_DEVICE_STATE_INIT</b> function initializes all of the <a href="wdf.wdf_device_state">WDF_DEVICE_STATE</a> structure's <a href="wdf.wdf_tri_state">WDF_TRI_STATE</a>-typed members to <b>WdfUseDefault</b>.

For a code example that uses <b>WDF_DEVICE_STATE_INIT</b>, see <a href="wdf.wdfdevicesetdevicestate">WdfDeviceSetDeviceState</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="wdf.wdf_device_state">WDF_DEVICE_STATE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DEVICE_STATE_INIT function%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

