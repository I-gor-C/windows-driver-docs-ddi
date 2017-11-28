---
UID: NF.wudfddi.IWDFDevice3.GetHardwareRegisterMappedAddress
title: IWDFDevice3::GetHardwareRegisterMappedAddress
author: windows-driver-content
description: A driver calls GetHardwareRegisterMappedAddress to get the user-mode mapped address of the memory resource it earlier mapped using MapIoSpace.
old-location: wdf\iwdfdevice3_gethardwareregistermappedaddress.htm
old-project: wdf
ms.assetid: 94852404-301F-4C09-81D2-CEDEECFCD6BD
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFDevice3, GetHardwareRegisterMappedAddress, IWDFDevice3::GetHardwareRegisterMappedAddress
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IWDFDevice3.GetHardwareRegisterMappedAddress
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFDevice3
req.product: Windows 10 or later.
---

# IWDFDevice3::GetHardwareRegisterMappedAddress method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>A driver calls <b>GetHardwareRegisterMappedAddress</b> to get the user-mode mapped address of the memory resource it earlier mapped using <a href="https://msdn.microsoft.com/library/windows/hardware/hh451225">MapIoSpace</a>.</p>


## -syntax

````
PVOID GetHardwareRegisterMappedAddress(
  [in] PVOID *PseudoBaseAddress
);
````


## -parameters
<dl>

### -param <i>PseudoBaseAddress</i> [in]

<dd>
<p>A pointer to the pseudo base address returned by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh451225">MapIoSpace</a>.</p>
</dd>
</dl>

## -returns
<p>User-mode base address of the resources mapped earlier using <a href="https://msdn.microsoft.com/library/windows/hardware/hh451225">MapIoSpace</a>.</p>

## -remarks
<p>After the driver calls <b>GetHardwareRegisterMappedAddress</b>, it can access the user-mode address directly to read and write to the register.</p>

<p>
<div class="alert"><b>Note</b>  This is not the recommended approach for accessing registers because it prevents UMDF from doing any validation on the access.</div>
<div> </div> For more information, see <a href="wdf.reading_and_writing_to_device_registers_in_umdf_1_x_drivers">Reading and Writing to Device Registers in UMDF 1.x Drivers</a>.</p>

<p>If you do use <b>GetHardwareRegisterMappedAddress</b>, you must set the <b>UmdfRegisterAccessMode</b> INF directive to <b>RegisterAccessUsingUserModeMapping</b>.  For more information about UMDF  INF directives, see <a href="wdf.specifying_wdf_directives_in_inf_files">Specifying WDF Directives in INF Files</a>.</p>

<p>After the driver calls <b>GetHardwareRegisterMappedAddress</b>, it can access the user-mode address directly to read and write to the register.</p>

<p>
<div class="alert"><b>Note</b>  This is not the recommended approach for accessing registers because it prevents UMDF from doing any validation on the access.</div>
<div> </div> For more information, see <a href="wdf.reading_and_writing_to_device_registers_in_umdf_1_x_drivers">Reading and Writing to Device Registers in UMDF 1.x Drivers</a>.</p>

<p>If you do use <b>GetHardwareRegisterMappedAddress</b>, you must set the <b>UmdfRegisterAccessMode</b> INF directive to <b>RegisterAccessUsingUserModeMapping</b>.  For more information about UMDF  INF directives, see <a href="wdf.specifying_wdf_directives_in_inf_files">Specifying WDF Directives in INF Files</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451197">IWDFDevice3</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice3::GetHardwareRegisterMappedAddress method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
