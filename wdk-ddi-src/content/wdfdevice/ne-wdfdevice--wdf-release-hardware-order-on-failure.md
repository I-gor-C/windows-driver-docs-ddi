---
UID: NE.wdfdevice._WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE
title: WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE
author: windows-driver-content
description: The WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE enumeration specifies when the framework calls a driver's EvtDeviceReleaseHardware callback function.
old-location: wdf\wdf_release_hardware_order_on_failure.htm
old-project: wdf
ms.assetid: 534B1E39-6B11-4954-8792-41A25FCA31B2
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_REL_TIMEOUT_IN_US
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.0
req.alt-api: WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>
   The <b>WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE</b> enumeration specifies when the framework calls a driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> callback function.</p>


## -syntax

````
typedef enum _WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE { 
  WdfReleaseHardwareOrderOnFailureInvalid           = 0,
  WdfReleaseHardwareOrderOnFailureEarly             = 1,
  WdfReleaseHardwareOrderOnFailureAfterDescendants  = 2
} WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE, *PWDF_RELEASE_HARDWARE_ORDER_ON_FAILURE;
````


## -enum-fields
<dl>

### -field <a id="WdfReleaseHardwareOrderOnFailureInvalid"></a><a id="wdfreleasehardwareorderonfailureinvalid"></a><a id="WDFRELEASEHARDWAREORDERONFAILUREINVALID"></a><b>WdfReleaseHardwareOrderOnFailureInvalid</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="WdfReleaseHardwareOrderOnFailureEarly"></a><a id="wdfreleasehardwareorderonfailureearly"></a><a id="WDFRELEASEHARDWAREORDERONFAILUREEARLY"></a><b>WdfReleaseHardwareOrderOnFailureEarly</b>

<dd>
<p>Except under certain error conditions, the framework calls the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> callback function after it has called the <i>EvtDeviceReleaseHardware</i> function for all child devices that the driver enumerates. For more information, see Remarks.</p>
</dd>

### -field <a id="WdfReleaseHardwareOrderOnFailureAfterDescendants"></a><a id="wdfreleasehardwareorderonfailureafterdescendants"></a><a id="WDFRELEASEHARDWAREORDERONFAILUREAFTERDESCENDANTS"></a><b>WdfReleaseHardwareOrderOnFailureAfterDescendants</b>

<dd>
<p>The framework always calls the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> callback function after it has called the <i>EvtDeviceReleaseHardware</i> function for all child devices that the driver enumerates.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE</b> enumeration is used as input to  <a href="https://msdn.microsoft.com/library/windows/hardware/hh706196">WdfDeviceInitSetReleaseHardwareOrderOnFailure</a>.</p>

<p>If a driver specifies <b>WdfReleaseHardwareOrderOnFailureEarly</b>, then in normal device removal, the framework calls the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> after it has called the <i>EvtDeviceReleaseHardware</i> function for all child devices that the driver enumerates. However, in the event of a device power-up or power-down failure, the framework might call the  driver's <i>EvtDeviceReleaseHardware</i> before it has called the <i>EvtDeviceReleaseHardware</i> functions for all child devices.</p>

<p>If a driver specifies <b>WdfReleaseHardwareOrderOnFailureAfterDescendants</b>, then the framework waits to  call the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> until it has called the <i>EvtDeviceReleaseHardware</i> functions of the child devices.</p>

<p>The <b>WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE</b> enumeration is used as input to  <a href="https://msdn.microsoft.com/library/windows/hardware/hh706196">WdfDeviceInitSetReleaseHardwareOrderOnFailure</a>.</p>

<p>If a driver specifies <b>WdfReleaseHardwareOrderOnFailureEarly</b>, then in normal device removal, the framework calls the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> after it has called the <i>EvtDeviceReleaseHardware</i> function for all child devices that the driver enumerates. However, in the event of a device power-up or power-down failure, the framework might call the  driver's <i>EvtDeviceReleaseHardware</i> before it has called the <i>EvtDeviceReleaseHardware</i> functions for all child devices.</p>

<p>If a driver specifies <b>WdfReleaseHardwareOrderOnFailureAfterDescendants</b>, then the framework waits to  call the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> until it has called the <i>EvtDeviceReleaseHardware</i> functions of the child devices.</p>

<p>The <b>WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE</b> enumeration is used as input to  <a href="https://msdn.microsoft.com/library/windows/hardware/hh706196">WdfDeviceInitSetReleaseHardwareOrderOnFailure</a>.</p>

<p>If a driver specifies <b>WdfReleaseHardwareOrderOnFailureEarly</b>, then in normal device removal, the framework calls the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> after it has called the <i>EvtDeviceReleaseHardware</i> function for all child devices that the driver enumerates. However, in the event of a device power-up or power-down failure, the framework might call the  driver's <i>EvtDeviceReleaseHardware</i> before it has called the <i>EvtDeviceReleaseHardware</i> functions for all child devices.</p>

<p>If a driver specifies <b>WdfReleaseHardwareOrderOnFailureAfterDescendants</b>, then the framework waits to  call the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> until it has called the <i>EvtDeviceReleaseHardware</i> functions of the child devices.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
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
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh706196">WdfDeviceInitSetReleaseHardwareOrderOnFailure</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
