---
UID: NF.icm.WcsGetDefaultColorProfile
title: WcsGetDefaultColorProfile
author: windows-driver-content
description: The WcsGetDefaultColorProfile function retrieves the default color profile for a device, or the device-independent default if the device is not specified.
old-location: print\wcsgetdefaultcolorprofile.htm
old-project: print
ms.assetid: a5ace7f3-dc61-4799-b129-3c25c392ebf6
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: WcsGetDefaultColorProfile
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
req.alt-api: WcsGetDefaultColorProfile
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

# WcsGetDefaultColorProfile function



## -description
<p>The <code>WcsGetDefaultColorProfile</code> function retrieves the default color profile for a device, or the device-independent default if the device is not specified.</p>


## -syntax

````
BOOL WcsGetDefaultColorProfile(
  _In_     WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_opt_ PCWSTR                       pDeviceName,
  _In_     COLORPROFILETYPE             cptColorProfileType,
  _In_     COLORPROFILESUBTYPE          cpstColorProfileSubType,
  _In_     DWORD                        dwProfileID,
  _In_     DWORD                        cbProfileName,
  _Out_    LPWSTR                       pProfileName
);
````


## -parameters
<dl>

### -param <i>profileManagementScope</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff563752">WCS_PROFILE_MANAGEMENT_SCOPE</a> value that specifies the scope of this profile management operation.</p>
</dd>

### -param <i>pDeviceName</i> [in, optional]

<dd>
<p>A pointer to the name of the device for which the default color profile is to be obtained. If <b>NULL</b>, a device-independent default profile will be obtained.</p>
</dd>

### -param <i>cptColorProfileType</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff546018">COLORPROFILETYPE</a> value that specifies the color profile type.</p>
</dd>

### -param <i>cpstColorProfileSubType</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff546012">COLORPROFILESUBTYPE</a> value that specifies the color profile subtype.</p>
</dd>

### -param <i>dwProfileID</i> [in]

<dd>
<p>The ID of the color space that the color profile represents.</p>
</dd>

### -param <i>cbProfileName</i> [in]

<dd>
<p>The buffer size, in bytes, of the buffer pointed to by <i>pProfileName</i>.</p>
</dd>

### -param <i>pProfileName</i> [out]

<dd>
<p>A pointer to a buffer to receive the name of the color profile.</p>
</dd>
</dl>

## -remarks
<p>Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563730">WcsGetDefaultColorProfileSize</a> function to obtain the required size of the buffer pointed to by the <i>pProfileName</i> parameter.</p>

<p>If WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER, the current user setting, is present, it overrides the system-wide default for <i>profileManagementScope</i>.</p>

<p>This function is executable in Least-Privileged User Account (LUA) context.</p>

<p>Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563730">WcsGetDefaultColorProfileSize</a> function to obtain the required size of the buffer pointed to by the <i>pProfileName</i> parameter.</p>

<p>If WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER, the current user setting, is present, it overrides the system-wide default for <i>profileManagementScope</i>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546012">COLORPROFILESUBTYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546018">COLORPROFILETYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563752">WCS_PROFILE_MANAGEMENT_SCOPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563730">WcsGetDefaultColorProfileSize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20WcsGetDefaultColorProfile function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
