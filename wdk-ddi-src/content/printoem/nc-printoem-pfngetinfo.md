---
UID: NC.printoem.PFNGETINFO
title: PFNGETINFO
author: windows-driver-content
description: The UNIFONTOBJ_GetInfo callback function is provided by the Unidrv driver so that rendering plug-ins can obtain font or glyph information.
old-location: print\unifontobj_getinfo.htm
old-project: print
ms.assetid: 2c0d350d-dcdf-4da7-8cca-7f36d4ca622e
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IPrintSchemaTicket2, IPrintSchemaTicket2::GetParameterInitializer, GetParameterInitializer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: printoem.h
req.include-header: Printoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UNIFONTOBJ_GetInfo
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
req.product: Windows 10 or later.
---

# PFNGETINFO callback



## -description
The <b>UNIFONTOBJ_GetInfo</b> callback function is provided by the Unidrv driver so that rendering plug-ins can obtain font or glyph information.



## -prototype

````
PFNGETINFO UNIFONTOBJ_GetInfo;

BOOL APIENTRY UNIFONTOBJ_GetInfo(
   struct _UNIFONTOBJ *pUFObj,
   DWORD              dwInfoID,
   PVOID              pData,
   DWORD              dwDataSize,
   PDWORD             pcbNeeded
)
{ ... }
````


## -parameters

### -param pUFObj 

Pointer to the <a href="print.unifontobj">UNIFONTOBJ</a> structure received by the function that is making the callback to <b>UNIFONTOBJ_GetInfo</b>. Supplied by the caller.


### -param dwInfoID 

Specifies the type of structure pointed to by <i>pData</i>. Supplied by the caller. See the following table.


### -param pData 

Pointer to a structure, as indicated in the following table. Supplied by the caller.

<table>
<tr>
<th>dwInfoID Value</th>
<th><i>pData</i> Structure</th>
</tr>
<tr>
<td>
UFO_GETINFO_FONTOBJ

</td>
<td>

<a href="print.getinfo_fontobj">GETINFO_FONTOBJ</a>


</td>
</tr>
<tr>
<td>
UFO_GETINFO_GLYPHBITMAP

</td>
<td>

<a href="print.getinfo_glyphbitmap">GETINFO_GLYPHBITMAP</a>


</td>
</tr>
<tr>
<td>
UFO_GETINFO_GLYPHSTRING

</td>
<td>

<a href="print.getinfo_glyphstring">GETINFO_GLYPHSTRING</a>


</td>
</tr>
<tr>
<td>
UFO_GETINFO_GLYPHWIDTH

</td>
<td>

<a href="print.getinfo_glyphwidth">GETINFO_GLYPHWIDTH</a>


</td>
</tr>
<tr>
<td>
UFO_GETINFO_MEMORY

</td>
<td>

<a href="print.getinfo_memory">GETINFO_MEMORY</a>


</td>
</tr>
<tr>
<td>
UFO_GETINFO_STDVARIABLE

</td>
<td>

<a href="print.getinfo_stdvar">GETINFO_STDVAR</a>


</td>
</tr>
</table>
 

<dl>
<dd>
For a summary of structure contents, see the following <b>Remarks</b> section.

</dd>
</dl>

### -param dwDataSize 

Specifies the size, in bytes, of the buffer pointed to by <i>pData</i>. Supplied by the caller.


### -param pcbNeeded 

Pointer to a location that receives the minimum buffer size, in bytes, required to contain the structure identified by <i>dwInfoID</i>. Supplied by the caller.


## -returns
If the operation succeeds, the function returns <b>TRUE</b>. Otherwise it returns <b>FALSE</b>.


## -remarks
The <b>UNIFONTOBJ_GetInfo</b> callback function allows a <a href="https://msdn.microsoft.com/e55ca083-2790-4929-9e5b-6fce49eb0404">rendering plug-in</a> to call back into Unidrv to obtain font or glyph information from GDI, needed for handling <a href="https://msdn.microsoft.com/6e643703-ace1-4660-990c-3a9ca735829d">customized font management</a> operations.

A rendering plug-in receives the <b>UNIFONTOBJ_GetInfo</b> function's address in the <a href="print.unifontobj">UNIFONTOBJ</a> structure that is passed to the font customization methods.

The type of information returned by the function is dependent on the input arguments. The caller supplies values for <i>dwInfoID</i>, <i>pData</i>, and <i>dwDataSize</i> to indicate the type of information wanted. The following table summarizes the types of information returned. For more information, see the structure descriptions.


<a href="print.getinfo_fontobj">GETINFO_FONTOBJ</a>


A FONTOBJ structure describing the current font.


<a href="print.getinfo_glyphbitmap">GETINFO_GLYPHBITMAP</a>


A single glyph bitmap.


<a href="print.getinfo_glyphstring">GETINFO_GLYPHSTRING</a>


An array of glyph specifiers in a specified format.


<a href="print.getinfo_glyphwidth">GETINFO_GLYPHWIDTH</a>


Total width of a set of glyphs.


<a href="print.getinfo_memory">GETINFO_MEMORY</a>


Amount of available printer memory remaining.


<a href="print.getinfo_stdvar">GETINFO_STDVAR</a>


The current value for one or more of Unidrv's <a href="https://msdn.microsoft.com/d3f85c0f-7387-4301-8b1e-904471aed4b0">standard variables</a>.

If the buffer described by <i>pData</i> and <i>dwDataSize</i> is too small to receive the structure indicated by <i>dwInfoID</i>, the function loads the required buffer size into the location pointed by <i>pcbNeeded</i> and returns <b>FALSE</b>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Printoem.h (include Printoem.h)</dt>
</dl>
</td>
</tr>
</table>