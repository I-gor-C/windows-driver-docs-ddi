---
UID: NF.icm.WcsTranslateColors
title: WcsTranslateColors
author: windows-driver-content
description: The WcsTranslateColors function translates an array of colors from the source color space to the destination color space as defined by a color transform.
old-location: print\wcstranslatecolors.htm
old-project: print
ms.assetid: 99843150-9e27-4f09-a3ba-5ff87d3f1c88
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: WcsTranslateColors
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: icm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Included in Windows Vista and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WcsTranslateColors
req.alt-loc: Mscms.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Mscms.lib
req.dll: Mscms.dll
req.irql: 
req.iface: 
---

# WcsTranslateColors function



## -description
<p>The <code>WcsTranslateColors</code> function translates an array of colors from the source color space to the destination color space as defined by a color transform.</p>


## -syntax

````
BOOL WcsTranslateColors(
  _In_  HTRANSFORM    hColorTransform,
  _In_  DWORD         nColors,
  _In_  DWORD         nInputChannels,
  _In_  COLORDATATYPE cdtInput,
  _In_  DWORD         cbInput,
  _In_  PVOID         pInputData,
  _In_  DWORD         nOutputChannels,
  _In_  COLORDATATYPE cdtOutput,
  _In_  DWORD         cbOutput,
  _Out_ PVOID         pOutputData
);
````


## -parameters
<dl>

### -param <i>hColorTransform</i> [in]

<dd>
<p>A handle to the WCS color transform to use.</p>
</dd>

### -param <i>nColors</i> [in]

<dd>
<p>The number of elements in the array pointed to by <i>pInputData</i> and <i>pOutputData</i>.</p>
</dd>

### -param <i>nInputChannels</i> [in]

<dd>
<p>The number of channels per element in the array pointed to by <i>pInputData</i>.</p>
</dd>

### -param <i>cdtInput</i> [in]

<dd>
<p>The input <a href="..\icm\ne-icm-colordatatype.md">COLORDATATYPE</a> color data type.</p>
</dd>

### -param <i>cbInput</i> [in]

<dd>
<p>The buffer size, in bytes, of <i>pInputData</i>.</p>
</dd>

### -param <i>pInputData</i> [in]

<dd>
<p>A pointer to an array of input colors.</p>
</dd>

### -param <i>nOutputChannels</i> [in]

<dd>
<p>The number of channels per element in the array pointed to by <i>pOutputData</i>.</p>
</dd>

### -param <i>cdtOutput</i> [in]

<dd>
<p>The output <a href="..\icm\ne-icm-colordatatype.md">COLORDATATYPE</a> color data type.</p>
</dd>

### -param <i>cbOutput</i> [in]

<dd>
<p>The buffer size, in bytes, of <i>pOutputData</i>.</p>
</dd>

### -param <i>pOutputData</i> [out]

<dd>
<p>A pointer to an array of colors that receives the results of the color translation.</p>
</dd>
</dl>

## -remarks
<p>If the input and the output color data types are not compatible with the color transform, this function will fail.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Included in Windows Vista and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Icm.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Mscms.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Mscms.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\icm\ne-icm-colordatatype.md">COLORDATATYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20WcsTranslateColors function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
