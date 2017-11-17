---
UID: NF.icm.WcsDisassociateColorProfileFromDevice
title: WcsDisassociateColorProfileFromDevice
author: windows-driver-content
description: The WcsDisassociateColorProfileFromDevice function disassociates a specified WCS color profile from a specified device.
old-location: print\wcsdisassociatecolorprofilefromdevice.htm
ms.assetid: d2ab6fe4-131a-4952-864c-7135026cb25c
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
req.alt-api: WcsDisassociateColorProfileFromDevice
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
ms.keywords: WcsDisassociateColorProfileFromDevice
req.iface: 
---

# WcsDisassociateColorProfileFromDevice function



## -description
<p>The <code>WcsDisassociateColorProfileFromDevice</code> function disassociates a specified WCS color profile from a specified device.</p>


## -syntax

````
BOOL WcsDisassociateColorProfileFromDevice(
  _In_ WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
  _In_ PCWSTR                       pProfileName,
  _In_ PCWSTR                       pDeviceName
);
````


## -parameters
<dl>

### -param <i>profileManagementScope</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff563752">WCS_PROFILE_MANAGEMENT_SCOPE</a> value that specifies the scope of this profile management operation.</p>
</dd>

### -param <i>pProfileName</i> [in]

<dd>
<p>A pointer to the file name of the profile to disassociate.</p>
</dd>

### -param <i>pDeviceName</i> [in]

<dd>
<p>A pointer to the name of the device from which the profile is to be disassociated.</p>
</dd>
</dl>

## -remarks
<p>The WCS color profile should be installed on the system and must have been associated with the device using the same value for the <i>profileManagementScope</i> parameter.</p>

<p>If <i>profileManagementScope</i> is WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE, the profile disassociation is system-wide and applies to all users. If <i>profileManagementScope</i> is WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER, the disassociation is only for the current user.</p>

<p>If more than one WCS color profile is associated with a device, WCS uses the last one associated as the default. That is, if your application sequentially associates three profiles with a device, WCS will use the last one associated as the default. If your application then calls the <code>WcsDisassociateColorProfileFromDevice</code> function to disassociate the third profile (which is the default in this example), WCS will use the second profile as the default.</p>

<p>If your application disassociates all profiles from a device, WCS uses the sRGB profile as the default.</p>

<p>This function is executable in Least-Privileged User Account (LUA) context if <i>profileManagementScope</i> is WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER. Otherwise, administrative privileges are required..</p>

<p>The WCS color profile should be installed on the system and must have been associated with the device using the same value for the <i>profileManagementScope</i> parameter.</p>

<p>If <i>profileManagementScope</i> is WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE, the profile disassociation is system-wide and applies to all users. If <i>profileManagementScope</i> is WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER, the disassociation is only for the current user.</p>

<p>If more than one WCS color profile is associated with a device, WCS uses the last one associated as the default. That is, if your application sequentially associates three profiles with a device, WCS will use the last one associated as the default. If your application then calls the <code>WcsDisassociateColorProfileFromDevice</code> function to disassociate the third profile (which is the default in this example), WCS will use the second profile as the default.</p>

<p>If your application disassociates all profiles from a device, WCS uses the sRGB profile as the default.</p>

<p>This function is executable in Least-Privileged User Account (LUA) context if <i>profileManagementScope</i> is WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER. Otherwise, administrative privileges are required..</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563709">WcsAssociateColorProfileWithDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20WcsDisassociateColorProfileFromDevice function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
