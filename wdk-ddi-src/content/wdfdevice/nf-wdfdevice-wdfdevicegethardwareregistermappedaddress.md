---
UID: NF.wdfdevice.WdfDeviceGetHardwareRegisterMappedAddress
title: WdfDeviceGetHardwareRegisterMappedAddress function
author: windows-driver-content
description: A driver calls WdfDeviceGetHardwareRegisterMappedAddress to get the user-mode mapped address of the memory resource it mapped previously using WdfDeviceMapIoSpace.
old-location: wdf\wdfdevicegethardwareregistermappedaddress.htm
old-project: wdf
ms.assetid: 4D172D39-0D28-4950-B428-330D5B4D0654
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDeviceGetHardwareRegisterMappedAddress
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
req.alt-api: WdfDeviceGetHardwareRegisterMappedAddress
req.alt-loc: WUDFx02000.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: WUDFx02000.lib
req.dll: WUDFx02000.dll
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceGetHardwareRegisterMappedAddress function



## -description
<p class="CCE_Message">[Applies to UMDF only]
A driver calls <b>WdfDeviceGetHardwareRegisterMappedAddress</b> to get the user-mode mapped address of the memory resource it mapped previously using <a href="wdf.wdfdevicemapiospace">WdfDeviceMapIoSpace</a>.


## -syntax

````
PVOID WdfDeviceGetHardwareRegisterMappedAddress(
  _In_ WDFDEVICE Device,
  _In_ PVOID     PseudoBaseAddress
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.

### -param PseudoBaseAddress [in]

The address of a location that receives a pointer to the pseudo base address.

## -returns
User-mode base address of the resources mapped earlier using <a href="wdf.wdfdevicemapiospace">WdfDeviceMapIoSpace</a>.

## -remarks
This function is the UMDF version 2 equivalent of <a href="wdf.iwdfdevice3_gethardwareregistermappedaddress">IWDFDevice3::GetHardwareRegisterMappedAddress</a>.

After the driver calls <b>WdfDeviceGetHardwareRegisterMappedAddress</b>, it can access the user-mode address directly to read and write to the register.


<div class="alert"><b>Note</b>  This is not the recommended approach for accessing registers because it prevents UMDF from doing any validation on the access.</div>
<div> </div>


If you do use <b>WdfDeviceGetHardwareRegisterMappedAddress</b>, you must set the <b>UmdfRegisterAccessMode</b> INF directive to <b>RegisterAccessUsingUserModeMapping</b>.  For more information about UMDF  INF directives, see <a href="wdf.specifying_wdf_directives_in_inf_files">Specifying WDF Directives in INF Files</a>.

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
Minimum support
</th>
<td width="70%">
Windows 8.1
</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version
</th>
<td width="70%">
2.0
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>WUDFx02000.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>WUDFx02000.dll</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfdevicemapiospace">WdfDeviceMapIoSpace</a>
</dt>
<dt>
<a href="wdf.iwdfdevice3_gethardwareregistermappedaddress">IWDFDevice3::GetHardwareRegisterMappedAddress</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceGetHardwareRegisterMappedAddress function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>