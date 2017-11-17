---
UID: NS.d3dkmdt._DISPLAYID_DETAILED_TIMING_TYPE_I
title: DISPLAYID_DETAILED_TIMING_TYPE_I
author: windows-driver-content
description: The DISPLAYID_DETAILED_TIMING_TYPE_I structure specifies an additional target mode set for a video present target.
old-location: display\displayid_detailed_timing_type_i.htm
ms.assetid: 7b3fa3a4-a77a-4c5f-b157-1fbdc3a7be33
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DISPLAYID_DETAILED_TIMING_TYPE_I
req.alt-loc: d3dkmdt.h
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
ms.keywords: DISPLAYID_DETAILED_TIMING_TYPE_I, DISPLAYID_DETAILED_TIMING_TYPE_I
req.iface: 
---

# DISPLAYID_DETAILED_TIMING_TYPE_I structure



## -description
<p>The DISPLAYID_DETAILED_TIMING_TYPE_I structure specifies an additional target mode set for a video present target.</p>


## -syntax

````
typedef struct _DISPLAYID_DETAILED_TIMING_TYPE_I {
  struct {
    ULONG PixelClock  :24;
    ULONG AspectRatio  :3;
    ULONG Reserved  :1;
    ULONG ScanningType  :1;
    ULONG StereoMode  :2;
    ULONG PreferredTiming  :1;
  };
  USHORT HorizontalActivePixels;
  USHORT HorizontalBlankPixels;
  struct {
    USHORT HorizontalFrontPorch  :15;
    USHORT HorizontalSyncPolarity  :1;
  };
  USHORT HorizontalSyncWidth;
  USHORT VerticalActiveLines;
  USHORT VerticalBlankLines;
  struct {
    USHORT VerticalFrontPorch  :15;
    USHORT VerticalSyncPolarity  :1;
  };
  USHORT VerticalSyncWidth;
} DISPLAYID_DETAILED_TIMING_TYPE_I;
````


## -struct-fields
<dl>

### -field <b>PixelClock</b>

<dd>
<p>[in] The display pixel clock rate, in units of 10 KHz. Clock rate must be between 1 MHz and 10 GHz, inclusive.</p>
</dd>

### -field <b>AspectRatio</b>

<dd>
<p>[in] The display aspect ratio, which must be one of the values in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554017">DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO</a> enumeration.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>[in] Reserved for system use.</p>
</dd>

### -field <b>ScanningType</b>

<dd>
<p>[in] The frame scanning type. Must be one of the values in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554019">DISPLAYID_DETAILED_TIMING_TYPE_I_SCANNING_MODE</a> enumeration.</p>
</dd>

### -field <b>StereoMode</b>

<dd>
<p>[in] The display stereo vision mode. Must be one of the values in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554023">DISPLAYID_DETAILED_TIMING_TYPE_I_STEREO_MODE</a> enumeration.</p>
</dd>

### -field <b>PreferredTiming</b>

<dd>
<p>
       [in] Indicates whether the first 128-byte block of a monitor's Extended Display Identification Data <a href="wdkgloss.e#wdkgloss.extended_display_identification_data__edid_#wdkgloss.extended_display_identification_data__edid_"><i>Extended Display Identification Data (EDID)</i></a> contains detailed timing data. This must be 1 if the display conforms to EDID version 1.3 and later.
      </p>
</dd>

### -field <b>HorizontalActivePixels</b>

<dd>
<p>[in] The number of active pixels in the horizontal direction.</p>
</dd>

### -field <b>HorizontalBlankPixels</b>

<dd>
<p>[in] The number of blank pixels in the horizontal direction.</p>
</dd>

### -field <b>HorizontalFrontPorch</b>

<dd>
<p>[in] The horizontal front porch interval, in pixels. The front porch is the blanking interval before the sync pulse.</p>
</dd>

### -field <b>HorizontalSyncPolarity</b>

<dd>
<p>[in] The horizontal sync polarity, which must be one of the values in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554026">DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY</a> enumeration.</p>
</dd>

### -field <b>HorizontalSyncWidth</b>

<dd>
<p>[in] The horizontal sync interval, in pixels.</p>
</dd>

### -field <b>VerticalActiveLines</b>

<dd>
<p>[in] The number of active scan lines.</p>
</dd>

### -field <b>VerticalBlankLines</b>

<dd>
<p>[in] The number of blank scan lines.</p>
</dd>

### -field <b>VerticalFrontPorch</b>

<dd>
<p>[in] The vertical front porch interval, in number of lines. The front porch is the blanking interval before the sync pulse.</p>
</dd>

### -field <b>VerticalSyncPolarity</b>

<dd>
<p>[in] The vertical sync polarity. Must be one of the values in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554026">DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY</a> enumeration.</p>
</dd>

### -field <b>VerticalSyncWidth</b>

<dd>
<p>[in] The vertical sync interval, in number of lines.</p>
</dd>
</dl>

## -remarks
<p>The Microsoft DirectX graphics kernel subsystem fills this structure by reading the additional target mode data that is stored in the registry at the following path:</p>

<p><b>HKEY_LOCAL_MACHINE\ SYSTEM\ CurrentControlSet\ Control\ GraphicsDrivers\ AdditionalTargetModeLists</b></p>

<p>The graphics kernel subsystem also validates that each registry value meets the requirements described above for each respective member.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554017">DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554019">DISPLAYID_DETAILED_TIMING_TYPE_I_SCANNING_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554023">DISPLAYID_DETAILED_TIMING_TYPE_I_STEREO_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554026">DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DISPLAYID_DETAILED_TIMING_TYPE_I structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
