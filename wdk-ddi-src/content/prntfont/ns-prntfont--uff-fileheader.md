---
UID: NS.prntfont._UFF_FILEHEADER
title: UFF_FILEHEADER
author: windows-driver-content
description: The UFF_FILEHEADER structure is used to define the contents of Unidrv font format files (.uff files).
old-location: print\uff_fileheader.htm
old-project: print
ms.assetid: 18eb526b-d615-4f02-b724-236c6bf16945
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: UFF_FILEHEADER, UFF_FILEHEADER, *PUFF_FILEHEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: prntfont.h
req.include-header: Prntfont.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UFF_FILEHEADER
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
req.iface: 
req.product: Windows 10 or later.
---

# UFF_FILEHEADER structure



## -description
<p>The UFF_FILEHEADER structure is used to define the contents of <a href="print.customized_font_management#ddk_unidrv_font_format_files_gg#ddk_unidrv_font_format_files_gg">Unidrv font format files</a> (.uff files).</p>


## -syntax

````
typedef struct _UFF_FILEHEADER {
  DWORD dwSignature;
  DWORD dwVersion;
  DWORD dwSize;
  DWORD nFonts;
  DWORD nGlyphSets;
  DWORD nVarData;
  DWORD offFontDir;
  DWORD dwFlags;
  DWORD dwReserved[4];
} UFF_FILEHEADER, *PUFF_FILEHEADER;
````


## -struct-fields
<dl>

### -field <b>dwSignature</b>

<dd>
<p>Specifies the signature for .uff files. This value must be UFF_FILE_MAGIC.</p>
</dd>

### -field <b>dwVersion</b>

<dd>
<p>Specifies the format version for .uff files. This value must be UFF_VERSION_NUMBER. The HIWORD contains the major version number and the LOWORD contains the minor version number.</p>
</dd>

### -field <b>dwSize</b>

<dd>
<p>Specifies the size, in bytes, of the UFF_FILEHEADER structure.</p>
</dd>

### -field <b>nFonts</b>

<dd>
<p>Specifies the number of fonts specified within the .uff file and identified by <a href="https://msdn.microsoft.com/library/windows/hardware/ff547364">DATA_HEADER</a> structures. This is also the number of <a href="https://msdn.microsoft.com/library/windows/hardware/ff562866">UFF_FONTDIRECTORY</a> structures within the .uff file.</p>
</dd>

### -field <b>nGlyphSets</b>

<dd>
<p>Specifies the  number of glyph sets specified within the .uff file and identified by DATA_HEADER structures. Some fonts might share a glyph set.</p>
</dd>

### -field <b>nVarData</b>

<dd>
<p>Specifies the  number of variable data sections specified within the .uff file and identified by DATA_HEADER structures.</p>
</dd>

### -field <b>offFontDir</b>

<dd>
<p>Specifies the offset, in bytes, from the beginning of the .uff file to the beginning of the first <a href="https://msdn.microsoft.com/library/windows/hardware/ff562866">UFF_FONTDIRECTORY</a> structure.</p>
</dd>

### -field <b>dwFlags</b>

<dd>
<p>Is a set of bit flags, as specified in the following table.</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>FONT_DIR_SORTED</p>
</td>
<td>
<p>The array of UFF_FONTDIRECTORY structures (specified by <b>offFontDir</b>) is sorted by the contents of that structure's <b>wFontID</b> member.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwReserved</b>

<dd>
<p>Reserved. Must be set to zero.</p>
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
<dt>Prntfont.h (include Prntfont.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562866">UFF_FONTDIRECTORY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547364">DATA_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20UFF_FILEHEADER structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
