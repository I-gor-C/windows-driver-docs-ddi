---
UID: NF.icm.WcsCheckColors
title: WcsCheckColors function
author: windows-driver-content
description: The WcsCheckColors function determines whether the colors in an array lie within the output gamut of a specified WCS color transform.
old-location: print\wcscheckcolors.htm
old-project: print
ms.assetid: 1254b0d4-cb72-4171-b09d-f0bca58a137a
ms.author: windowsdriverdev
ms.date: 12/14/2017
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
---

# WcsCheckColors function



## -description
The <code>WcsCheckColors</code> function determines whether the colors in an array lie within the output gamut of a specified WCS color transform.



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

### -param hColorTransform [in]

A handle to the WCS color transform to use.


### -param nColors [in]

The number of elements in the array pointed to by <i>pInputData</i> and <i>paResult</i>.


### -param nInputChannels [in]

The number of channels per element in the array pointed to by <i>pInputData</i>.


### -param cdtInput [in]

The input COLORDATATYPE color data type.


### -param cbInput [in]

The buffer size of <i>pInputData</i>.


### -param pInputData [in]

A pointer to an array of input colors. Colors in this array correspond to the color space of the source profile.


### -param paResult [out]

A pointer to an array of <i>nColors</i> bytes that receives the results of the test.


## -remarks
If the input and the output color data types are not compatible with the color transform, this function will convert the input color data as required.

This function will fail if an ICC transform is used.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Included in Windows Vista and later.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Icm.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Mscms.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Mscms.dll</dt>
</dl>
</td>
</tr>
</table>