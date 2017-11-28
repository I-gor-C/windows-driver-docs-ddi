---
UID: NF.icm.WcsCheckColors
title: WcsCheckColors
author: windows-driver-content
description: The WcsCheckColors function determines whether the colors in an array lie within the output gamut of a specified WCS color transform.
old-location: print\wcscheckcolors.htm
old-project: print
ms.assetid: 1254b0d4-cb72-4171-b09d-f0bca58a137a
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: WcsCheckColors
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
req.alt-api: WcsCheckColors
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

# WcsCheckColors function



## -description
<p>The <code>WcsCheckColors</code> function determines whether the colors in an array lie within the output gamut of a specified WCS color transform.</p>


## -syntax

````
BOOL WcsCheckColors(
  _In_  HTRANSFORM    hColorTransform,
  _In_  DWORD         nColors,
  _In_  DWORD         nInputChannels,
  _In_  COLORDATATYPE cdtInput,
  _In_  DWORD         cbInput,
  _In_  PVOID         pInputData,
  _Out_ PBYTE         paResult
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
<p>The number of elements in the array pointed to by <i>pInputData</i> and <i>paResult</i>.</p>
</dd>

### -param <i>nInputChannels</i> [in]

<dd>
<p>The number of channels per element in the array pointed to by <i>pInputData</i>.</p>
</dd>

### -param <i>cdtInput</i> [in]

<dd>
<p>The input COLORDATATYPE color data type.</p>
</dd>

### -param <i>cbInput</i> [in]

<dd>
<p>The buffer size of <i>pInputData</i>.</p>
</dd>

### -param <i>pInputData</i> [in]

<dd>
<p>A pointer to an array of input colors. Colors in this array correspond to the color space of the source profile.</p>
</dd>

### -param <i>paResult</i> [out]

<dd>
<p>A pointer to an array of <i>nColors</i> bytes that receives the results of the test.</p>
</dd>
</dl>

## -remarks
<p>If the input and the output color data types are not compatible with the color transform, this function will convert the input color data as required.</p>

<p>This function will fail if an ICC transform is used.</p>

<p>If the input and the output color data types are not compatible with the color transform, this function will convert the input color data as required.</p>

<p>This function will fail if an ICC transform is used.</p>

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