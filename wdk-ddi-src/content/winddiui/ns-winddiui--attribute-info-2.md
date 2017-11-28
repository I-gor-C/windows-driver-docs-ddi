---
UID: NS.winddiui._ATTRIBUTE_INFO_2
title: ATTRIBUTE_INFO_2
author: windows-driver-content
description: The ATTRIBUTE_INFO_2 structure is used as a parameter for a printer interface DLL's DrvQueryJobAttributes function. All member values are function-supplied.
old-location: print\attribute_info_2.htm
old-project: print
ms.assetid: c5bb9943-ee5b-4128-9e5f-438971119e3a
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: ATTRIBUTE_INFO_2, ATTRIBUTE_INFO_2, *PATTRIBUTE_INFO_2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winddiui.h
req.include-header: Winddiui.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ATTRIBUTE_INFO_2
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
req.iface: 
req.product: Windows 10 or later.
---

# ATTRIBUTE_INFO_2 structure



## -description
<p>The ATTRIBUTE_INFO_2 structure is used as a parameter for a printer interface DLL's <a href="https://msdn.microsoft.com/library/windows/hardware/ff548581">DrvQueryJobAttributes</a> function. All member values are function-supplied.</p>


## -syntax

````
typedef struct _ATTRIBUTE_INFO_2 {
  DWORD dwJobNumberOfPagesPerSide;
  DWORD dwDrvNumberOfPagesPerSide;
  DWORD dwNupBorderFlags;
  DWORD dwJobPageOrderFlags;
  DWORD dwDrvPageOrderFlags;
  DWORD dwJobNumberOfCopies;
  DWORD dwDrvNumberOfCopies;
  DWORD dwColorOptimization;
} ATTRIBUTE_INFO_2, *PATTRIBUTE_INFO_2;
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
</dl>

## -remarks
<p>The EMF print processor uses the flag specified for <b>dwColorOptimization</b> to determine whether to request GDI to perform monochrome color optimization. If monochrome color optimization is enabled, the print job can be switched between monochrome and color rendering as appropriate.</p>

<p>If you are creating a Unidrv rendering plug-in to generate color watermarks, note that when the <b>dwColorOptimization</b> member is set to COLOR_OPTIMIZATION, color watermarks are printed in black and white when they are printed on black-and-white documents. To ensure that color watermarks print correctly with color and black-and-white documents, disable color optimization. Color optimization also can be controlled by the Unidrv *<b>ChangeColorModeOnDoc?</b> color attribute (see <a href="NULL">Color Attributes</a>), and by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549468">GdiEndPageEMF</a> function. </p>

<p>For more information about other structure members, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545090">ATTRIBUTE_INFO_1</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548581">DrvQueryJobAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545090">ATTRIBUTE_INFO_1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549468">GdiEndPageEMF</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20ATTRIBUTE_INFO_2 structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
