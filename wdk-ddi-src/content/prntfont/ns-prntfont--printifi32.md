---
UID: NS.prntfont._PRINTIFI32
title: PRINTIFI32
author: windows-driver-content
description: The PRINTIFI32 structure is a fixed-size version of the IFIMETRICS structure, and defines information for a given typeface that GDI can use.
old-location: display\printifi32.htm
old-project: display
ms.assetid: f8e77eb1-3964-4ca0-8ae7-2e9617671990
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: PRINTIFI32, PRINTIFI32, *PPRINTIFI32
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
req.alt-api: PRINTIFI32
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

# PRINTIFI32 structure



## -description
<p>The PRINTIFI32 structure is a fixed-size version of the <a href="display.ifimetrics">IFIMETRICS</a> structure, and defines information for a given typeface that GDI can use. </p>


## -syntax

````
typedef struct _PRINTIFI32 {
  ULONG   cjThis;
  ULONG   cjIfiExtra;
  PTRDIFF dpwszFamilyName;
  PTRDIFF dpwszStyleName;
  PTRDIFF dpwszFaceName;
  PTRDIFF dpwszUniqueName;
  PTRDIFF dpFontSim;
  LONG    lEmbedId;
  LONG    lItalicAngle;
  LONG    lCharBias;
  PTRDIFF dpCharSets;
  BYTE    jWinCharSet;
  BYTE    jWinPitchAndFamily;
  USHORT  usWinWeight;
  ULONG   flInfo;
  USHORT  fsSelection;
  USHORT  fsType;
  FWORD   fwdUnitsPerEm;
  FWORD   fwdLowestPPEm;
  FWORD   fwdWinAscender;
  FWORD   fwdWinDescender;
  FWORD   fwdMacAscender;
  FWORD   fwdMacDescender;
  FWORD   fwdMacLineGap;
  FWORD   fwdTypoAscender;
  FWORD   fwdTypoDescender;
  FWORD   fwdTypoLineGap;
  FWORD   fwdAveCharWidth;
  FWORD   fwdMaxCharInc;
  FWORD   fwdCapHeight;
  FWORD   fwdXHeight;
  FWORD   fwdSubscriptXSize;
  FWORD   fwdSubscriptYSize;
  FWORD   fwdSubscriptXOffset;
  FWORD   fwdSubscriptYOffset;
  FWORD   fwdSuperscriptXSize;
  FWORD   fwdSuperscriptYSize;
  FWORD   fwdSuperscriptXOffset;
  FWORD   fwdSuperscriptYOffset;
  FWORD   fwdUnderscoreSize;
  FWORD   fwdUnderscorePosition;
  FWORD   fwdStrikeoutSize;
  FWORD   fwdStrikeoutPosition;
  BYTE    chFirstChar;
  BYTE    chLastChar;
  BYTE    chDefaultChar;
  BYTE    chBreakChar;
  WCHAR   wcFirstChar;
  WCHAR   wcLastChar;
  WCHAR   wcDefaultChar;
  WCHAR   wcBreakChar;
  POINTL  ptlBaseline;
  POINTL  ptlAspect;
  POINTL  ptlCaret;
  RECTL   rclFontBox;
  BYTE    achVendId[4];
  ULONG   cKerningPairs;
  ULONG   ulPanoseCulture;
  PANOSE  panose;
} PRINTIFI32, *PPRINTIFI32;
````


## -struct-fields
<dl>

### -field cjThis

<dd>
<p>Specifies the size in bytes of this structure. The specified size includes any Unicode strings appended to the end of this structure, plus the size in bytes of the optional <a href="display.ifiextra">IFIEXTRA</a> structure.</p>
</dd>

### -field cjIfiExtra

<dd>
<p>Specifies the size in bytes of the IFIEXTRA structure that follows this structure. A value of zero indicates that no IFIEXTRA structure is present.</p>
</dd>

### -field dpwszFamilyName

<dd>
<p>Specifies the offset in bytes to a null-terminated Unicode string containing the family name of the font (for example, "Times Roman"). Generally, this string immediately follows this structure. This string should be the same as the name recorded in the <b>lfFaceName</b> member of the Win32 LOGFONT structure.</p>
</dd>

### -field dpwszStyleName

<dd>
<p>Specifies the offset in bytes to a null-terminated Unicode string describing the style of the font (for example, "Bold").</p>
</dd>

### -field dpwszFaceName

<dd>
<p>Specifies the offset in bytes to a null-terminated Unicode string representing the unique and complete name of the font. The name contains the family and subfamily names of the font (for example, "Times New Roman Bold").</p>
</dd>

### -field dpwszUniqueName

<dd>
<p>Specifies the offset in bytes to a null-terminated Unicode string representing the unique identifier of the font (for example, "Monotype:Times New Roman:1990").</p>
</dd>

### -field dpFontSim

<dd>
<p>Specifies the offset in bytes from the beginning of this structure to a <a href="display.fontsim">FONTSIM</a> structure that describes the simulations that the font supports. The driver should set this member to a nonzero value only if the font supports bold, italic, or bold italic simulations; otherwise, the driver should set this to zero.</p>
<p>Note that if a font is italic by design, the driver should not indicate font support for italic simulation although it can indicate font support for bold italic simulation. Similarly, the driver should not indicate font support for bold simulation if the font is bold by design, but can indicate font support for bold italic simulation. If the font is both bold and italic by design, it should not support any simulations.</p>
<p>The offsets in the <a href="display.fontsim">FONTSIM</a> structure are relative to the base of the FONTSIM structure.</p>
</dd>

### -field lEmbedId

<dd>
<p>Specifies the Embedding ID of the font. This value is TrueType-specific and should be set to zero by all other font providers.</p>
</dd>

### -field lItalicAngle

<dd>
<p>Specifies the italic angle of the font. This value is TrueType-specific and should be set to zero by all other font providers.</p>
</dd>

### -field lCharBias

<dd>
<p>Specifies the character bias. This value is TrueType-specific and should be set to zero by all other font providers.</p>
</dd>

### -field dpCharSets

<dd>
<p>Specifies the offset from the beginning of this structure to an array containing a list of all Windows character sets supported by this font. The array is 16 bytes in size and is always terminated with DEFAULT_CHARSET. The first value of the array should identify the Windows character set that has the best and most complete coverage in the font; this value should also be stored in <b>jWinCharSet</b>. For instance, if this is a Japanese font that also supports US ANSI and Cyrillic character sets, then <b>jWinCharSet</b> should be set to SHIFTJIS_CHARSET and the array identified by <b>dpCharSets</b> would contain SHIFTJIS_CHARSET, ANSI_CHARSET, RUSSIAN_CHARSET, DEFAULT_CHARSET.</p>
<p>If this font does not support more than one Windows character set, <b>dpCharSets</b> should be set to zero.</p>
</dd>

### -field jWinCharSet

<dd>
<p>Identifies the character set best supported by this font. If the font supports only a single Windows character set, the driver should store the corresponding value in <b>jWinCharSet</b>. The driver should not store DEFAULT_CHARSET in this field. This member can be one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ANSI_CHARSET</p>
</td>
<td>
<p>This font supports the Windows ANSI character set.</p>
</td>
</tr>
<tr>
<td>
<p>ARABIC_CHARSET</p>
</td>
<td>
<p>This font supports the Arabic character set.</p>
</td>
</tr>
<tr>
<td>
<p>BALTIC_CHARSET</p>
</td>
<td>
<p>This font supports the Baltic character set.</p>
</td>
</tr>
<tr>
<td>
<p>CHINESEBIG5_CHARSET</p>
</td>
<td>
<p>This font supports the traditional Chinese (Big 5) character set.</p>
</td>
</tr>
<tr>
<td>
<p>EASTEUROPE_CHARSET</p>
</td>
<td>
<p>This font supports the Eastern European character set.</p>
</td>
</tr>
<tr>
<td>
<p>GB2312_CHARSET</p>
</td>
<td>
<p>This font supports the simplified (PRC) Chinese character set.</p>
</td>
</tr>
<tr>
<td>
<p>GREEK_CHARSET</p>
</td>
<td>
<p>This font supports the Greek character set.</p>
</td>
</tr>
<tr>
<td>
<p>HANGEUL_CHARSET</p>
</td>
<td>
<p>This font supports the Korean (Hangeul) character set.</p>
</td>
</tr>
<tr>
<td>
<p>HEBREW_CHARSET</p>
</td>
<td>
<p>This font supports the Hebrew character set.</p>
</td>
</tr>
<tr>
<td>
<p>JOHAB_CHARSET</p>
</td>
<td>
<p>This font supports the Korean (Johab) character set.</p>
</td>
</tr>
<tr>
<td>
<p>OEM_CHARSET</p>
</td>
<td>
<p>This font supports an OEM-specific character set. The OEM character set is system dependent.</p>
</td>
</tr>
<tr>
<td>
<p>SHIFTJIS_CHARSET</p>
</td>
<td>
<p>This font supports the Shift-JIS (Japanese Industry Standard) character set.</p>
</td>
</tr>
<tr>
<td>
<p>SYMBOL_CHARSET</p>
</td>
<td>
<p>This font supports the Windows symbol character set.</p>
</td>
</tr>
<tr>
<td>
<p>RUSSIAN_CHARSET</p>
</td>
<td>
<p>This font supports the Cyrillic character set.</p>
</td>
</tr>
<tr>
<td>
<p>THAI_CHARSET</p>
</td>
<td>
<p>This font supports the Thai character set.</p>
</td>
</tr>
<tr>
<td>
<p>TURKISH_CHARSET</p>
</td>
<td>
<p>This font supports the Turkish character set.</p>
</td>
</tr>
<tr>
<td>
<p>VIETNAMESE_CHARSET</p>
</td>
<td>
<p>This font supports the Vietnamese character set.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field jWinPitchAndFamily

<dd>
<p>Specifies the pitch of the font. The two low-order bits specify the pitch of the font and can be one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FIXED_PITCH</p>
</td>
<td>
<p>For fixed pitch fonts</p>
</td>
</tr>
<tr>
<td>
<p>VARIABLE_PITCH</p>
</td>
<td>
<p>For variable pitch fonts</p>
</td>
</tr>
</table>
<p> </p>
<p>Bits 4 through 7 of this member specify the font family and can be one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FF_DECORATIVE</p>
</td>
<td>
<p>Novelty fonts, such as Old English.</p>
</td>
</tr>
<tr>
<td>
<p>FF_DONTCARE</p>
</td>
<td>
<p>Don't care or unknown.</p>
</td>
</tr>
<tr>
<td>
<p>FF_MODERN</p>
</td>
<td>
<p>Fonts with constant stroke width (fixed-pitch), with or without serifs. Fixed-pitch fonts are usually modern, such as Pica, Elite, and Courier.</p>
</td>
</tr>
<tr>
<td>
<p>FF_ROMAN</p>
</td>
<td>
<p>Fonts with variable stroke width (proportionally spaced) and with serifs, such as Times Roman, Palatino, and Century Schoolbook.</p>
</td>
</tr>
<tr>
<td>
<p>FF_SCRIPT</p>
</td>
<td>
<p>Fonts designed to look like handwriting, such as Script and Cursive.</p>
</td>
</tr>
<tr>
<td>
<p>FF_SWISS</p>
</td>
<td>
<p>Fonts with variable stroke width (proportionally spaced) and without serifs, such as Helvetica and Swiss.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field usWinWeight

<dd>
<p>Specifies the weight of the font in the range 0 to 1000 (for example, 400 is normal and 700 is bold). This value is provided to the application in the <b>lfWeight</b> member of the Win32 LOGFONT structure.</p>
</dd>

### -field flInfo

<dd>
<p>Specifies additional information about the font. This field can be a combination of the following flag values:</p>
<p>Value</p>
<p>Meaning</p>
<p></p>
<dl>

### -field FM_INFO_1BPP

<dd>
<p>Indicates that a glyph bitmap has a color depth of one bit per pixel. For Windows NT 3.1, the first version of Windows NT, this flag must be set.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_4BPP

<dd>
<p>Indicates that a glyph bitmap has a color depth of four bits per pixel. The driver should set this if the font supports antialiased glyph bitmaps with 16 levels of gray.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_8BPP

<dd>
<p>Indicates that a glyph bitmap has a color depth of eight bits per pixel. The current version of GDI will ignore this setting as it does not support color fonts.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_16BPP

<dd>
<p>Indicates that a glyph bitmap has a color depth of 16 bits per pixel. The current version of GDI will ignore this setting as it does not support color fonts.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_24BPP

<dd>
<p>Indicates that a glyph bitmap has a color depth of 24 bits per pixel. The current version of GDI will ignore this setting as it does not support color fonts.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_32BPP

<dd>
<p>Indicates that a glyph bitmap has a color depth of 32 bits per pixel. The current version of GDI will ignore this setting as it does not support color fonts.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_90DEGREE_ROTATIONS

<dd>
<p>Indicates that the font can be realized in 90 degree rotations of the original notional shape. GDI requests the rotation of a font by including the rotation in the notional to device transformation passed to the driver when creating the font. This member has meaning only when the FM_INFO_ARB_XFORMS flag has not been set.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_ANISOTROPIC_SCALING_ONLY

<dd>
<p>Indicates that the font supports only arbitrary anisotropic scaling. That is, transforms are equivalent to a diagonal matrix multiplied by a positive real number. If this flag is set, then the FM_INFO_ARB_XFORMS and the FM_INFO_ISOTROPIC_SCALING_ONLY flags cannot be set. If the FM_INFO_90DEGREE_ROTATIONS flag is also set, the font supports transformations that are a combination of a simple anisotropic scaling followed by a rotation by a multiple of 90 degrees.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_ARB_XFORMS

<dd>
<p>Indicates that a font can be realized under a continuous range of two dimensional linear transformations.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_CONSTANT_WIDTH

<dd>
<p>Indicates that all glyphs of the font under all realizations have the same value of character increment. If this flag is set, the FM_INFO_OPTICALLY_FIXED_PITCH flag must also be set.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_DBCS_FIXED_PITCH

<dd>
<p>Indicates that double-byte characters for this font are fixed pitch. Nothing is implied about single byte characters. This flag is meaningful only for fonts that support a double-byte character set (DBCS), such as shift JIS. Fonts that do not support a DBCS should not set this flag.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_DO_NOT_ENUMERATE

<dd>
<p>Indicates that this font will not be enumerated by the Win32 <b>EnumFontFamiliesEx</b>, <b>EnumFontFamilies</b> or <b>EnumFonts</b> routines. Moreover, the string returned to a Win32 application call to <b>GetTextFace</b> will be retrieved from the string <b>dpwszUniqueName</b>. This flag allows the font provider to associate more than one PRINTIFI32 structure with one of its fonts.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_DSIG

<dd>
<p>Indicates that a font is compliant with the Unicode standard.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_FAMILY_EQUIV

<dd>
<p>Indicates that the <b>dpwszFamilyName</b> offset in PRINTIFI32 is actually the offset to a list of equivalent family names or aliases. The first name is the base or real name; the subsequent names are equivalents or aliases. Each name in the list is null-terminated; the list is terminated by two zeros.</p>
<p>
<dl>

### -field &lt;base name&gt; &lt;0&gt; &lt;alias 1&gt; &lt;0&gt;...&lt;alias n&gt;


### -field &lt;0&gt; &lt;0&gt;

</dl>
</p>
<p>The based names are used only for mapping; they are not enumerated.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_IGNORE_TC_RA_ABLE

<dd>
<p>Indicates that, for this font, the TC_RA_ABLE flag is ignored.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_INTEGER_WIDTH

<dd>
<p>Indicates that all glyphs have nonfractional advance widths. Bitmap fonts usually set this flag.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_INTEGRAL_SCALING

<dd>
<p>Indicates that the font can be scaled by an integral amount in both the x and y directions. If this flag is set, then the driver must be able to render glyphs in the case where the notional to device transformation is scaled by integral amounts in the x and y directions. GDI requests the integral scaling of a font by including the axial scalings in the notional to device transformation passed to the driver when creating the font. This flag is meaningful only when the FM_INFO_ARB_XFORMS flag has not been set.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_ISOTROPIC_SCALING_ONLY

<dd>
<p>Indicates that the font supports arbitrary isotropic scaling only. That is, transforms are equivalent to the identity matrix multiplied by a positive real number. If this flag is set, then neither the FM_INFO_ARB_XFORMS nor the FM_INFO_ANISOTROPIC_SCALING_ONLY flags can be set. If the FM_INFO_90DEGREE_ROTATIONS flag is set, the font supports transformations equivalent to an isotropic scaling followed by a rotation by a multiple of 90 degrees.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_OPTICALLY_FIXED_PITCH

<dd>
<p>Indicates that this font is considered typographically as fixed pitch. This is an optical quality of the font and does not necessarily indicate that all the glyphs of the font have the same character increment.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_NONNEGATIVE_AC

<dd>
<p>Indicates that all glyphs of this font have nonnegative <i>a</i> and <i>c</i> spacing. That is, the glyph black box never extends outside the region bordered by the character origin and the character concatenation point.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_NOT_CONTIGUOUS

<dd>
<p>Indicates that the supported character set is not contiguous.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_RETURNS_BITMAPS

<dd>
<p>Indicates that the font contains a valid digital signature.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_RETURNS_OUTLINES

<dd>
<p>Indicates that for any glyph supported by the driver, GDI can request a <a href="display.pathobj">PATHOBJ</a> structure that describes the outline of that glyph. If possible, when the outline is filled using GDI's path filling conventions, the resulting bitmap should be identical to the bitmap returned by the driver. The FM_INFO_RETURNS_OUTLINES and FM_INFO_RETURNS_STOKES flags cannot be set concurrently.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_RETURNS_STROKES

<dd>
<p>Indicates that for any glyph supported by the drivers, GDI can request a PATHOBJ structure that describes the spline of the glyph. This path cannot be filled but can be stroked to give a representation of the glyph. The FM_INFO_RETURNS_OUTLINES and FM_INFO_RETURNS_STOKES flags cannot be set concurrently.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_RIGHT_HANDED

<dd>
<p>Indicates that the ascent direction of the font is 90 degrees counterclockwise from the baseline direction. The ascent direction is the direction along which height is measured and is always perpendicular to the baseline direction.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_TECH_BITMAP

<dd>
<p>Indicates that the font is a bitmap font.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_TECH_CFF

<dd>
<p>Indicates that the font is a Pscript OpenType font that contains a Compact Font Format (CFF) table.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_TECH_MM

<dd>
<p>Indicates that this is a Multiple Master (MM) font.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_TECH_OUTLINE_NOT_TRUETYPE

<dd>
<p>Indicates that the font is based on a scalable font technology that uses outline paths, but is not based on TrueType. This flag does not specify whether the paths returned for this font should be filled or stroked; the consumer should examine the FM_INFO_RETURNS_STROKES and FM_INFO_RETURNS_OUTLINES flags for this information.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_TECH_STROKE

<dd>
<p>Indicates that the font is based on a stroked font technology. This flag does not specify whether the paths returned for this font should be filled or stroked; the consumer should examine the FM_INFO_RETURNS_STROKES and FM_INFO_RETURNS_OUTLINES flags for this information.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_TECH_TRUETYPE

<dd>
<p>Indicates that the font is a TrueType font.</p>
</dd>
</dl>
<p></p>
<dl>

### -field FM_INFO_TECH_TYPE1

<dd>
<p>Indicates that this font is a PostScript screen font (either Type1 or OpenType PostScript).</p>
</dd>
</dl>
</dd>

### -field fsSelection

<dd>
<p>Specifies a combination of the following flags:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FM_SEL_BOLD</p>
</td>
<td>
<p>Set if the characters of the font are bold.</p>
</td>
</tr>
<tr>
<td>
<p>FM_SEL_ITALIC</p>
</td>
<td>
<p>Set if the characters of the font are italic.</p>
</td>
</tr>
<tr>
<td>
<p>FM_SEL_NEGATIVE</p>
</td>
<td>
<p>Set if the characters of the font have the foreground and background reversed.</p>
</td>
</tr>
<tr>
<td>
<p>FM_SEL_OUTLINED</p>
</td>
<td>
<p>Set if the characters of the font are hollow.</p>
</td>
</tr>
<tr>
<td>
<p>FM_SEL_REGULAR</p>
</td>
<td>
<p>Set if the characters of the font are normal weight.</p>
</td>
</tr>
<tr>
<td>
<p>FM_SEL_STRIKEOUT</p>
</td>
<td>
<p>Set if the characters of the font are struck out by default; otherwise strikeouts must be simulated.</p>
</td>
</tr>
<tr>
<td>
<p>FM_SEL_UNDERSCORE</p>
</td>
<td>
<p>Set if all the characters of the font are underscored by default; otherwise underscoring must be simulated.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field fsType

<dd>
<p>This is a TrueType-specific bitfield indicating certain properties for the font, such as font embedding and licensing rights for the font. Embeddable fonts can be stored in a document. When a document with embedded fonts is opened on a system that does not have the font installed (the remote system), the embedded font can be loaded for temporary (and in some cases permanent) use on that system by an embedding-aware application. Embedding licensing rights are granted by the font vendor. The following flags can be set:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FM_EDITABLE_EMBED</p>
</td>
<td>
<p>Set if the font can be embedded and temporarily loaded on other systems. Documents containing Editable fonts can be opened for reading and writing.</p>
</td>
</tr>
<tr>
<td>
<p>FM_READONLY_EMBED</p>
</td>
<td>
<p>Set if read/write embedding is not permitted; only "preview and print" encapsulation is allowed. When this bit is set, the font can be embedded and temporarily loaded on the remote system. Documents containing "preview and print" fonts must be opened "read-only;" no edits can be applied to the document.</p>
</td>
</tr>
<tr>
<td>
<p>
<dl>

### -field FM_TYPE_LICENSED


### -field FM_NO_EMBEDDING

</dl>
</p>
</td>
<td>
<p>Set if the font is a Restricted License font. When only this bit is set, this font <i>must not be modified, embedded, or exchanged in any manner</i> without first obtaining permission of the legal owner. For Restricted License embedding to take effect, it must be the only level of embedding selected.</p>
</td>
</tr>
</table>
<p> </p>
<p>Fonts with the FM_READONLY_EMBED bit set indicate that they can be embedded within documents but must only be installed <i>temporarily</i> on the remote system. Any document that includes an FM_READONLY_EMBED font must be opened "read-only." That is, the application can let the user view and/or print the document, but not edit it.</p>
<p>Fonts with the FM_EDITABLE_EMBED bit set indicate that they can be embedded in documents, but must only be installed <i>temporarily</i> on the remote system. In contrast to FM_READONLY_EMBED fonts, documents containing Editable fonts can be opened "read/write;" editing is permitted, and changes can be saved.</p>
<p>Fonts with no <b>fsType</b> bits set indicate that they can be embedded and permanently installed on the remote system by an application. The user of the remote system acquires the identical rights, obligations, and licenses for that font as the original purchaser of the font, and is subject to the same end-user license agreement, copyright, design patent, and/or trademark as was the original purchaser.</p>
<p>Applications that implement support for font embedding, either through use of the Font Embedding DLL or through other means, must not embed fonts that are not licensed to permit embedding. Further, applications loading embedded fonts for temporary use <i>must</i> delete the fonts when the document containing the embedded font is closed.</p>
<p>If multiple embedding bits are set, the <i>least</i> restrictive license granted takes precedence. For example, if bits 1 and 3 are set, bit 3 takes precedence over bit 1and the font can be embedded with Editable rights. For compatibility purposes, most vendors granting Editable embedding rights also set the Preview &amp; Print bit (0x000C). This permits an application that only supports Preview &amp; Print embedding to detect that font embedding is allowed.</p>
</dd>

### -field fwdUnitsPerEm

<dd>
<p>Specifies the em-height of the font.</p>
</dd>

### -field fwdLowestPPEm

<dd>
<p>Specifies the smallest readable size of the font, in pixels. This value is ignored for bitmap fonts.</p>
</dd>

### -field fwdWinAscender

<dd>
<p>Specifies the Windows ascender value for the font.</p>
</dd>

### -field fwdWinDescender

<dd>
<p>Specifies the Windows descender value for the font.</p>
</dd>

### -field fwdMacAscender

<dd>
<p>Specifies the Macintosh ascender value for the font.</p>
</dd>

### -field fwdMacDescender

<dd>
<p>Specifies the Macintosh descender value for the font. This number is typically less than zero. It measures the signed displacement from the base line of the lowest descender in the Macintosh character set.</p>
</dd>

### -field fwdMacLineGap

<dd>
<p>Specifies the Macintosh line gap for the font. The suggested Macintosh interline spacing is equal to <b>fwdMacLineGap</b> + <b>fwdMacAscender</b> âˆ’ <b>fwdMacDescender</b>.</p>
</dd>

### -field fwdTypoAscender

<dd>
<p>Specifies the typographic ascender value for the font.</p>
</dd>

### -field fwdTypoDescender

<dd>
<p>Specifies the typographic descender value for the font. This value specifies the signed displacement of the lowest descender from the baseline.</p>
</dd>

### -field fwdTypoLineGap

<dd>
<p>Specifies the typographic line gap for the font.</p>
</dd>

### -field fwdAveCharWidth

<dd>
<p>Specifies the arithmetic average of the width of all of the 26 lower case letters 'a' through 'z' of the Latin alphabet and the space character. If any of the 26 lowercase letters are not present, then this member should be set equal to the weighted average of all glyphs in the font.</p>
</dd>

### -field fwdMaxCharInc

<dd>
<p>Specifies the maximum character increment of all glyphs in the font.</p>
</dd>

### -field fwdCapHeight

<dd>
<p>Specifies the height of the optical line describing the top of the uppercase 'H' in font units (FUnits). This might not be the same as the measured height of the uppercase 'H.' If this information does not exist, <b>fwdCapHeight</b> should be set to zero, which indicates that it is undefined.</p>
</dd>

### -field fwdXHeight

<dd>
<p>Specifies the height of the optical line describing the height of the lowercase 'x' in font units. This might not be the same as the measured height of the lowercase 'x.' A value of zero indicates that this member is undefined.</p>
</dd>

### -field fwdSubscriptXSize

<dd>
<p>Specifies the suggested character width (the size along the baseline direction) of the subscript font.</p>
</dd>

### -field fwdSubscriptYSize

<dd>
<p>Specifies the suggested character height (the size along the ascender direction) of the subscript font.</p>
</dd>

### -field fwdSubscriptXOffset

<dd>
<p>Specifies the suggested offset in the baseline direction of the subscript character. The offset is with respect to the character origin of the base character.</p>
</dd>

### -field fwdSubscriptYOffset

<dd>
<p>Specifies the suggested offset in the baseline direction of the subscript character. The offset is taken from the character origin of the base character.</p>
</dd>

### -field fwdSuperscriptXSize

<dd>
<p>Specifies the suggested character width (the size along the baseline direction) of the superscript font.</p>
</dd>

### -field fwdSuperscriptYSize

<dd>
<p>Specifies the suggested character height (the size along the ascender direction) of the superscript font.</p>
</dd>

### -field fwdSuperscriptXOffset

<dd>
<p>Specifies the suggested offset in the baseline direction of the superscript character. The offset is taken from the character origin of the base character.</p>
</dd>

### -field fwdSuperscriptYOffset

<dd>
<p>Specifies the suggested offset in the baseline direction of the superscript character. The offset is taken from the character origin of the base character.</p>
</dd>

### -field fwdUnderscoreSize

<dd>
<p>Specifies the suggested width of the underscore bar, in font units.</p>
</dd>

### -field fwdUnderscorePosition

<dd>
<p>Specifies the suggested displacement, in font units, from the base line to the middle of the underscore bar.</p>
</dd>

### -field fwdStrikeoutSize

<dd>
<p>Specifies the suggested width of the strike-out bar, in font coordinates.</p>
</dd>

### -field fwdStrikeoutPosition

<dd>
<p>Specifies the suggested displacement of the middle of the strikeout bar from the baseline.</p>
</dd>

### -field chFirstChar

<dd>
<p>Specifies the lowest supported character in the code page specified in <b>jWinCharSet</b>. This field is provided for Windows 3.1 compatibility.</p>
</dd>

### -field chLastChar

<dd>
<p>Specifies the highest supported character in the code page specified in <b>jWinCharSet</b>. This field is provided for Windows 3.1 compatibility.</p>
</dd>

### -field chDefaultChar

<dd>
<p>Specifies the default character in the code page specified in <b>jWinCharSet</b>. This field is provided for Windows 3.1 compatibility.</p>
</dd>

### -field chBreakChar

<dd>
<p>Specifies the break character in the code page specified in <b>jWinCharSet</b>. This field is provided for Windows 3.1 compatibility.</p>
</dd>

### -field wcFirstChar

<dd>
<p>Specifies the supported character with the smallest Unicode character code.</p>
</dd>

### -field wcLastChar

<dd>
<p>Specifies the supported character with the largest Unicode character code.</p>
</dd>

### -field wcDefaultChar

<dd>
<p>Specifies the character to be substituted when an application requests a character that is not supported by the font.</p>
</dd>

### -field wcBreakChar

<dd>
<p>Specifies the code point of the space character or its equivalent.</p>
</dd>

### -field ptlBaseline

<dd>
<p>Specifies a <a href="display.pointl">POINTL</a> structure that contains the intended writing direction of this font. For example, a typical Latin font specifies a value of (1,0).</p>
</dd>

### -field ptlAspect

<dd>
<p>Specifies a POINTL structure that contains the aspect ratio of the pixel centers for which the bitmap font was designed. This value is used only by bitmap fonts.</p>
</dd>

### -field ptlCaret

<dd>
<p>Specifies a POINTL structure that contains the direction of the ascender direction of the font. For example, the value for a nonitalicized Latin font is (0,1) while an italicized Latin font might specify a value of (2,5).</p>
</dd>

### -field rclFontBox

<dd>
<p>Specifies a <a href="display.rectl">RECTL</a> structure that describes the bounding box of all glyphs in the font in design space.</p>
</dd>

### -field achVendId

<dd>
<p>Specifies a four character identifier for the font vendor. Identifiers are documented in the Microsoft TrueType specification.</p>
</dd>

### -field cKerningPairs

<dd>
<p>Specifies the number of kerning pairs associated with this font.</p>
</dd>

### -field ulPanoseCulture

<dd>
<p>Specifies the manner in which to interpret the panose number. This number should be set to FM_PANOSE_CULTURE_LATIN for Latin-based fonts. See the Microsoft Window SDK documentation for information about the PANOSE structure.</p>
</dd>

### -field panose

<dd>
<p>Is an array of 10 bytes used to describe the visual characteristics of a given typeface. These characteristics are then used to associate the font with other fonts of similar appearance having different names. See the Window SDK documentation for information about the PANOSE structure.</p>
</dd>
</dl>

## -remarks
<p>The PRINTIFI32 structure is available in Windows Server 2003 SP1 and later. Because this structure is of fixed size, and it is guaranteed not to change across architectures or operating system versions, it can be used for binary file layouts. Unidrv UFM files are laid out in the format described in this structure, for all platforms. Pscript5 NTF files use the platform-specific version of this structure.</p>

<p>Additional information for a typeface can optionally be specified in the <a href="display.ifiextra">IFIEXTRA</a> structure.</p>

<p>A driver's <a href="display.drvqueryfont">DrvQueryFont</a> routine fills out and returns an IFIMETRICS structure to GDI.</p>

<p>The PRINTIFI32 structure defines all the information for a typeface that GDI understands. Most of the members are FWORD values, which are signed 16-bit quantities in design space. If the font is a raster font, design space and device space are the same and a font unit is equivalent to the distance between pixels.</p>

<p>The coordinate system in the font/notional space is such that the y coordinate increases in an upward direction and the x coordinate increases to the right.</p>

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
<a href="display.ifimetrics">IFIMETRICS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PRINTIFI32 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
