---
UID: NE.wdm._POWER_REQUEST_TYPE
title: POWER_REQUEST_TYPE
author: windows-driver-content
description: The POWER_REQUEST_TYPE enumeration indicates the power request type.
old-location: kernel\power_request_type.htm
old-project: kernel
ms.assetid: 266cdf1a-6122-4f46-8e93-8f76fceb0180
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: POWER_REQUEST_TYPE
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# POWER_REQUEST_TYPE enumeration



## -description
<p>The <b>POWER_REQUEST_TYPE</b> enumeration indicates the power request type.</p>


## -syntax

````
typedef enum _POWER_REQUEST_TYPE { 
  PowerRequestDisplayRequired,
  PowerRequestSystemRequired,
  PowerRequestAwayModeRequired,
  PowerRequestExecutionRequired
} POWER_REQUEST_TYPE, *PPOWER_REQUEST_TYPE;
````


## -enum-fields
<dl>

### -field <a id="PowerRequestDisplayRequired"></a><a id="powerrequestdisplayrequired"></a><a id="POWERREQUESTDISPLAYREQUIRED"></a><b>PowerRequestDisplayRequired</b>

<dd>
<p>Not used by drivers. For more information, see Remarks.</p>
</dd>

### -field <a id="PowerRequestSystemRequired"></a><a id="powerrequestsystemrequired"></a><a id="POWERREQUESTSYSTEMREQUIRED"></a><b>PowerRequestSystemRequired</b>

<dd>
<p>Prevents the computer from automatically entering sleep mode after a period of user inactivity.</p>
</dd>

### -field <a id="PowerRequestAwayModeRequired"></a><a id="powerrequestawaymoderequired"></a><a id="POWERREQUESTAWAYMODEREQUIRED"></a><b>PowerRequestAwayModeRequired</b>

<dd>
<p>Not used by drivers. For more information, see Remarks.</p>
</dd>

### -field <a id="PowerRequestExecutionRequired"></a><a id="powerrequestexecutionrequired"></a><a id="POWERREQUESTEXECUTIONREQUIRED"></a><b>PowerRequestExecutionRequired</b>

<dd>
<p>Not used by drivers. For more information, see Remarks.</p>
</dd>
</dl>

## -remarks
<p>This enumeration is used by the kernel-mode <a href="..\ntifs\nf-ntifs-poclearpowerrequest.md">PoClearPowerRequest</a> and <a href="..\ntifs\nf-ntifs-posetpowerrequest.md">PoSetPowerRequest</a> routines. Drivers that call these routines must specify the <b>PowerRequestSystemRequired</b> enumeration value.</p>

<p>The other three enumeration values—<b>PowerRequestDisplayRequired</b>, <b>PowerRequestAwayModeRequired</b>, and <b>PowerRequestExecutionRequired</b>—are not used by drivers. Applications specify these power request types in calls to the <a href="base.powersetrequest">PowerSetRequest</a> and <a href="base.powerclearrequest">PowerClearRequest</a> functions.</p>

<p>A <b>PowerRequestDisplayRequired</b> power request has the following effects:</p>

<p>After a period of user inactivity, the session display stays on and will not automatically turn off. If the display is already turned off, the power request turns the display on.</p>

<p>A screensaver will not automatically start after a period of user inactivity. If a screensaver is already running, the power request stops the screensaver.</p>

<p>The session will not be automatically locked after a period of user inactivity. If the session is already locked when the driver sends the power request, the session remains locked.</p>

<p>While a <b>PowerRequestAwayModeRequired</b> power request is in effect, if the user tries to put the computer into sleep mode (for example, by clicking <b>Start</b> and then clicking <b>Sleep</b>), the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559829">power manager</a> turns off audio and video so that the computer appears to be in sleep mode, but the computer continues to run.</p>

<p>While a <b>PowerRequestExecutionRequired</b> power request is in effect, the calling process continues to run instead of being suspended or terminated by process lifetime management (PLM) mechanisms. When and how long the process is allowed to run depends on the operating system and power policy settings. This type of power request is supported starting with Windows 8.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 7.</p>
</td>
</tr>
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
<a href="..\ntifs\nf-ntifs-poclearpowerrequest.md">PoClearPowerRequest</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-posetpowerrequest.md">PoSetPowerRequest</a>
</dt>
<dt>
<a href="base.powerclearrequest">PowerClearRequest</a>
</dt>
<dt>
<a href="base.powersetrequest">PowerSetRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20POWER_REQUEST_TYPE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
