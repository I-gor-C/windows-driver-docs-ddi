---
UID: NF.winddiui.DrvQueryColorProfile
title: DrvQueryColorProfile
author: windows-driver-content
description: The DrvQueryColorProfile function allows a printer interface DLL to specify an ICC profile to use for color management.
old-location: print\drvquerycolorprofile.htm
old-project: print
ms.assetid: f6eec5a1-7d73-415f-84d9-1ec3f512abaf
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: DrvQueryColorProfile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winddiui.h
req.include-header: Winddiui.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DrvQueryColorProfile
req.alt-loc: winddiui.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# DrvQueryColorProfile function



## -description
<p>The <b>DrvQueryColorProfile</b> function allows a printer interface DLL to specify an ICC profile to use for color management.</p>


## -syntax

````
BOOL DrvQueryColorProfile(
        HANDLE    hPrinter,
  _In_  PDEVMODEW pdevmode,
        ULONG     ulQueryMode,
  _Out_ VOID      *pvProfileData,
  _Out_ ULONG     *pcbProfileData,
  _Out_ FLONG     *pflProfileData
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> 

<dd>
<p>Caller-supplied printer handle.</p>
</dd>

### -param <i>pdevmode</i> [in]

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure.</p>
</dd>

### -param <i>ulQueryMode</i> 

<dd>
<p>One of the following caller-supplied bit flags, indicating the type of profile to be specified.</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>QCP_DEVICEPROFILE</p>
</td>
<td>
<p>The caller is requesting a device profile.</p>
</td>
</tr>
<tr>
<td>
<p>QCP_SOURCEPROFILE</p>
</td>
<td>
<p>The caller is requesting a source profile.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pvProfileData</i> [out]

<dd>
<p>Caller-supplied pointer to a buffer to receive profile information.</p>
</dd>

### -param <i>pcbProfileData</i> [out]

<dd>
<p>Caller-supplied pointer to a value representing the size, in bytes, of the buffer pointed to by <i>pvProfileData</i>.</p>
</dd>

### -param <i>pflProfileData</i> [out]

<dd>
<p>One of the following function-supplied bit flags, indicating the type of information the function is returning.</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>QCP_PROFILEDISK</p>
</td>
<td>
<p>The function is returning the file name of an ICC profile in the buffer pointed to by <i>pvProfileData</i>.</p>
</td>
</tr>
<tr>
<td>
<p>QCP_PROFILEMEMORY</p>
</td>
<td>
<p>The function is returning profile data in the buffer pointed to by <i>pvProfileData</i>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function returns <b>TRUE</b>; otherwise, it returns <b>FALSE</b>.</p>

## -remarks
<p>A <a href="NULL">printer interface DLL</a> can optionally provide a <b>DrvQueryColorProfile</b> function. If the function is provided, GDI calls it if ICM has been enabled for a print job. The function's purpose is to determine and specify an ICC profile that is appropriate for use with the print job.</p>

<p>If a driver's printer interface DLL does not provide a <b>DrvQueryColorProfile</b> function, or if the function returns <b>FALSE</b>, GDI attempts to find a profile. For more information, see <a href="NULL">Locating ICC Profiles</a>.</p>

<p>If the output buffer size specified by <i>pcbProfileData</i> is too small, the driver should overwrite the size value supplied by <i>pcbProfileData</i> with the required buffer size, call SetLastError(ERROR_INSUFFICIENT_BUFFER), and return <b>FALSE</b>.</p>

<p>A <a href="NULL">printer interface DLL</a> can optionally provide a <b>DrvQueryColorProfile</b> function. If the function is provided, GDI calls it if ICM has been enabled for a print job. The function's purpose is to determine and specify an ICC profile that is appropriate for use with the print job.</p>

<p>If a driver's printer interface DLL does not provide a <b>DrvQueryColorProfile</b> function, or if the function returns <b>FALSE</b>, GDI attempts to find a profile. For more information, see <a href="NULL">Locating ICC Profiles</a>.</p>

<p>If the output buffer size specified by <i>pcbProfileData</i> is too small, the driver should overwrite the size value supplied by <i>pcbProfileData</i> with the required buffer size, call SetLastError(ERROR_INSUFFICIENT_BUFFER), and return <b>FALSE</b>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winddiui.h (include Winddiui.h)</dt>
</dl>
</td>
</tr>
</table>