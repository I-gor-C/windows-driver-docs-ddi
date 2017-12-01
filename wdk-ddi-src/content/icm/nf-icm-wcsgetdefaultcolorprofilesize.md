---
UID: NF.icm.WcsGetDefaultColorProfileSize
title: WcsGetDefaultColorProfileSize
author: windows-driver-content
description: The WcsGetDefaultColorProfileSize function returns the size, in bytes, of the default color profile name for a device, including the NULL terminator.
old-location: print\wcsgetdefaultcolorprofilesize.htm
old-project: print
ms.assetid: d04306e2-3479-4ba4-ac4d-bf3715487fcf
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: WcsGetDefaultColorProfileSize
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
req.alt-api: WcsGetDefaultColorProfileSize
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

# WcsGetDefaultColorProfileSize function



## -description
<p>The <code>WcsGetDefaultColorProfileSize</code> function returns the size, in bytes, of the default color profile name for a device, including the <b>NULL</b> terminator.</p>


## -syntax

````
BOOL WcsGetDefaultColorProfileSize(
  _In_     WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_opt_ PCWSTR                       pDeviceName,
  _In_     COLORPROFILETYPE             cptColorProfileType,
  _In_     COLORPROFILESUBTYPE          cpstColorProfileSubType,
  _In_     DWORD                        dwProfileID,
  _Out_    PDWORD                       pcbProfileName
);
````


## -parameters
<dl>

### -param <i>profileManagementScope</i> [in]

<dd>
<p>
      A <a href="..\icm\ne-icm-wcs-profile-management-scope.md">WCS_PROFILE_MANAGEMENT_SCOPE</a> value that specifies the scope of this profile management operation.</p>
</dd>

### -param <i>pDeviceName</i> [in, optional]

<dd>
<p>A pointer to the name of the device for which the default color profile is to be obtained. If <b>NULL</b>, a device-independent default profile will be used.</p>
</dd>

### -param <i>cptColorProfileType</i> [in]

<dd>
<p>A <a href="..\icm\ne-icm-colorprofiletype.md">COLORPROFILETYPE</a> value that specifies the color profile type.</p>
</dd>

### -param <i>cpstColorProfileSubType</i> [in]

<dd>
<p>A <a href="..\icm\ne-icm-colorprofilesubtype.md">COLORPROFILESUBTYPE</a> value that specifies the color profile subtype.</p>
</dd>

### -param <i>dwProfileID</i> [in]

<dd>
<p>The ID of the color space that the color profile represents.</p>
</dd>

### -param <i>pcbProfileName</i> [out]

<dd>
<p>A pointer to a location that receives the size, in bytes, of the path name of the default color profile, including the null terminator.</p>
</dd>
</dl>

## -remarks
<p>Use this function to return the required size of the buffer pointed to by the <i>pProfileName</i> parameter in the <a href="..\icm\nf-icm-wcsgetdefaultcolorprofile.md">WcsGetDefaultColorProfile</a> function.</p>

<p>This function is executable in Least-Privileged User Account (LUA) context.</p>

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
<a href="..\icm\ne-icm-colorprofilesubtype.md">COLORPROFILESUBTYPE</a>
</dt>
<dt>
<a href="..\icm\ne-icm-colorprofiletype.md">COLORPROFILETYPE</a>
</dt>
<dt>
<a href="..\icm\ne-icm-wcs-profile-management-scope.md">WCS_PROFILE_MANAGEMENT_SCOPE</a>
</dt>
<dt>
<a href="..\icm\nf-icm-wcsgetdefaultcolorprofile.md">WcsGetDefaultColorProfile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20WcsGetDefaultColorProfileSize function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
