---
UID: NE.wdfdevice._WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE
title: WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE
author: windows-driver-content
description: The WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE enumeration identifies how the idle timeout for a device is determined.
old-location: wdf\wdf_power_policy_idle_timeout_type.htm
ms.assetid: CFB7E2EA-22D9-4181-B773-BC5691B28CFD
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.0
req.alt-api: WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE
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
ms.keywords: WDF_REL_TIMEOUT_IN_US
req.iface: 
req.product: Windows 10 or later.
---

# WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>
   The <b>WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE</b> enumeration identifies how the idle timeout for a device is determined.</p>


## -syntax

````
typedef enum _WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE { 
  DriverManagedIdleTimeout          = 0,
  SystemManagedIdleTimeout          = 1,
  SystemManagedIdleTimeoutWithHint  = 2
} WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE, *PWDF_POWER_POLICY_IDLE_TIMEOUT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="DriverManagedIdleTimeout"></a><a id="drivermanagedidletimeout"></a><a id="DRIVERMANAGEDIDLETIMEOUT"></a><b>DriverManagedIdleTimeout</b>

<dd>
<p>The idle timeout value is determined by the <b>IdleTimeout</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a> structure.</p>
</dd>

### -field <a id="SystemManagedIdleTimeout"></a><a id="systemmanagedidletimeout"></a><a id="SYSTEMMANAGEDIDLETIMEOUT"></a><b>SystemManagedIdleTimeout</b>

<dd>
<p>Starting in Windows 8, the timeout value is determined by the power framework (PoFx). The value of the <b>IdleTimeout</b> member is not used.</p>
<p>On operating systems earlier than Windows 8, the behavior is same as <b>DriverManagedIdleTimeout</b>.</p>
</dd>

### -field <a id="SystemManagedIdleTimeoutWithHint"></a><a id="systemmanagedidletimeoutwithhint"></a><a id="SYSTEMMANAGEDIDLETIMEOUTWITHHINT"></a><b>SystemManagedIdleTimeoutWithHint</b>

<dd>
<p>Starting in Windows 8, the PoFx uses the value specified in the <b>IdleTimeout</b> member as an input when determining at what point after all the components are idle to transition the device to a low-power (Dx) state. This option enables the driver to delay the transition to a low-power state.</p>
<p>Typically, PoFx waits until the end of the time-out interval to initiate the power transition. However, if PoFx is preparing to enter a low-power system state, PoFx might end the time-out interval early.</p>
<p>The  <b>IdleTimeout</b> value is only advisory. The actual duration after which the PoFx allows the device to enter a low-power state might be greater than or less than the <b>IdleTimeout</b> value.</p>
<p>On operating systems earlier than Windows 8, the behavior is the same as <b>DriverManagedIdleTimeout</b>.</p>
<p></p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a> structure. </p>

<p>The <b>WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a> structure. </p>

<p>The <b>WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a> structure. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
