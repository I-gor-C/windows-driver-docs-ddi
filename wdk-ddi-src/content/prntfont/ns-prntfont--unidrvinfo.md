---
UID: NS.prntfont._UNIDRVINFO
title: UNIDRVINFO
author: windows-driver-content
description: The UNIDRVINFO structure is used to specify printer-specific information within Unidrv font metrics files (.ufm files).
old-location: print\unidrvinfo.htm
ms.assetid: f57514ed-33b2-4895-aaba-5866b6fc01d2
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: prntfont.h
req.include-header: Prntfont.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UNIDRVINFO
req.alt-loc: prntfont.h
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
ms.keywords: UNIDRVINFO, UNIDRVINFO, *PUNIDRVINFO
req.iface: 
req.product: Windows 10 or later.
---

# UNIDRVINFO structure



## -description
<p>The UNIDRVINFO structure is used to specify printer-specific information within <a href="print.customized_font_management#ddk_unidrv_font_metrics_files_gg#ddk_unidrv_font_metrics_files_gg">Unidrv font metrics files</a> (.ufm files).</p>


## -syntax

````
typedef struct _UNIDRVINFO {
  DWORD dwSize;
  DWORD flGenFlags;
  WORD  wType;
  WORD  fCaps;
  WORD  wXRes;
  WORD  wYRes;
  short sYAdjust;
  short sYMoved;
  WORD  wPrivateData;
  short sShift;
  INVOC SelectFont;
  INVOC UnSelectFont;
  WORD  wReserved[4];
} UNIDRVINFO, *PUNIDRVINFO;
````


## -struct-fields
<dl>

### -field <b>dwSize</b>

<dd>
<p>Specifies the size, in bytes, of the UNIDRVINFO structure.</p>
</dd>

### -field <b>flGenFlags</b>

<dd>
<p>Contains one or more bit flags describing font characteristics. The following flags are defined:</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>UFM_CART</p>
</td>
<td>
<p>The font is contained in a cartridge.</p>
</td>
</tr>
<tr>
<td>
<p>UFM_SCALABLE</p>
</td>
<td>
<p>The font is scalable.</p>
</td>
</tr>
<tr>
<td>
<p>UFM_SOFT</p>
</td>
<td>
<p>The font is a soft font, requiring downloading.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>wType</b>

<dd>
<p>Contains an integer constant describing the font type. The following constants are defined: </p>
<table>
<tr>
<th>Constant</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>DF_TYPE_CAPSL</p>
</td>
<td>
<p>Canon CAPSL scalable font</p>
</td>
</tr>
<tr>
<td>
<p>DF_TYPE_HPINTELLIFONT</p>
</td>
<td>
<p>HP Intellifont font</p>
</td>
</tr>
<tr>
<td>
<p>DF_TYPE_OEM1</p>
</td>
<td>
<p>OEM-supplied scalable font</p>
</td>
</tr>
<tr>
<td>
<p>DF_TYPE_OEM2</p>
</td>
<td>
<p>OEM-supplied scalable font</p>
</td>
</tr>
<tr>
<td>
<p>DF_TYPE_PST1</p>
</td>
<td>
<p>Lexmark PPDS scalable font</p>
</td>
</tr>
<tr>
<td>
<p>DF_TYPE_TRUETYPE</p>
</td>
<td>
<p>HP PCLETTO font for LJ4 printers</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>fCaps</b>

<dd>
<p>Contains one or more bit flags identifying limitations on the capabilities provided by a device font. The following flags are defined:</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>DF_BKSP_OK</p>
</td>
<td>
<p>If set, a single backspace character can move the cursor to the beginning of the overstrike region. If not set, an x-movement cursor command must be sent.</p>
<p>(Used only if MTYPE_PAIRED is specified for the character's <a href="https://msdn.microsoft.com/library/windows/hardware/ff562816">TRANSDATA</a> structure in <a href="https://msdn.microsoft.com/library/windows/hardware/ff556509">MAPTABLE</a>. Otherwise ignored.)</p>
</td>
</tr>
<tr>
<td>
<p>DF_NO_BOLD</p>
</td>
<td>
<p>The device font cannot be bolded using underline simulation.</p>
</td>
</tr>
<tr>
<td>
<p>DF_NO_DOUBLE_UNDERLINE</p>
</td>
<td>
<p>The device font cannot be double-underlined using double-underline simulation.</p>
</td>
</tr>
<tr>
<td>
<p>DF_NO_STRIKETHRU</p>
</td>
<td>
<p>The device font cannot be struck through using strike-through simulation.</p>
</td>
</tr>
<tr>
<td>
<p>DF_NOITALIC</p>
</td>
<td>
<p>The device font cannot be italicized using italic simulation.</p>
</td>
</tr>
<tr>
<td>
<p>DF_NOUNDER</p>
</td>
<td>
<p>The device font cannot be underlined using underline simulation.</p>
</td>
</tr>
<tr>
<td>
<p>DF_XM_CR</p>
</td>
<td>
<p>Unidrv must send a carriage return command after each line of text.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>wXRes</b>

<dd>
<p>Specifies the font's x-resolution.</p>
</dd>

### -field <b>wYRes</b>

<dd>
<p>Specifies the font's y-resolution.</p>
</dd>

### -field <b>sYAdjust</b>

<dd>
<p>Specifies the amount of vertical adjustment required before output of double-height characters on dot-matrix printers.</p>
</dd>

### -field <b>sYMoved</b>

<dd>
<p>Specifies the amount of vertical cursor movement that results when a double-height character is printed on a dot-matrix printer.</p>
</dd>

### -field <b>wPrivateData</b>

<dd>
<p>Can be used for printer-specific information such as, for example, HP DeskJet permutations.</p>
</dd>

### -field <b>sShift</b>

<dd>
<p>Specifies the number of pixels by which each character must be shifted. Used for the Microsoft Z1a cartridge.</p>
</dd>

### -field <b>SelectFont</b>

<dd>
<p>Is an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551796">INVOC</a> structure containing the printer's font selection command.</p>
</dd>

### -field <b>UnSelectFont</b>

<dd>
<p>Is an INVOC structure containing the printer's font deselection command.</p>
</dd>

### -field <b>wReserved</b>

<dd>
<p>Not used.</p>
</dd>
</dl>

## -remarks
<p>A .ufm (Unidrv Font Metrics) file's UNIDRVINFO structure is accessed by a pointer in the file's <a href="https://msdn.microsoft.com/library/windows/hardware/ff563587">UNIFM_HDR</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Prntfont.h (include Prntfont.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551796">INVOC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20UNIDRVINFO structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
