---
UID: NF.prcomoem.IPrintCoreHelperUni.SetFontSubstitution
title: IPrintCoreHelperUni::SetFontSubstitution
author: windows-driver-content
description: The IPrintCoreHelperUni::SetFontSubstitution method specifies the device font to print in place of a given TrueType font.
old-location: print\iprintcorehelperuni_setfontsubstitution.htm
ms.assetid: 73afb4e9-23c7-473c-937f-045bf5e332f7
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintCoreHelperUni.SetFontSubstitution
req.alt-loc: Prcomoem.h
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
ms.keywords: IPrintCoreHelperUni, SetFontSubstitution, IPrintCoreHelperUni::SetFontSubstitution
req.iface: IPrintCoreHelperUni
req.product: Windows 10 or later.
---

# IPrintCoreHelperUni::SetFontSubstitution method



## -description
<p>The <code>IPrintCoreHelperUni::SetFontSubstitution</code> method specifies the device font to print in place of a given TrueType font. </p>


## -syntax

````
STDMETHOD SetFontSubstitution(
  [in] PCWSTR pszTrueTypeFontName,
  [in] PCWSTR pszDevFontName
);
````


## -parameters
<dl>

### -param <i>pszTrueTypeFontName</i> [in]

<dd>
<p>A pointer to a null-terminated Unicode string that contains a valid TrueType font name. This parameter must not be <b>NULL</b>.</p>
</dd>

### -param <i>pszDevFontName</i> [in]

<dd>
<p>A pointer to a null-terminated Unicode string that contains the name of the device font. </p>
</dd>
</dl>

## -returns
<p><code>IPrintCoreHelperUni::SetFontSubstitution</code> should return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method read the option for the specified feature.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The font that was requested does not exist or was not a TrueType font.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>One or more of the arguments is invalid.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>The core driver was not able to service the request because there was insufficient memory.</p><dl>
<dt><b>E_UNEXPECTED, or other return codes not listed here</b></dt>
</dl><p>The core driver seems to be in an invalid state. The caller should return a failure code.</p>

<p> </p>

## -remarks
<p>Setting a device font to use in place of a specified TrueType font can occur only during the device property sheets session and only if full UI replacement is enabled. The font that is represented by the <i>pszTrueTypeFontName</i> parameter must be a valid TrueType font and must be installed on the printer. The device font that is represented by the <i>pszDevFontName</i> parameter must be a valid font for this printer.</p>

<p>If a substitution mapping for the specified TrueType font already exists on this queue, the <code>SetFontSubstitution</code> method will silently replace the mapping. To remove a substitution mapping, call this method with the TrueType font name specified in <i>pszTrueTypeFontName</i> and with <b>NULL</b> specified in <i>pszDevFontName</i>.</p>

<p>To obtain a list of valid device fonts, create an information context for the current printer, and call <b>SetGraphicsMode</b>(hIC, GM_ADVANCED). Then, enumerate device fonts by calling <b>EnumFontFamilies</b>. The callback parameter (see <b>EnumFontFamProc</b> in the Microsoft Windows SDK documentation) of <b>EnumFontFamilies</b> should filter for device fonts by incrementing a counter for each font for which the bitwise AND result (FontType &amp; TRUETYPE_FONTTYPE) is nonzero. The <b>SetGraphicsMode</b>, <b>EnumFontFamilies</b>, and <b>EnumFontFamProc</b> functions are described in the Windows SDK documentation.</p>

<p>Setting a device font to use in place of a specified TrueType font can occur only during the device property sheets session and only if full UI replacement is enabled. The font that is represented by the <i>pszTrueTypeFontName</i> parameter must be a valid TrueType font and must be installed on the printer. The device font that is represented by the <i>pszDevFontName</i> parameter must be a valid font for this printer.</p>

<p>If a substitution mapping for the specified TrueType font already exists on this queue, the <code>SetFontSubstitution</code> method will silently replace the mapping. To remove a substitution mapping, call this method with the TrueType font name specified in <i>pszTrueTypeFontName</i> and with <b>NULL</b> specified in <i>pszDevFontName</i>.</p>

<p>To obtain a list of valid device fonts, create an information context for the current printer, and call <b>SetGraphicsMode</b>(hIC, GM_ADVANCED). Then, enumerate device fonts by calling <b>EnumFontFamilies</b>. The callback parameter (see <b>EnumFontFamProc</b> in the Microsoft Windows SDK documentation) of <b>EnumFontFamilies</b> should filter for device fonts by incrementing a counter for each font for which the bitwise AND result (FontType &amp; TRUETYPE_FONTTYPE) is nonzero. The <b>SetGraphicsMode</b>, <b>EnumFontFamilies</b>, and <b>EnumFontFamProc</b> functions are described in the Windows SDK documentation.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Prcomoem.h (include Prcomoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552936">IPrintCoreHelperUni::GetFontSubstitution</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreHelperUni::SetFontSubstitution method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
