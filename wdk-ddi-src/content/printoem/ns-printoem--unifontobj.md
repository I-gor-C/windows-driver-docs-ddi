---
UID: NS.printoem._UNIFONTOBJ
title: UNIFONTOBJ
author: windows-driver-content
description: The UNIFONTOBJ structure is used as an input parameter to font functions in rendering plug-ins.
old-location: print\unifontobj.htm
old-project: print
ms.assetid: ff3ecef2-abf2-4ecb-b4af-81e6c6d8fb4c
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: UNIFONTOBJ, UNIFONTOBJ, *PUNIFONTOBJ
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: printoem.h
req.include-header: Printoem.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UNIFONTOBJ
req.alt-loc: printoem.h
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
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# UNIFONTOBJ structure



## -description
<p>The UNIFONTOBJ structure is used as an input parameter to font functions in rendering plug-ins.</p>


## -syntax

````
typedef struct _UNIFONTOBJ {
  ULONG      ulFontID;
  DWORD      dwFlags;
  IFIMETRICS *pIFIMetrics;
  PFNGETINFO pfnGetInfo;
} UNIFONTOBJ, *PUNIFONTOBJ;
````


## -struct-fields
<dl>

### -field <b>ulFontID</b>

<dd>
<p>Specifies a resource identifier for an RC_UFM resource contained in a Unidrv minidriver's resource DLL. Supplied by Unidrv.</p>
</dd>

### -field <b>dwFlags</b>

<dd>
<p>Is a set of Unidrv-supplied bit flags. Flag definitions are as follows:</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>UFOFLAG_TTDOWNLOAD_BITMAP</p>
</td>
<td>
<p>If set, the font is a bitmap font.</p>
</td>
</tr>
<tr>
<td>
<p>UFOFLAG_TTDOWNLOAD_TTOUTLINE</p>
</td>
<td>
<p>If set, the font is a TrueType outline font.</p>
</td>
</tr>
<tr>
<td>
<p>UFOFLAG_TTFONT</p>
</td>
<td>
<p>If set, the font is a downloadable TrueType font.</p>
<p>If not set, the font is a device font.</p>
</td>
</tr>
<tr>
<td>
<p>UFOFLAG_TTOUTLINE_BOLD_SIM</p>
</td>
<td>
<p>If set, the TrueType font has bold simulation done by GDI.</p>
</td>
</tr>
<tr>
<td>
<p>UFOFLAG_TTOUTLINE_ITALIC_SIM</p>
</td>
<td>
<p>If set, the TrueType font has italic simulation done by GDI.</p>
</td>
</tr>
<tr>
<td>
<p>UFOFLAG_TTOUTLINE_VERTICAL</p>
</td>
<td>
<p>If set, the TrueType font is a vertical font. Note that this flag is available only for those Asian fonts that can be written vertically.</p>
<p>If not set, text is written horizontally.</p>
</td>
</tr>
<tr>
<td>
<p>UFOFLAG_TTSUBSTITUTED</p>
</td>
<td>
<p>If set, the device font is a font substituted for the TrueType font. In the font substitution, GDI requests that Unidrv print using a TrueType font. For performance reasons, Unidrv substitutes a device font for the TrueType font. (The substitution is specified by a <a href="wdkgloss.g#wdkgloss.generic_printer_description__gpd_#wdkgloss.generic_printer_description__gpd_"><i>generic printer description (GPD)</i></a> file or in a table in the registry.) For this substitution, for some printers, it is necessary to adjust the baseline position of the device font, because the baseline position of the device font can be higher than that of the TrueType font. The adjustment causes the output of the substituted device font to be shifted down to correct this discrepancy. Depending on the flags set in the UNIFONTOBJ structure, the printer minidriver is able to adjust the baseline position of device fonts.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>pIFIMetrics</b>

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff567418">IFIMETRICS</a> structure. Supplied by Unidrv.</p>
</dd>

### -field <b>pfnGetInfo</b>

<dd>
<p>Pointer to Unidrv's <a href="https://msdn.microsoft.com/library/windows/hardware/ff563594">UNIFONTOBJ_GetInfo</a> callback function. Supplied by Unidrv.</p>
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
<dt>Printoem.h (include Printoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563594">UNIFONTOBJ_GetInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567418">IFIMETRICS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20UNIFONTOBJ structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
