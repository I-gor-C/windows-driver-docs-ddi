---
UID: NE.wdfdevice._WDF_POWER_POLICY_SX_WAKE_USER_CONTROL
title: WDF_POWER_POLICY_SX_WAKE_USER_CONTROL
author: windows-driver-content
description: The WDF_POWER_POLICY_SX_WAKE_USER_CONTROL enumeration identifies whether a user can control a device's ability to wake the system from a low system power state.
old-location: wdf\wdf_power_policy_sx_wake_user_control.htm
old-project: wdf
ms.assetid: d5f4eb5f-28bb-4906-b9f5-3adae31cac80
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_REL_TIMEOUT_IN_US
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 1.11
req.alt-api: WDF_POWER_POLICY_SX_WAKE_USER_CONTROL
req.alt-loc: wdfdevice.h,wudfddi_types.h
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

# WDF_POWER_POLICY_SX_WAKE_USER_CONTROL enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_POWER_POLICY_SX_WAKE_USER_CONTROL</b> enumeration identifies whether a user can control a device's ability to wake the system from a low system power state.</p>


## -syntax

````
typedef enum _WDF_POWER_POLICY_SX_WAKE_USER_CONTROL { 
  WakeUserControlInvalid     = 0,
  WakeDoNotAllowUserControl  = 1,
  WakeAllowUserControl       = 2
} WDF_POWER_POLICY_SX_WAKE_USER_CONTROL;
````


## -enum-fields
<dl>

### -field <a id="WakeUserControlInvalid"></a><a id="wakeusercontrolinvalid"></a><a id="WAKEUSERCONTROLINVALID"></a><b>WakeUserControlInvalid</b>

<dd>
<p>For internal use only.</p>
</dd>

### -field <a id="WakeDoNotAllowUserControl"></a><a id="wakedonotallowusercontrol"></a><a id="WAKEDONOTALLOWUSERCONTROL"></a><b>WakeDoNotAllowUserControl</b>

<dd>
<p>Users cannot control the device's ability to wake the system from a low system power state.</p>
</dd>

### -field <a id="WakeAllowUserControl"></a><a id="wakeallowusercontrol"></a><a id="WAKEALLOWUSERCONTROL"></a><b>WakeAllowUserControl</b>

<dd>
<p>Users can control the device's ability to wake the system from a low system power state.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_POWER_POLICY_SX_WAKE_USER_CONTROL</b> enumeration is used as a member type in the <a href="..\wdfdevice\ns-wdfdevice--wdf-device-power-policy-wake-settings.md">WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS</a> structure.</p>

<p>To control a device's ability to wake the system from a low system power state, users modify information on a <a href="wdf.user_control_of_device_idle_and_wake_behavior">property sheet</a>. The framework creates the property sheet and Device Manager displays it.</p>

## -requirements
<table>
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
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h); </dt>
<dt>Wudfddi_types.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\ns-wdfdevice--wdf-device-power-policy-wake-settings.md">WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_POWER_POLICY_SX_WAKE_USER_CONTROL enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
