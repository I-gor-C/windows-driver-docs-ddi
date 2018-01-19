---
UID : NS:prntfont._PRINTIFI32
title : _PRINTIFI32
author : windows-driver-content
description : The PRINTIFI32 structure is a fixed-size version of the IFIMETRICS structure, and defines information for a given typeface that GDI can use.
old-location : display\printifi32.htm
old-project : display
ms.assetid : f8e77eb1-3964-4ca0-8ae7-2e9617671990
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _PRINTIFI32, PRINTIFI32, *PPRINTIFI32
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : prntfont.h
req.include-header : Prntfont.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PRINTIFI32
req.alt-loc : prntfont.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : PRINTIFI32, *PPRINTIFI32
req.product : Windows 10 or later.
---

# _PRINTIFI32 structure
The PRINTIFI32 structure is a fixed-size version of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567418">IFIMETRICS</a> structure, and defines information for a given typeface that GDI can use.

## Syntax
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

## Members

        
            `achVendId`

            Specifies a four character identifier for the font vendor. Identifiers are documented in the Microsoft TrueType specification.
        
            `chBreakChar`

            Specifies the break character in the code page specified in <b>jWinCharSet</b>. This field is provided for Windows 3.1 compatibility.
        
            `chDefaultChar`

            Specifies the default character in the code page specified in <b>jWinCharSet</b>. This field is provided for Windows 3.1 compatibility.
        
            `chFirstChar`

            Specifies the lowest supported character in the code page specified in <b>jWinCharSet</b>. This field is provided for Windows 3.1 compatibility.
        
            `chLastChar`

            Specifies the highest supported character in the code page specified in <b>jWinCharSet</b>. This field is provided for Windows 3.1 compatibility.
        
            `cjIfiExtra`

            Specifies the size in bytes of the IFIEXTRA structure that follows this structure. A value of zero indicates that no IFIEXTRA structure is present.
        
            `cjThis`

            Specifies the size in bytes of this structure. The specified size includes any Unicode strings appended to the end of this structure, plus the size in bytes of the optional <a href="https://msdn.microsoft.com/library/windows/hardware/ff567416">IFIEXTRA</a> structure.
        
            `cKerningPairs`

            Specifies the number of kerning pairs associated with this font.
        
            `dpCharSets`

            Specifies the offset from the beginning of this structure to an array containing a list of all Windows character sets supported by this font. The array is 16 bytes in size and is always terminated with DEFAULT_CHARSET. The first value of the array should identify the Windows character set that has the best and most complete coverage in the font; this value should also be stored in <b>jWinCharSet</b>. For instance, if this is a Japanese font that also supports US ANSI and Cyrillic character sets, then <b>jWinCharSet</b> should be set to SHIFTJIS_CHARSET and the array identified by <b>dpCharSets</b> would contain SHIFTJIS_CHARSET, ANSI_CHARSET, RUSSIAN_CHARSET, DEFAULT_CHARSET.

If this font does not support more than one Windows character set, <b>dpCharSets</b> should be set to zero.
        
            `dpFontSim`

            Specifies the offset in bytes from the beginning of this structure to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566017">FONTSIM</a> structure that describes the simulations that the font supports. The driver should set this member to a nonzero value only if the font supports bold, italic, or bold italic simulations; otherwise, the driver should set this to zero.

Note that if a font is italic by design, the driver should not indicate font support for italic simulation although it can indicate font support for bold italic simulation. Similarly, the driver should not indicate font support for bold simulation if the font is bold by design, but can indicate font support for bold italic simulation. If the font is both bold and italic by design, it should not support any simulations.

The offsets in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566017">FONTSIM</a> structure are relative to the base of the FONTSIM structure.
        
            `dpwszFaceName`

            Specifies the offset in bytes to a null-terminated Unicode string representing the unique and complete name of the font. The name contains the family and subfamily names of the font (for example, "Times New Roman Bold").
        
            `dpwszFamilyName`

            Specifies the offset in bytes to a null-terminated Unicode string containing the family name of the font (for example, "Times Roman"). Generally, this string immediately follows this structure. This string should be the same as the name recorded in the <b>lfFaceName</b> member of the Win32 LOGFONT structure.
        
            `dpwszStyleName`

            Specifies the offset in bytes to a null-terminated Unicode string describing the style of the font (for example, "Bold").
        
            `dpwszUniqueName`

            Specifies the offset in bytes to a null-terminated Unicode string representing the unique identifier of the font (for example, "Monotype:Times New Roman:1990").
        
            `flInfo`

            Specifies additional information about the font. This field can be a combination of the following flag values:

Value

Meaning
        
            `fsSelection`

            Specifies a combination of the following flags:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
FM_SEL_BOLD

</td>
<td>
Set if the characters of the font are bold.

</td>
</tr>
<tr>
<td>
FM_SEL_ITALIC

</td>
<td>
Set if the characters of the font are italic.

</td>
</tr>
<tr>
<td>
FM_SEL_NEGATIVE

</td>
<td>
Set if the characters of the font have the foreground and background reversed.

</td>
</tr>
<tr>
<td>
FM_SEL_OUTLINED

</td>
<td>
Set if the characters of the font are hollow.

</td>
</tr>
<tr>
<td>
FM_SEL_REGULAR

</td>
<td>
Set if the characters of the font are normal weight.

</td>
</tr>
<tr>
<td>
FM_SEL_STRIKEOUT

</td>
<td>
Set if the characters of the font are struck out by default; otherwise strikeouts must be simulated.

</td>
</tr>
<tr>
<td>
FM_SEL_UNDERSCORE

</td>
<td>
Set if all the characters of the font are underscored by default; otherwise underscoring must be simulated.

</td>
</tr>
</table>
        
            `fsType`

            This is a TrueType-specific bitfield indicating certain properties for the font, such as font embedding and licensing rights for the font. Embeddable fonts can be stored in a document. When a document with embedded fonts is opened on a system that does not have the font installed (the remote system), the embedded font can be loaded for temporary (and in some cases permanent) use on that system by an embedding-aware application. Embedding licensing rights are granted by the font vendor. The following flags can be set:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
FM_EDITABLE_EMBED

</td>
<td>
Set if the font can be embedded and temporarily loaded on other systems. Documents containing Editable fonts can be opened for reading and writing.

</td>
</tr>
<tr>
<td>
FM_READONLY_EMBED

</td>
<td>
Set if read/write embedding is not permitted; only "preview and print" encapsulation is allowed. When this bit is set, the font can be embedded and temporarily loaded on the remote system. Documents containing "preview and print" fonts must be opened "read-only;" no edits can be applied to the document.

</td>
</tr>
<tr>
<td>
        
            `fwdAveCharWidth`

            Specifies the arithmetic average of the width of all of the 26 lower case letters 'a' through 'z' of the Latin alphabet and the space character. If any of the 26 lowercase letters are not present, then this member should be set equal to the weighted average of all glyphs in the font.
        
            `fwdCapHeight`

            Specifies the height of the optical line describing the top of the uppercase 'H' in font units (FUnits). This might not be the same as the measured height of the uppercase 'H.' If this information does not exist, <b>fwdCapHeight</b> should be set to zero, which indicates that it is undefined.
        
            `fwdLowestPPEm`

            Specifies the smallest readable size of the font, in pixels. This value is ignored for bitmap fonts.
        
            `fwdMacAscender`

            Specifies the Macintosh ascender value for the font.
        
            `fwdMacDescender`

            Specifies the Macintosh descender value for the font. This number is typically less than zero. It measures the signed displacement from the base line of the lowest descender in the Macintosh character set.
        
            `fwdMacLineGap`

            Specifies the Macintosh line gap for the font. The suggested Macintosh interline spacing is equal to <b>fwdMacLineGap</b> + <b>fwdMacAscender</b> âˆ’ <b>fwdMacDescender</b>.
        
            `fwdMaxCharInc`

            Specifies the maximum character increment of all glyphs in the font.
        
            `fwdStrikeoutPosition`

            Specifies the suggested displacement of the middle of the strikeout bar from the baseline.
        
            `fwdStrikeoutSize`

            Specifies the suggested width of the strike-out bar, in font coordinates.
        
            `fwdSubscriptXOffset`

            Specifies the suggested offset in the baseline direction of the subscript character. The offset is with respect to the character origin of the base character.
        
            `fwdSubscriptXSize`

            Specifies the suggested character width (the size along the baseline direction) of the subscript font.
        
            `fwdSubscriptYOffset`

            Specifies the suggested offset in the baseline direction of the subscript character. The offset is taken from the character origin of the base character.
        
            `fwdSubscriptYSize`

            Specifies the suggested character height (the size along the ascender direction) of the subscript font.
        
            `fwdSuperscriptXOffset`

            Specifies the suggested offset in the baseline direction of the superscript character. The offset is taken from the character origin of the base character.
        
            `fwdSuperscriptXSize`

            Specifies the suggested character width (the size along the baseline direction) of the superscript font.
        
            `fwdSuperscriptYOffset`

            Specifies the suggested offset in the baseline direction of the superscript character. The offset is taken from the character origin of the base character.
        
            `fwdSuperscriptYSize`

            Specifies the suggested character height (the size along the ascender direction) of the superscript font.
        
            `fwdTypoAscender`

            Specifies the typographic ascender value for the font.
        
            `fwdTypoDescender`

            Specifies the typographic descender value for the font. This value specifies the signed displacement of the lowest descender from the baseline.
        
            `fwdTypoLineGap`

            Specifies the typographic line gap for the font.
        
            `fwdUnderscorePosition`

            Specifies the suggested displacement, in font units, from the base line to the middle of the underscore bar.
        
            `fwdUnderscoreSize`

            Specifies the suggested width of the underscore bar, in font units.
        
            `fwdUnitsPerEm`

            Specifies the em-height of the font.
        
            `fwdWinAscender`

            Specifies the Windows ascender value for the font.
        
            `fwdWinDescender`

            Specifies the Windows descender value for the font.
        
            `fwdXHeight`

            Specifies the height of the optical line describing the height of the lowercase 'x' in font units. This might not be the same as the measured height of the lowercase 'x.' A value of zero indicates that this member is undefined.
        
            `jWinCharSet`

            Identifies the character set best supported by this font. If the font supports only a single Windows character set, the driver should store the corresponding value in <b>jWinCharSet</b>. The driver should not store DEFAULT_CHARSET in this field. This member can be one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
ANSI_CHARSET

</td>
<td>
This font supports the Windows ANSI character set.

</td>
</tr>
<tr>
<td>
ARABIC_CHARSET

</td>
<td>
This font supports the Arabic character set.

</td>
</tr>
<tr>
<td>
BALTIC_CHARSET

</td>
<td>
This font supports the Baltic character set.

</td>
</tr>
<tr>
<td>
CHINESEBIG5_CHARSET

</td>
<td>
This font supports the traditional Chinese (Big 5) character set.

</td>
</tr>
<tr>
<td>
EASTEUROPE_CHARSET

</td>
<td>
This font supports the Eastern European character set.

</td>
</tr>
<tr>
<td>
GB2312_CHARSET

</td>
<td>
This font supports the simplified (PRC) Chinese character set.

</td>
</tr>
<tr>
<td>
GREEK_CHARSET

</td>
<td>
This font supports the Greek character set.

</td>
</tr>
<tr>
<td>
HANGEUL_CHARSET

</td>
<td>
This font supports the Korean (Hangeul) character set.

</td>
</tr>
<tr>
<td>
HEBREW_CHARSET

</td>
<td>
This font supports the Hebrew character set.

</td>
</tr>
<tr>
<td>
JOHAB_CHARSET

</td>
<td>
This font supports the Korean (Johab) character set.

</td>
</tr>
<tr>
<td>
OEM_CHARSET

</td>
<td>
This font supports an OEM-specific character set. The OEM character set is system dependent.

</td>
</tr>
<tr>
<td>
SHIFTJIS_CHARSET

</td>
<td>
This font supports the Shift-JIS (Japanese Industry Standard) character set.

</td>
</tr>
<tr>
<td>
SYMBOL_CHARSET

</td>
<td>
This font supports the Windows symbol character set.

</td>
</tr>
<tr>
<td>
RUSSIAN_CHARSET

</td>
<td>
This font supports the Cyrillic character set.

</td>
</tr>
<tr>
<td>
THAI_CHARSET

</td>
<td>
This font supports the Thai character set.

</td>
</tr>
<tr>
<td>
TURKISH_CHARSET

</td>
<td>
This font supports the Turkish character set.

</td>
</tr>
<tr>
<td>
VIETNAMESE_CHARSET

</td>
<td>
This font supports the Vietnamese character set.

</td>
</tr>
</table>
        
            `jWinPitchAndFamily`

            Specifies the pitch of the font. The two low-order bits specify the pitch of the font and can be one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
FIXED_PITCH

</td>
<td>
For fixed pitch fonts

</td>
</tr>
<tr>
<td>
VARIABLE_PITCH

</td>
<td>
For variable pitch fonts

</td>
</tr>
</table>
 

Bits 4 through 7 of this member specify the font family and can be one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
FF_DECORATIVE

</td>
<td>
Novelty fonts, such as Old English.

</td>
</tr>
<tr>
<td>
FF_DONTCARE

</td>
<td>
Don't care or unknown.

</td>
</tr>
<tr>
<td>
FF_MODERN

</td>
<td>
Fonts with constant stroke width (fixed-pitch), with or without serifs. Fixed-pitch fonts are usually modern, such as Pica, Elite, and Courier.

</td>
</tr>
<tr>
<td>
FF_ROMAN

</td>
<td>
Fonts with variable stroke width (proportionally spaced) and with serifs, such as Times Roman, Palatino, and Century Schoolbook.

</td>
</tr>
<tr>
<td>
FF_SCRIPT

</td>
<td>
Fonts designed to look like handwriting, such as Script and Cursive.

</td>
</tr>
<tr>
<td>
FF_SWISS

</td>
<td>
Fonts with variable stroke width (proportionally spaced) and without serifs, such as Helvetica and Swiss.

</td>
</tr>
</table>
        
            `lCharBias`

            Specifies the character bias. This value is TrueType-specific and should be set to zero by all other font providers.
        
            `lEmbedId`

            Specifies the Embedding ID of the font. This value is TrueType-specific and should be set to zero by all other font providers.
        
            `lItalicAngle`

            Specifies the italic angle of the font. This value is TrueType-specific and should be set to zero by all other font providers.
        
            `panose`

            Is an array of 10 bytes used to describe the visual characteristics of a given typeface. These characteristics are then used to associate the font with other fonts of similar appearance having different names. See the Window SDK documentation for information about the PANOSE structure.
        
            `ptlAspect`

            Specifies a POINTL structure that contains the aspect ratio of the pixel centers for which the bitmap font was designed. This value is used only by bitmap fonts.
        
            `ptlBaseline`

            Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff569166">POINTL</a> structure that contains the intended writing direction of this font. For example, a typical Latin font specifies a value of (1,0).
        
            `ptlCaret`

            Specifies a POINTL structure that contains the direction of the ascender direction of the font. For example, the value for a nonitalicized Latin font is (0,1) while an italicized Latin font might specify a value of (2,5).
        
            `rclFontBox`

            Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff569236">RECTL</a> structure that describes the bounding box of all glyphs in the font in design space.
        
            `ulPanoseCulture`

            Specifies the manner in which to interpret the panose number. This number should be set to FM_PANOSE_CULTURE_LATIN for Latin-based fonts. See the Microsoft Window SDK documentation for information about the PANOSE structure.
        
            `usWinWeight`

            Specifies the weight of the font in the range 0 to 1000 (for example, 400 is normal and 700 is bold). This value is provided to the application in the <b>lfWeight</b> member of the Win32 LOGFONT structure.
        
            `wcBreakChar`

            Specifies the code point of the space character or its equivalent.
        
            `wcDefaultChar`

            Specifies the character to be substituted when an application requests a character that is not supported by the font.
        
            `wcFirstChar`

            Specifies the supported character with the smallest Unicode character code.
        
            `wcLastChar`

            Specifies the supported character with the largest Unicode character code.

    ## Remarks
        The PRINTIFI32 structure is available in Windows Server 2003 SP1 and later. Because this structure is of fixed size, and it is guaranteed not to change across architectures or operating system versions, it can be used for binary file layouts. Unidrv UFM files are laid out in the format described in this structure, for all platforms. Pscript5 NTF files use the platform-specific version of this structure.

Additional information for a typeface can optionally be specified in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567416">IFIEXTRA</a> structure.

A driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556262">DrvQueryFont</a> routine fills out and returns an IFIMETRICS structure to GDI.

The PRINTIFI32 structure defines all the information for a typeface that GDI understands. Most of the members are FWORD values, which are signed 16-bit quantities in design space. If the font is a raster font, design space and device space are the same and a font unit is equivalent to the distance between pixels.

The coordinate system in the font/notional space is such that the y coordinate increases in an upward direction and the x coordinate increases to the right.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | prntfont.h (include Prntfont.h) |

    ## See Also

        <dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567418">IFIMETRICS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PRINTIFI32 structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>