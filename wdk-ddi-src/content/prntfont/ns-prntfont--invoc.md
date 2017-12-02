---
UID: NS.prntfont._INVOC
title: INVOC
author: windows-driver-content
description: The INVOC structure is used for describing printer command strings in Unidrv font metrics files (.ufm files) and glyph translation table files (.gtt files).
old-location: print\invoc.htm
old-project: print
ms.assetid: 5eeaa7f7-dc99-4cf7-846c-801954cc9040
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: INVOC, INVOC, *PINVOC
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
req.alt-api: INVOC
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

# INVOC structure



## -description
<p>The INVOC structure is used for describing printer command strings in <a href="print.customized_font_management#ddk_unidrv_font_metrics_files_gg#ddk_unidrv_font_metrics_files_gg">Unidrv font metrics files</a> (.ufm files) and <a href="print.customized_font_management#ddk_glyph_translation_table_files_gg#ddk_glyph_translation_table_files_gg">glyph translation table files</a> (.gtt files).</p>


## -syntax

````
typedef struct _INVOC {
  DWORD dwCount;
  DWORD loOffset;
} INVOC, *PINVOC;
````


## -struct-fields
<dl>

### -field dwCount

<dd>
<p>Specifies the number of characters in the command.</p>
</dd>

### -field loOffset

<dd>
<p>Indicates one of the following:</p>
<p></p>
<dl>

### -field For .ufm files:

<dd>
<p>Specifies the byte offset from the beginning of the .ufm file's <a href="..\prntfont\ns-prntfont--unidrvinfo.md">UNIDRVINFO</a> structure to beginning of the command string.</p>
</dd>

### -field For .gtt files:

<dd>
<p>Specifies the byte offset from the beginning of the .gtt file's <a href="..\prntfont\ns-prntfont--uni-codepageinfo.md">UNI_CODEPAGEINFO</a> structure to beginning of the command string.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>INVOC structures are used within <a href="..\prntfont\ns-prntfont--unidrvinfo.md">UNIDRVINFO</a> structures.</p>

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
<a href="..\prntfont\ns-prntfont--unidrvinfo.md">UNIDRVINFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20INVOC structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
