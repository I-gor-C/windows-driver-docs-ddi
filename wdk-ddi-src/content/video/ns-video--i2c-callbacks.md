---
UID: NS.video._I2C_CALLBACKS
title: I2C_CALLBACKS
author: windows-driver-content
description: The I2C_CALLBACKS structure contains pointers to functions, implemented by the video miniport driver, that read from and write to the serial data and serial clock lines of the I2C bus.
old-location: display\i2c_callbacks.htm
old-project: display
ms.assetid: fc67ef79-41c8-414c-aaa9-ef8a80edd696
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: I2C_CALLBACKS, I2C_CALLBACKS, *PI2C_CALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: video.h
req.include-header: Video.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: I2C_CALLBACKS
req.alt-loc: video.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# I2C_CALLBACKS structure



## -description
<p>The I2C_CALLBACKS structure contains pointers to functions, implemented by the video miniport driver, that read from and write to the serial data and serial clock lines of the I2C bus.</p>


## -syntax

````
typedef struct _I2C_CALLBACKS {
  PVIDEO_WRITE_CLOCK_LINE WriteClockLine;
  PVIDEO_WRITE_DATA_LINE  WriteDataLine;
  PVIDEO_READ_CLOCK_LINE  ReadClockLine;
  PVIDEO_READ_DATA_LINE   ReadDataLine;
} I2C_CALLBACKS, *PI2C_CALLBACKS;
````


## -struct-fields
<dl>

### -field <b>WriteClockLine</b>

<dd>
<p>A pointer to the <a href="..\video\nc-video-pvideo-write-clock-line.md">WriteClockLine</a> function implemented by the video miniport driver.</p>
</dd>

### -field <b>WriteDataLine</b>

<dd>
<p>A pointer to the <a href="..\video\nc-video-pvideo-write-data-line.md">WriteDataLine</a> function implemented by the video miniport driver.</p>
</dd>

### -field <b>ReadClockLine</b>

<dd>
<p>A pointer to the <a href="..\video\nc-video-pvideo-read-clock-line.md">ReadClockLine</a> function implemented by the video miniport driver.</p>
</dd>

### -field <b>ReadDataLine</b>

<dd>
<p>A pointer to the <a href="..\video\nc-video-pvideo-read-data-line.md">ReadDataLine</a> function implemented by the video miniport driver.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\video\ns-video--ddc-control.md">DDC_CONTROL</a>
</dt>
<dt>
<a href="..\video\nc-video-pvideo-hw-get-child-descriptor.md">HwVidGetVideoChildDescriptor</a>
</dt>
<dt>
<a href="display.i2c_functions">I2C Functions</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportddcmonitorhelper.md">VideoPortDDCMonitorHelper</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20I2C_CALLBACKS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
