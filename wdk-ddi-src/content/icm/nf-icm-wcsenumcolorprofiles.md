---
UID: NF.icm.WcsEnumColorProfiles
title: WcsEnumColorProfiles
author: windows-driver-content
description: The WcsEnumColorProfiles function enumerates all color profiles that satisfy the enumeration criteria in the specified profile management scope.
old-location: print\wcsenumcolorprofiles.htm
ms.assetid: 54cb2647-5685-4856-9b70-97733758aac2
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
req.alt-api: WcsEnumColorProfiles
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
ms.keywords: WcsEnumColorProfiles
req.iface: 
---

# WcsEnumColorProfiles function



## -description
<p>The <code>WcsEnumColorProfiles</code> function enumerates all color profiles that satisfy the enumeration criteria in the specified profile management scope.</p>


## -syntax

````
BOOL WcsEnumColorProfiles(
  _In_      WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_      PENUMTYPEW                   pEnumRecord,
  _Out_     PBYTE                        pBuffer,
  _In_      DWORD                        dwSize,
  _Out_opt_ PDWORD                       pnProfiles
);
````


## -parameters
<dl>

### -param <i>profileManagementScope</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff563752">WCS_PROFILE_MANAGEMENT_SCOPE</a> value that specifies the scope of this profile management operation.</p>
</dd>

### -param <i>pEnumRecord</i> [in]

<dd>
<p>A pointer to a structure that specifies the enumeration criteria.</p>
</dd>

### -param <i>pBuffer</i> [out]

<dd>
<p>A pointer to a buffer in which the profile names are to be enumerated. A MULTI_SZ string that consists of profile names that satisfy the criteria specified in <i>*pEnumRecord</i> will be placed in this buffer.</p>
</dd>

### -param <i>dwSize</i> [in]

<dd>
<p>A variable that contains the size, in bytes, of the buffer pointed to by <i>pBuffer</i>. See Remarks.</p>
</dd>

### -param <i>pnProfiles</i> [out, optional]

<dd>
<p>An optional pointer to a variable that receives the number of profile names actually copied to the buffer pointed to by <i>pBuffer</i>. Can be <b>NULL</b> if this information is not needed.</p>
</dd>
</dl>

## -remarks
<p>Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563722">WcsEnumColorProfilesSize</a> function to obtain the value for the <i>dwSize</i> parameter, which is the size, in bytes, of the buffer pointed to by the <i>pBuffer</i> parameter.</p>

<p>If the <i>profileManagementScope</i> parameter is WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE, only system-wide associations of profiles to the device are considered. If <i>profileManagementScope</i> is WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER, only per-user associations for the current user are considered. If either <a href="https://msdn.microsoft.com/library/windows/hardware/ff563741">WcsSetUsePerUserProfiles</a> has never been called for this user, or <b>WcsSetUsePerUserProfiles</b> was most recently called for this user with its <i>usePerUserProfiles</i> parameter set to <b>FALSE</b>, then <code>WCSEnumColorProfiles</code> returns an empty list.</p>

<p>If WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER, the current user setting, is present, it overrides the system-wide default for the <i>profileManagementScope</i> parameter.</p>

<p>This function is executable in Least-Privileged User Account (LUA) context.</p>

<p>Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563722">WcsEnumColorProfilesSize</a> function to obtain the value for the <i>dwSize</i> parameter, which is the size, in bytes, of the buffer pointed to by the <i>pBuffer</i> parameter.</p>

<p>If the <i>profileManagementScope</i> parameter is WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE, only system-wide associations of profiles to the device are considered. If <i>profileManagementScope</i> is WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER, only per-user associations for the current user are considered. If either <a href="https://msdn.microsoft.com/library/windows/hardware/ff563741">WcsSetUsePerUserProfiles</a> has never been called for this user, or <b>WcsSetUsePerUserProfiles</b> was most recently called for this user with its <i>usePerUserProfiles</i> parameter set to <b>FALSE</b>, then <code>WCSEnumColorProfiles</code> returns an empty list.</p>

<p>If WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER, the current user setting, is present, it overrides the system-wide default for the <i>profileManagementScope</i> parameter.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563752">WCS_PROFILE_MANAGEMENT_SCOPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563722">WcsEnumColorProfilesSize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20WcsEnumColorProfiles function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
