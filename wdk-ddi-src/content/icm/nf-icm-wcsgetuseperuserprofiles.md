---
UID: NF.icm.WcsGetUsePerUserProfiles
title: WcsGetUsePerUserProfiles
author: windows-driver-content
description: The WcsGetUsePerUserProfiles function determines whether the user has chosen to use a per-user profile association list for the specified device.
old-location: print\wcsgetuseperuserprofiles.htm
old-project: print
ms.assetid: 6a970bec-c773-498e-b93a-2bd9f625e194
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: WcsGetUsePerUserProfiles
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
req.alt-api: WcsGetUsePerUserProfiles
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

# WcsGetUsePerUserProfiles function



## -description
<p>The <code>WcsGetUsePerUserProfiles</code> function determines whether the user has chosen to use a per-user profile association list for the specified device.</p>


## -syntax

````
BOOL WcsGetUsePerUserProfiles(
  _In_  LPCWSTR pDeviceName,
  _In_  DWORD   dwDeviceClass,
  _Out_ PBOOL   pUsePerUserProfiles
);
````


## -parameters
<dl>

### -param <i>pDeviceName</i> [in]

<dd>
<p>A pointer to a string that contains the friendly name of the device.</p>
</dd>

### -param <i>dwDeviceClass</i> [in]

<dd>
<p>A flag value that specifies the class of the device. This parameter must take one of the following values:</p>
<p></p>
<dl>

### -param <a id="CLASS_MONITOR"></a><a id="class_monitor"></a>CLASS_MONITOR

<dd>
<p>Specifies a display device.</p>
</dd>

### -param <a id="CLASS_PRINTER"></a><a id="class_printer"></a>CLASS_PRINTER

<dd>
<p>Specifies a printer.</p>
</dd>

### -param <a id="CLASS_SCANNER"></a><a id="class_scanner"></a>CLASS_SCANNER

<dd>
<p>Specifies an image capture device.</p>
</dd>
</dl>
</dd>

### -param <i>pUsePerUserProfiles</i> [out]

<dd>
<p>A pointer to a location to receive a Boolean value that is <b>TRUE</b> if the user has chosen to use a per-user profile association list for the specified device; otherwise <b>FALSE</b>.</p>
</dd>
</dl>

## -remarks
<p>This function will fail if the device pointed to by <i>pDeviceName</i> is not of the class specified by <i>dwDeviceClass</i>.</p>

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
<a href="..\icm\nf-icm-wcssetuseperuserprofiles.md">WcsSetUsePerUserProfiles</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20WcsGetUsePerUserProfiles function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
