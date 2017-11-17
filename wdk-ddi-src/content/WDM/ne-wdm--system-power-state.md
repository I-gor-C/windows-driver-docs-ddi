---
UID: NE.wdm._SYSTEM_POWER_STATE
title: SYSTEM_POWER_STATE
author: windows-driver-content
description: The SYSTEM_POWER_STATE enumeration type is used to indicate a system power state.
old-location: kernel\system_power_state.htm
ms.assetid: aa027f03-7d74-4c0e-8f62-d53f41ae86ae
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SYSTEM_POWER_STATE
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
req.iface: 
req.product: Windows 10 or later.
---

# SYSTEM_POWER_STATE enumeration



## -description
<p>The <b>SYSTEM_POWER_STATE</b> enumeration type is used to indicate a <a href="https://msdn.microsoft.com/bb30bc89-d1f2-4cb3-bcfb-fb76c69dba27">system power state</a>.</p>


## -syntax

````
typedef enum _SYSTEM_POWER_STATE { 
  PowerSystemUnspecified  = 0,
  PowerSystemWorking      = 1,
  PowerSystemSleeping1    = 2,
  PowerSystemSleeping2    = 3,
  PowerSystemSleeping3    = 4,
  PowerSystemHibernate    = 5,
  PowerSystemShutdown     = 6,
  PowerSystemMaximum      = 7
} SYSTEM_POWER_STATE, *PSYSTEM_POWER_STATE;
````


## -enum-fields
<dl>

### -field <a id="PowerSystemUnspecified"></a><a id="powersystemunspecified"></a><a id="POWERSYSTEMUNSPECIFIED"></a><b>PowerSystemUnspecified</b>

<dd>
<p>Indicates an unspecified system power state. </p>
</dd>

### -field <a id="PowerSystemWorking"></a><a id="powersystemworking"></a><a id="POWERSYSTEMWORKING"></a><b>PowerSystemWorking</b>

<dd>
<p>Indicates maximum system power, which corresponds to <a href="https://msdn.microsoft.com/library/windows/hardware/ff564591">system working state S0</a>. </p>
</dd>

### -field <a id="PowerSystemSleeping1"></a><a id="powersystemsleeping1"></a><a id="POWERSYSTEMSLEEPING1"></a><b>PowerSystemSleeping1</b>

<dd>
<p>Indicates a <a href="https://msdn.microsoft.com/2fd883b5-4e89-4ce9-b75a-b821348ac860">system sleeping state</a> less than <b>PowerSystemWorking</b> and greater than <b>PowerSystemSleeping2</b>, which corresponds to system power state S1. </p>
</dd>

### -field <a id="PowerSystemSleeping2"></a><a id="powersystemsleeping2"></a><a id="POWERSYSTEMSLEEPING2"></a><b>PowerSystemSleeping2</b>

<dd>
<p>Indicates a system sleeping state less than <b>PowerSystemSleeping1</b> and greater than <b>PowerSystemSleeping3</b>, which corresponds to system power state S2. </p>
</dd>

### -field <a id="PowerSystemSleeping3"></a><a id="powersystemsleeping3"></a><a id="POWERSYSTEMSLEEPING3"></a><b>PowerSystemSleeping3</b>

<dd>
<p>Indicates a system sleeping state less than <b>PowerSystemSleeping2</b> and greater than <b>PowerSystemHibernate</b>, which corresponds to system power state S3. </p>
</dd>

### -field <a id="PowerSystemHibernate"></a><a id="powersystemhibernate"></a><a id="POWERSYSTEMHIBERNATE"></a><b>PowerSystemHibernate</b>

<dd>
<p>Indicates the lowest-powered sleeping state, which corresponds to system power state S4. </p>
</dd>

### -field <a id="PowerSystemShutdown"></a><a id="powersystemshutdown"></a><a id="POWERSYSTEMSHUTDOWN"></a><b>PowerSystemShutdown</b>

<dd>
<p>Indicates the system is turned off, which corresponds to <a href="https://msdn.microsoft.com/library/windows/hardware/ff564572">system shutdown state S5</a>. </p>
</dd>

### -field <a id="PowerSystemMaximum"></a><a id="powersystemmaximum"></a><a id="POWERSYSTEMMAXIMUM"></a><b>PowerSystemMaximum</b>

<dd>
<p>The number of system power state values for this enumeration type that represents actual power states. This value is the number of elements in the <b>DeviceState</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543095">DEVICE_CAPABILITIES</a> structure for a device. The other system power state values are less than this value.</p>
</dd>
</dl>

## -remarks
<p>A power state indicates the level of power consumption—and thus the extent of computing activity—by the system or by a single device. The power manager sets the power state of the system as a whole, where the system power state is indicated by one of the values of the <b>SYSTEM_POWER_STATE</b> enumeration type. Device drivers set the power state of their individual devices, where the device power state is indicated by one of the values of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554628">DEVICE_POWER_STATE</a> enumeration type.</p>

<p>For more information about system power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546941">Handling System Power State Requests</a> and for more information about device power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554397">Managing Power for Individual Devices</a>.</p>

<p>For more information about power management in general, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548108">Introduction to Power Management</a>.</p>

<p>A power state indicates the level of power consumption—and thus the extent of computing activity—by the system or by a single device. The power manager sets the power state of the system as a whole, where the system power state is indicated by one of the values of the <b>SYSTEM_POWER_STATE</b> enumeration type. Device drivers set the power state of their individual devices, where the device power state is indicated by one of the values of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554628">DEVICE_POWER_STATE</a> enumeration type.</p>

<p>For more information about system power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546941">Handling System Power State Requests</a> and for more information about device power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554397">Managing Power for Individual Devices</a>.</p>

<p>For more information about power management in general, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548108">Introduction to Power Management</a>.</p>

<p>A power state indicates the level of power consumption—and thus the extent of computing activity—by the system or by a single device. The power manager sets the power state of the system as a whole, where the system power state is indicated by one of the values of the <b>SYSTEM_POWER_STATE</b> enumeration type. Device drivers set the power state of their individual devices, where the device power state is indicated by one of the values of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554628">DEVICE_POWER_STATE</a> enumeration type.</p>

<p>For more information about system power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546941">Handling System Power State Requests</a> and for more information about device power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554397">Managing Power for Individual Devices</a>.</p>

<p>For more information about power management in general, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548108">Introduction to Power Management</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554628">DEVICE_POWER_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20SYSTEM_POWER_STATE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
