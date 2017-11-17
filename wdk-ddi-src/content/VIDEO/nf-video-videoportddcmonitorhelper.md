---
UID: NF.video.VideoPortDDCMonitorHelper
title: VideoPortDDCMonitorHelper
author: windows-driver-content
description: Queries a monitor for EDID information using the DDC protocol.
old-location: display\videoportddcmonitorhelper.htm
ms.assetid: 2e4bd9c7-73be-47bc-b4e7-daea7781c46b
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortDDCMonitorHelper
req.alt-loc: Videoprt.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: PASSIVE_LEVEL
ms.keywords: VideoPortDDCMonitorHelper
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortDDCMonitorHelper function



## -description
<p>Queries a monitor for <a href="wdkgloss.e#wdkgloss.edid#wdkgloss.edid"><i>EDID</i></a> information using the DDC protocol.</p>


## -syntax

````
BOOLEAN VideoPortDDCMonitorHelper(
  _In_    PVOID  HwDeviceExtension,
  _In_    PVOID  DDCControl,
  _Inout_ PUCHAR EdidBuffer,
  _In_    ULONG  EdidBufferSize
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>DDCControl</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff549272">DDC_CONTROL</a> structure.</p>
</dd>

### -param <i>EdidBuffer</i> [in, out]

<dd>
<p>A pointer to a buffer in which the video port driver returns the <a href="wdkgloss.e#wdkgloss.edid#wdkgloss.edid"><i>EDID</i></a> structure. For ACPI devices, the first four bytes are preset by the video port driver to indicate an attempt to read the <i>EDID</i>. </p>
</dd>

### -param <i>EdidBufferSize</i> [in]

<dd>
<p>The size in bytes of the buffer to which <i>EdidBuffer</i> points.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortDDCMonitorHelper</b> returns <b>TRUE</b> if successful.</p>

## -remarks
<p class="note">This function existed prior to the Windows XP release, but has been changed.</p><p class="note">The video miniport driver's <a href="https://msdn.microsoft.com/175030c1-95d9-4a3b-976c-16e04852cb91">HwVidGetVideoChildDescriptor</a> function can call <b>VideoPortDDCMonitorHelper</b> for assistance in reading the <a href="wdkgloss.e#wdkgloss.edid#wdkgloss.edid"><i>EDID</i></a> structure from a DDC2-compliant monitor. <b>VideoPortDDCMonitorHelper </b>implements the details of reading the EDID structure according to the I²C specification, but must call back into the video miniport driver to read and write individual data bits to the I²C serial clock and data lines.</p><p class="note">The four functions, implemented by the video miniport driver, that read and write individual bits to the I²C clock and data lines are <a href="https://msdn.microsoft.com/1051a234-ef63-454e-8957-292e86f4efcd">ReadClockLine</a>, <a href="https://msdn.microsoft.com/071000a3-c1b7-47fd-aec7-9e9f32edddf6">ReadDataLine</a>, <a href="https://msdn.microsoft.com/4dfd6223-420e-4087-b5bd-8277575321f7">WriteClockLine</a>, and <a href="https://msdn.microsoft.com/3f860619-a479-4291-b3f3-ea4d309beee7">WriteDataLine</a>. When the video miniport driver calls <b>VideoPortDDCMonitorHelper</b>, it supplies pointers to those four functions in <i>DDCControl</i><b>-&gt;I2CCallbacks</b>.</p><p class="note">The <a href="wdkgloss.e#wdkgloss.edid#wdkgloss.edid"><i>EDID</i></a> can be obtained using the ACPI_METHOD_OUTPUT_DDC method whose alias is defined in Dispmprt.h. This method is required for integrated LCDs that do not have another standard mechanism for returning EDID data.</p><p class="note">In a 256-byte buffer, a caller of this function can receive:</p>

<p>One 128-byte EDID</p>

<p>Two 128-byte EDIDs</p>

<p>One 256-byte EDID (from P&amp;D display)</p>

<p>No EDID</p><p class="note">The caller should always ask for the full 256 bytes, because it is impossible to read just the second 128-byte block of the segment.</p><p class="note">This function existed prior to the Windows XP release, but has been changed.</p><p class="note">The video miniport driver's <a href="https://msdn.microsoft.com/175030c1-95d9-4a3b-976c-16e04852cb91">HwVidGetVideoChildDescriptor</a> function can call <b>VideoPortDDCMonitorHelper</b> for assistance in reading the <a href="wdkgloss.e#wdkgloss.edid#wdkgloss.edid"><i>EDID</i></a> structure from a DDC2-compliant monitor. <b>VideoPortDDCMonitorHelper </b>implements the details of reading the EDID structure according to the I²C specification, but must call back into the video miniport driver to read and write individual data bits to the I²C serial clock and data lines.</p><p class="note">The four functions, implemented by the video miniport driver, that read and write individual bits to the I²C clock and data lines are <a href="https://msdn.microsoft.com/1051a234-ef63-454e-8957-292e86f4efcd">ReadClockLine</a>, <a href="https://msdn.microsoft.com/071000a3-c1b7-47fd-aec7-9e9f32edddf6">ReadDataLine</a>, <a href="https://msdn.microsoft.com/4dfd6223-420e-4087-b5bd-8277575321f7">WriteClockLine</a>, and <a href="https://msdn.microsoft.com/3f860619-a479-4291-b3f3-ea4d309beee7">WriteDataLine</a>. When the video miniport driver calls <b>VideoPortDDCMonitorHelper</b>, it supplies pointers to those four functions in <i>DDCControl</i><b>-&gt;I2CCallbacks</b>.</p><p class="note">The <a href="wdkgloss.e#wdkgloss.edid#wdkgloss.edid"><i>EDID</i></a> can be obtained using the ACPI_METHOD_OUTPUT_DDC method whose alias is defined in Dispmprt.h. This method is required for integrated LCDs that do not have another standard mechanism for returning EDID data.</p><p class="note">In a 256-byte buffer, a caller of this function can receive:</p>

<p>One 128-byte EDID</p>

<p>Two 128-byte EDIDs</p>

<p>One 256-byte EDID (from P&amp;D display)</p>

<p>No EDID</p><p class="note">The caller should always ask for the full 256 bytes, because it is impossible to read just the second 128-byte block of the segment.</p>

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
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567383">I2C Functions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/175030c1-95d9-4a3b-976c-16e04852cb91">HwVidGetVideoChildDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1051a234-ef63-454e-8957-292e86f4efcd">ReadClockLine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/071000a3-c1b7-47fd-aec7-9e9f32edddf6">ReadDataLine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4dfd6223-420e-4087-b5bd-8277575321f7">WriteClockLine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/3f860619-a479-4291-b3f3-ea4d309beee7">WriteDataLine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortDDCMonitorHelper function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
