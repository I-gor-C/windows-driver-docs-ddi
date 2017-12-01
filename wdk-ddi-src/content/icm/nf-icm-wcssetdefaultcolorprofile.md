---
UID: NF.icm.WcsSetDefaultColorProfile
title: WcsSetDefaultColorProfile
author: windows-driver-content
description: The WcsSetDefaultColorProfile function sets the default color profile name of the specified profile type in the specified profile management scope.
old-location: print\wcssetdefaultcolorprofile.htm
old-project: print
ms.assetid: 302f271c-801e-409c-a0fc-53f01e5e2055
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: WcsSetDefaultColorProfile
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
req.alt-api: WcsSetDefaultColorProfile
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

# WcsSetDefaultColorProfile function



## -description
<p>The <code>WcsSetDefaultColorProfile</code> function sets the default color profile name of the specified profile type in the specified profile management scope.</p>


## -syntax

````
BOOL WcsSetDefaultColorProfile(
  _In_     WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_opt_ PCWSTR                       pDeviceName,
  _In_     COLORPROFILETYPE             cptColorProfileType,
  _In_     COLORPROFILESUBTYPE          cpstColorProfileSubType,
  _In_     DWORD                        dwProfileID,
  _In_opt_ LPCWSTR                      pProfileName
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
<p>A pointer to the name of the device for which the default color profile is to be set. If <b>NULL</b>, a device-independent default profile will be used.</p>
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

### -param <i>pProfileName</i> [in, optional]

<dd>
<p>A pointer to a buffer to receive the name of the color profile. See Remarks.</p>
</dd>
</dl>

## -remarks
<p>If the <i>pProfileName</i> parameter is <b>NULL</b> and the <i>profileManagementScope</i> parameter is WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER, subsequent calls to <b>WcsSetDefaultColorProfile</b> will return the system-wide default profile.</p>

<p>This function is executable in Least-Privileged User Account (LUA) context if <i>profileManagementScope</i> is WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER. Otherwise, administrative privileges are required. The specified profile must already be installed, but it need not yet be associated with the specified device in the specified profile management scope..</p>

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
<a href="..\icm\nf-icm-wcsgetdefaultcolorprofilesize.md">WcsGetDefaultColorProfileSize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20WcsSetDefaultColorProfile function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
