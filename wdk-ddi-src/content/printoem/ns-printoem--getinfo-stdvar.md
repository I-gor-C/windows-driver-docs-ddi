---
UID: NS.printoem._GETINFO_STDVAR
title: GETINFO_STDVAR
author: windows-driver-content
description: The GETINFO_STDVAR structure is used as input to the UNIFONTOBJ_GetInfo callback function.
old-location: print\getinfo_stdvar.htm
ms.assetid: 9f2ae88c-34a4-46b3-9571-5f2f023b7d6b
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: printoem.h
req.include-header: Printoem.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GETINFO_STDVAR
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
req.irql: <= APC_LEVEL
ms.keywords: GETINFO_STDVAR, GETINFO_STDVAR, *PGETINFO_STDVAR
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# GETINFO_STDVAR structure



## -description
<p>The GETINFO_STDVAR structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563594">UNIFONTOBJ_GetInfo</a> callback function.</p>


## -syntax

````
typedef struct _GETINFO_STDVAR {
  DWORD  dwSize;
  DWORD  dwNumOfVariable;
  struct {
    DWORD dwStdVarID;
    LONG  lStdVariable;
  } StdVar[1];
} GETINFO_STDVAR, *PGETINFO_STDVAR;
````


## -struct-fields
<dl>

### -field <b>dwSize</b>

<dd>
<p>Specifies the size, in bytes, of the GETINFO_STDVAR structure. Supplied by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563594">UNIFONTOBJ_GetInfo</a> caller.</p>
</dd>

### -field <b>dwNumOfVariable</b>

<dd></dd>

### -field <b>StdVar</b>

<dd>
<p>Is an array specifying standard variable indexes and values. Each array element contains two members: a <b>dwStdVarID</b> member and an <b>lStdVariable</b> member.</p>
<dl>

### -field <b>dwStdVarID</b>

<dd>
<p>Specifies the <a href="NULL">standard variables</a> for which a value should be returned. Supplied by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563594">UNIFONTOBJ_GetInfo</a> caller. Valid values are contained in the following table.</p>
<table>
<tr>
<th>Identifier</th>
<th>Standard Variable</th>
</tr>
<tr>
<td>
<p>FNT_INFO_CURRENTFONTID</p>
</td>
<td>
<p><code>CurrentFontID</code></p>
</td>
</tr>
<tr>
<td>
<p>FNT_INFO_FONTBOLD</p>
</td>
<td>
<p><code>FontBold</code></p>
</td>
</tr>
<tr>
<td>
<p>FNT_INFO_FONTHEIGHT</p>
</td>
<td>
<p><code>FontHeight</code></p>
</td>
</tr>
<tr>
<td>
<p>FNT_INFO_FONTITALIC</p>
</td>
<td>
<p><code>FontItalic</code></p>
</td>
</tr>
<tr>
<td>
<p>FNT_INFO_FONTMAXWIDTH</p>
</td>
<td>
<p><code>FontMaxWidth</code></p>
</td>
</tr>
<tr>
<td>
<p>FNT_INFO_FONTSTRIKETHRU</p>
</td>
<td>
<p><code>FontStrikeThru</code></p>
</td>
</tr>
<tr>
<td>
<p>FNT_INFO_FONTUNDERLINE</p>
</td>
<td>
<p><code>FontUnderline</code></p>
</td>
</tr>
<tr>
<td>
<p>FNT_INFO_FONTWIDTH</p>
</td>
<td>
<p><code>FontWidth</code></p>
</td>
</tr>
<tr>
<td>
<p>FNT_INFO_GRAYPERCENTAGE</p>
</td>
<td>
<p><code>GrayPercentage</code></p>
</td>
</tr>
<tr>
<td>
<p>FNT_INFO_NEXTFONTID</p>
</td>
<td>
<p><code>NextFontID</code></p>
</td>
</tr>
<tr>
<td>
<p>FNT_INFO_NEXTGLYPH</p>
</td>
<td>
<p><code>NextGlyph</code></p>
</td>
</tr>
<tr>
<td>
<p>FNT_INFO_PRINTDIRINCCDEGREES</p>
</td>
<td>
<p><code>PrintDirInCCDegrees</code></p>
</td>
</tr>
<tr>
<td>
<p>FNT_INFO_TEXTXRES</p>
</td>
<td>
<p><code>TextXRes</code></p>
</td>
</tr>
<tr>
<td>
<p>FNT_INFO_TEXTYRES</p>
</td>
<td>
<p><code>TextYRes</code></p>
</td>
</tr>
</table>
<p> </p>
<p>Supplied by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563594">UNIFONTOBJ_GetInfo</a> caller.</p>
</dd>

### -field <b>lStdVariable</b>

<dd>
<p>Specifies the current value of the specified standard variable. Supplied by Unidrv's <a href="https://msdn.microsoft.com/library/windows/hardware/ff563594">UNIFONTOBJ_GetInfo</a> callback function.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>To obtain the current value for one or more of Unidrv's standard variables, a rendering plug-in can supply the address of a GETINFO_STDVAR structure when calling Unidrv's <a href="https://msdn.microsoft.com/library/windows/hardware/ff563594">UNIFONTOBJ_GetInfo</a> callback function.</p>

<p>For more information about <a href="NULL">standard variables</a>, see <a href="NULL">Microsoft Universal Printer Driver</a>.</p>

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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20GETINFO_STDVAR structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
