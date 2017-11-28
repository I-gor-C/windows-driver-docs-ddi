---
UID: NC.videoagp.PAGP_SET_RATE
title: PAGP_SET_RATE
author: windows-driver-content
description: The AgpSetRate function reprograms the data transfer rate of the AGP chipset.
old-location: display\agpsetrate.htm
old-project: display
ms.assetid: 6885df05-8cc4-4ae0-b7ca-6fd94374cfbf
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VPOSVERSIONINFO, VPOSVERSIONINFO, *PVPOSVERSIONINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: videoagp.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AgpSetRate
req.alt-loc: videoagp.h
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

# PAGP_SET_RATE callback



## -description
<p>The <b>AgpSetRate</b> function reprograms the data transfer rate of the AGP chipset.</p>


## -prototype

````
PAGP_SET_RATE AgpSetRate;

BOOLEAN APIENTRY AgpSetRate(
  _In_ PVOID HwDeviceExtension,
  _In_ ULONG AgpRate
)
{ ... }
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>AgpRate</i> [in]

<dd>
<p>Specifies the transfer rate to be set. This value can be one of the following:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>VIDEO_AGP_RATE_1X</p>
</td>
<td>
<p>Single speed (66 Mhz)</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_AGP_RATE_2X</p>
</td>
<td>
<p>Two times single speed</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_AGP_RATE_4X</p>
</td>
<td>
<p>Four times single speed</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_AGP_RATE_8X</p>
</td>
<td>
<p>Eight times single speed</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>AgpSetRate</b> returns <b>TRUE</b> if it was successful in changing the transfer rate; otherwise, it returns <b>FALSE</b>.</p>

## -remarks
<p>This function is available in Microsoft Windows XP and later.</p>

<p>The transfer rate set by the <b>AgpSetRate</b> function is persistent across changes in power state. The video miniport driver does not have to reset the AGP transfer rate when it changes from a low power state to a full power state. For information about change of power state, see <a href="..\video\nc-video-pvideo-hw-power-set.md">HwVidSetPowerState</a>.</p>

<p>The <b>AgpSetRate</b> function can be used to change an AGP chipset's data transfer rate to any of the rates shown in the preceding table, as long as that transfer rate has not been explicitly eliminated in the INF file that loaded the display driver. For more information, see <a href="https://msdn.microsoft.com/2075a10f-a504-4bdc-8112-9c583c5084bb">Display INF File Sections</a>.</p>

<p>This function is available in Microsoft Windows XP and later.</p>

<p>The transfer rate set by the <b>AgpSetRate</b> function is persistent across changes in power state. The video miniport driver does not have to reset the AGP transfer rate when it changes from a low power state to a full power state. For information about change of power state, see <a href="..\video\nc-video-pvideo-hw-power-set.md">HwVidSetPowerState</a>.</p>

<p>The <b>AgpSetRate</b> function can be used to change an AGP chipset's data transfer rate to any of the rates shown in the preceding table, as long as that transfer rate has not been explicitly eliminated in the INF file that loaded the display driver. For more information, see <a href="https://msdn.microsoft.com/2075a10f-a504-4bdc-8112-9c583c5084bb">Display INF File Sections</a>.</p>

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
<p>Available in Windows 2000 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Videoagp.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570528">VIDEO_PORT_AGP_INTERFACE_2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PAGP_SET_RATE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
