---
UID: NS.winddiui._ATTRIBUTE_INFO_4
title: ATTRIBUTE_INFO_4
author: windows-driver-content
description: The ATTRIBUTE_INFO_4 structure is used as a parameter for a printer interface DLL's DrvQueryJobAttributes function.
old-location: print\attribute_info_4.htm
ms.assetid: 09071fff-834b-452b-ae1e-b75c9f191b15
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: winddiui.h
req.include-header: Winddiui.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ATTRIBUTE_INFO_4
req.alt-loc: winddiui.h
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
ms.keywords: ATTRIBUTE_INFO_4, ATTRIBUTE_INFO_4, *PATTRIBUTE_INFO_4
req.iface: 
req.product: Windows 10 or later.
---

# ATTRIBUTE_INFO_4 structure



## -description
<p>The ATTRIBUTE_INFO_4 structure is used as a parameter for a printer interface DLL's <a href="https://msdn.microsoft.com/library/windows/hardware/ff548581">DrvQueryJobAttributes</a> function. All member values are function-supplied. This structure is similar to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545093">ATTRIBUTE_INFO_3</a>, but it includes additional members to control N-up, duplex and booklet printing, and scaling.</p>


## -syntax

````
typedef struct _ATTRIBUTE_INFO_4 {
  DWORD dwJobNumberOfPagesPerSide;
  DWORD dwDrvNumberOfPagesPerSide;
  DWORD dwNupBorderFlags;
  DWORD dwJobPageOrderFlags;
  DWORD dwDrvPageOrderFlags;
  DWORD dwJobNumberOfCopies;
  DWORD dwDrvNumberOfCopies;
  DWORD dwColorOptimization;
  short dmPrintQuality;
  short dmYResolution;
  DWORD dwDuplexFlags;
  DWORD dwNupDirection;
  DWORD dwBookletFlags;
  DWORD dwScalingPercentX;
  DWORD dwScalingPercentY;
} ATTRIBUTE_INFO_4, *PATTRIBUTE_INFO_4;
````


## -struct-fields
<dl>

### -field <b>dwJobNumberOfPagesPerSide</b>

<dd>
<p>Number of document pages to be placed on one side of a physical page, as requested by the user. Allowable values are 1, 2, 4, 6, 9, or 16.</p>
</dd>

### -field <b>dwDrvNumberOfPagesPerSide</b>

<dd>
<p>Number of document pages that the printer and driver can place on one side of a physical page. This value must be 1 or the value specified for <b>dwJobNumberOfPagesPerSide</b>.</p>
</dd>

### -field <b>dwNupBorderFlags</b>

<dd>
<p>One of the following bit flag values:</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>BORDER_PRINT</p>
</td>
<td>
<p>The print processor should draw a border around the page.</p>
</td>
</tr>
<tr>
<td>
<p>NO_BORDER_PRINT</p>
</td>
<td>
<p>The print processor should not draw a border around the page.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwJobPageOrderFlags</b>

<dd>
<p>One of the following bit flag values:</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>BOOKLET_PRINT</p>
</td>
<td>
<p>Pages should be printed in booklet form, with two document pages printed on one side of a physical page. In landscape mode, the two document pages are printed side-by-side on the paper. In portrait mode, the two document pages are printed top-and-bottom.</p>
</td>
</tr>
<tr>
<td>
<p>NORMAL_PRINT</p>
</td>
<td>
<p>Pages should be printed in normal order: page 1, page 2, and so on.</p>
</td>
</tr>
<tr>
<td>
<p>REVERSE_PRINT</p>
</td>
<td>
<p>Pages should be printed in reverse order: last page, next-to-last page, and so on.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwDrvPageOrderFlags</b>

<dd>
<p>Bit flags indicating which page ordering options are supported by the printer and driver. Uses the same flags as <b>dwJobPageOrderFlags</b>.</p>
</dd>

### -field <b>dwJobNumberOfCopies</b>

<dd>
<p>Number of copies of the print job, as requested by the user.</p>
</dd>

### -field <b>dwDrvNumberOfCopies</b>

<dd>
<p>Maximum number of copies the printer and driver can handle at once, taking into account such job attributes as collating and stapling.</p>
</dd>

### -field <b>dwColorOptimization</b>

<dd>
<p>One of the following bit flag values:</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>COLOR_OPTIMIZATION</p>
</td>
<td>
<p>The print processor should use monochrome color optimization.</p>
</td>
</tr>
<tr>
<td>
<p>NO_COLOR_OPTIMIZATION</p>
</td>
<td>
<p>The print processor should not use monochrome color optimization.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dmPrintQuality</b>

<dd>
<p>Value to be used instead of the <b>dmPrintQuality</b> member of the print job's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure, if the COLOR_OPTIMIZATION flag is set in <b>dwColorOptimization</b>.</p>
</dd>

### -field <b>dmYResolution</b>

<dd>
<p>Value to be used instead of the <b>dmYResolution</b> member of the print job's DEVMODEW structure, if the COLOR_OPTIMIZATION flag is set in <b>dwColorOptimization</b>.
     </p>
</dd>

### -field <b>dwDuplexFlags</b>

<dd>
<p>One of the following bit flag values used in duplex printing:</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>DONT_SEND_EXTRA_PAGES_FOR_DUPLEX</p>
</td>
<td>
<p>The print processor should not send extra blank pages when duplex printing.</p>
<p>For example, if you send a three-page job for duplex printing, some printers expect to receive four pages. If you print this job on Microsoft Windows XP or Windows Server 2003, the print processor sends four pages to the printer by default (the fourth page is a blank page). If you print this job on Windows Vista with this flag set, the print processor sends only the three pages of the print job and does not send the extra blank page.</p>
</td>
</tr>
<tr>
<td>
<p>REVERSE_PAGES_FOR_REVERSE_DUPLEX</p>
</td>
<td>
<p>The print processor should reverse the order of page pairs when printing in reverse duplex mode. For example, when this flag is set, the print processor should print pages in order 7, 8, 5, 6, 3, 4, 1, 2 instead of 8, 7, 6, 5, 4, 3, 2, 1.</p>
</td>
</tr>
</table>
<p> </p>
<p>Set to 0 if your driver does not require any of these options.</p>
</dd>

### -field <b>dwNupDirection</b>

<dd>
<p>One of the following bit flag values used in N-up printing:</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>RIGHT_THEN_DOWN</p>
</td>
<td>
<p>The print processor should provide page images in sequence from left to right, then down the final printed page. Also set to this value if N-up printing is not needed.</p>
</td>
</tr>
<tr>
<td>
<p>DOWN_THEN_RIGHT</p>
</td>
<td>
<p>The print processor should provide page images in sequence from top to bottom, then left to right on the final printed page.</p>
</td>
</tr>
<tr>
<td>
<p>LEFT_THEN_DOWN</p>
</td>
<td>
<p>The print processor should provide page images in sequence from right to left, then down the final printed page.</p>
</td>
</tr>
<tr>
<td>
<p>DOWN_THEN_LEFT</p>
</td>
<td>
<p>The print processor should provide page images in sequence from top to bottom, then right to left on the final printed page.</p>
</td>
</tr>
</table>
<p> </p>
<p>This flag is considered only if <b>dwJobNumberOfPagesPerSide</b> and/or <b>dwDrvNumberOfPagesPerSide</b> indicate that N-up printing is active. For more information, see the descriptions  above for <b>dwJobNumberOfPagesPerSide</b> and <b>dwDrvNumberOfPagesPerSide</b>.</p>
</dd>

### -field <b>dwBookletFlags</b>

<dd>
<p>If <b>dwJobPageOrderFlags</b> is set to BOOKLET_PRINT, one of the following values. </p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>BOOKLET_EDGE_LEFT</p>
</td>
<td>
<p>The print processor should print pages in a left-to-right booklet layout, where the bound edge of the final folded booklet is on the left edge of page one.</p>
</td>
</tr>
<tr>
<td>
<p>BOOKLET_EDGE_RIGHT</p>
</td>
<td>
<p>The print processor should print pages in a right-to-left booklet layout, where the bound edge of the final folded booklet is on the right edge of page one.</p>
</td>
</tr>
</table>
<p> </p>
<p>If <b>dwJobPageOrderFlags</b> is not set to BOOKLET_PRINT, <b>dwBookletFlags </b>is set to 0.</p>
<p>This flag is considered only if the <b>dwJobPageOrderFlags</b> member is set to BOOKLET_PRINT.</p>
</dd>

### -field <b>dwScalingPercentX</b>

<dd>
<p>Scaling percentage in the horizontal (x) direction with respect to the normal paper size. Must be in the range of 1 to 1000. Set to 100 if scaling will not be done.</p>
<div class="alert"><b>Note</b>    To ensure predictable printing results, <b>dwScalingPercentX</b> and <b>dwScalingPercentY</b> must have the same value.</div>
<div> </div>
</dd>

### -field <b>dwScalingPercentY</b>

<dd>
<p>Scaling percentage in the vertical (y) direction with respect to the normal paper size. Must be in the range of 1 to 1000. Set to 100 if scaling will not be done.</p>
<div class="alert"><b>Note</b>    To ensure predictable printing results, <b>dwScalingPercentX</b> and <b>dwScalingPercentY</b> must have the same value.</div>
<div> </div>
</dd>
</dl>

## -remarks
<p>If the <b>dmPrintQuality</b> member of a print job's DEVMODEW structure is a negative value, such as DMRES_HIGH, and if monochrome color optimization is enabled, then switching between color and monochrome could result in different resolutions being used. This is because DMRES_HIGH might be assigned to different DPI values for color and monochrome rendering. (For Unidrv-supported devices, this assignment occurs in the printer's <a href="wdkgloss.g#wdkgloss.generic_printer_description__gpd_#wdkgloss.generic_printer_description__gpd_"><i>GPD</i></a> file.) To ensure a consistent resolution throughout the print job, the driver can specify positive <b>dmPrintQuality</b> and <b>dmYResolution</b> values (representing a specific DPI resolution) to override the equivalent <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> values. </p>

<p>The EMF print processor uses the flag specified for <b>dwColorOptimization</b> to determine whether to request GDI to perform monochrome color optimization. If monochrome color optimization is enabled, the print job can be switched between monochrome and color rendering as appropriate.</p>

<p>If you are creating a Unidrv rendering plug-in to generate color watermarks, note that when the <b>dwColorOptimization</b> member is set to COLOR_OPTIMIZATION, color watermarks are printed in black and white when they are printed on black-and-white documents. To ensure that color watermarks print correctly with color and black-and-white documents, disable color optimization. Color optimization also can be controlled by the Unidrv *<b>ChangeColorModeOnDoc?</b> color attribute (see <a href="NULL">Color Attributes</a>), and by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549468">GdiEndPageEMF</a> function.</p>

<p>For a list of default values for ATTRIBUTE_INFO_4 members, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550459">GetJobAttributesEx</a>.</p>

<p>This structure is available in Windows Vista.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winddiui.h (include Winddiui.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545091">ATTRIBUTE_INFO_2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545093">ATTRIBUTE_INFO_3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548581">DrvQueryJobAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550459">GetJobAttributesEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549468">GdiEndPageEMF</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20ATTRIBUTE_INFO_4 structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
