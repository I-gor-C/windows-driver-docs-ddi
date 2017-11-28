---
UID: NF.wudfddi.IWDFDriver.RetrieveVersionString
title: IWDFDriver::RetrieveVersionString
author: windows-driver-content
description: The RetrieveVersionString method retrieves the version of the framework.
old-location: wdf\iwdfdriver_retrieveversionstring.htm
old-project: wdf
ms.assetid: 2fa320df-bafd-42f4-a0a1-14151c39d68a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFDriver, RetrieveVersionString, IWDFDriver::RetrieveVersionString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFDriver.RetrieveVersionString
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
req.iface: IWDFDriver
req.product: Windows 10 or later.
---

# IWDFDriver::RetrieveVersionString method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>RetrieveVersionString</b> method retrieves the version of the framework.</p>


## -syntax

````
HRESULT RetrieveVersionString(
  [out]     PWSTR pVersion,
  [in, out] DWORD *pdwVersionLength
);
````


## -parameters
<dl>

### -param <i>pVersion</i> [out]

<dd>
<p>A pointer to a buffer that receives a <b>NULL</b>-terminated string that represents the version of the framework if the supplied buffer is non-<b>NULL</b> and <b>RetrieveVersionString</b> is successful. </p>
</dd>

### -param <i>pdwVersionLength</i> [in, out]

<dd>
<p>A pointer to a variable that receives the size, in characters, of the version string that <i>pVersion</i> points to. On input, this variable contains the size, in bytes, of the buffer at <i>pVersion</i>.</p>
<p>If the buffer at <i>pVersion</i> is <b>NULL</b>, the value that the driver supplies is zero. The framework then returns the size, in characters, that is required for the version string.</p>
<p>If the buffer at <i>pVersion</i> is non-<b>NULL</b>, the framework returns the size, in characters, of the version string.</p>
</dd>
</dl>

## -returns
<p><b>RetrieveVersionString</b> returns S_OK for the following scenarios:</p>

<p>
<ul>
<li>
<p>The buffer that the <i>pVersion</i> parameter points to was non-<b>NULL</b> and large enough to hold the version string, including the <b>NULL</b> character. In addition, the framework successfully copied the string into the supplied buffer and set the variable that is pointed to by the <i>pdwVersionLength</i> parameter to the number of characters in the string.</p>
</li>
<li>
<p>The buffer at <i>pVersion</i> was <b>NULL</b>, the driver preset the variable at <i>pdwVersionLength</i> to 0, and the framework set the variable at <i>pdwVersionLength</i> to the number of characters that are required for the string. 
</p>
</li>
</ul><b>RetrieveVersionString</b> returns HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER) to indicate that the supplied buffer is non-<b>NULL</b> and did not contain enough space to hold the version. The framework sets the variable at <i>pdwVersionLength</i> to the number of characters that are required for the string.

</p>

<p>The buffer that the <i>pVersion</i> parameter points to was non-<b>NULL</b> and large enough to hold the version string, including the <b>NULL</b> character. In addition, the framework successfully copied the string into the supplied buffer and set the variable that is pointed to by the <i>pdwVersionLength</i> parameter to the number of characters in the string.</p>

<p>The buffer at <i>pVersion</i> was <b>NULL</b>, the driver preset the variable at <i>pdwVersionLength</i> to 0, and the framework set the variable at <i>pdwVersionLength</i> to the number of characters that are required for the string. 
</p>

<p><b>RetrieveVersionString</b> might also return other HRESULT values.

</p>

## -remarks


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
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
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