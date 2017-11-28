---
UID: NS.ntddvdeo._VIDEO_POWER_MANAGEMENT
title: VIDEO_POWER_MANAGEMENT
author: windows-driver-content
description: The VIDEO_POWER_MANAGEMENT structure contains information required by the miniport driver to perform power management.
old-location: display\video_power_management.htm
old-project: display
ms.assetid: 9522c504-9bdb-4388-b047-340a211463dd
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VIDEO_POWER_MANAGEMENT, VIDEO_POWER_MANAGEMENT, *PVIDEO_POWER_MANAGEMENT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddvdeo.h
req.include-header: Ntddvdeo.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_POWER_MANAGEMENT
req.alt-loc: ntddvdeo.h
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

# VIDEO_POWER_MANAGEMENT structure



## -description
<p>The VIDEO_POWER_MANAGEMENT structure contains information required by the miniport driver to perform power management.</p>


## -syntax

````
typedef struct _VIDEO_POWER_MANAGEMENT {
  ULONG Length;
  ULONG DPMSVersion;
  ULONG PowerState;
} VIDEO_POWER_MANAGEMENT, *PVIDEO_POWER_MANAGEMENT;
````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>Is the size in bytes of this VIDEO_POWER_MANAGEMENT structure.</p>
</dd>

### -field <b>DPMSVersion</b>

<dd>
<p>Specifies the version of the Display Power Management Signaling (DPMS) standard supported by the device. Currently, the video port driver sets this member to zero, which corresponds with Version 1.0 of the <a href="wdkgloss.v#wdkgloss.video_electronics_standards_association__vesa_#wdkgloss.video_electronics_standards_association__vesa_"><i>VESA</i></a> DPMS Standard.</p>
</dd>

### -field <b>PowerState</b>

<dd>
<p>Specifies the power management state to be set or queried. This member can be one of the following values in the VIDEO_POWER_STATE enumeration:</p>
<p></p>
<dl>

### -field <a id="VideoPowerOn"></a><a id="videopoweron"></a><a id="VIDEOPOWERON"></a><b>VideoPowerOn</b>

<dd>
<p>The monitor and graphics adapter are both fully powered on and operational.</p>
</dd>

### -field <a id="VideoPowerStandBy"></a><a id="videopowerstandby"></a><a id="VIDEOPOWERSTANDBY"></a><b>VideoPowerStandBy</b>

<dd>
<p>The monitor is running at a reduced power level that requires a short recovery time to <b>VideoPowerOn</b>. The graphics adapter is powered on (registers are still active and video memory is refreshed); however, clocks might be lost.</p>
</dd>

### -field <a id="VideoPowerSuspend"></a><a id="videopowersuspend"></a><a id="VIDEOPOWERSUSPEND"></a><b>VideoPowerSuspend</b>

<dd>
<p>The monitor is running at a substantially reduced power level that requires a possibly longer recovery time than <b>VideoPowerStandBy</b> to <b>VideoPowerOn</b>. The graphics adapter is off.</p>
</dd>

### -field <a id="VideoPowerOff"></a><a id="videopoweroff"></a><a id="VIDEOPOWEROFF"></a><b>VideoPowerOff</b>

<dd>
<p>The monitor and graphics adapter are both off, consuming no power at all.</p>
</dd>

### -field <a id="VideoPowerHibernate"></a><a id="videopowerhibernate"></a><a id="VIDEOPOWERHIBERNATE"></a><b>VideoPowerHibernate</b>

<dd>
<p>The monitor and graphics adapter are both fully powered on and operational.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The video port driver allocates and fills in the VIDEO_POWER_MANAGEMENT structure. Depending on the power management request dispatched to the video port, the video port driver passes this structure to the miniport driver's <a href="..\video\nc-video-pvideo-hw-power-get.md">HwVidGetPowerState</a> or <a href="..\video\nc-video-pvideo-hw-power-set.md">HwVidSetPowerState</a> routine.</p>

<p><b>VideoPowerHibernate</b> is provided to the miniport driver as notification only. The miniport driver's <i>HwVidSetPowerState</i> function must leave the monitor and graphics adapter fully powered on and operational. For all other states, the miniport driver must put the device into the specified power state.</p>

<p>A driver will always enter all other power states from the <b>VideoPowerOn</b> state. For example, a driver will not move directly to <b>VideoPowerHibernate</b> from <b>VideoPowerOff</b>; it will always go from <b>VideoPowerHibernate</b> to <b>VideoPowerOn</b> and then to <b>VideoPowerOff</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddvdeo.h (include Ntddvdeo.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\video\nc-video-pvideo-hw-power-get.md">HwVidGetPowerState</a>
</dt>
<dt>
<a href="..\video\nc-video-pvideo-hw-power-set.md">HwVidSetPowerState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VIDEO_POWER_MANAGEMENT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
