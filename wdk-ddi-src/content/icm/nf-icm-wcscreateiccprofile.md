---
UID: NF.icm.WcsCreateIccProfile
title: WcsCreateIccProfile
author: windows-driver-content
description: The WcsCreateIccProfile function converts a WCS profile into an ICC profile.
old-location: print\wcscreateiccprofile.htm
ms.assetid: fbe37d6c-9b91-46d8-9d29-1de3ef542c19
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: icm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Included in Windows Vista and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WcsCreateIccProfile
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
ms.keywords: WcsCreateIccProfile
req.iface: 
---

# WcsCreateIccProfile function



## -description
<p>The <code>WcsCreateIccProfile</code> function converts a WCS profile into an ICC profile.</p>


## -syntax

````
HPROFILE WcsCreateIccProfile(
  _In_ HPROFILE hWcsProfile,
  _In_ DWORD    dwOptions
);
````


## -parameters
<dl>

### -param <i>hWcsProfile</i> [in]

<dd>
<p>A handle to the WCS color profile to transform. See Remarks.</p>
</dd>

### -param <i>dwOptions</i> [in]

<dd>
<p>A flag value that specifies the profile conversion options. This parameter must take the following value:</p>
<p></p>
<dl>

### -param <a id="PREFER_WCS_PROFILES"></a><a id="prefer_wcs_profiles"></a>PREFER_WCS_PROFILES

<dd>
<p>Specifies that when WCS encounters an ICC profile, it should extract and use the WCS profiles that are contained in <b>WcsProfilesTag</b>.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The WCS profile that is to be translated must be a Device Model Profile (DMP) in combination with a Color Appearance Model Profile (CAMP) and a Gamut Map Model Profile (GMMP).</p>

<p>The WCS profile that is to be translated must be a Device Model Profile (DMP) in combination with a Color Appearance Model Profile (CAMP) and a Gamut Map Model Profile (GMMP).</p>

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