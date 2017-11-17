---
UID: NE.wudfddi._DEVICE_POWER_STATE~r1
title: DEVICE_POWER_STATE
author: windows-driver-content
description: The DEVICE_POWER_STATE enumeration identifies the device power states that a device can enter.
old-location: wdf\device_power_state.htm
ms.assetid: 7dd4d0ae-876a-4156-8a09-2ebc82a25117
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: DEVICE_POWER_STATE
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: WSK_TRANSPORT, WSK_TRANSPORT, *PWSK_TRANSPORT
req.iface: 
req.product: Windows 10 or later.
---

# DEVICE_POWER_STATE enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>DEVICE_POWER_STATE</b> enumeration identifies the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543162">device power states</a> that a device can enter.</p>


## -syntax

````
typedef enum _DEVICE_POWER_STATE { 
  PowerDeviceUnspecified  = 0,
  PowerDeviceD0           = ( PowerDeviceUnspecified + 1 ),
  PowerDeviceD1           = ( PowerDeviceD0 + 1 ),
  PowerDeviceD2           = ( PowerDeviceD1 + 1 ),
  PowerDeviceD3           = ( PowerDeviceD2 + 1 ),
  PowerDeviceMaximum      = ( PowerDeviceD3 + 1 )
} DEVICE_POWER_STATE, *PDEVICE_POWER_STATE;
````


## -enum-fields
<dl>

### -field <a id="PowerDeviceUnspecified"></a><a id="powerdeviceunspecified"></a><a id="POWERDEVICEUNSPECIFIED"></a><b>PowerDeviceUnspecified</b>

<dd>
<p>The device power state is unspecified.</p>
</dd>

### -field <a id="PowerDeviceD0"></a><a id="powerdeviced0"></a><a id="POWERDEVICED0"></a><b>PowerDeviceD0</b>

<dd>
<p>The device's working (D0) state. This is the device's highest power state.</p>
</dd>

### -field <a id="PowerDeviceD1"></a><a id="powerdeviced1"></a><a id="POWERDEVICED1"></a><b>PowerDeviceD1</b>

<dd>
<p>The device's D1 <a href="https://msdn.microsoft.com/f594a63f-10ce-439d-abe3-d342555d98f0">sleeping state</a>.</p>
</dd>

### -field <a id="PowerDeviceD2"></a><a id="powerdeviced2"></a><a id="POWERDEVICED2"></a><b>PowerDeviceD2</b>

<dd>
<p>The device's D2 sleeping state.</p>
</dd>

### -field <a id="PowerDeviceD3"></a><a id="powerdeviced3"></a><a id="POWERDEVICED3"></a><b>PowerDeviceD3</b>

<dd>
<p>The device's D3 sleeping state.</p>
</dd>

### -field <a id="PowerDeviceMaximum"></a><a id="powerdevicemaximum"></a><a id="POWERDEVICEMAXIMUM"></a><b>PowerDeviceMaximum</b>

<dd>
<p>For system use only.</p>
</dd>
</dl>

## -remarks
<p>The <b>DEVICE_POWER_STATE</b> enumeration is used as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556920">IWDFDevice2::AssignS0IdleSettings</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff556923">IWDFDevice2::AssignSxWakeSettings</a>.</p>

<p>The <b>DEVICE_POWER_STATE</b> enumeration is used as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556920">IWDFDevice2::AssignS0IdleSettings</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff556923">IWDFDevice2::AssignSxWakeSettings</a>.</p>

<p>The <b>DEVICE_POWER_STATE</b> enumeration is used as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556920">IWDFDevice2::AssignS0IdleSettings</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff556923">IWDFDevice2::AssignSxWakeSettings</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556920">IWDFDevice2::AssignS0IdleSettings</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556923">IWDFDevice2::AssignSxWakeSettings</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20DEVICE_POWER_STATE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
