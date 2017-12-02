---
UID: NF.wdfinstaller.WdfPreDeviceRemove
title: WdfPreDeviceRemove
author: windows-driver-content
description: The co-installer's WdfPreDeviceRemove function performs any operations that the co-installer might require before a non-Plug and Play (PnP) driver's installer deletes the driver's kernel-mode service.
old-location: wdf\wdfpredeviceremove.htm
old-project: wdf
ms.assetid: 8cde623d-a255-45ff-ab1e-bdd0c14a02a0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfPreDeviceRemove
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfinstaller.h
req.include-header: Wdfinstaller.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfPreDeviceRemove
req.alt-loc: N/A,N/A.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: N/A (Exported by the KMDF co-installer library. For information about the co-installer library's filename, see Using the KMDF Co-installer.)
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# WdfPreDeviceRemove function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The co-installer's <b>WdfPreDeviceRemove</b> function performs any operations that the co-installer might require before a non-Plug and Play (PnP) driver's installer deletes the driver's kernel-mode service. </p>


## -syntax

````
ULONG WdfPreDeviceRemove(
  _In_     LPCWSTR InfPath,
  _In_opt_ LPCWSTR InfSectionName
);
````


## -parameters
<dl>

### -param InfPath [in]

<dd>
<p>A pointer to a null-terminated wide-character string that contains the directory path to the driver's INF file. The driver's installer can obtain this string by calling <a href="fs.getcurrentdirectory">GetCurrentDirectory</a>, which is described in the Microsoft Windows SDK.</p>
</dd>

### -param InfSectionName [in, optional]

<dd>
<p>A pointer to a null-terminated wide-character string that contains the <i>Wdf-install-section</i> name in the driver's INF file. For more information about this name, see <a href="wdf.installing_the_framework_s_co_installer">Using the KMDF Co-installer</a>. If this pointer is <b>NULL</b>, the co-installer uses <b>WdfSection</b> for the name.</p>
</dd>
</dl>

## -returns
<p><b>WdfPreDeviceRemove</b> returns <b>ERROR_SUCCESS</b> if the operation succeeds. Otherwise, the function returns one of the additional <b>ERROR_XXX</b> values that are defined in Winerror.h.</p>

## -remarks
<p>The installer for the framework-based drivers of a non-PnP device must call <b>WdfPreDeviceRemove</b> before the installer calls <a href="base.deleteservice">DeleteService</a>.</p>

<p>To obtain the address of the co-installer's <b>WdfPreDeviceRemove</b> function, the installer must call <a href="base.getprocaddress">GetProcAddress</a> after the installer has called <a href="base.loadlibrary">LoadLibrary</a> to load the co-installer.</p>

<p>For more information about the <b>WdfPreDeviceRemove</b> function and installers for framework-based drivers of non-PnP devices, see <a href="wdf.installing_a_non_pnp_driver">Installing a Non-PnP Driver</a>. For more information about <a href="base.deleteservice">DeleteService</a>, <a href="base.getprocaddress">GetProcAddress</a>, and <a href="base.loadlibrary">LoadLibrary</a>, see the Microsoft Windows SDK documentation.</p>

<p>For a code example that uses the <b>WdfPreDeviceRemove</b> function, see the installer for the <a href="wdf.sample_kmdf_drivers">NONPNP</a> sample.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfinstaller.h (include Wdfinstaller.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>N/A (Exported by the KMDF co-installer library. For information about the co-installer library's filename, see <a href="wdf.installing_the_framework_s_co_installer">Using the KMDF Co-installer</a>.)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfinstaller\nf-wdfinstaller-wdfpostdeviceremove.md">WdfPostDeviceRemove</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfPreDeviceRemove function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
